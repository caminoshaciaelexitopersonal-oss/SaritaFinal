'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import { FiHome, FiBox, FiUsers, FiArchive, FiDollarSign, FiClipboard, FiTrendingUp, FiBookOpen, FiGrid, FiShoppingCart, FiBed } from 'react-icons/fi';

// --- Componente Sidebar ---
const Sidebar = () => {
  const pathname = usePathname();
  const { user } = useAuth();

  const menuItems = [
    { href: '/dashboard/prestador', label: 'Inicio', icon: FiHome },
    { href: '/dashboard/prestador/productos', label: 'Productos', icon: FiBox },
    { href: '/dashboard/prestador/clientes', label: 'Clientes', icon: FiUsers },
    { href: '/dashboard/prestador/inventario', label: 'Inventario', icon: FiArchive },
    { href: '/dashboard/prestador/costos', label: 'Costos', icon: FiDollarSign },
    { href: '/dashboard/prestador/recursos', label: 'Recursos', icon: FiClipboard },
    { href: '/dashboard/prestador/reglas-precio', label: 'Reglas de Precios', icon: FiTrendingUp },
  ];

  const restauranteItems = [
    { href: '/dashboard/prestador/restaurante/menu', label: 'Menú Restaurante', icon: FiBookOpen },
    { href: '/dashboard/prestador/restaurante/mesas', label: 'Gestión de Mesas', icon: FiGrid },
    { href: '/dashboard/prestador/restaurante/pedidos', label: 'Pedidos (TPV)', icon: FiShoppingCart },
  ];

  const hotelItems = [
      { href: '/dashboard/prestador/hotel/habitaciones', label: 'Habitaciones', icon: FiBed },
  ];

  // Lógica para mostrar menús según el tipo de prestador (a futuro)
  const isRestaurante = true; // Placeholder
  const isHotel = true; // Placeholder

  const renderMenuItems = (items: { href: string; label: string; icon: any }[]) => (
    <ul>
      {items.map((item) => (
        <li key={item.href} className="mb-1">
          <Link
            href={item.href}
            className={`w-full text-left flex items-center p-2 rounded-md transition-colors text-sm ${
              pathname === item.href ? 'bg-gray-900' : 'hover:bg-gray-700'
            }`}
          >
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
      <nav>
        <p className="px-2 text-xs uppercase text-gray-400 mb-2">General</p>
        {renderMenuItems(menuItems)}

        {isRestaurante && (
            <>
            <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Restaurante</p>
            {renderMenuItems(restauranteItems)}
            </>
        )}
        {isHotel && (
            <>
            <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Hotel</p>
            {renderMenuItems(hotelItems)}
            </>
        )}
      </nav>
    </div>
  );
};


// --- Layout Principal del Dashboard ---
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return <div className="flex justify-center items-center h-screen">Cargando...</div>;
  }

  if (!user) {
    return <div className="flex justify-center items-center h-screen">No estás autorizado. Por favor, inicia sesión.</div>;
  }

  return (
    <div className="flex flex-1 h-full bg-gray-50">
      <Sidebar />
      <main className="flex-1 p-8 overflow-y-auto">
        {children}
      </main>
    </div>
  )
}