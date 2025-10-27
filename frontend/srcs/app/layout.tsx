// src/app/layout.tsx
import React from 'react';

// Este es el layout raíz requerido por Next.js App Router.
// Debe contener las etiquetas <html> y <body>.
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        {children}
      </body>
    </html>
  );
}
