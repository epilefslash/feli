'use client';
import { useEffect, useRef } from 'react';
import type Phaser from 'phaser';

// Singleton global para evitar múltiples instancias en dev/HMR
let globalGame: Phaser.Game | null = null;

export default function WaflesGame() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Destruir instancia previa si existe (React StrictMode / HMR)
    if (globalGame) {
      globalGame.destroy(true);
      globalGame = null;
      // Limpiar canvas huérfano si quedó
      const old = document.getElementById('wafles-game');
      if (old) old.querySelectorAll('canvas').forEach(c => c.remove());
    }

    let cancelled = false;

    import('../../game/index').then(({ createGame }) => {
      if (cancelled || !containerRef.current) return;
      globalGame = createGame(containerRef.current);
    });

    return () => {
      cancelled = true;
      if (globalGame) {
        globalGame.destroy(true);
        globalGame = null;
      }
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
