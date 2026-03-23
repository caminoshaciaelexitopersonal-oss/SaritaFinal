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

import { useState, useEffect } from 'react';
import { httpClient } from '../../../../../sarita-platform/shared-sdk/src/api/httpClient';

export const BusinessSummary = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await httpClient.get('/providers/business-profiles/me/');
        setData(response.data);
      } catch (error) {
        console.error("Error loading profile", error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <div className="p-10 text-center animate-pulse">Cargando datos empresariales...</div>;

  const stats = data?.stats || {
    revenue: "$0",
    bookings: 0,
    satisfaction: "N/A"
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <StatGrid columns={3}>
        <StatCard title="Ventas Totales" value={stats.revenue} trend={data?.trends?.revenue} trendDirection="up" />
        <StatCard title="Reservas" value={stats.bookings} trend={data?.trends?.bookings} trendDirection="up" />
        <StatCard title="Reputación" value={stats.satisfaction} />
      </StatGrid>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <PayrollSnapshot data={data?.payroll || {}} />
        <InventoryWidget items={data?.inventory || []} />
      </div>
    </div>
  );
};
