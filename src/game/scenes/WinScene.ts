import * as Phaser from 'phaser';
import { W, H, C } from '../config';

export class WinScene extends Phaser.Scene {
  constructor() {
    super({ key: 'WinScene' });
  }

  create(data: { score: number; notes: number; total: number }): void {
    const score = data?.score ?? 0;
    const notes = data?.notes ?? 0;
    const total = data?.total ?? 1;

    // Background
    const bg = this.add.graphics();
    bg.fillGradientStyle(C.purpleDark, C.purpleDark, C.bg, C.bg, 1);
    bg.fillRect(0, 0, W, H);

    // Continuous fireworks
    this.launchFireworks();

    // Big title
    this.add.text(W / 2 + 3, 73, '¡COMPLETASTE EL JUEGO!', {
      fontSize: '38px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#3D0E6E',
    }).setOrigin(0.5);

    const title = this.add.text(W / 2, 70, '¡COMPLETASTE EL JUEGO!', {
      fontSize: '38px',
      fontFamily: 'Impact, Arial Black, sans-serif',
      color: '#F5A623',
      stroke: '#7B2FBE',
      strokeThickness: 5,
    }).setOrigin(0.5);

    this.tweens.add({
      targets: title,
      scaleX: 1.05,
      scaleY: 1.05,
      duration: 600,
      yoyo: true,
      repeat: -1,
    });

    // Sunshine lyric
    this.add.text(W / 2, 120, '"Sunshine my love — contagiar una idea de no necesitar una excusa real"', {
      fontSize: '11px',
      fontFamily: 'Arial, sans-serif',
      fontStyle: 'italic',
      color: '#B567FF',
      align: 'center',
      wordWrap: { width: 500 },
    }).setOrigin(0.5);

    // Stats panel
    const px = W / 2 - 170;
    const py = 150;
    const panelBg = this.add.graphics();
    panelBg.fillStyle(C.bg, 0.8);
    panelBg.fillRoundedRect(px, py, 340, 140, 12);
    panelBg.lineStyle(2, C.purple, 1);
    panelBg.strokeRoundedRect(px, py, 340, 140, 12);

    this.add.text(W / 2, py + 24, `PUNTAJE  ${score.toLocaleString()}`, {
      fontSize: '26px',
      fontFamily: 'Impact, sans-serif',
      color: '#F5A623',
    }).setOrigin(0.5);

    const notesPct = Math.round((notes / total) * 100);
    this.add.text(W / 2, py + 58, `♪ Notas  ${notes} / ${total}  (${notesPct}%)`, {
      fontSize: '16px',
      fontFamily: 'Arial, sans-serif',
      color: '#B567FF',
    }).setOrigin(0.5);

    let rating = '★★★';
    let ratingColor = '#F5A623';
    if (notesPct < 50) { rating = '★☆☆'; ratingColor = '#888888'; }
    else if (notesPct < 80) { rating = '★★☆'; ratingColor = '#FF5BA3'; }

    const ratingText = this.add.text(W / 2, py + 95, rating, {
      fontSize: '32px',
      fontFamily: 'Arial, sans-serif',
      color: ratingColor,
    }).setOrigin(0.5);

    this.tweens.add({ targets: ratingText, angle: 5, duration: 400, yoyo: true, repeat: -1, ease: 'Sine.InOut' });

    // Buttons
    this.makeButton(W / 2 - 105, 320, '↺  JUGAR DE NUEVO', C.purple, C.pink, () => {
      this.scene.stop('WinScene');
      this.scene.start('GameScene');
    });

    this.makeButton(W / 2 - 105, 378, '⌂  MENÚ PRINCIPAL', C.purpleDark, C.gold, () => {
      this.scene.stop('WinScene');
      this.scene.start('MenuScene');
    });

    // Bottom tag
    this.add.text(W / 2, H - 18, '♪  WAFLES  —  Mudar Piel  ♪', {
      fontSize: '12px',
      fontFamily: 'Arial, sans-serif',
      color: '#7B2FBE',
    }).setOrigin(0.5);

    this.cameras.main.fadeIn(800);
  }

  private launchFireworks(): void {
    const colors = [C.gold, C.pink, C.purple, C.purpleLight, C.white, C.goldLight];
    const shoot = () => {
      const fx = Phaser.Math.Between(80, W - 80);
      const fy = Phaser.Math.Between(50, H * 0.5);
      const p = this.add.particles(fx, fy, 'particle', {
        speed: { min: 60, max: 200 },
        scale: { start: 0.9, end: 0 },
        lifespan: { min: 500, max: 900 },
        quantity: 20,
        tint: Phaser.Utils.Array.Shuffle([...colors]).slice(0, 3),
        angle: { min: 0, max: 360 },
      });
      this.time.delayedCall(900, () => p.destroy());
    };

    for (let i = 0; i < 8; i++) {
      this.time.delayedCall(i * 300, shoot);
    }
    this.time.addEvent({ delay: 2800, callback: shoot, repeat: -1 });
  }

  private makeButton(x: number, y: number, label: string, fill: number, border: number, onClick: () => void): void {
    const g = this.add.graphics();
    g.fillStyle(fill);
    g.fillRoundedRect(x, y, 210, 44, 10);
    g.lineStyle(2, border, 1);
    g.strokeRoundedRect(x, y, 210, 44, 10);

    const t = this.add.text(x + 105, y + 22, label, {
      fontSize: '16px',
      fontFamily: 'Impact, sans-serif',
      color: '#FFFFFF',
    }).setOrigin(0.5);

    const zone = this.add.zone(x + 105, y + 22, 210, 44).setInteractive({ useHandCursor: true });
    zone.on('pointerover', () => { t.setColor('#F5A623'); g.setAlpha(0.8); });
    zone.on('pointerout', () => { t.setColor('#FFFFFF'); g.setAlpha(1); });
    zone.on('pointerdown', onClick);
  }
}
