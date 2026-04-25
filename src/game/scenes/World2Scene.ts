import * as Phaser from 'phaser';
import { H, C } from '../config';
import { BaseWorldScene, WorldColors, PlatformDef, NoteDef, EnemyDef, ExtraLifeDef } from './BaseWorldScene';
import { NarradorEnemy } from '../objects/NarradorEnemy';

export class World2Scene extends BaseWorldScene {
  protected worldNum  = 2;
  protected worldName = 'P.P.P.';
  protected songName  = 'P.P.P.';
  protected lyric     = '"Estaba el diablo bien parado en la puerta de mi casa"';
  protected nextScene = 'World3Scene';
  protected levelW    = 5200;
  protected groundY   = 460;

  protected colors: WorldColors = {
    bgTop: 0x1A0000, bgBot: 0x0A0010,
    platformFill: 0x220011, platformLine: 0xFF0055, platformTop: 0xFF0055,
    groundFill: 0x1A0010, groundTop: 0xFF0055,
  };

  protected platforms_data: PlatformDef[] = [
    { x: 200,  y: 380, w: 100 }, { x: 380,  y: 320, w: 90  },
    { x: 540,  y: 270, w: 100 }, { x: 700,  y: 330, w: 90  },
    { x: 880,  y: 260, w: 100 }, { x: 1060, y: 310, w: 90  },
    { x: 1240, y: 260, w: 100 }, { x: 1420, y: 320, w: 90  },
    { x: 1620, y: 270, w: 100 }, { x: 1820, y: 220, w: 90  },
    { x: 2020, y: 290, w: 100 }, { x: 2220, y: 240, w: 90  },
    { x: 2420, y: 300, w: 100 }, { x: 2620, y: 250, w: 90  },
    { x: 2820, y: 310, w: 100 }, { x: 3020, y: 260, w: 90  },
    { x: 3220, y: 220, w: 100 }, { x: 3420, y: 280, w: 90  },
    { x: 3620, y: 240, w: 100 }, { x: 3820, y: 300, w: 90  },
    { x: 4020, y: 260, w: 100 }, { x: 4220, y: 220, w: 90  },
    { x: 4420, y: 280, w: 110 }, { x: 4640, y: 240, w: 100 },
  ];

  protected notes_data: NoteDef[] = [
    { x: 240, y: 350 }, { x: 420, y: 290 }, { x: 580, y: 240 },
    { x: 740, y: 300 }, { x: 920, y: 230 }, { x: 1100, y: 280 },
    { x: 1280, y: 230 }, { x: 1460, y: 290 }, { x: 1660, y: 240 },
    { x: 1860, y: 190 }, { x: 2060, y: 260 }, { x: 2260, y: 210 },
    { x: 2460, y: 270 }, { x: 2660, y: 220 }, { x: 2860, y: 280 },
    { x: 3060, y: 230 }, { x: 3260, y: 190 }, { x: 3460, y: 250 },
    { x: 3660, y: 210 }, { x: 3860, y: 270 }, { x: 4060, y: 230 },
    { x: 4260, y: 190 }, { x: 4460, y: 250 }, { x: 4680, y: 210 },
    { x: 4900, y: 420 }, { x: 4960, y: 420 }, { x: 5020, y: 420 },
  ];

  protected enemies_data: EnemyDef[] = [
    { x: 400,  y: 460, range: 140 }, { x: 700,  y: 460, range: 130 },
    { x: 1060, y: 280, range: 80  }, { x: 1440, y: 290, range: 80  },
    { x: 1820, y: 190, range: 80  }, { x: 2240, y: 460, range: 150 },
    { x: 2640, y: 220, range: 80  }, { x: 3040, y: 460, range: 150 },
    { x: 3440, y: 250, range: 80  }, { x: 3840, y: 270, range: 80  },
    { x: 4240, y: 190, range: 80  }, { x: 4460, y: 250, range: 100 },
    { x: 4800, y: 460, range: 100, type: 'diablo' },
  ];

  protected extraLives_data: ExtraLifeDef[] = [
    { x: 580,  y: 235 }, { x: 1660, y: 205 },
    { x: 2860, y: 245 }, { x: 4460, y: 215 },
  ];

  private enemies: NarradorEnemy[] = [];
  private diabloHp = 5;
  private diablo?: Phaser.Physics.Arcade.Sprite;
  private diabloHpText?: Phaser.GameObjects.Text;

  protected drawBackground(): void {
    // Dark red gradient sky
    const sky = this.add.graphics();
    sky.fillGradientStyle(0x1A0000, 0x1A0000, 0x0A0010, 0x0A0010, 1);
    sky.fillRect(0, 0, 800, H);
    sky.setScrollFactor(0).setDepth(-10);

    // Dripping neon lines
    for (let i = 0; i < 30; i++) {
      const x = Phaser.Math.Between(0, 800);
      const drip = this.add.graphics();
      drip.fillStyle(0xFF0066, Phaser.Math.FloatBetween(0.1, 0.35));
      drip.fillRect(x, Phaser.Math.Between(0, 300), 2, Phaser.Math.Between(20, 80));
      drip.setScrollFactor(Phaser.Math.FloatBetween(0.05, 0.3)).setDepth(-9);
    }

    // Neon signs in background
    const signs = [
      { x: 120, y: 200, text: '♦' }, { x: 350, y: 160, text: '✦' },
      { x: 580, y: 220, text: '♦' }, { x: 700, y: 180, text: '✦' },
    ];
    for (const s of signs) {
      const t = this.add.text(s.x, s.y, s.text, {
        fontSize: '28px', color: '#FF0066',
      }).setScrollFactor(0.1).setDepth(-8).setAlpha(0.6);
      this.tweens.add({ targets: t, alpha: 0.1, duration: Phaser.Math.Between(400, 900), yoyo: true, repeat: -1 });
    }

    // Floating latex particles
    this.time.addEvent({
      delay: 400, repeat: -1,
      callback: () => {
        const lx = this.cameras.main.scrollX + Phaser.Math.Between(0, 800);
        const p = this.add.graphics();
        p.fillStyle(0xFF0066, 0.4);
        p.fillCircle(lx, -10, Phaser.Math.Between(3, 8));
        this.tweens.add({ targets: p, y: H + 20, duration: Phaser.Math.Between(3000, 6000), onComplete: () => p.destroy() });
      },
    });
  }

  protected spawnEnemies(): void {
    this.enemies = [];
    for (const ep of this.enemies_data) {
      if (ep.type === 'diablo') {
        this.spawnDiablo(ep.x, ep.y);
      } else {
        const e = new NarradorEnemy(this, ep.x, ep.y - 25, ep.range);
        e.setTint(0xFF0044);
        this.enemies.push(e);
        this.allEnemyBullets.push(e.bullets);
        this.physics.add.collider(e, this.platforms);
      }
    }
    this.setupEnemyCollisions();
  }

  private spawnDiablo(x: number, y: number): void {
    // Big red devil boss
    const g = this.make.graphics({}, false);
    // Body
    g.fillStyle(0xCC0022);
    g.fillRoundedRect(4, 10, 52, 50, 8);
    // Horns
    g.fillStyle(0x880011);
    g.fillTriangle(10, 10, 20, 10, 15, -10);
    g.fillTriangle(40, 10, 50, 10, 45, -10);
    // Eyes (glowing)
    g.fillStyle(0xFF4400);
    g.fillCircle(18, 28, 8);
    g.fillCircle(42, 28, 8);
    g.fillStyle(0xFFFF00);
    g.fillCircle(19, 28, 4);
    g.fillCircle(43, 28, 4);
    g.fillStyle(0x000000);
    g.fillCircle(20, 28, 2);
    g.fillCircle(44, 28, 2);
    // Mouth
    g.lineStyle(3, 0xFF4400, 1);
    g.lineBetween(18, 44, 42, 44);
    g.lineBetween(22, 44, 22, 50);
    g.lineBetween(30, 44, 30, 52);
    g.lineBetween(38, 44, 38, 50);
    // Tail
    g.lineStyle(4, 0x880011, 1);
    g.lineBetween(56, 40, 70, 28);
    g.lineBetween(70, 28, 64, 22);
    g.generateTexture('diablo', 80, 70);
    g.destroy();

    this.diablo = this.physics.add.sprite(x, y - 35, 'diablo');
    this.diablo.setDepth(9).setScale(1.4);
    (this.diablo.body as Phaser.Physics.Arcade.Body).setSize(52, 50).setOffset(14, 10);

    // Boss patrol
    const startX = x;
    this.tweens.add({
      targets: this.diablo, x: startX - 100,
      duration: 1800, yoyo: true, repeat: -1, ease: 'Sine.InOut',
    });

    // Shoot fire periodically
    const fireGroup = this.physics.add.group({ defaultKey: 'particle', maxSize: 8 });
    this.allEnemyBullets.push(fireGroup);
    this.time.addEvent({
      delay: 1800, repeat: -1,
      callback: () => {
        if (!this.diablo?.active) return;
        const bullet = fireGroup.get(this.diablo.x, this.diablo.y) as Phaser.Physics.Arcade.Image;
        if (!bullet) return;
        bullet.setActive(true).setVisible(true).setTint(0xFF4400).setScale(2);
        const dir = this.player.x < this.diablo.x ? -1 : 1;
        (bullet.body as Phaser.Physics.Arcade.Body).setVelocity(dir * 320, -80).setAllowGravity(false);
        this.time.delayedCall(2000, () => { bullet.setActive(false).setVisible(false); });
      },
    });

    // HP bar
    this.diabloHpText = this.add.text(x, y - 80, '♥♥♥♥♥', {
      fontSize: '14px', fontFamily: 'Arial', color: '#FF0022',
    }).setOrigin(0.5).setDepth(12);

    // Player bullets hit diablo
    this.physics.add.overlap(this.player.bullets, this.diablo, (bulletObj) => {
      const bullet = bulletObj as Phaser.Physics.Arcade.Image;
      bullet.setActive(false).setVisible(false);
      this.diabloHp--;
      const hearts = '♥'.repeat(Math.max(0, this.diabloHp)) + '♡'.repeat(5 - Math.max(0, this.diabloHp));
      this.diabloHpText?.setText(hearts);
      this.diablo?.setAlpha(0.4);
      this.time.delayedCall(150, () => this.diablo?.setAlpha(1));
      if (this.diabloHp <= 0) this.killDiablo();
    });

    // Diablo touches player
    this.physics.add.overlap(this.player, this.diablo, () => { this.player.hit(); });
  }

  private killDiablo(): void {
    if (!this.diablo) return;
    this.diabloHpText?.destroy();
    const p = this.add.particles(this.diablo.x, this.diablo.y, 'particle', {
      speed: { min: 80, max: 280 }, scale: { start: 1.5, end: 0 },
      lifespan: 700, quantity: 30, tint: [0xFF0022, 0xFF4400, 0xFFFF00],
    });
    this.time.delayedCall(700, () => p.destroy());
    const txt = this.add.text(this.diablo.x, this.diablo.y - 20, '¡EL DIABLO HUYÓ!', {
      fontSize: '20px', fontFamily: 'Impact, sans-serif', color: '#FF4400',
    }).setOrigin(0.5).setDepth(20);
    this.tweens.add({ targets: txt, y: txt.y - 60, alpha: 0, duration: 1200, onComplete: () => txt.destroy() });
    this.player.score += 1000;
    this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
    this.diablo.destroy();
    this.cameras.main.shake(300, 0.02);
  }

  private setupEnemyCollisions(): void {
    for (const enemy of this.enemies) {
      this.physics.add.overlap(this.player.bullets, enemy, (bulletObj) => {
        const b = bulletObj as Phaser.Physics.Arcade.Image;
        b.setActive(false).setVisible(false);
        if (!enemy.isDead) {
          enemy.kill();
          this.player.score += 200;
          this.scoreText.setText(`♪ ${this.player.score.toLocaleString()}`);
        }
      });
      this.physics.add.overlap(this.player, enemy, () => { if (!enemy.isDead) this.player.hit(); });
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
    for (const e of this.enemies) {
      if (!e.isDead) e.update(delta, this.player.x);
    }
    if (this.diabloHpText && this.diablo?.active) {
      this.diabloHpText.setPosition(this.diablo.x, this.diablo.y - 60);
    }
  }
}
