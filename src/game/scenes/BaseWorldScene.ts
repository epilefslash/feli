import * as Phaser from 'phaser';
import { W, H, GRAVITY } from '../config';
import { Player } from '../objects/Player';

export interface WorldColors {
  bgTop: number; bgBot: number;
  platformFill: number; platformLine: number; platformTop: number;
  groundFill: number; groundTop: number;
}

export interface PlatformDef  { x: number; y: number; w: number }
export interface NoteDef      { x: number; y: number }
export interface EnemyDef     { x: number; y: number; range: number; type?: string }
export interface ExtraLifeDef { x: number; y: number }

export abstract class BaseWorldScene extends Phaser.Scene {
  constructor(key: string) {
    super({ key });
  }
  protected player!: Player;
  protected platforms!: Phaser.Physics.Arcade.StaticGroup;
  protected notes!: Phaser.Physics.Arcade.StaticGroup;
  protected extraLives!: Phaser.Physics.Arcade.StaticGroup;
  protected allEnemyBullets: Phaser.Physics.Arcade.Group[] = [];

  protected scoreText!: Phaser.GameObjects.Text;
  protected livesGroup!: Phaser.GameObjects.Group;
  protected noteCount = 0;

  protected abstract worldNum:   number;
  protected abstract worldName:  string;
  protected abstract songName:   string;
  protected abstract lyric:      string;
  protected abstract nextScene:  string;
  protected abstract levelW:     number;
  protected abstract groundY:    number;
  protected abstract colors:     WorldColors;
  protected abstract platforms_data: PlatformDef[];
  protected abstract notes_data:     NoteDef[];
  protected abstract enemies_data:   EnemyDef[];
  protected abstract extraLives_data: ExtraLifeDef[];

  // Subclasses implement background + enemy spawning
  protected abstract drawBackground(): void;
  protected abstract spawnEnemies(): void;

  create(): void {
    this.noteCount = 0;
    this.allEnemyBullets = [];

    this.physics.world.gravity.y = GRAVITY;
    this.physics.world.setBounds(0, -200, this.levelW, H + 300);

    this.drawBackground();
    this.buildLevel();
    this.buildNotes();
    this.buildExtraLives();
    this.buildPlayer();
    this.spawnEnemies();
    this.buildUI();
    this.setupBaseCollisions();
    this.setupCamera();
    this.showWorldTitle();
    this.cameras.main.fadeIn(600);
  }

  update(_t: number, delta: number): void {
    this.player.update(delta);
    this.onUpdate(delta);
  }

  protected onUpdate(_delta: number): void {}

  // ── LEVEL ─────────────────────────────────────────────────────────────────

  private buildLevel(): void {
    this.platforms = this.physics.add.staticGroup();
    this.buildGround(0, this.levelW);
    for (const p of this.platforms_data) this.buildPlatform(p.x, p.y, p.w);
    this.buildFinishLine();
  }

  protected buildGround(startX: number, endX: number): void {
    for (let x = startX; x < endX; x += 32) {
      const t = this.platforms.create(x + 16, this.groundY + 16, 'ground_tile') as Phaser.Physics.Arcade.Image;
      t.setDisplaySize(32, 32).refreshBody()
        .setTint(this.colors.groundFill);
    }
  }

  protected buildPlatform(x: number, y: number, width: number): void {
    for (let tx = x; tx < x + width; tx += 32) {
      const aw = Math.min(32, x + width - tx);
      const t = this.platforms.create(tx + aw / 2, y + 8, 'platform_tile') as Phaser.Physics.Arcade.Image;
      t.setDisplaySize(aw, 16).refreshBody()
        .setTint(this.colors.platformFill);
    }
  }

  protected buildFinishLine(): void {
    this.add.image(this.levelW - 280, this.groundY - 40, 'microphone')
      .setOrigin(0.5, 1).setDepth(5);
    const glow = this.add.graphics();
    glow.fillStyle(0xF5A623, 0.15);
    glow.fillRect(this.levelW - 350, 0, 100, H);
    glow.setDepth(4);
    this.add.text(this.levelW - 280, this.groundY - 130, '¡LLEGÁ\nACÁ!', {
      fontSize: '16px', fontFamily: 'Impact, sans-serif',
      color: '#F5A623', align: 'center',
    }).setOrigin(0.5, 1).setDepth(6);
  }

  // ── NOTES ─────────────────────────────────────────────────────────────────

  private buildNotes(): void {
    this.notes = this.physics.add.staticGroup();
    for (const pos of this.notes_data) {
      const note = this.notes.create(pos.x, pos.y, 'note') as Phaser.Physics.Arcade.Image;
      note.setDepth(7);
      this.tweens.add({
        targets: note, y: pos.y - 8,
        duration: 800 + Phaser.Math.Between(0, 400),
        yoyo: true, repeat: -1, ease: 'Sine.InOut',
      });
    }
  }

  // ── EXTRA LIVES ───────────────────────────────────────────────────────────

  private buildExtraLives(): void {
    this.extraLives = this.physics.add.staticGroup();
    for (const pos of this.extraLives_data) {
      const item = this.extraLives.create(pos.x, pos.y, 'heart') as Phaser.Physics.Arcade.Image;
      item.setDepth(7).setScale(1.3);
      this.tweens.add({ targets: item, y: pos.y - 10, duration: 600, yoyo: true, repeat: -1 });
    }
  }

  // ── PLAYER ────────────────────────────────────────────────────────────────

  private buildPlayer(): void {
    this.player = new Player(this, 80, this.groundY - 60);
    this.player.onLivesChange = (lives) => this.updateLivesUI(lives);
    this.player.onScoreChange = (score) => this.scoreText.setText(`♪ ${score.toLocaleString()}`);
    this.player.onDie = () => {
      this.cameras.main.fade(600, 0, 0, 0);
      this.time.delayedCall(600, () =>
        this.scene.start('GameOverScene', { score: this.player.score, fromWorld: this.worldNum })
      );
    };
  }

  // ── UI ────────────────────────────────────────────────────────────────────

  private buildUI(): void {
    const uiBg = this.add.graphics();
    uiBg.fillStyle(0x0A001A, 0.75);
    uiBg.fillRoundedRect(8, 8, 200, 36, 8);
    uiBg.setScrollFactor(0).setDepth(20);

    this.scoreText = this.add.text(18, 18, '♪ 0', {
      fontSize: '20px', fontFamily: 'Impact, Arial Black, sans-serif', color: '#F5A623',
    }).setScrollFactor(0).setDepth(21);

    this.livesGroup = this.add.group();
    this.updateLivesUI(this.player.lives);

    this.add.text(W / 2, 12, `MUNDO ${this.worldNum} · ${this.worldName}`, {
      fontSize: '13px', fontFamily: 'Impact, sans-serif', color: '#B567FF',
    }).setOrigin(0.5, 0).setScrollFactor(0).setDepth(21);
  }

  protected updateLivesUI(lives: number): void {
    this.livesGroup.clear(true, true);
    for (let i = 0; i < lives; i++) {
      const h = this.add.image(W - 30 - i * 28, 22, 'heart')
        .setScale(0.85).setScrollFactor(0).setDepth(21);
      this.livesGroup.add(h);
    }
  }

  // ── COLLISIONS ────────────────────────────────────────────────────────────

  protected setupBaseCollisions(): void {
    this.physics.add.collider(this.player, this.platforms);

    // Collect notes
    this.physics.add.overlap(this.player, this.notes, (_p, noteObj) => {
      const note = noteObj as Phaser.Physics.Arcade.Image;
      note.setActive(false).setVisible(false);
      note.destroy();
      this.player.collectNote();
      this.noteCount++;
      this.spawnNoteEffect(note.x, note.y);
    });

    // Collect extra lives
    this.physics.add.overlap(this.player, this.extraLives, (_p, heartObj) => {
      const heart = heartObj as Phaser.Physics.Arcade.Image;
      const hx = heart.x; const hy = heart.y;
      heart.setActive(false).setVisible(false);
      heart.destroy();
      if (this.player.lives < 5) {
        this.player.lives++;
        this.updateLivesUI(this.player.lives);
      }
      const txt = this.add.text(hx, hy - 10, '+1 VIDA', {
        fontSize: '16px', fontFamily: 'Impact, sans-serif', color: '#FF5BA3',
      }).setDepth(20).setOrigin(0.5);
      this.tweens.add({ targets: txt, y: hy - 50, alpha: 0, duration: 900, onComplete: () => txt.destroy() });
    });

    // Finish zone
    const fin = this.add.zone(this.levelW - 230, this.groundY - 50, 80, 120).setDepth(4);
    this.physics.add.existing(fin, true);
    this.physics.add.overlap(this.player, fin, () => {
      if (!this.player.isDead) this.reachFinish();
    });
  }

  // ── CAMERA ────────────────────────────────────────────────────────────────

  private setupCamera(): void {
    this.cameras.main.setBounds(0, -200, this.levelW, H + 300);
    this.cameras.main.startFollow(this.player, true, 0.12, 0.12);
    this.cameras.main.setDeadzone(80, 60);
  }

  // ── EFFECTS ───────────────────────────────────────────────────────────────

  protected spawnNoteEffect(x: number, y: number): void {
    const p = this.add.particles(x, y, 'note_particle', {
      speed: { min: 30, max: 100 }, scale: { start: 1, end: 0 },
      lifespan: 350, quantity: 8, tint: [0x7B2FBE, 0xFF5BA3, 0xB567FF],
    });
    this.time.delayedCall(350, () => p.destroy());
    const txt = this.add.text(x, y - 10, '+100', {
      fontSize: '14px', fontFamily: 'Impact, sans-serif', color: '#F5A623',
    }).setDepth(15).setOrigin(0.5);
    this.tweens.add({ targets: txt, y: y - 40, alpha: 0, duration: 700, onComplete: () => txt.destroy() });
  }

  private showWorldTitle(): void {
    const bg = this.add.graphics();
    bg.fillStyle(0x0A001A, 0.85);
    bg.fillRect(0, H / 2 - 45, W, 90);
    bg.setScrollFactor(0).setDepth(30);

    const t1 = this.add.text(W / 2, H / 2 - 14, `MUNDO ${this.worldNum}`, {
      fontSize: '16px', fontFamily: 'Impact, sans-serif', color: '#B567FF', letterSpacing: 6,
    }).setOrigin(0.5).setScrollFactor(0).setDepth(31);

    const t2 = this.add.text(W / 2, H / 2 + 14, this.songName.toUpperCase().split('').join(' '), {
      fontSize: '30px', fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#F5A623', stroke: '#7B2FBE', strokeThickness: 4,
    }).setOrigin(0.5).setScrollFactor(0).setDepth(31);

    this.tweens.add({
      targets: [bg, t1, t2], alpha: 0, delay: 2200, duration: 800,
      onComplete: () => { bg.destroy(); t1.destroy(); t2.destroy(); },
    });
  }

  private reachFinish(): void {
    if (this.player.isDead) return;
    this.player.isDead = true;
    for (let i = 0; i < 6; i++) {
      this.time.delayedCall(i * 180, () => {
        const p = this.add.particles(
          this.player.x + Phaser.Math.Between(-100, 100),
          this.player.y + Phaser.Math.Between(-120, -20), 'particle', {
            speed: { min: 80, max: 200 }, scale: { start: 1, end: 0 },
            lifespan: 600, quantity: 18,
            tint: [0xF5A623, 0xFF5BA3, 0x7B2FBE, 0xB567FF, 0xFFFFFF],
          });
        this.time.delayedCall(600, () => p.destroy());
      });
    }
    this.cameras.main.fade(1200, 0, 0, 0);
    this.time.delayedCall(1400, () =>
      this.scene.start(this.nextScene, {
        score: this.player.score, notes: this.noteCount,
        total: this.notes_data.length, fromWorld: this.worldNum,
      })
    );
  }
}
