// src/app/dashboard/layout.tsx
import React from 'react';

// Este es un layout simple que no requiere autenticación.
// Se aplicará a las páginas de login, registro, etc.
export default function PublicLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
