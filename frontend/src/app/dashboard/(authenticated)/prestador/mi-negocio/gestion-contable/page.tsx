// /app/dashboard/prestador/mi-negocio/gestion-contable/page.tsx
'use client';

import Link from 'next/link';

export default function GestionContablePage() {

  const features = [
    { name: 'Plan de Cuentas', href: '/dashboard/prestador/mi-negocio/gestion-contable/plan-de-cuentas', description: 'Gestione su catálogo de cuentas contables.' },
    { name: 'Asientos Contables', href: '#', description: 'Cree y consulte los asientos o comprobantes contables.' },
    { name: 'Reportes', href: '#', description: 'Genere balances, estados de resultados y otros reportes.' },
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-4 text-gray-800">Módulo de Gestión Contable</h1>
      <p className="text-gray-600 mb-8">
        Aquí puede administrar todos los aspectos contables de su negocio.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {features.map((feature) => (
          <Link href={feature.href} key={feature.name}>
            <div className="block p-6 bg-white rounded-lg border border-gray-200 shadow-md hover:bg-gray-100 transition-colors duration-200 cursor-pointer">
              <h5 className="mb-2 text-xl font-bold tracking-tight text-gray-900">{feature.name}</h5>
              <p className="font-normal text-gray-700">{feature.description}</p>
              {feature.href === '#' && (
                 <span className="text-xs text-blue-500 mt-2 block">(Próximamente)</span>
              )}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
