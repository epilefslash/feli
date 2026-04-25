import * as Phaser from 'phaser';
import { H, C } from '../config';
import { BaseWorldScene, WorldColors, PlatformDef, NoteDef, EnemyDef, ExtraLifeDef } from './BaseWorldScene';

export class World3Scene extends BaseWorldScene {
  protected worldNum  = 3;
  protected worldName = 'CINE TOTAL';
  protected songName  = 'Cine Total';
  protected lyric     = '"El mono baila y luego agita"';
  protected nextScene = 'World4Scene';
  protected levelW    = 5600;
  protected groundY   = 460;

  protected colors: WorldColors = {
    bgTop: 0x1A1000, bgBot: 0x0A0800,
    platformFill: 0x3D2800, platformLine: 0xD4881A, platformTop: 0xFFD166,
    groundFill: 0x2A1800, groundTop: 0xD4881A,
  };

  protected platforms_data: PlatformDef[] = [
    { x: 180,  y: 390, w: 110 }, { x: 360,  y: 340, w: 100 },
    { x: 540,  y: 290, w: 90  }, { x: 700,  y: 360, w: 100 },
    { x: 880,  y: 300, w: 90  }, { x: 1060, y: 250, w: 100 },
    { x: 1260, y: 320, w: 90  }, { x: 1440, y: 270, w: 100 },
    { x: 1640, y: 220, w: 90  }, { x: 1820, y: 290, w: 100 },
    { x: 2020, y: 350, w: 90  }, { x: 2200, y: 280, w: 100 },
    { x: 2400, y: 230, w: 90  }, { x: 2600, y: 300, w: 110 },
    { x: 2820, y: 260, w: 90  }, { x: 3020, y: 320, w: 100 },
    { x: 3220, y: 270, w: 90  }, { x: 3420, y: 230, w: 100 },
    { x: 3640, y: 290, w: 90  }, { x: 3840, y: 350, w: 100 },
    { x: 4060, y: 290, w: 90  }, { x: 4260, y: 240, w: 100 },
    { x: 4480, y: 300, w: 90  }, { x: 4680, y: 260, w: 110 },
    { x: 4900, y: 320, w: 90  },
  ];

  protected notes_data: NoteDef[] = [
    { x: 220, y: 360 }, { x: 400, y: 310 }, { x: 580, y: 260 },
    { x: 740, y: 330 }, { x: 920, y: 270 }, { x: 1100, y: 220 },
    { x: 1300, y: 290 }, { x: 1480, y: 240 }, { x: 1680, y: 190 },
    { x: 1860, y: 260 }, { x: 2060, y: 320 }, { x: 2240, y: 250 },
    { x: 2440, y: 200 }, { x: 2640, y: 270 }, { x: 2860, y: 230 },
    { x: 3060, y: 290 }, { x: 3260, y: 240 }, { x: 3460, y: 200 },
    { x: 3680, y: 260 }, { x: 3880, y: 320 }, { x: 4100, y: 260 },
    { x: 4300, y: 210 }, { x: 4520, y: 270 }, { x: 4720, y: 230 },
    { x: 5100, y: 420 }, { x: 5160, y: 420 }, { x: 5220, y: 420 },
  ];

  protected enemies_data: EnemyDef[] = [
    { x: 380,  y: 460, range: 150, type: 'mono' },
    { x: 720,  y: 460, range: 130, type: 'mono' },
    { x: 1080, y: 220, range: 90  },
    { x: 1460, y: 240, range: 90  },
    { x: 1840, y: 460, range: 150, type: 'mono' },
    { x: 2220, y: 460, range: 130 },
    { x: 2640, y: 270, range: 90, type: 'mono' },
    { x: 3060, y: 460, range: 150 },
    { x: 3460, y: 200, range: 90, type: 'mono' },
    { x: 3880, y: 460, range: 150 },
    { x: 4300, y: 210, range: 90 },
    { x: 4700, y: 230, range: 90, type: 'mono' },
    { x: 5000, y: 460, range: 120 },
  ];

  protected extraLives_data: ExtraLifeDef[] = [
    { x: 560,  y: 255 }, { x: 1660, y: 185 },
    { x: 2820, y: 225 }, { x: 4480, y: 265 },
  ];

  private monos: { sprite: Phaser.Physics.Arcade.Sprite; startX: number; enraged: boolean; enrageTimer: number; dir: number }[] = [];
  private normalEnemies: any[] = [];
  private fogTimer = 0;
  private fogOverlay?: Phaser.GameObjects.Graphics;

  protected drawBackground(): void {
    // Sepia/dark cinema atmosphere
    const sky = this.add.graphics();
    sky.fillGradientStyle(0x1A1000, 0x1A1000, 0x0A0800, 0x0A0800, 1);
    sky.fillRect(0, 0, 800, H);
    sky.setScrollFactor(0).setDepth(-10);

    // Cinema curtains on sides
    const curtL = this.add.graphics();
    curtL.fillStyle(0x4D0000, 0.8);
    curtL.fillRect(0, 0, 40, H);
    curtL.setScrollFactor(0).setDepth(-8);
    const curtR = this.add.graphics();
    curtR.fillStyle(0x4D0000, 0.8);
    curtR.fillRect(760, 0, 40, H);
    curtR.setScrollFactor(0).setDepth(-8);

    // Film grain dots
    for (let i = 0; i < 40; i++) {
      const dot = this.add.graphics();
      dot.fillStyle(0xD4881A, Phaser.Math.FloatBetween(0.05, 0.2));
      dot.fillCircle(Phaser.Math.Between(0, 800), Phaser.Math.Between(0, H), Phaser.Math.Between(1, 3));
      dot.setScrollFactor(0).setDepth(-9);
    }

    // Screen/projector light effect
    const projector = this.add.graphics();
    projector.fillStyle(0xFFD166, 0.06);
    projector.fillTriangle(400, 0, 200, H, 600, H);
    projector.setScrollFactor(0).setDepth(-7);
    this.tweens.add({ targets: projector, alpha: 0.02, duration: 2000, yoyo: true, repeat: -1 });

    // Fog overlay (appears periodically)
    this.fogOverlay = this.add.graphics();
    this.fogOverlay.fillStyle(0x222210, 0);
    this.fogOverlay.fillRect(0, 0, 800, H);
    this.fogOverlay.setScrollFactor(0).setDepth(15);
  }

  protected spawnEnemies(): void {
    this.monos = [];
    this.normalEnemies = [];

    // Create mono texture
    const g = this.make.graphics({}, false);
    g.fillStyle(0x6B4226);
    g.fillRoundedRect(6, 8, 28, 28, 6);
    g.fillStyle(0x8B5A2B);
    g.fillEllipse(20, 8, 24, 18);
    g.fillStyle(0xFFD166);
    g.fillCircle(13, 22, 5);
    g.fillCircle(27, 22, 5);
    g.fillStyle(0x000000);
    g.fillCircle(13, 22, 2.5);
    g.fillCircle(27, 22, 2.5);
    g.fillStyle(0xFF6B6B);
    g.fillEllipse(20, 30, 10, 6);
    g.fillStyle(0x6B4226);
    g.fillRect(8, 36, 7, 12);
    g.fillRect(25, 36, 7, 12);
    g.fillStyle(0x4A2E0F);
    g.fillRoundedRect(6, 44, 10, 8, 2);
    g.fillRoundedRect(24, 44, 10, 8, 2);
    g.generateTexture('mono', 40, 52);
    g.destroy();

    for (const ep of this.enemies_data) {
      if (ep.type === 'mono') {
        const sprite = this.physics.add.sprite(ep.x, ep.y - 26, 'mono');
        sprite.setDepth(9);
        (sprite.body as Phaser.Physics.Arcade.Body).setSize(28, 44).setOffset(6, 8);
        this.physics.add.collider(sprite, this.platforms);
        this.monos.push({ sprite, startX: ep.x, enraged: false, enrageTimer: Phaser.Math.Between(3000, 6000), dir: 1 });

        const mbullets = this.physics.add.group({ defaultKey: 'note_particle', maxSize: 4 });
        this.allEnemyBullets.push(mbullets);

        this.physics.add.overlap(this.player.bullets, sprite, (b) => {
          const bullet = b as Phaser.Physics.Arcade.Image;
          bullet.setActive(false).setVisible(false);
          sprite.destroy();
          this.player.score += 250;
          this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
          const pp = this.add.particles(sprite.x, sprite.y, 'particle', {
            speed: { min: 60, max: 160 }, scale: { start: 0.8, end: 0 },
            lifespan: 500, quantity: 12, tint: [0x6B4226, 0xFFD166],
          });
          this.time.delayedCall(500, () => pp.destroy());
        });
        this.physics.add.overlap(this.player, sprite, () => { this.player.hit(); });
      } else {
        // Import NarradorEnemy dynamically
        const { NarradorEnemy } = require('../objects/NarradorEnemy');
        const e = new NarradorEnemy(this, ep.x, ep.y - 25, ep.range);
        e.setTint(0xD4881A);
        this.normalEnemies.push(e);
        this.allEnemyBullets.push(e.bullets);
        this.physics.add.collider(e, this.platforms);
        this.physics.add.overlap(this.player.bullets, e, (b) => {
          const bullet = b as Phaser.Physics.Arcade.Image;
          bullet.setActive(false).setVisible(false);
          if (!e.isDead) { e.kill(); this.player.score += 200; this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`); }
        });
        this.physics.add.overlap(this.player, e, () => { if (!e.isDead) this.player.hit(); });
      }
    }

    for (const bg of this.allEnemyBullets) {
      this.physics.add.overlap(this.player, bg, (_p, b) => {
        const bullet = b as Phaser.Physics.Arcade.Image;
        bullet.setActive(false).setVisible(false);
        this.player.hit();
      });
    }
  }

  protected onUpdate(delta: number): void {
    // Update mono enemies (patrol + enrage)
    for (const m of this.monos) {
      if (!m.sprite.active) continue;
      const body = m.sprite.body as Phaser.Physics.Arcade.Body;
      const speed = m.enraged ? 220 : 70;
      body.setVelocityX(m.dir * speed);
      m.sprite.setFlipX(m.dir < 0);

      if (m.sprite.x > m.startX + 120) m.dir = -1;
      if (m.sprite.x < m.startX - 120) m.dir = 1;

      m.enrageTimer -= delta;
      if (m.enrageTimer <= 0) {
        m.enraged = !m.enraged;
        m.enrageTimer = m.enraged ? 2000 : Phaser.Math.Between(3000, 6000);
        m.sprite.setTint(m.enraged ? 0xFF4444 : 0xFFFFFF);
        if (m.enraged) {
          this.cameras.main.shake(200, 0.008);
        }
      }
    }

    for (const e of this.normalEnemies) {
      if (!e.isDead) e.update(delta, this.player.x);
    }

    // Fog effect
    this.fogTimer += delta;
    if (this.fogTimer > 8000) {
      this.fogTimer = 0;
      this.tweens.add({
        targets: this.fogOverlay, alpha: 0.7, duration: 1500,
        yoyo: true, hold: 2000,
      });
    }
  }
}
