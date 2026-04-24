import * as Phaser from 'phaser';
import { W, H, C } from '../config';

export class MenuScene extends Phaser.Scene {
  constructor() {
    super({ key: 'MenuScene' });
  }

  create(): void {
    // Gradient background
    const bg = this.add.graphics();
    bg.fillGradientStyle(C.bg, C.bg, C.skyMid, C.skyMid, 1);
    bg.fillRect(0, 0, W, H);

    // Floating stars
    for (let i = 0; i < 60; i++) {
      const x = Phaser.Math.Between(0, W);
      const y = Phaser.Math.Between(0, H * 0.7);
      const s = this.add.graphics();
      s.fillStyle(C.white, Phaser.Math.FloatBetween(0.3, 0.9));
      s.fillCircle(x, y, Phaser.Math.Between(1, 3));
      this.tweens.add({
        targets: s,
        alpha: 0.1,
        duration: Phaser.Math.Between(1000, 3000),
        yoyo: true,
        repeat: -1,
        delay: Phaser.Math.Between(0, 2000),
      });
    }

    // Ground strip
    const ground = this.add.graphics();
    ground.fillStyle(C.purpleDark);
    ground.fillRect(0, H - 60, W, 60);
    ground.fillStyle(C.gold);
    ground.fillRect(0, H - 60, W, 8);

    // Waffle mascot (decorative, large)
    this.drawMascot(150, H - 100);
    this.drawMascot(650, H - 100, 0.8);

    // Main title "WAFLES"
    const titleShadow = this.add.text(W / 2 + 4, 90 + 4, 'WAFLES', {
      fontSize: '72px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#3D0E6E',
    }).setOrigin(0.5);

    const title = this.add.text(W / 2, 90, 'WAFLES', {
      fontSize: '72px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#F5A623',
      stroke: '#7B2FBE',
      strokeThickness: 6,
    }).setOrigin(0.5);

    this.tweens.add({
      targets: title,
      scaleX: 1.04,
      scaleY: 1.04,
      duration: 1200,
      yoyo: true,
      repeat: -1,
      ease: 'Sine.InOut',
    });

    // Subtitle
    this.add.text(W / 2, 155, 'MUDAR PIEL', {
      fontSize: '22px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#FF5BA3',
      letterSpacing: 8,
    }).setOrigin(0.5);

    // World label
    this.add.text(W / 2, 190, '◆  MUNDO 1: SUNSHINE  ◆', {
      fontSize: '14px',
      fontFamily: 'Arial, sans-serif',
      color: '#B567FF',
    }).setOrigin(0.5);

    // Play button
    const btnBg = this.add.graphics();
    btnBg.fillStyle(C.purple);
    btnBg.fillRoundedRect(W / 2 - 110, 240, 220, 54, 12);
    btnBg.lineStyle(3, C.pink, 1);
    btnBg.strokeRoundedRect(W / 2 - 110, 240, 220, 54, 12);

    const btnText = this.add.text(W / 2, 267, '►  JUGAR', {
      fontSize: '26px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#FFFFFF',
    }).setOrigin(0.5);

    const btnZone = this.add.zone(W / 2, 267, 220, 54).setInteractive({ useHandCursor: true });
    btnZone.on('pointerover', () => {
      btnBg.clear();
      btnBg.fillStyle(C.pink);
      btnBg.fillRoundedRect(W / 2 - 110, 240, 220, 54, 12);
      btnBg.lineStyle(3, C.gold, 1);
      btnBg.strokeRoundedRect(W / 2 - 110, 240, 220, 54, 12);
      btnText.setColor('#0A001A');
    });
    btnZone.on('pointerout', () => {
      btnBg.clear();
      btnBg.fillStyle(C.purple);
      btnBg.fillRoundedRect(W / 2 - 110, 240, 220, 54, 12);
      btnBg.lineStyle(3, C.pink, 1);
      btnBg.strokeRoundedRect(W / 2 - 110, 240, 220, 54, 12);
      btnText.setColor('#FFFFFF');
    });
    btnZone.on('pointerdown', () => {
      this.cameras.main.fade(400, 0, 0, 0);
      this.time.delayedCall(400, () => this.scene.start('GameScene'));
    });

    // Also start on ENTER or SPACE
    this.input.keyboard!.once('keydown-ENTER', () => {
      this.cameras.main.fade(400, 0, 0, 0);
      this.time.delayedCall(400, () => this.scene.start('GameScene'));
    });
    this.input.keyboard!.once('keydown-SPACE', () => {
      this.cameras.main.fade(400, 0, 0, 0);
      this.time.delayedCall(400, () => this.scene.start('GameScene'));
    });

    // Controls hint
    this.add.text(W / 2, 320, '← → / A D  moverse    ↑ / W / SPACE  saltar (2x)    Z  lanzar nota', {
      fontSize: '11px',
      fontFamily: 'Arial, sans-serif',
      color: '#B567FF',
      align: 'center',
    }).setOrigin(0.5);

    // Bottom credits
    this.add.text(W / 2, H - 18, '♪  WAFLES  ·  un juego para los fans  ♪', {
      fontSize: '11px',
      fontFamily: 'Arial, sans-serif',
      color: '#7B2FBE',
    }).setOrigin(0.5);

    // Fade in
    this.cameras.main.fadeIn(600);
  }

  private drawMascot(x: number, y: number, scale = 1): void {
    const g = this.add.graphics();
    g.setPosition(x, y);
    const s = scale;

    // Body
    g.fillStyle(C.gold);
    g.fillRoundedRect(-22 * s, -30 * s, 44 * s, 38 * s, 6 * s);
    g.lineStyle(1.5 * s, C.goldDark, 1);
    for (let gx = -14 * s; gx < 22 * s; gx += 8 * s) g.lineBetween(gx, -30 * s, gx, 8 * s);
    for (let gy = -22 * s; gy < 8 * s; gy += 8 * s) g.lineBetween(-22 * s, gy, 22 * s, gy);

    // Sunglasses
    g.fillStyle(0x111111);
    g.fillRoundedRect(-18 * s, -18 * s, 14 * s, 9 * s, 3 * s);
    g.fillRoundedRect(4 * s, -18 * s, 14 * s, 9 * s, 3 * s);
    g.fillRect(-4 * s, -15 * s, 8 * s, 4 * s);

    // Cap
    g.fillStyle(C.purple);
    g.fillRoundedRect(-20 * s, -42 * s, 40 * s, 14 * s, 4 * s);
    g.fillRect(-24 * s, -32 * s, 48 * s, 6 * s);

    // Shoes
    g.fillStyle(C.purple);
    g.fillRoundedRect(-20 * s, 8 * s, 16 * s, 12 * s, 4 * s);
    g.fillRoundedRect(4 * s, 8 * s, 16 * s, 12 * s, 4 * s);

    // Bounce animation
    this.tweens.add({
      targets: g,
      y: y - 12,
      duration: 700 + Phaser.Math.Between(0, 200),
      yoyo: true,
      repeat: -1,
      ease: 'Sine.InOut',
    });
  }
}
