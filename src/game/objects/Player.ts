import * as Phaser from 'phaser';
import { C, SPEED, JUMP_VEL, DOUBLE_JUMP, SHOOT_COOLDOWN } from '../config';

export class Player extends Phaser.Physics.Arcade.Sprite {
  private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
  private wasd!: Record<string, Phaser.Input.Keyboard.Key>;
  private shootKey!: Phaser.Input.Keyboard.Key;
  private spaceKey!: Phaser.Input.Keyboard.Key;

  private jumpCount = 0;
  private canJump = false;
  private justJumped = false;
  private jumpKeyHeld = false;

  private shootCooldown = 0;
  private invincibleTimer = 0;

  lives = 3;
  score = 0;
  isDead = false;

  bullets!: Phaser.Physics.Arcade.Group;

  onDie?: () => void;
  onScoreChange?: (score: number) => void;
  onLivesChange?: (lives: number) => void;

  constructor(scene: Phaser.Scene, x: number, y: number) {
    super(scene, x, y, 'player');
    scene.add.existing(this);
    scene.physics.add.existing(this);

    const body = this.body as Phaser.Physics.Arcade.Body;
    body.setSize(28, 36);
    body.setOffset(6, 11);

    this.cursors = scene.input.keyboard!.createCursorKeys();
    this.wasd = scene.input.keyboard!.addKeys('W,A,S,D') as Record<string, Phaser.Input.Keyboard.Key>;
    this.shootKey = scene.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.Z);
    this.spaceKey = scene.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);

    this.bullets = scene.physics.add.group({
      defaultKey: 'note',
      maxSize: 8,
      runChildUpdate: true,
    });

    this.setDepth(10);
  }

  update(delta: number): void {
    if (this.isDead) return;

    const body = this.body as Phaser.Physics.Arcade.Body;
    const onGround = body.blocked.down;
    const left = this.cursors.left.isDown || this.wasd['A'].isDown;
    const right = this.cursors.right.isDown || this.wasd['D'].isDown;
    const jumpPressed =
      Phaser.Input.Keyboard.JustDown(this.cursors.up) ||
      Phaser.Input.Keyboard.JustDown(this.wasd['W']) ||
      Phaser.Input.Keyboard.JustDown(this.spaceKey);

    if (onGround) this.jumpCount = 0;

    // Horizontal
    if (left) {
      body.setVelocityX(-SPEED);
      this.setFlipX(true);
    } else if (right) {
      body.setVelocityX(SPEED);
      this.setFlipX(false);
    } else {
      const vx = body.velocity.x;
      body.setVelocityX(vx * (onGround ? 0.75 : 0.92));
      if (Math.abs(body.velocity.x) < 5) body.setVelocityX(0);
    }

    // Jump
    if (jumpPressed && this.jumpCount < 2) {
      const vel = this.jumpCount === 0 ? JUMP_VEL : DOUBLE_JUMP;
      body.setVelocityY(vel);
      this.jumpCount++;
      if (this.jumpCount === 2) {
        this.spawnDoubleJumpEffect();
      }
    }

    // Texture by state
    if (!onGround) {
      this.setTexture('player_jump');
    } else {
      this.setTexture('player');
    }

    // Shoot
    this.shootCooldown -= delta;
    if (Phaser.Input.Keyboard.JustDown(this.shootKey) && this.shootCooldown <= 0) {
      this.shoot();
      this.shootCooldown = SHOOT_COOLDOWN;
    }

    // Invincibility flash
    if (this.invincibleTimer > 0) {
      this.invincibleTimer -= delta;
      this.setAlpha(Math.floor(this.invincibleTimer / 80) % 2 === 0 ? 1 : 0.3);
      if (this.invincibleTimer <= 0) this.setAlpha(1);
    }

    // Kill if fell off world
    if (this.y > 600) this.die();
  }

  private shoot(): void {
    const bullet = this.bullets.get(this.x, this.y + 5) as Phaser.Physics.Arcade.Image;
    if (!bullet) return;
    bullet.setActive(true).setVisible(true).setDepth(9);
    bullet.setScale(1.2);
    const direction = this.flipX ? -1 : 1;
    (bullet.body as Phaser.Physics.Arcade.Body).setVelocity(direction * 380, -60);
    (bullet.body as Phaser.Physics.Arcade.Body).setAllowGravity(false);

    this.scene.time.delayedCall(1200, () => {
      bullet.setActive(false).setVisible(false);
    });
  }

  private spawnDoubleJumpEffect(): void {
    const particles = this.scene.add.particles(this.x, this.y + 20, 'particle', {
      speed: { min: 40, max: 120 },
      scale: { start: 0.8, end: 0 },
      lifespan: 400,
      quantity: 10,
      tint: [C.purple, C.pink, C.gold],
      gravityY: -50,
    });
    this.scene.time.delayedCall(400, () => particles.destroy());
  }

  hit(): void {
    if (this.invincibleTimer > 0 || this.isDead) return;
    this.lives--;
    this.onLivesChange?.(this.lives);
    this.invincibleTimer = 1500;
    this.setTexture('player_hurt');

    // Knockback
    const body = this.body as Phaser.Physics.Arcade.Body;
    body.setVelocityY(-200);

    this.scene.cameras.main.shake(150, 0.012);

    if (this.lives <= 0) {
      this.scene.time.delayedCall(300, () => this.die());
    }
  }

  die(): void {
    if (this.isDead) return;
    this.isDead = true;
    const body = this.body as Phaser.Physics.Arcade.Body;
    body.setVelocity(0, -300);
    body.setAllowGravity(true);
    this.scene.time.delayedCall(800, () => this.onDie?.());
  }

  collectNote(): void {
    this.score += 100;
    this.onScoreChange?.(this.score);
  }
}
