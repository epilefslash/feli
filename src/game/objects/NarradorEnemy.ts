import * as Phaser from 'phaser';
import { BULLET_SPEED } from '../config';

export class NarradorEnemy extends Phaser.Physics.Arcade.Sprite {
  private patrol: number;
  private startX: number;
  private direction = 1;
  private shootTimer = 0;
  private shootInterval: number;

  bullets: Phaser.Physics.Arcade.Group;
  isDead = false;

  constructor(scene: Phaser.Scene, x: number, y: number, patrolRange = 120) {
    super(scene, x, y, 'narrador');
    scene.add.existing(this);
    scene.physics.add.existing(this);

    this.patrol = patrolRange;
    this.startX = x;
    this.shootInterval = Phaser.Math.Between(2200, 3800);
    this.setDepth(9);

    const body = this.body as Phaser.Physics.Arcade.Body;
    body.setSize(28, 42);
    body.setOffset(7, 8);

    this.bullets = scene.physics.add.group({
      defaultKey: 'sound_wave',
      maxSize: 4,
    });
  }

  update(delta: number, playerX: number): void {
    if (this.isDead) return;

    const body = this.body as Phaser.Physics.Arcade.Body;

    // Patrol
    body.setVelocityX(this.direction * 70);
    this.setFlipX(this.direction < 0);

    if (this.x > this.startX + this.patrol) {
      this.direction = -1;
    } else if (this.x < this.startX - this.patrol) {
      this.direction = 1;
    }

    // Turn to face player
    if (playerX < this.x) {
      this.setFlipX(true);
    } else {
      this.setFlipX(false);
    }

    // Shoot
    this.shootTimer += delta;
    if (this.shootTimer >= this.shootInterval) {
      this.shootTimer = 0;
      this.shootInterval = Phaser.Math.Between(2200, 3800);
      this.shootAtPlayer(playerX);
    }
  }

  private shootAtPlayer(playerX: number): void {
    const bullet = this.bullets.get(this.x + (playerX < this.x ? -20 : 20), this.y + 10) as Phaser.Physics.Arcade.Image;
    if (!bullet) return;
    bullet.setActive(true).setVisible(true).setDepth(8);
    bullet.setScale(1.5);
    const dir = playerX < this.x ? -1 : 1;
    (bullet.body as Phaser.Physics.Arcade.Body).setVelocity(dir * BULLET_SPEED, -30);
    (bullet.body as Phaser.Physics.Arcade.Body).setAllowGravity(false);

    this.scene.time.delayedCall(2000, () => {
      bullet.setActive(false).setVisible(false);
    });
  }

  kill(): void {
    if (this.isDead) return;
    this.isDead = true;

    const particles = this.scene.add.particles(this.x, this.y, 'particle', {
      speed: { min: 60, max: 180 },
      scale: { start: 0.7, end: 0 },
      lifespan: 500,
      quantity: 12,
      tint: [0x7B2FBE, 0xFF5BA3],
    });
    this.scene.time.delayedCall(500, () => particles.destroy());

    this.scene.tweens.add({
      targets: this,
      y: this.y - 40,
      alpha: 0,
      duration: 400,
      onComplete: () => this.destroy(),
    });

    this.bullets.getChildren().forEach((b) => {
      (b as Phaser.GameObjects.GameObject).destroy();
    });
  }
}
