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
          <Briefcase size={24} /> Gestión Comercial y CRM
        </h2>
        <nav className="flex gap-4">
          {navItems.map(item => (
            <NavLink
              key={item.label}
              to={item.path}
              end
              className={({ isActive }) => `flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition ${isActive ? 'bg-primary text-white' : 'text-gray-500 hover:bg-gray-50'}`}
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

export const BusinessSummary = () => (
  <div className="bg-white p-8 rounded-lg shadow-sm border border-gray-100">
    <h3 className="text-lg font-bold text-gray-800 mb-4">Estado General del Negocio</h3>
    <p className="text-gray-600 mb-8">Administra tus servicios turísticos, reservas y clientes desde esta central operativa.</p>

    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div className="border p-6 rounded-lg hover:border-primary transition cursor-pointer group">
        <h3 className="font-bold mb-2 group-hover:text-primary transition">Servicios Activos</h3>
        <p className="text-3xl font-bold text-primary">12</p>
      </div>
      <div className="border p-6 rounded-lg hover:border-primary transition cursor-pointer group">
        <h3 className="font-bold mb-2 group-hover:text-primary transition">Reservas Pendientes</h3>
        <p className="text-3xl font-bold text-secondary">5</p>
      </div>
    </div>
  </div>
);
