import * as Phaser from 'phaser';
import { W, H, C, LEVEL_W, GROUND_Y, GRAVITY, PLATFORMS, NOTE_POSITIONS, ENEMY_POSITIONS, EXTRA_LIVES } from '../config';
import { Player } from '../objects/Player';
import { NarradorEnemy } from '../objects/NarradorEnemy';

export class GameScene extends Phaser.Scene {
  private player!: Player;
  private platforms!: Phaser.Physics.Arcade.StaticGroup;
  private notes!: Phaser.Physics.Arcade.StaticGroup;
  private extraLives!: Phaser.Physics.Arcade.StaticGroup;
  private enemies: NarradorEnemy[] = [];
  private allEnemyBullets!: Phaser.Physics.Arcade.Group[];

  // UI (scroll-fixed)
  private scoreText!: Phaser.GameObjects.Text;
  private livesGroup!: Phaser.GameObjects.Group;
  private worldLabel!: Phaser.GameObjects.Text;
  private noteCount = 0;
  private totalNotes = NOTE_POSITIONS.length;

  constructor() {
    super({ key: 'GameScene' });
  }

  create(): void {
    this.physics.world.gravity.y = GRAVITY;
    this.physics.world.setBounds(0, -200, LEVEL_W, H + 300);

    this.enemies = [];

    this.buildBackground();
    this.buildLevel();
    this.buildNotes();
    this.buildExtraLives();
    this.buildEnemies();
    this.buildPlayer();
    this.buildUI();
    this.setupCollisions();
    this.setupCamera();
    this.showWorldTitle();

    this.cameras.main.fadeIn(600);
  }

  update(_time: number, delta: number): void {
    this.player.update(delta);

    for (const enemy of this.enemies) {
      if (!enemy.isDead) {
        enemy.update(delta, this.player.x);
      }
    }
  }

  // ── BACKGROUND ─────────────────────────────────────────────────────────────

  private buildBackground(): void {
    // Sky gradient via tileSprite / fillRect
    const sky = this.add.graphics();
    sky.fillGradientStyle(C.sky, C.sky, C.bg, C.bg, 1);
    sky.fillRect(0, 0, W, H);
    sky.setScrollFactor(0).setDepth(-10);

    // Stars
    for (let i = 0; i < 80; i++) {
      const sx = Phaser.Math.Between(0, W);
      const sy = Phaser.Math.Between(0, H * 0.7);
      const star = this.add.graphics();
      star.fillStyle(C.white, Phaser.Math.FloatBetween(0.2, 0.8));
      star.fillCircle(sx, sy, Phaser.Math.FloatBetween(0.8, 2));
      star.setScrollFactor(0.05).setDepth(-9);
    }

    // Moon / Sun
    const sun = this.add.graphics();
    sun.fillStyle(C.goldLight, 0.9);
    sun.fillCircle(680, 80, 38);
    sun.fillStyle(C.gold, 0.5);
    sun.fillCircle(680, 80, 28);
    sun.setScrollFactor(0.05).setDepth(-9);
    this.tweens.add({ targets: sun, alpha: 0.7, duration: 2000, yoyo: true, repeat: -1 });

    // Far buildings (parallax 0.15)
    for (let i = 0; i < Math.ceil(LEVEL_W / 1400) + 1; i++) {
      this.add.image(i * 1400, H - 100, 'bg_far')
        .setOrigin(0, 1).setScrollFactor(0.15).setDepth(-8)
        .setTint(C.purpleLight).setAlpha(0.5);
    }

    // Near buildings (parallax 0.4)
    for (let i = 0; i < Math.ceil(LEVEL_W / 960) + 1; i++) {
      this.add.image(i * 960, H - 100, 'bg_near')
        .setOrigin(0, 1).setScrollFactor(0.4).setDepth(-7)
        .setAlpha(0.7);
    }
  }

  // ── LEVEL ──────────────────────────────────────────────────────────────────

  private buildLevel(): void {
    this.platforms = this.physics.add.staticGroup();

    // Ground — solid from 0 to ~1380, gap ~1380-1570, then continues
    this.buildGroundSegment(0, 1380);
    this.buildGroundSegment(1570, LEVEL_W);

    // Elevated platforms
    for (const p of PLATFORMS) {
      this.buildPlatform(p.x, p.y, p.w);
    }

    // Finish line microphone
    this.add.image(LEVEL_W - 280, GROUND_Y - 40, 'microphone')
      .setOrigin(0.5, 1).setDepth(5);

    // Finish zone glow
    const glow = this.add.graphics();
    glow.fillStyle(C.gold, 0.15);
    glow.fillRect(LEVEL_W - 350, 0, 100, H);
    glow.setDepth(4);

    // "LLEGASTE" sign above mic
    this.add.text(LEVEL_W - 280, GROUND_Y - 130, '¡LLEGÁ\nACÁ!', {
      fontSize: '16px',
      fontFamily: 'Impact, sans-serif',
      color: '#F5A623',
      align: 'center',
    }).setOrigin(0.5, 1).setDepth(6);
  }

  private buildGroundSegment(startX: number, endX: number): void {
    const tileW = 32;
    for (let x = startX; x < endX; x += tileW) {
      const tile = this.platforms.create(x + 16, GROUND_Y + 16, 'ground_tile') as Phaser.Physics.Arcade.Image;
      tile.setDisplaySize(tileW, 32).refreshBody();
    }
  }

  private buildPlatform(x: number, y: number, width: number): void {
    const tileW = 32;
    for (let tx = x; tx < x + width; tx += tileW) {
      const actualW = Math.min(tileW, x + width - tx);
      const tile = this.platforms.create(tx + actualW / 2, y + 8, 'platform_tile') as Phaser.Physics.Arcade.Image;
      tile.setDisplaySize(actualW, 16).refreshBody();
    }
  }

  // ── NOTES ─────────────────────────────────────────────────────────────────

  private buildNotes(): void {
    this.notes = this.physics.add.staticGroup();
    for (const pos of NOTE_POSITIONS) {
      const note = this.notes.create(pos.x, pos.y, 'note') as Phaser.Physics.Arcade.Image;
      note.setDepth(7);
      // Float animation
      this.tweens.add({
        targets: note,
        y: pos.y - 8,
        duration: 800 + Phaser.Math.Between(0, 400),
        yoyo: true,
        repeat: -1,
        ease: 'Sine.InOut',
      });
    }
    this.totalNotes = NOTE_POSITIONS.length;
  }

  // ── EXTRA LIVES ───────────────────────────────────────────────────────────

  private buildExtraLives(): void {
    this.extraLives = this.physics.add.staticGroup();
    for (const pos of EXTRA_LIVES) {
      const item = this.extraLives.create(pos.x, pos.y, 'heart') as Phaser.Physics.Arcade.Image;
      item.setDepth(7).setScale(1.3);
      this.tweens.add({
        targets: item,
        y: pos.y - 10,
        duration: 600,
        yoyo: true,
        repeat: -1,
        ease: 'Sine.InOut',
      });
      // Golden glow ring
      const glow = this.add.graphics();
      glow.lineStyle(2, C.gold, 0.5);
      glow.strokeCircle(pos.x, pos.y, 18);
      this.tweens.add({ targets: glow, alpha: 0, duration: 800, yoyo: true, repeat: -1 });
    }
  }

  // ── ENEMIES ────────────────────────────────────────────────────────────────

  private buildEnemies(): void {
    this.allEnemyBullets = [];
    for (const ep of ENEMY_POSITIONS) {
      const enemy = new NarradorEnemy(this, ep.x, ep.y - 25, ep.range);
      this.enemies.push(enemy);
      this.allEnemyBullets.push(enemy.bullets);
    }
  }

  // ── PLAYER ────────────────────────────────────────────────────────────────

  private buildPlayer(): void {
    this.player = new Player(this, 80, GROUND_Y - 60);

    this.player.onLivesChange = (lives) => this.updateLivesUI(lives);
    this.player.onScoreChange = (score) => this.scoreText.setText(`♪ ${score.toLocaleString()}`);
    this.player.onDie = () => {
      this.cameras.main.fade(600, 0, 0, 0);
      this.time.delayedCall(600, () =>
        this.scene.start('GameOverScene', { score: this.player.score })
      );
    };
  }

  // ── UI ────────────────────────────────────────────────────────────────────

  private buildUI(): void {
    // Score background bar
    const uiBg = this.add.graphics();
    uiBg.fillStyle(C.bg, 0.75);
    uiBg.fillRoundedRect(8, 8, 200, 36, 8);
    uiBg.setScrollFactor(0).setDepth(20);

    this.scoreText = this.add.text(18, 18, '♪ 0', {
      fontSize: '20px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#F5A623',
    }).setScrollFactor(0).setDepth(21);

    // Lives
    this.livesGroup = this.add.group();
    this.updateLivesUI(this.player.lives);

    // World name
    this.worldLabel = this.add.text(W / 2, 12, 'MUNDO 1 · SUNSHINE', {
      fontSize: '13px',
      fontFamily: 'Impact, sans-serif',
      color: '#B567FF',
    }).setOrigin(0.5, 0).setScrollFactor(0).setDepth(21);

    // Controls mini hint (fades after 4s)
    const hint = this.add.text(W / 2, H - 22, '← → moverse  |  ↑ saltar (2×)  |  Z lanzar', {
      fontSize: '10px',
      fontFamily: 'Arial, sans-serif',
      color: '#7B2FBE',
    }).setOrigin(0.5).setScrollFactor(0).setDepth(21);
    this.tweens.add({ targets: hint, alpha: 0, delay: 4000, duration: 1500 });
  }

  private updateLivesUI(lives: number): void {
    this.livesGroup.clear(true, true);
    for (let i = 0; i < lives; i++) {
      const heart = this.add.image(W - 30 - i * 28, 22, 'heart')
        .setScale(0.85).setScrollFactor(0).setDepth(21);
      this.livesGroup.add(heart);
    }
  }

  // ── COLLISIONS ───────────────────────────────────────────────────────────

  private setupCollisions(): void {
    // Player on platforms
    this.physics.add.collider(this.player, this.platforms);

    // Enemy on platforms
    for (const e of this.enemies) {
      this.physics.add.collider(e, this.platforms);
    }

    // Player collects notes
    this.physics.add.overlap(
      this.player,
      this.notes,
      (_p, noteObj) => {
        const note = noteObj as Phaser.Physics.Arcade.Image;
        note.setActive(false).setVisible(false);
        note.destroy();
        this.player.collectNote();
        this.noteCount++;
        this.spawnNotePickupEffect(note.x, note.y);

        if (this.noteCount >= this.totalNotes) {
          // all notes collected bonus
        }
      }
    );

    // Player collects extra lives
    this.physics.add.overlap(
      this.player,
      this.extraLives,
      (_p, heartObj) => {
        const heart = heartObj as Phaser.Physics.Arcade.Image;
        heart.setActive(false).setVisible(false);
        heart.destroy();
        if (this.player.lives < 5) {
          this.player.lives++;
          this.updateLivesUI(this.player.lives);
        }
        // Flash text
        const txt = this.add.text(heart.x, heart.y - 10, '+1 VIDA', {
          fontSize: '16px',
          fontFamily: 'Impact, sans-serif',
          color: '#FF5BA3',
        }).setDepth(20).setOrigin(0.5);
        this.tweens.add({
          targets: txt,
          y: heart.y - 50,
          alpha: 0,
          duration: 900,
          onComplete: () => txt.destroy(),
        });
        // Particle burst
        const p = this.add.particles(heart.x, heart.y, 'particle', {
          speed: { min: 40, max: 120 },
          scale: { start: 0.7, end: 0 },
          lifespan: 400,
          quantity: 10,
          tint: [C.pink, C.white],
        });
        this.time.delayedCall(400, () => p.destroy());
      }
    );

    // Player bullets hit enemies
    for (const enemy of this.enemies) {
      this.physics.add.overlap(
        this.player.bullets,
        enemy,
        (bulletObj, _enemy) => {
          const bullet = bulletObj as Phaser.Physics.Arcade.Image;
          bullet.setActive(false).setVisible(false);
          if (!enemy.isDead) {
            enemy.kill();
            this.player.score += 200;
            this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
          }
        }
      );
    }

    // Enemy bullets hit player
    for (const bulletGroup of this.allEnemyBullets) {
      this.physics.add.overlap(
        this.player,
        bulletGroup,
        (_p, bulletObj) => {
          const bullet = bulletObj as Phaser.Physics.Arcade.Image;
          bullet.setActive(false).setVisible(false);
          this.player.hit();
        }
      );
    }

    // Player touches enemy body
    for (const enemy of this.enemies) {
      this.physics.add.overlap(
        this.player,
        enemy,
        () => {
          if (!enemy.isDead) this.player.hit();
        }
      );
    }

    // Reach finish
    const finishZone = this.add.zone(LEVEL_W - 230, GROUND_Y - 50, 80, 120)
      .setDepth(4);
    this.physics.add.existing(finishZone, true);
    this.physics.add.overlap(this.player, finishZone, () => {
      if (!this.player.isDead) this.reachFinish();
    });
  }

  // ── CAMERA ────────────────────────────────────────────────────────────────

  private setupCamera(): void {
    this.cameras.main.setBounds(0, -200, LEVEL_W, H + 300);
    this.cameras.main.startFollow(this.player, true, 0.12, 0.12);
    this.cameras.main.setDeadzone(80, 60);
  }

  // ── EFFECTS ───────────────────────────────────────────────────────────────

  private spawnNotePickupEffect(x: number, y: number): void {
    const particles = this.add.particles(x, y, 'note_particle', {
      speed: { min: 30, max: 100 },
      scale: { start: 1, end: 0 },
      lifespan: 350,
      quantity: 8,
      tint: [C.purple, C.pink, C.purpleLight],
    });
    this.time.delayedCall(350, () => particles.destroy());

    const txt = this.add.text(x, y - 10, '+100', {
      fontSize: '14px',
      fontFamily: 'Impact, sans-serif',
      color: '#F5A623',
    }).setDepth(15).setOrigin(0.5);
    this.tweens.add({
      targets: txt,
      y: y - 40,
      alpha: 0,
      duration: 700,
      onComplete: () => txt.destroy(),
    });
  }

  private showWorldTitle(): void {
    const bg = this.add.graphics();
    bg.fillStyle(C.bg, 0.85);
    bg.fillRect(0, H / 2 - 45, W, 90);
    bg.setScrollFactor(0).setDepth(30);

    const t1 = this.add.text(W / 2, H / 2 - 14, 'MUNDO 1', {
      fontSize: '16px',
      fontFamily: 'Impact, sans-serif',
      color: '#B567FF',
      letterSpacing: 6,
    }).setOrigin(0.5).setScrollFactor(0).setDepth(31);

    const t2 = this.add.text(W / 2, H / 2 + 14, 'S U N S H I N E', {
      fontSize: '34px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#F5A623',
      stroke: '#7B2FBE',
      strokeThickness: 4,
    }).setOrigin(0.5).setScrollFactor(0).setDepth(31);

    this.tweens.add({
      targets: [bg, t1, t2],
      alpha: 0,
      delay: 2200,
      duration: 800,
      onComplete: () => { bg.destroy(); t1.destroy(); t2.destroy(); },
    });
  }

  private reachFinish(): void {
    if (this.player.isDead) return;
    this.player.isDead = true;

    // Fireworks!
    for (let i = 0; i < 6; i++) {
      this.time.delayedCall(i * 180, () => {
        const fx = this.player.x + Phaser.Math.Between(-100, 100);
        const fy = this.player.y + Phaser.Math.Between(-120, -20);
        const p = this.add.particles(fx, fy, 'particle', {
          speed: { min: 80, max: 200 },
          scale: { start: 1, end: 0 },
          lifespan: 600,
          quantity: 18,
          tint: [C.gold, C.pink, C.purple, C.purpleLight, C.white],
        });
        this.time.delayedCall(600, () => p.destroy());
      });
    }

    this.cameras.main.fade(1200, 0, 0, 0);
    this.time.delayedCall(1400, () =>
      this.scene.start('World2Scene', { score: this.player.score })
    );
  }
}
