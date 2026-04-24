'use client';
import { useEffect, useRef } from 'react';
import type Phaser from 'phaser';

export default function WaflesGame() {
  const containerRef = useRef<HTMLDivElement>(null);
  const gameRef = useRef<Phaser.Game | null>(null);

  useEffect(() => {
    if (!containerRef.current || gameRef.current) return;

    let game: Phaser.Game | null = null;

    import('../../game/index').then(({ createGame }) => {
      if (!containerRef.current) return;
      game = createGame(containerRef.current);
      gameRef.current = game;
    });

    return () => {
      game?.destroy(true);
      gameRef.current = null;
    };
  }, []);

  return (
    <div
      ref={containerRef}
      id="wafles-game"
      style={{
        width: '100%',
        maxWidth: '800px',
        aspectRatio: '800 / 500',
        margin: '0 auto',
        display: 'block',
        background: '#0A001A',
        borderRadius: '12px',
        overflow: 'hidden',
        boxShadow: '0 0 40px rgba(123,47,190,0.6), 0 0 80px rgba(255,91,163,0.2)',
      }}
    />
  );
}
