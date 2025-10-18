'use client';

import React, { ReactNode } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import {
  FiHome, FiBox, FiUsers, FiCalendar, FiStar,
  FiAward, FiMap, FiTruck, FiBriefcase, FiImage, FiBarChart2, FiUser,
  FiBookOpen, FiGrid, FiShoppingCart
} from 'react-icons/fi';

// --- Componente Sidebar ---
const Sidebar = () => {
  const { user } = useAuth();
  const pathname = usePathname();

  const menuItems = [
    { href: '/dashboard', label: 'Inicio', icon: FiHome },
    { href: '/dashboard/prestador/perfil', label: 'Mi Perfil', icon: FiUser },
    { href: '/dashboard/prestador/productos', label: 'Productos/Servicios', icon: FiBox },
    { href: '/dashboard/prestador/clientes', label: 'Clientes', icon: FiUsers },
    { href: '/dashboard/prestador/reservas', label: 'Reservas', icon: FiCalendar },
    { href: '/dashboard/prestador/valoraciones', label: 'Valoraciones', icon: FiStar },
    { href: '/dashboard/prestador/certificaciones', label: 'Documentos', icon: FiAward },
    { href: '/dashboard/prestador/galeria', label: 'Galería', icon: FiImage },
    { href: '/dashboard/prestador/estadisticas', label: 'Estadísticas', icon: FiBarChart2 },
  ];

  const hotelItems = [ { href: '/dashboard/prestador/hotel/habitaciones', label: 'Habitaciones', icon: FiBed } ];
  const restauranteItems = [
    { href: '/dashboard/prestador/restaurante/menu', label: 'Menú/Carta', icon: FiBookOpen },
    { href: '/dashboard/prestador/restaurante/mesas', label: 'Gestión de Mesas', icon: FiGrid },
    { href: '/dashboard/prestador/restaurante/pedidos', label: 'Pedidos (TPV)', icon: FiShoppingCart },
  ];
  const guiaItems = [ { href: '/dashboard/prestador/guias', label: 'Mis Rutas', icon: FiMap } ];
  const transporteItems = [ { href: '/dashboard/prestador/transporte', label: 'Vehículos', icon: FiTruck } ];
  const agenciaItems = [ { href: '/dashboard/prestador/agencias', label: 'Paquetes Turísticos', icon: FiBriefcase } ];

  const categoriaPrestador = user?.perfil_prestador?.categoria?.nombre?.toLowerCase() || '';

  const renderMenuItems = (items: { href: string; label: string; icon: any }[]) => (
    <ul>
      {items.map((item) => (
        <li key={item.href} className="mb-1">
          <Link href={item.href} className={`w-full text-left flex items-center p-2 rounded-md transition-colors text-sm ${
              pathname === item.href ? 'bg-gray-900' : 'hover:bg-gray-700'
            }`}>
              <item.icon className="mr-3" />
              {item.label}
          </Link>
        </li>
      ))}
    </ul>
  );

  return (
    <div className="w-64 bg-gray-800 text-white p-4 flex flex-col h-full">
      <h2 className="text-xl font-bold mb-6">Panel de Prestador</h2>
      <nav className="flex-grow">
        <p className="px-2 text-xs uppercase text-gray-400 mb-2">General</p>
        {renderMenuItems(menuItems)}

        {categoriaPrestador.includes('hotel') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Hotel</p>
                {renderMenuItems(hotelItems)}
            </>
        )}
        {categoriaPrestador.includes('restaurante') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Restaurante</p>
                {renderMenuItems(restauranteItems)}
            </>
        )}
        {categoriaPrestador.includes('guía') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Guía Turístico</p>
                {renderMenuItems(guiaItems)}
            </>
        )}
        {categoriaPrestador.includes('transporte') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Transporte</p>
                {renderMenuItems(transporteItems)}
            </>
        )}
        {categoriaPrestador.includes('agencia') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Agencia de Viajes</p>
                {renderMenuItems(agenciaItems)}
            </>
        )}
      </nav>
    </div>
  );
};


// --- Layout Principal del Dashboard ---
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
      <div className="flex flex-1 h-full bg-gray-50">
        <Sidebar />
        <main className="flex-1 p-8 overflow-y-auto">
          {children}
        </main>
      </div>
  );
}