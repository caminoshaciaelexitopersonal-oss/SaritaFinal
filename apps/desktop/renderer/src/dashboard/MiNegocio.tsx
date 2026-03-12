import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { ShoppingCart, Users, Target, Tag, BarChart3, Briefcase, Anchor, FileText, Calculator, Landmark } from 'lucide-react';

export const BusinessManager = () => {
  const navItems = [
    { label: 'Resumen', path: '', icon: Briefcase },
    { label: 'Clientes', path: 'clientes', icon: Users },
    { label: 'Oportunidades', path: 'oportunidades', icon: Target },
    { label: 'Ventas', path: 'ventas', icon: ShoppingCart },
    { label: 'Promociones', path: 'promociones', icon: Tag },
    { label: 'Operaciones', path: 'operaciones', icon: Anchor },
    { label: 'Archivo', path: 'archivo', icon: FileText },
    { label: 'Contabilidad', path: 'contabilidad', icon: Calculator },
    { label: 'Finanzas', path: 'finanzas', icon: Landmark },
    { label: 'Reportes', path: 'reportes', icon: BarChart3 },
  ];

  return (
    <div className="space-y-8">
      <header className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
        <h2 className="text-xl font-bold text-primary mb-6 flex items-center gap-2">
          <Briefcase size={24} /> Tablero Mi Negocio - ERP
        </h2>
        <nav className="flex gap-4 overflow-x-auto pb-2">
          {navItems.map(item => (
            <NavLink
              key={item.label}
              to={item.path}
              end
              className={({ isActive }) => `flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition whitespace-nowrap ${isActive ? 'bg-primary text-white' : 'text-gray-500 hover:bg-gray-50'}`}
            >
              <item.icon size={16} />
              {item.label}
            </NavLink>
          ))}
        </nav>
      </header>

      <div className="min-h-[500px]">
        <Outlet />
      </div>
    </div>
  );
};

import { InventoryWidget, PayrollSnapshot, StatCard, StatGrid } from '@sarita/shared-ui';

export const BusinessSummary = () => {
  const PRESTADOR_MOCK = {
    inventory: [
      { id: '1', name: 'Toallas Blancas', stock: 15, minStock: 20, unit: 'unidades' },
      { id: '2', name: 'Jabón Biodegradable', stock: 50, minStock: 10, unit: 'litros' }
    ],
    payroll: {
      totalEmployees: 12,
      totalPayable: "$8,500,000",
      nextPaymentDate: "30 Mar 2026",
      pendingLiquidations: 1
    },
    stats: {
      revenue: "$45.2M",
      bookings: 85,
      satisfaction: "4.8/5"
    }
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <StatGrid columns={3}>
        <StatCard title="Ventas Totales" value={PRESTADOR_MOCK.stats.revenue} trend="+12%" trendDirection="up" />
        <StatCard title="Reservas" value={PRESTADOR_MOCK.stats.bookings} trend="+5%" trendDirection="up" />
        <StatCard title="Reputación" value={PRESTADOR_MOCK.stats.satisfaction} />
      </StatGrid>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <PayrollSnapshot data={PRESTADOR_MOCK.payroll} />
        <InventoryWidget items={PRESTADOR_MOCK.inventory} />
      </div>
    </div>
  );
};
