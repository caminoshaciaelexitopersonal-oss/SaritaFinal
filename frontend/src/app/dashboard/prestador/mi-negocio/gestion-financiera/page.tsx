// /app/dashboard/prestador/mi-negocio/gestion-financiera/page.tsx
'use client';

import Link from 'next/link';

export default function GestionFinancieraPage() {

  const features = [
    { name: 'Cuentas Bancarias', href: '/dashboard/prestador/mi-negocio/gestion-financiera/cuentas-bancarias', description: 'Administre sus cuentas bancarias y saldos.' },
    { name: 'Transacciones', href: '/dashboard/prestador/mi-negocio/gestion-financiera/transacciones', description: 'Registre depósitos, retiros y transferencias.' },
    { name: 'Flujo de Caja', href: '#', description: 'Visualice las entradas y salidas de dinero.' },
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-4 text-gray-800">Módulo de Gestión Financiera</h1>
      <p className="text-gray-600 mb-8">
        Controle la tesorería y los movimientos de dinero de su negocio.
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
