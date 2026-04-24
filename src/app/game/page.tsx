'use client';
import dynamic from 'next/dynamic';

const WaflesGame = dynamic(() => import('../../components/game/WaflesGame'), {
  ssr: false,
  loading: () => (
    <div
      style={{
        width: '100%',
        maxWidth: '800px',
        aspectRatio: '800/500',
        margin: '0 auto',
        background: '#0A001A',
        borderRadius: '12px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: '#F5A623',
        fontFamily: 'Impact, sans-serif',
        fontSize: '24px',
        letterSpacing: '4px',
      }}
    >
      &#9834; CARGANDO...
    </div>
  ),
});

export default function GamePage() {
  return (
    <main
      style={{
        minHeight: '100vh',
        background: 'linear-gradient(180deg, #0A001A 0%, #1A0840 100%)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '24px 16px',
        gap: '16px',
      }}
    >
      <div
        style={{
          textAlign: 'center',
          marginBottom: '8px',
        }}
      >
        <h1
          style={{
            fontFamily: 'Impact, Arial Black, sans-serif',
            fontSize: 'clamp(28px, 5vw, 48px)',
            color: '#F5A623',
            WebkitTextStroke: '2px #7B2FBE',
            margin: 0,
            letterSpacing: '4px',
          }}
        >
          WAFLES
        </h1>
        <p
          style={{
            fontFamily: 'Impact, sans-serif',
            color: '#FF5BA3',
            fontSize: '14px',
            letterSpacing: '6px',
            margin: '4px 0 0',
          }}
        >
          MUDAR PIEL
        </p>
      </div>

      <WaflesGame />

      <p
        style={{
          fontFamily: 'Arial, sans-serif',
          color: '#7B2FBE',
          fontSize: '12px',
          textAlign: 'center',
          marginTop: '8px',
        }}
      >
        ← → / A D moverse &nbsp;·&nbsp; ↑ / W / SPACE saltar (doble salto disponible) &nbsp;·&nbsp; Z lanzar nota
      </p>

      <a
        href="/"
        style={{
          color: '#B567FF',
          fontFamily: 'Arial, sans-serif',
          fontSize: '13px',
          textDecoration: 'none',
          opacity: 0.7,
        }}
      >
        ← volver al sitio
      </a>
    </main>
  );
}
