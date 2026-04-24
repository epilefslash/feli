import * as Phaser from 'phaser';
import { W, H, GRAVITY } from './config';
import { BootScene } from './scenes/BootScene';
import { PreloadScene } from './scenes/PreloadScene';
import { MenuScene } from './scenes/MenuScene';
import { GameScene } from './scenes/GameScene';
import { GameOverScene } from './scenes/GameOverScene';
import { WinScene } from './scenes/WinScene';

export function createGame(parent: HTMLElement): Phaser.Game {
  return new Phaser.Game({
    type: Phaser.AUTO,
    width: W,
    height: H,
    parent,
    backgroundColor: '#0A001A',
    physics: {
      default: 'arcade',
      arcade: {
        gravity: { x: 0, y: GRAVITY },
        debug: false,
      },
    },
    scene: [BootScene, PreloadScene, MenuScene, GameScene, GameOverScene, WinScene],
    scale: {
      mode: Phaser.Scale.FIT,
      autoCenter: Phaser.Scale.CENTER_BOTH,
    },
  });
}
