import * as Phaser from 'phaser';
import { H } from '../config';
import { BaseWorldScene, WorldColors, PlatformDef, NoteDef, EnemyDef, ExtraLifeDef } from './BaseWorldScene';

export class World4Scene extends BaseWorldScene {
  constructor() { super('World4Scene'); }
  protected worldNum  = 4;
  protected worldName = 'REY DE LA NOCHE';
  protected songName  = 'Rey de la Noche';
  protected lyric     = '"Es la ley de la nocturnidad"';
  protected nextScene = 'World5Scene';
  protected levelW    = 5400;
  protected groundY   = 460;

  protected colors: WorldColors = {
    bgTop: 0x000A1A, bgBot: 0x000510,
    platformFill: 0x0A1A2A, platformLine: 0x4488FF, platformTop: 0x88BBFF,
    groundFill: 0x050F1A, groundTop: 0x4488FF,
  };

  protected platforms_data: PlatformDef[] = [
    { x: 200,  y: 380, w: 110 }, { x: 400,  y: 330, w: 100 },
    { x: 580,  y: 280, w: 90  }, { x: 760,  y: 340, w: 100 },
    { x: 940,  y: 290, w: 90  }, { x: 1120, y: 240, w: 100 },
    { x: 1320, y: 310, w: 90  }, { x: 1500, y: 260, w: 100 },
    { x: 1700, y: 220, w: 90  }, { x: 1880, y: 280, w: 100 },
    { x: 2080, y: 340, w: 90  }, { x: 2260, y: 270, w: 100 },
    { x: 2460, y: 220, w: 90  }, { x: 2660, y: 290, w: 110 },
    { x: 2880, y: 250, w: 90  }, { x: 3080, y: 310, w: 100 },
    { x: 3280, y: 260, w: 90  }, { x: 3480, y: 220, w: 100 },
    { x: 3700, y: 280, w: 90  }, { x: 3900, y: 340, w: 100 },
    { x: 4120, y: 280, w: 90  }, { x: 4320, y: 230, w: 100 },
    { x: 4540, y: 290, w: 90  }, { x: 4740, y: 250, w: 110 },
  ];

  protected notes_data: NoteDef[] = [
    { x: 240, y: 350 }, { x: 440, y: 300 }, { x: 620, y: 250 },
    { x: 800, y: 310 }, { x: 980, y: 260 }, { x: 1160, y: 210 },
    { x: 1360, y: 280 }, { x: 1540, y: 230 }, { x: 1740, y: 190 },
    { x: 1920, y: 250 }, { x: 2120, y: 310 }, { x: 2300, y: 240 },
    { x: 2500, y: 190 }, { x: 2700, y: 260 }, { x: 2920, y: 220 },
    { x: 3120, y: 280 }, { x: 3320, y: 230 }, { x: 3520, y: 190 },
    { x: 3740, y: 250 }, { x: 3940, y: 310 }, { x: 4160, y: 250 },
    { x: 4360, y: 200 }, { x: 4580, y: 260 }, { x: 4780, y: 220 },
    { x: 5000, y: 420 }, { x: 5060, y: 420 }, { x: 5120, y: 420 },
  ];

  protected enemies_data: EnemyDef[] = [
    { x: 420,  y: 460, range: 150 },
    { x: 760,  y: 460, range: 130 },
    { x: 1140, y: 210, range: 90, type: 'eduardo' },
    { x: 1520, y: 230, range: 90 },
    { x: 1900, y: 460, range: 150, type: 'eduardo' },
    { x: 2280, y: 460, range: 130 },
    { x: 2680, y: 260, range: 90, type: 'eduardo' },
    { x: 3100, y: 460, range: 150 },
    { x: 3500, y: 190, range: 90, type: 'eduardo' },
    { x: 3920, y: 460, range: 150 },
    { x: 4340, y: 200, range: 90 },
    { x: 4760, y: 220, range: 90, type: 'eduardo' },
    { x: 5000, y: 460, range: 130 },
  ];

  protected extraLives_data: ExtraLifeDef[] = [
    { x: 600,  y: 245 }, { x: 1720, y: 185 },
    { x: 2900, y: 215 }, { x: 4560, y: 255 },
  ];

  private normalEnemies: any[] = [];
  private eduardos: { sprite: Phaser.Physics.Arcade.Sprite; hp: number; shootTimer: number; bullets: Phaser.Physics.Arcade.Group }[] = [];
  private rainEmitter?: Phaser.GameObjects.Particles.ParticleEmitter;

  protected drawBackground(): void {
    const sky = this.add.graphics();
    sky.fillGradientStyle(0x000A1A, 0x000A1A, 0x000510, 0x000510, 1);
    sky.fillRect(0, 0, 800, H);
    sky.setScrollFactor(0).setDepth(-10);

    // Moon
    const moon = this.add.graphics();
    moon.fillStyle(0xCCDDFF, 0.9);
    moon.fillCircle(680, 60, 30);
    moon.fillStyle(0x000A1A, 1);
    moon.fillCircle(695, 55, 24);
    moon.setScrollFactor(0.05).setDepth(-9);

    // Stars
    for (let i = 0; i < 60; i++) {
      const star = this.add.graphics();
      star.fillStyle(0xFFFFFF, Phaser.Math.FloatBetween(0.3, 0.9));
      star.fillCircle(Phaser.Math.Between(0, 800), Phaser.Math.Between(0, 250), Phaser.Math.FloatBetween(0.5, 1.5));
      star.setScrollFactor(0.05).setDepth(-9);
      this.tweens.add({ targets: star, alpha: 0.1, duration: Phaser.Math.Between(1000, 3000), yoyo: true, repeat: -1 });
    }

    // Rain
    this.rainEmitter = this.add.particles(0, -10, 'star', {
      speedX: { min: -20, max: 20 },
      speedY: { min: 300, max: 600 },
      scale: { start: 0.3, end: 0.1 },
      alpha: { start: 0.6, end: 0 },
      lifespan: 1200,
      quantity: 3,
      frequency: 40,
      tint: 0x4488FF,
    });
    this.rainEmitter.setScrollFactor(0).setDepth(-8);

    // Neon bar signs
    for (let i = 0; i < 5; i++) {
      const bx = i * 160 + 40;
      const bar = this.add.graphics();
      bar.fillStyle(0x4488FF, 0.3);
      bar.fillRect(bx, 120 + i * 20, 80, 30);
      bar.lineStyle(1, 0x88BBFF, 0.6);
      bar.strokeRect(bx, 120 + i * 20, 80, 30);
      bar.setScrollFactor(0.1).setDepth(-8);
      this.tweens.add({ targets: bar, alpha: 0.1, duration: Phaser.Math.Between(500, 1500), yoyo: true, repeat: -1 });
    }
  }

  protected spawnEnemies(): void {
    // Eduardo texture
    const g = this.make.graphics({}, false);
    // Suit body
    g.fillStyle(0x1A1A2E);
    g.fillRoundedRect(6, 14, 28, 32, 4);
    // White shirt
    g.fillStyle(0xDDDDDD);
    g.fillRect(14, 14, 12, 18);
    // Tie
    g.fillStyle(0x4488FF);
    g.fillTriangle(18, 14, 22, 14, 20, 30);
    // Head
    g.fillStyle(0xF5CBA7);
    g.fillCircle(20, 10, 10);
    // Hair
    g.fillStyle(0x2C1810);
    g.fillRect(10, 2, 20, 6);
    // Eyes
    g.fillStyle(0x000000);
    g.fillCircle(16, 9, 2);
    g.fillCircle(24, 9, 2);
    // Mouth (open - talking)
    g.fillStyle(0xCC0000);
    g.fillEllipse(20, 15, 8, 5);
    // Arms out (blocking)
    g.fillStyle(0x1A1A2E);
    g.fillRect(0, 20, 8, 20);
    g.fillRect(32, 20, 8, 20);
    // Shoes
    g.fillStyle(0x0A0A0A);
    g.fillRoundedRect(4, 44, 13, 8, 2);
    g.fillRoundedRect(23, 44, 13, 8, 2);
    g.generateTexture('eduardo', 40, 52);
    g.destroy();

    for (const ep of this.enemies_data) {
      if (ep.type === 'eduardo') {
        const sprite = this.physics.add.sprite(ep.x, ep.y - 26, 'eduardo');
        sprite.setDepth(9);
        (sprite.body as Phaser.Physics.Arcade.Body).setSize(28, 44).setOffset(6, 8);
        this.physics.add.collider(sprite, this.platforms);

        const bulletGroup = this.physics.add.group({ defaultKey: 'sound_wave', maxSize: 3 });
        this.allEnemyBullets.push(bulletGroup);
        this.eduardos.push({ sprite, hp: 3, shootTimer: Phaser.Math.Between(2000, 4000), bullets: bulletGroup });

        this.physics.add.overlap(this.player.bullets, sprite, (b) => {
          const bullet = b as Phaser.Physics.Arcade.Image;
          bullet.setActive(false).setVisible(false);
          const edu = this.eduardos.find(e => e.sprite === sprite);
          if (!edu) return;
          edu.hp--;
          sprite.setAlpha(0.4);
          this.time.delayedCall(150, () => sprite.setAlpha(1));
          if (edu.hp <= 0) {
            const txt = this.add.text(sprite.x, sprite.y - 20, '"...me olvidé el estribillo"', {
              fontSize: '11px', fontFamily: 'Arial, sans-serif',
              fontStyle: 'italic', color: '#88BBFF',
            }).setOrigin(0.5).setDepth(20);
            this.tweens.add({ targets: txt, y: txt.y - 50, alpha: 0, duration: 1200, onComplete: () => txt.destroy() });
            sprite.destroy();
            this.player.score += 300;
            this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
          }
        });
        this.physics.add.overlap(this.player, sprite, () => { this.player.hit(); });
      } else {
        const { NarradorEnemy } = require('../objects/NarradorEnemy');
        const e = new NarradorEnemy(this, ep.x, ep.y - 25, ep.range);
        e.setTint(0x4488FF);
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
    for (const e of this.normalEnemies) {
      if (!e.isDead) e.update(delta, this.player.x);
    }

    for (const edu of this.eduardos) {
      if (!edu.sprite.active) continue;
      // Oscillate (Eduardo pacing)
      edu.shootTimer -= delta;
      if (edu.shootTimer <= 0) {
        edu.shootTimer = Phaser.Math.Between(2500, 5000);
        // Shoot words (speech bubble)
        const b = edu.bullets.get(edu.sprite.x, edu.sprite.y) as Phaser.Physics.Arcade.Image;
        if (b) {
          b.setActive(true).setVisible(true).setDepth(8).setScale(1.8).setTint(0x88BBFF);
          const dir = this.player.x < edu.sprite.x ? -1 : 1;
          (b.body as Phaser.Physics.Arcade.Body).setVelocity(dir * 260, -40).setAllowGravity(false);
          this.time.delayedCall(2000, () => { b.setActive(false).setVisible(false); });
        }
        // Show speech bubble
        const phrases = ['"Yo soy Eduardo..."', '"¿Me escuchás?"', '"Esperá que termino..."'];
        const txt = this.add.text(edu.sprite.x, edu.sprite.y - 50, phrases[Phaser.Math.Between(0, 2)], {
          fontSize: '10px', fontFamily: 'Arial', color: '#FFFFFF',
          backgroundColor: '#1A1A2E', padding: { x: 4, y: 2 },
        }).setOrigin(0.5).setDepth(20);
        this.tweens.add({ targets: txt, alpha: 0, delay: 1500, duration: 500, onComplete: () => txt.destroy() });
      }

      // Face player
      edu.sprite.setFlipX(this.player.x < edu.sprite.x);
    }

    // Rain follows camera
    if (this.rainEmitter) {
      this.rainEmitter.setPosition(this.cameras.main.scrollX + Phaser.Math.Between(0, 800), -10);
    }
  }
}
