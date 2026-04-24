import * as Phaser from 'phaser';
import { W, H, C } from '../config';

export class GameOverScene extends Phaser.Scene {
  constructor() {
    super({ key: 'GameOverScene' });
  }

  create(data: { score: number }): void {
    const score = data?.score ?? 0;

    // Dark overlay
    const bg = this.add.graphics();
    bg.fillStyle(C.bg, 0.97);
    bg.fillRect(0, 0, W, H);

    // Sad mascot
    this.drawSadMascot(W / 2, H / 2 + 60);

    // Game Over title
    this.add.text(W / 2 + 4, 104, 'GAME OVER', {
      fontSize: '60px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#3D0E6E',
    }).setOrigin(0.5);

    this.add.text(W / 2, 100, 'GAME OVER', {
      fontSize: '60px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#FF5BA3',
      stroke: '#7B2FBE',
      strokeThickness: 5,
    }).setOrigin(0.5);

    // Flavor text from lyrics
    const flavors = [
      '"Tengo que mudar piel de nuevo..."',
      '"Mis fantasmas no me dejan dormir"',
      '"Este papelon está armado"',
      '"Qué alguien llame a alguien que me apague la luz"',
    ];
    this.add.text(W / 2, 158, flavors[Phaser.Math.Between(0, flavors.length - 1)], {
      fontSize: '13px',
      fontFamily: 'Arial, sans-serif',
      fontStyle: 'italic',
      color: '#B567FF',
    }).setOrigin(0.5);

    // Score
    this.add.text(W / 2, 195, `PUNTAJE FINAL: ${score.toLocaleString()}`, {
      fontSize: '22px',
      fontFamily: 'Impact, sans-serif',
      color: '#F5A623',
    }).setOrigin(0.5);

    // Buttons (stacked vertically)
    this.makeButton(W / 2 - 100, 240, '↺  REINTENTAR', C.purple, C.pink, () => {
      this.cameras.main.fade(300, 0, 0, 0);
      this.time.delayedCall(300, () => this.scene.start('GameScene'));
    });

    this.makeButton(W / 2 - 100, 305, '⌂  MENÚ PRINCIPAL', C.purpleDark, C.gold, () => {
      this.cameras.main.fade(300, 0, 0, 0);
      this.time.delayedCall(300, () => this.scene.start('MenuScene'));
    });

    this.cameras.main.fadeIn(500);
  }

  private makeButton(x: number, y: number, label: string, fill: number, border: number, onClick: () => void): void {
    const g = this.add.graphics();
    g.fillStyle(fill);
    g.fillRoundedRect(x, y, 200, 48, 10);
    g.lineStyle(2, border, 1);
    g.strokeRoundedRect(x, y, 200, 48, 10);

    const t = this.add.text(x + 100, y + 24, label, {
      fontSize: '18px',
      fontFamily: 'Impact, sans-serif',
      color: '#FFFFFF',
    }).setOrigin(0.5);

    const zone = this.add.zone(x + 100, y + 24, 200, 48).setInteractive({ useHandCursor: true });
    zone.on('pointerover', () => { t.setColor('#F5A623'); g.setAlpha(0.8); });
    zone.on('pointerout', () => { t.setColor('#FFFFFF'); g.setAlpha(1); });
    zone.on('pointerdown', onClick);
  }

  private drawSadMascot(x: number, y: number): void {
    const g = this.add.graphics().setPosition(x, y);

    g.fillStyle(C.gold, 0.8);
    g.fillRoundedRect(-22, -40, 44, 38, 6);
    g.lineStyle(1.5, C.goldDark, 0.8);
    for (let gx = -14; gx < 22; gx += 8) g.lineBetween(gx, -40, gx, -2);
    for (let gy = -32; gy < -2; gy += 8) g.lineBetween(-22, gy, 22, gy);

    // X eyes
    g.lineStyle(3, C.pink, 1);
    g.lineBetween(-14, -28, -6, -20);
    g.lineBetween(-6, -28, -14, -20);
    g.lineBetween(6, -28, 14, -20);
    g.lineBetween(14, -28, 6, -20);

    // Frown
    g.lineStyle(2, C.purple, 1);
    g.beginPath();
    g.arc(0, -6, 5, Math.PI, 0);
    g.strokePath();

    g.fillStyle(C.purple);
    g.fillRoundedRect(-20, -2, 16, 12, 3);
    g.fillRoundedRect(4, -2, 16, 12, 3);

    this.tweens.add({ targets: g, angle: -5, duration: 600, yoyo: true, repeat: -1, ease: 'Sine.InOut' });
  }
}
