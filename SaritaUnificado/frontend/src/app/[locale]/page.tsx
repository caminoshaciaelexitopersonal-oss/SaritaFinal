// src/app/[locale]/page.tsx
import React from 'react';

export default function HomePage() {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      fontFamily: 'sans-serif',
      backgroundColor: '#f0f2f5',
    }}>
      <h1 style={{ fontSize: '3rem', color: '#333' }}>Bienvenido a Sarita Unificado</h1>
      <p style={{ fontSize: '1.2rem', color: '#666' }}>La plataforma de turismo inteligente.</p>
      <p style={{ marginTop: '2rem', color: '#999' }}>Página de inicio en construcción.</p>
    </div>
  );
}
