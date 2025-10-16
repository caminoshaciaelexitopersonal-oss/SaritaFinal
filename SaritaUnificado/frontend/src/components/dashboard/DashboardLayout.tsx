'use client';

import React, { ReactNode } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import {
  FiHome, FiBox, FiUsers, FiCalendar, FiStar,
  FiAward, FiMap, FiTruck, FiBriefcase, FiImage, FiBarChart2, FiUser
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
  // Añadir aquí otros items específicos...

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
        {/* Añadir aquí otros renderizados condicionales */}
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