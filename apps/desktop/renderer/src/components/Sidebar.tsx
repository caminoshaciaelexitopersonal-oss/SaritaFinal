import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { LayoutDashboard, Wallet, Truck, Briefcase, Users, FileText, Settings, LogOut, UserCheck, DollarSign, FileStack, Signature, Archive } from 'lucide-react';

export const Sidebar = () => {
  const { logout, user } = useAuth();

  const menuItems = [
    { icon: LayoutDashboard, label: 'Dashboard', path: '/dashboard/home' },
    { icon: Briefcase, label: 'Mi Negocio', path: '/dashboard/negocio', role: ['provider', 'operator', 'admin'] },
    { icon: UserCheck, label: 'Empleados', path: '/dashboard/erp/empleados', role: ['provider', 'admin'] },
    { icon: DollarSign, label: 'Nómina', path: '/dashboard/erp/nomina', role: ['provider', 'admin'] },
    { icon: FileStack, label: 'Documentos', path: '/dashboard/erp/documentos', role: ['provider', 'admin'] },
    { icon: Signature, label: 'Contratos', path: '/dashboard/erp/contratos', role: ['provider', 'admin'] },
    { icon: Archive, label: 'Archivo', path: '/dashboard/erp/archivistica', role: ['provider', 'admin'] },
    { icon: Wallet, label: 'Wallet', path: '/dashboard/wallet' },
    { icon: Truck, label: 'Delivery', path: '/dashboard/delivery' },
    { icon: Users, label: 'Admin', path: '/dashboard/admin', role: ['admin'] },
    { icon: FileText, label: 'Reportes', path: '/dashboard/reportes' },
  ];

  return (
    <div className="w-64 bg-gray-900 text-white min-h-screen flex flex-col p-4">
      <div className="text-2xl font-bold mb-10 text-secondary text-center px-4">SARITA Admin</div>

      <nav className="flex-1 space-y-2">
        {menuItems.filter(item => !item.role || (user && item.role.includes(user.role))).map((item) => (
          <NavLink
            key={item.label}
            to={item.path}
            className={({ isActive }) => `flex items-center gap-3 p-3 rounded transition ${isActive ? 'bg-primary text-white' : 'text-gray-400 hover:bg-gray-800'}`}
          >
            <item.icon size={20} />
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>

      <div className="pt-10 border-t border-gray-800">
        <button
          onClick={logout}
          className="flex items-center gap-3 p-3 text-red-400 hover:bg-gray-800 rounded w-full transition"
        >
          <LogOut size={20} />
          <span>Cerrar Sesión</span>
        </button>
      </div>
    </div>
  );
};
