import React from 'react';
import Link from 'next/link';

export default function PrestadorLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-gray-800 text-white p-4">
        <h2 className="text-xl font-bold mb-4">Panel del Prestador</h2>
        <nav>
          <ul>
            <li><Link href="/prestador/dashboard" className="block py-2 px-4 hover:bg-gray-700 rounded">Dashboard</Link></li>
            <li><Link href="/prestador/servicios" className="block py-2 px-4 hover:bg-gray-700 rounded">Servicios</Link></li>
            <li><Link href="/prestador/reservas" className="block py-2 px-4 hover:bg-gray-700 rounded">Reservas</Link></li>
            <li><Link href="/prestador/facturacion" className="block py-2 px-4 hover:bg-gray-700 rounded">Facturación</Link></li>
          </ul>
        </nav>
      </aside>
      <main className="flex-1 p-8 bg-gray-100">
        {children}
      </main>
    </div>
  );
}