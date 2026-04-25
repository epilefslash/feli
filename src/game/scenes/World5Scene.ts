import * as Phaser from 'phaser';
import { H } from '../config';
import { BaseWorldScene, WorldColors, PlatformDef, NoteDef, EnemyDef, ExtraLifeDef } from './BaseWorldScene';

export class World5Scene extends BaseWorldScene {
  protected worldNum  = 5;
  protected worldName = 'DEIDAD';
  protected songName  = 'Deidad';
  protected lyric     = '"Algo debe estar perdido en mi placard — son mis sombras las que no dejan mirar"';
  protected nextScene = 'WinScene';
  protected levelW    = 5600;
  protected groundY   = 460;

  protected colors: WorldColors = {
    bgTop: 0x000010, bgBot: 0x050020,
    platformFill: 0x0A0830, platformLine: 0xB567FF, platformTop: 0xFFFFFF,
    groundFill: 0x050018, groundTop: 0xB567FF,
  };

  protected platforms_data: PlatformDef[] = [
    { x: 200,  y: 390, w: 110 }, { x: 400,  y: 340, w: 100 },
    { x: 600,  y: 290, w: 90  }, { x: 780,  y: 350, w: 100 },
    { x: 960,  y: 300, w: 90  }, { x: 1140, y: 250, w: 100 },
    { x: 1340, y: 320, w: 90  }, { x: 1520, y: 270, w: 100 },
    { x: 1720, y: 220, w: 90  }, { x: 1900, y: 290, w: 100 },
    { x: 2100, y: 350, w: 90  }, { x: 2280, y: 280, w: 100 },
    { x: 2480, y: 230, w: 90  }, { x: 2680, y: 300, w: 110 },
    { x: 2900, y: 260, w: 90  }, { x: 3100, y: 320, w: 100 },
    { x: 3300, y: 270, w: 90  }, { x: 3500, y: 230, w: 100 },
    { x: 3720, y: 290, w: 90  }, { x: 3920, y: 360, w: 100 },
    { x: 4140, y: 300, w: 90  }, { x: 4340, y: 250, w: 100 },
    { x: 4560, y: 310, w: 90  }, { x: 4760, y: 270, w: 110 },
    { x: 4980, y: 340, w: 90  },
  ];

  protected notes_data: NoteDef[] = [
    { x: 240, y: 360 }, { x: 440, y: 310 }, { x: 640, y: 260 },
    { x: 820, y: 320 }, { x: 1000, y: 270 }, { x: 1180, y: 220 },
    { x: 1380, y: 290 }, { x: 1560, y: 240 }, { x: 1760, y: 190 },
    { x: 1940, y: 260 }, { x: 2140, y: 320 }, { x: 2320, y: 250 },
    { x: 2520, y: 200 }, { x: 2720, y: 270 }, { x: 2940, y: 230 },
    { x: 3140, y: 290 }, { x: 3340, y: 240 }, { x: 3540, y: 200 },
    { x: 3760, y: 260 }, { x: 3960, y: 330 }, { x: 4180, y: 270 },
    { x: 4380, y: 220 }, { x: 4600, y: 280 }, { x: 4800, y: 240 },
    { x: 5200, y: 420 }, { x: 5260, y: 420 }, { x: 5320, y: 420 },
  ];

  protected enemies_data: EnemyDef[] = [
    { x: 420,  y: 460, range: 150, type: 'sombra' },
    { x: 800,  y: 460, range: 130, type: 'sombra' },
    { x: 1160, y: 220, range: 90, type: 'sombra' },
    { x: 1540, y: 240, range: 90 },
    { x: 1920, y: 460, range: 150, type: 'sombra' },
    { x: 2300, y: 460, range: 130 },
    { x: 2700, y: 270, range: 90, type: 'sombra' },
    { x: 3120, y: 460, range: 150 },
    { x: 3520, y: 200, range: 90, type: 'sombra' },
    { x: 3940, y: 460, range: 150, type: 'sombra' },
    { x: 4360, y: 220, range: 90 },
    { x: 4780, y: 240, range: 90, type: 'sombra' },
    { x: 5000, y: 460, range: 120 },
    // Final boss
    { x: 5100, y: 460, range: 0, type: 'deidad' },
  ];

  protected extraLives_data: ExtraLifeDef[] = [
    { x: 620,  y: 255 }, { x: 1740, y: 185 },
    { x: 2920, y: 225 }, { x: 4580, y: 275 },
  ];

  private sombras: { sprite: Phaser.Physics.Arcade.Sprite; visible: boolean; visTimer: number }[] = [];
  private normalEnemies: any[] = [];
  private deidad?: Phaser.Physics.Arcade.Sprite;
  private deidadHp = 8;
  private deidadHpText?: Phaser.GameObjects.Text;
  private saturn?: Phaser.GameObjects.Graphics;

  protected drawBackground(): void {
    const sky = this.add.graphics();
    sky.fillGradientStyle(0x000010, 0x000010, 0x050020, 0x050020, 1);
    sky.fillRect(0, 0, 800, H);
    sky.setScrollFactor(0).setDepth(-10);

    // Stars (lots of them — space!)
    for (let i = 0; i < 120; i++) {
      const star = this.add.graphics();
      const alpha = Phaser.Math.FloatBetween(0.3, 1);
      star.fillStyle(0xFFFFFF, alpha);
      star.fillCircle(Phaser.Math.Between(0, 800), Phaser.Math.Between(0, H), Phaser.Math.FloatBetween(0.5, 2));
      star.setScrollFactor(Phaser.Math.FloatBetween(0.02, 0.1)).setDepth(-9);
      this.tweens.add({ targets: star, alpha: 0.1, duration: Phaser.Math.Between(800, 2500), yoyo: true, repeat: -1 });
    }

    // Saturn
    this.saturn = this.add.graphics();
    this.saturn.fillStyle(0xD4881A, 0.8);
    this.saturn.fillCircle(600, 90, 40);
    this.saturn.fillStyle(0xB8860B, 0.5);
    this.saturn.fillEllipse(600, 90, 110, 18);
    this.saturn.fillStyle(0xD4881A, 0.8);
    this.saturn.fillCircle(600, 90, 40);
    this.saturn.setScrollFactor(0.05).setDepth(-8);
    this.tweens.add({ targets: this.saturn, angle: 360, duration: 80000, repeat: -1 });

    // Nebula clouds
    for (let i = 0; i < 5; i++) {
      const nebula = this.add.graphics();
      nebula.fillStyle(0x7B2FBE, Phaser.Math.FloatBetween(0.05, 0.12));
      nebula.fillEllipse(
        Phaser.Math.Between(0, 800), Phaser.Math.Between(50, 300),
        Phaser.Math.Between(150, 300), Phaser.Math.Between(60, 120)
      );
      nebula.setScrollFactor(Phaser.Math.FloatBetween(0.05, 0.15)).setDepth(-9);
    }

    // Floating cosmic dust particles
    this.time.addEvent({
      delay: 600, repeat: -1,
      callback: () => {
        const px = this.cameras.main.scrollX + Phaser.Math.Between(0, 800);
        const p = this.add.graphics();
        p.fillStyle(0xB567FF, Phaser.Math.FloatBetween(0.2, 0.5));
        p.fillCircle(px, Phaser.Math.Between(0, H), Phaser.Math.Between(1, 3));
        this.tweens.add({
          targets: p, y: '-=60', alpha: 0, duration: Phaser.Math.Between(2000, 4000),
          onComplete: () => p.destroy(),
        });
      },
    });
  }

  protected spawnEnemies(): void {
    // Sombra texture (shadow enemy - dark with subtle edges)
    const gs = this.make.graphics({}, false);
    gs.fillStyle(0x0A0020, 0.95);
    gs.fillRoundedRect(4, 8, 32, 34, 6);
    gs.lineStyle(1.5, 0xB567FF, 0.7);
    gs.strokeRoundedRect(4, 8, 32, 34, 6);
    gs.fillStyle(0xB567FF, 0.8);
    gs.fillCircle(14, 22, 4);
    gs.fillCircle(26, 22, 4);
    gs.fillStyle(0xFFFFFF, 0.9);
    gs.fillCircle(14, 22, 1.5);
    gs.fillCircle(26, 22, 1.5);
    gs.fillStyle(0x0A0020, 0.95);
    gs.fillRect(6, 42, 8, 12);
    gs.fillRect(26, 42, 8, 12);
    gs.generateTexture('sombra', 40, 54);
    gs.destroy();

    // Deidad (final boss) texture
    const gd = this.make.graphics({}, false);
    gd.fillStyle(0x1A0030);
    gd.fillCircle(40, 40, 38);
    gd.fillStyle(0xB567FF, 0.9);
    gd.fillCircle(40, 40, 32);
    gd.fillStyle(0x000000);
    gd.fillCircle(28, 32, 8);
    gd.fillCircle(52, 32, 8);
    gd.fillStyle(0xFFFF00);
    gd.fillCircle(28, 32, 5);
    gd.fillCircle(52, 32, 5);
    gd.fillStyle(0x000000);
    gd.fillCircle(29, 32, 3);
    gd.fillCircle(53, 32, 3);
    gd.lineStyle(3, 0xFFFFFF, 0.9);
    gd.beginPath();
    gd.arc(40, 44, 10, 0.2, Math.PI - 0.2);
    gd.strokePath();
    // Crown
    gd.fillStyle(0xF5A623);
    gd.fillTriangle(20, 8, 28, 0, 36, 8);
    gd.fillTriangle(36, 8, 40, -4, 44, 8);
    gd.fillTriangle(44, 8, 52, 0, 60, 8);
    gd.fillRect(20, 8, 40, 12);
    // Aura rays
    gd.lineStyle(2, 0xB567FF, 0.5);
    for (let a = 0; a < 360; a += 30) {
      const rad = (a * Math.PI) / 180;
      gd.lineBetween(40, 40, 40 + Math.cos(rad) * 52, 40 + Math.sin(rad) * 52);
    }
    gd.generateTexture('deidad', 80, 80);
    gd.destroy();

    for (const ep of this.enemies_data) {
      if (ep.type === 'sombra') {
        const sprite = this.physics.add.sprite(ep.x, ep.y - 27, 'sombra');
        sprite.setDepth(9).setAlpha(0.15);
        (sprite.body as Phaser.Physics.Arcade.Body).setSize(28, 44).setOffset(6, 8);
        this.physics.add.collider(sprite, this.platforms);
        this.sombras.push({ sprite, visible: false, visTimer: Phaser.Math.Between(2000, 5000) });

        const sbullets = this.physics.add.group({ defaultKey: 'note_particle', maxSize: 3 });
        this.allEnemyBullets.push(sbullets);

        this.physics.add.overlap(this.player.bullets, sprite, (b) => {
          const bullet = b as Phaser.Physics.Arcade.Image;
          bullet.setActive(false).setVisible(false);
          sprite.destroy();
          this.player.score += 250;
          this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
          const p = this.add.particles(sprite.x, sprite.y, 'particle', {
            speed: { min: 60, max: 180 }, scale: { start: 0.8, end: 0 },
            lifespan: 500, quantity: 14, tint: [0xB567FF, 0x0A0020],
          });
          this.time.delayedCall(500, () => p.destroy());
        });
        this.physics.add.overlap(this.player, sprite, () => { this.player.hit(); });

      } else if (ep.type === 'deidad') {
        this.spawnDeidad(ep.x, ep.y);

      } else {
        const { NarradorEnemy } = require('../objects/NarradorEnemy');
        const e = new NarradorEnemy(this, ep.x, ep.y - 25, ep.range);
        e.setTint(0xB567FF);
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

  private spawnDeidad(x: number, y: number): void {
    this.deidad = this.physics.add.sprite(x, y - 40, 'deidad');
    this.deidad.setDepth(9).setScale(1.6);
    (this.deidad.body as Phaser.Physics.Arcade.Body)
      .setSize(60, 60).setOffset(10, 10).setAllowGravity(false);

    // Float up and down
    this.tweens.add({
      targets: this.deidad, y: y - 80,
      duration: 2000, yoyo: true, repeat: -1, ease: 'Sine.InOut',
    });
    // Rotate slowly
    this.tweens.add({ targets: this.deidad, angle: 10, duration: 3000, yoyo: true, repeat: -1 });

    // HP display
    this.deidadHpText = this.add.text(x, y - 120, '♥♥♥♥♥♥♥♥', {
      fontSize: '16px', fontFamily: 'Arial', color: '#B567FF',
    }).setOrigin(0.5).setDepth(12);

    // Shoot cosmic orbs in multiple directions
    const orbGroup = this.physics.add.group({ defaultKey: 'particle', maxSize: 12 });
    this.allEnemyBullets.push(orbGroup);
    this.time.addEvent({
      delay: 1200, repeat: -1,
      callback: () => {
        if (!this.deidad?.active) return;
        const angles = [0, 90, 180, 270, 45, 135, 225, 315];
        for (const angle of angles.slice(0, 4)) {
          const orb = orbGroup.get(this.deidad.x, this.deidad.y) as Phaser.Physics.Arcade.Image;
          if (!orb) continue;
          orb.setActive(true).setVisible(true).setDepth(8).setScale(2.5).setTint(0xB567FF);
          const rad = (angle * Math.PI) / 180;
          (orb.body as Phaser.Physics.Arcade.Body)
            .setVelocity(Math.cos(rad) * 280, Math.sin(rad) * 280).setAllowGravity(false);
          this.time.delayedCall(2500, () => { orb.setActive(false).setVisible(false); });
        }
      },
    });

    // Player bullets hit deidad
    this.physics.add.overlap(this.player.bullets, this.deidad, (b) => {
      const bullet = b as Phaser.Physics.Arcade.Image;
      bullet.setActive(false).setVisible(false);
      this.deidadHp--;
      const hearts = '♥'.repeat(Math.max(0, this.deidadHp)) + '♡'.repeat(8 - Math.max(0, this.deidadHp));
      this.deidadHpText?.setText(hearts);
      this.deidad?.setAlpha(0.3);
      this.cameras.main.shake(100, 0.01);
      this.time.delayedCall(150, () => this.deidad?.setAlpha(1));
      if (this.deidadHp <= 0) this.killDeidad();
    });
    this.physics.add.overlap(this.player, this.deidad, () => { this.player.hit(); });
  }

  private killDeidad(): void {
    if (!this.deidad) return;
    this.deidadHpText?.destroy();
    this.cameras.main.shake(500, 0.025);
    for (let i = 0; i < 5; i++) {
      this.time.delayedCall(i * 200, () => {
        if (!this.deidad) return;
        const p = this.add.particles(
          this.deidad.x + Phaser.Math.Between(-60, 60),
          this.deidad.y + Phaser.Math.Between(-60, 60), 'particle', {
            speed: { min: 100, max: 300 }, scale: { start: 2, end: 0 },
            lifespan: 800, quantity: 25, tint: [0xB567FF, 0xFFFFFF, 0xF5A623],
          });
        this.time.delayedCall(800, () => p.destroy());
      });
    }
    const txt = this.add.text(this.deidad.x, this.deidad.y - 30, '¡LA DEIDAD FUE DERROTADA!', {
      fontSize: '18px', fontFamily: 'Impact, sans-serif', color: '#F5A623',
      stroke: '#7B2FBE', strokeThickness: 4,
    }).setOrigin(0.5).setDepth(25);
    this.tweens.add({ targets: txt, y: txt.y - 80, alpha: 0, duration: 1800, onComplete: () => txt.destroy() });
    this.player.score += 2000;
    this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
    this.deidad.destroy();
  }

  protected onUpdate(delta: number): void {
    for (const e of this.normalEnemies) {
      if (!e.isDead) e.update(delta, this.player.x);
    }

    // Sombra visibility cycle
    for (const s of this.sombras) {
      if (!s.sprite.active) continue;
      s.visTimer -= delta;
      if (s.visTimer <= 0) {
        s.visible = !s.visible;
        s.visTimer = s.visible ? 2500 : Phaser.Math.Between(3000, 6000);
        this.tweens.add({ targets: s.sprite, alpha: s.visible ? 0.9 : 0.1, duration: 600 });
      }
      // Slowly drift towards player when visible
      if (s.visible) {
        const body = s.sprite.body as Phaser.Physics.Arcade.Body;
        const dir = this.player.x < s.sprite.x ? -1 : 1;
        body.setVelocityX(dir * 50);
        s.sprite.setFlipX(dir < 0);
      }
    }

    if (this.deidadHpText && this.deidad?.active) {
      this.deidadHpText.setPosition(this.deidad.x, this.deidad.y - 80);
    }
  }
}
