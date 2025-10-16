'use client';

import React, { useState, createContext, useContext, ReactNode } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import {
  FiHome, FiBox, FiUsers, FiArchive, FiDollarSign, FiClipboard, FiTrendingUp,
  FiBookOpen, FiGrid, FiShoppingCart, FiBed, FiUser, FiCalendar, FiStar,
  FiAward, FiMap, FiTruck, FiBriefcase, FiImage
} from 'react-icons/fi';

// --- Contexto para el Dashboard ---
interface DashboardContextType {
  activeView: string;
  setActiveView: (view: string) => void;
}

const DashboardContext = createContext<DashboardContextType | undefined>(undefined);

export const useDashboard = () => {
  const context = useContext(DashboardContext);
  if (!context) {
    throw new Error('useDashboard must be used within a DashboardProvider');
  }
  return context;
};

export const DashboardProvider = ({ children }: { children: ReactNode }) => {
  const [activeView, setActiveView] = useState('inicio');
  return (
    <DashboardContext.Provider value={{ activeView, setActiveView }}>
      {children}
    </DashboardContext.Provider>
  );
};

// --- Componente Sidebar ---
const Sidebar = () => {
  const { setActiveView, activeView } = useDashboard();
  const { user } = useAuth(); // Asumimos que user.perfil_prestador.categoria.nombre está disponible

  // Módulos Genéricos (comunes a todos)
  const menuItems = [
    { name: 'inicio', label: 'Inicio', icon: FiHome },
    { name: 'perfil', label: 'Mi Perfil', icon: FiUser },
    { name: 'productos', label: 'Productos/Servicios', icon: FiBox },
    { name: 'clientes', label: 'Clientes', icon: FiUsers },
    { name: 'reservas', label: 'Reservas', icon: FiCalendar },
    { name: 'valoraciones', label: 'Valoraciones', icon: FiStar },
    { name: 'certificaciones', label: 'Documentos', icon: FiAward },
    { name: 'galeria', label: 'Galería', icon: FiImage },
  ];

  // Módulos Específicos
  const restauranteItems = [
    { name: 'menu-restaurante', label: 'Menú/Carta', icon: FiBookOpen },
    { name: 'pedidos', label: 'Pedidos (TPV)', icon: FiShoppingCart },
    { name: 'mesas', label: 'Gestión de Mesas', icon: FiGrid },
  ];

  const hotelItems = [
      { name: 'habitaciones', label: 'Habitaciones', icon: FiBed },
  ];

  const guiaItems = [
      { name: 'rutas-guias', label: 'Mis Rutas', icon: FiMap },
  ];

  const transporteItems = [
      { name: 'vehiculos', label: 'Vehículos', icon: FiTruck },
  ];

  const agenciaItems = [
      { name: 'paquetes', label: 'Paquetes Turísticos', icon: FiBriefcase },
  ];

  const categoriaPrestador = user?.perfil_prestador?.categoria?.nombre?.toLowerCase() || '';

  const renderMenuItems = (items: any[]) => (
    <ul>
      {items.map((item) => (
        <li key={item.name} className="mb-1">
          <button
            onClick={() => setActiveView(item.name)}
            className={`w-full text-left flex items-center p-2 rounded-md transition-colors text-sm ${
              activeView === item.name ? 'bg-gray-900' : 'hover:bg-gray-700'
            }`}
          >
            <item.icon className="mr-3" />
            {item.label}
          </button>
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

        {/* Renderizado condicional de módulos específicos */}
        {categoriaPrestador.includes('restaurante') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Restaurante</p>
                {renderMenuItems(restauranteItems)}
            </>
        )}

        {categoriaPrestador.includes('hotel') && (
            <>
                <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Hotel</p>
                {renderMenuItems(hotelItems)}
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
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <DashboardProvider>
      <div className="flex flex-1 h-full bg-gray-50">
        <Sidebar />
        <main className="flex-1 p-8 overflow-y-auto">
          {children}
        </main>
      </div>
    </DashboardProvider>
  );
}