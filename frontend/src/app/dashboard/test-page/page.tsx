// src/app/[locale]/test-page/page.tsx
import React from 'react';

export default function TestPage() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="p-8 bg-white rounded-lg shadow-md text-center">
        <h1 className="text-2xl font-bold text-green-600">Página de Prueba de Aislamiento</h1>
        <p className="mt-2 text-gray-700">Si puedes ver esto, la ruta y el renderizado básico funcionan.</p>
      </div>
    </div>
  );
}