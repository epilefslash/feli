import * as Phaser from 'phaser';
import { C } from '../config';

export class PreloadScene extends Phaser.Scene {
  constructor() {
    super({ key: 'PreloadScene' });
  }

  create(): void {
    this.makePlayer();
    this.makePlayerJump();
    this.makePlayerHurt();
    this.makePlatformTile();
    this.makeGroundTile();
    this.makeNote();
    this.makeNarrador();
    this.makeSoundWave();
    this.makeHeart();
    this.makeMicrophone();
    this.makeParticle();
    this.makeNoteParticle();
    this.makeStar();
    this.makeBuildings();
    this.scene.start('MenuScene');
  }

  private makePlayer(): void {
    const g = this.make.graphics({}, false);
    // Purple cap
    g.fillStyle(C.purple);
    g.fillRoundedRect(5, 0, 30, 10, 3);
    g.fillRect(2, 8, 36, 5);
    // Cap detail
    g.fillStyle(C.purpleLight);
    g.fillRect(20, 2, 12, 4);
    // Waffle body
    g.fillStyle(C.gold);
    g.fillRoundedRect(4, 11, 32, 28, 5);
    // Grid lines
    g.lineStyle(1.5, C.goldDark, 1);
    for (let x = 11; x < 36; x += 8) {
      g.lineBetween(x, 11, x, 39);
    }
    for (let y = 18; y < 39; y += 8) {
      g.lineBetween(4, y, 36, y);
    }
    // Sunglasses
    g.fillStyle(0x111111);
    g.fillRoundedRect(6, 17, 11, 8, 3);
    g.fillRoundedRect(23, 17, 11, 8, 3);
    g.fillRect(17, 19, 6, 4);
    // Lens shine
    g.fillStyle(C.white, 0.5);
    g.fillRect(7, 18, 4, 3);
    g.fillRect(24, 18, 4, 3);
    // Smile
    g.lineStyle(2, C.pink, 1);
    g.beginPath();
    g.arc(20, 31, 5, 0, Math.PI);
    g.strokePath();
    // Purple shoes
    g.fillStyle(C.purple);
    g.fillRoundedRect(5, 37, 12, 10, 3);
    g.fillRoundedRect(23, 37, 12, 10, 3);
    // White shoe stripe
    g.fillStyle(C.white);
    g.fillRect(6, 43, 5, 2);
    g.fillRect(24, 43, 5, 2);
    // "W" on shoe
    g.fillStyle(C.pink);
    g.fillRect(8, 40, 2, 2);
    g.fillRect(25, 40, 2, 2);
    g.generateTexture('player', 40, 47);
    g.destroy();
  }

  private makePlayerJump(): void {
    const g = this.make.graphics({}, false);
    // Same waffle body but legs up/together
    g.fillStyle(C.purple);
    g.fillRoundedRect(5, 0, 30, 10, 3);
    g.fillRect(2, 8, 36, 5);
    g.fillStyle(C.purpleLight);
    g.fillRect(20, 2, 12, 4);
    g.fillStyle(C.gold);
    g.fillRoundedRect(4, 11, 32, 28, 5);
    g.lineStyle(1.5, C.goldDark, 1);
    for (let x = 11; x < 36; x += 8) g.lineBetween(x, 11, x, 39);
    for (let y = 18; y < 39; y += 8) g.lineBetween(4, y, 36, y);
    g.fillStyle(0x111111);
    g.fillRoundedRect(6, 17, 11, 8, 3);
    g.fillRoundedRect(23, 17, 11, 8, 3);
    g.fillRect(17, 19, 6, 4);
    g.fillStyle(C.white, 0.5);
    g.fillRect(7, 18, 4, 3);
    g.fillRect(24, 18, 4, 3);
    // O mouth (surprised face for jump)
    g.fillStyle(0x111111);
    g.fillCircle(20, 32, 4);
    g.fillStyle(C.pink);
    g.fillCircle(20, 32, 2.5);
    // Shoes tucked up
    g.fillStyle(C.purple);
    g.fillRoundedRect(8, 37, 10, 9, 3);
    g.fillRoundedRect(22, 37, 10, 9, 3);
    g.fillStyle(C.white);
    g.fillRect(9, 42, 4, 2);
    g.fillRect(23, 42, 4, 2);
    g.generateTexture('player_jump', 40, 47);
    g.destroy();
  }

  private makePlayerHurt(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.pink, 0.9);
    g.fillRoundedRect(4, 11, 32, 28, 5);
    g.lineStyle(1.5, C.pinkDark, 1);
    for (let x = 11; x < 36; x += 8) g.lineBetween(x, 11, x, 39);
    for (let y = 18; y < 39; y += 8) g.lineBetween(4, y, 36, y);
    g.fillStyle(0x111111);
    g.fillRoundedRect(6, 17, 11, 8, 3);
    g.fillRoundedRect(23, 17, 11, 8, 3);
    g.fillRect(17, 19, 6, 4);
    // X eyes
    g.lineStyle(2, C.white, 1);
    g.lineBetween(7, 18, 11, 22);
    g.lineBetween(11, 18, 7, 22);
    g.lineBetween(24, 18, 28, 22);
    g.lineBetween(28, 18, 24, 22);
    g.generateTexture('player_hurt', 40, 47);
    g.destroy();
  }

  private makePlatformTile(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.gold);
    g.fillRect(0, 0, 32, 16);
    g.lineStyle(1, C.goldDark, 0.8);
    for (let x = 0; x <= 32; x += 8) g.lineBetween(x, 0, x, 16);
    for (let y = 0; y <= 16; y += 8) g.lineBetween(0, y, 32, y);
    // Top highlight
    g.fillStyle(C.goldLight, 0.4);
    g.fillRect(0, 0, 32, 3);
    // Bottom shadow
    g.fillStyle(C.goldDark, 0.6);
    g.fillRect(0, 14, 32, 2);
    g.generateTexture('platform_tile', 32, 16);
    g.destroy();
  }

  private makeGroundTile(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.purpleDark);
    g.fillRect(0, 0, 32, 32);
    g.fillStyle(C.gold);
    g.fillRect(0, 0, 32, 8);
    g.lineStyle(1, C.goldDark, 0.8);
    for (let x = 0; x <= 32; x += 8) g.lineBetween(x, 0, x, 8);
    g.fillStyle(C.goldLight, 0.3);
    g.fillRect(0, 0, 32, 2);
    g.generateTexture('ground_tile', 32, 32);
    g.destroy();
  }

  private makeNote(): void {
    const g = this.make.graphics({}, false);
    // Note head
    g.fillStyle(C.purple);
    g.fillEllipse(8, 16, 14, 11);
    g.fillStyle(C.purpleLight);
    g.fillEllipse(6, 14, 6, 5);
    // Stem
    g.lineStyle(3, C.purple, 1);
    g.lineBetween(14, 11, 14, 2);
    // Flag
    g.lineStyle(2, C.purple, 1);
    g.beginPath();
    g.moveTo(14, 2);
    g.lineTo(20, 5);
    g.lineTo(15, 9);
    g.strokePath();
    // Sparkle
    g.fillStyle(C.pink, 0.8);
    g.fillCircle(19, 4, 2);
    g.generateTexture('note', 24, 20);
    g.destroy();
  }

  private makeNarrador(): void {
    const g = this.make.graphics({}, false);
    // Body
    g.fillStyle(C.purpleDark);
    g.fillRoundedRect(4, 8, 30, 28, 5);
    // Highlight
    g.fillStyle(C.purpleLight, 0.3);
    g.fillRoundedRect(6, 10, 12, 8, 3);
    // Eyes (angry)
    g.fillStyle(C.pink);
    g.fillEllipse(12, 18, 8, 6);
    g.fillEllipse(26, 18, 8, 6);
    g.fillStyle(0x111111);
    g.fillCircle(13, 18, 2.5);
    g.fillCircle(27, 18, 2.5);
    // Angry eyebrows
    g.lineStyle(2, C.pink, 1);
    g.lineBetween(9, 13, 16, 15);
    g.lineBetween(30, 13, 23, 15);
    // Mouth (megaphone)
    g.fillStyle(C.goldDark);
    g.fillRect(6, 28, 18, 6);
    // Megaphone
    g.fillStyle(C.gold);
    g.fillTriangle(24, 28, 24, 34, 38, 22);
    g.fillStyle(C.goldDark);
    g.fillRect(22, 28, 4, 6);
    // Legs
    g.fillStyle(C.purpleDark);
    g.fillRect(8, 36, 8, 10);
    g.fillRect(22, 36, 8, 10);
    // Boots
    g.fillStyle(0x111111);
    g.fillRoundedRect(6, 42, 12, 8, 2);
    g.fillRoundedRect(20, 42, 12, 8, 2);
    g.generateTexture('narrador', 42, 50);
    g.destroy();
  }

  private makeSoundWave(): void {
    const g = this.make.graphics({}, false);
    g.lineStyle(2, C.pink, 0.9);
    g.beginPath();
    g.arc(12, 8, 4, -0.5, 0.5);
    g.strokePath();
    g.lineStyle(2, C.pink, 0.65);
    g.beginPath();
    g.arc(12, 8, 8, -0.6, 0.6);
    g.strokePath();
    g.lineStyle(2, C.purpleLight, 0.4);
    g.beginPath();
    g.arc(12, 8, 12, -0.7, 0.7);
    g.strokePath();
    g.generateTexture('sound_wave', 28, 16);
    g.destroy();
  }

  private makeHeart(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.pink);
    g.fillCircle(7, 7, 6);
    g.fillCircle(15, 7, 6);
    g.fillTriangle(1, 10, 21, 10, 11, 22);
    // Shine
    g.fillStyle(C.white, 0.5);
    g.fillCircle(6, 5, 2.5);
    g.generateTexture('heart', 22, 22);
    g.destroy();
  }

  private makeMicrophone(): void {
    const g = this.make.graphics({}, false);
    // Mic head
    g.fillStyle(C.gray);
    g.fillRoundedRect(18, 4, 24, 34, 10);
    g.fillStyle(0x555555);
    // Mesh grid on mic
    for (let mx = 22; mx < 40; mx += 4) g.fillRect(mx, 8, 2, 26);
    for (let my = 10; my < 34; my += 6) g.fillRect(18, my, 24, 2);
    // Highlight
    g.fillStyle(C.white, 0.4);
    g.fillRoundedRect(20, 6, 8, 12, 4);
    // Stand
    g.lineStyle(4, C.gold, 1);
    g.lineBetween(30, 38, 30, 72);
    // Base
    g.fillStyle(C.gold);
    g.fillEllipse(30, 74, 40, 10);
    g.fillStyle(C.goldLight, 0.5);
    g.fillEllipse(30, 72, 20, 5);
    // Wafles "W" on base
    g.fillStyle(C.purple);
    g.fillRect(20, 72, 3, 6);
    g.fillRect(25, 72, 3, 6);
    g.fillRect(30, 72, 3, 6);
    g.generateTexture('microphone', 60, 80);
    g.destroy();
  }

  private makeParticle(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.gold);
    g.fillCircle(4, 4, 4);
    g.generateTexture('particle', 8, 8);
    g.destroy();
  }

  private makeNoteParticle(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.purple);
    g.fillCircle(3, 3, 3);
    g.generateTexture('note_particle', 6, 6);
    g.destroy();
  }

  private makeStar(): void {
    const g = this.make.graphics({}, false);
    g.fillStyle(C.white);
    g.fillRect(3, 0, 2, 8);
    g.fillRect(0, 3, 8, 2);
    g.generateTexture('star', 8, 8);
    g.destroy();
  }

  private makeBuildings(): void {
    // Far background buildings
    const g1 = this.make.graphics({}, false);
    g1.fillStyle(C.purpleDark);
    const farBuildings = [
      [0, 160, 60, 200], [70, 100, 80, 260], [160, 140, 50, 220],
      [220, 80, 70, 280], [300, 120, 60, 240], [370, 60, 90, 300],
      [470, 100, 70, 260], [550, 140, 50, 220], [610, 80, 80, 280],
      [700, 120, 60, 240], [770, 100, 80, 260], [860, 60, 70, 300],
      [940, 140, 60, 220], [1010, 90, 80, 270], [1100, 120, 70, 240],
      [1180, 70, 60, 290], [1250, 100, 80, 260], [1340, 140, 60, 220],
    ];
    for (const [x, y, w, h] of farBuildings) g1.fillRect(x, y, w, h);
    // Windows
    g1.fillStyle(C.goldLight, 0.5);
    for (const [x, y, w] of farBuildings) {
      for (let wy = y + 10; wy < 360; wy += 20) {
        for (let wx = x + 5; wx < x + w - 5; wx += 12) {
          if (Math.random() > 0.4) g1.fillRect(wx, wy, 5, 8);
        }
      }
    }
    g1.generateTexture('bg_far', 1400, 360);
    g1.destroy();

    // Near buildings (darker, larger)
    const g2 = this.make.graphics({}, false);
    g2.fillStyle(0x150030);
    const nearBuildings = [
      [0, 200, 80, 200], [90, 140, 100, 260], [200, 180, 70, 220],
      [280, 100, 90, 300], [380, 160, 80, 240], [470, 80, 110, 320],
      [590, 140, 80, 260], [680, 100, 90, 300], [780, 180, 70, 220],
      [860, 120, 100, 280],
    ];
    for (const [x, y, w, h] of nearBuildings) g2.fillRect(x, y, w, h);
    g2.fillStyle(C.gold, 0.2);
    for (const [x, y, w] of nearBuildings) {
      for (let wy = y + 15; wy < 380; wy += 25) {
        for (let wx = x + 8; wx < x + w - 8; wx += 15) {
          if (Math.random() > 0.5) g2.fillRect(wx, wy, 6, 10);
        }
      }
    }
    g2.generateTexture('bg_near', 960, 380);
    g2.destroy();
  }
}
