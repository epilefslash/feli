import * as Phaser from 'phaser';
import { W, H, GRAVITY } from './config';
import { BootScene }     from './scenes/BootScene';
import { PreloadScene }  from './scenes/PreloadScene';
import { MenuScene }     from './scenes/MenuScene';
import { GameScene }     from './scenes/GameScene';
import { World2Scene }   from './scenes/World2Scene';
import { World3Scene }   from './scenes/World3Scene';
import { World4Scene }   from './scenes/World4Scene';
import { World5Scene }   from './scenes/World5Scene';
import { GameOverScene } from './scenes/GameOverScene';
import { WinScene }      from './scenes/WinScene';

export function createGame(parent: HTMLElement): Phaser.Game {
  return new Phaser.Game({
    type: Phaser.AUTO,
    width: W,
    height: H,
    parent,
    backgroundColor: '#0A001A',
    physics: {
      default: 'arcade',
      arcade: { gravity: { x: 0, y: GRAVITY }, debug: false },
    },
    scene: [BootScene, PreloadScene, MenuScene, GameScene, World2Scene, World3Scene, World4Scene, World5Scene, GameOverScene, WinScene],
    scale: {
      mode: Phaser.Scale.FIT,
      autoCenter: Phaser.Scale.CENTER_BOTH,
    },
  });
}
