'use client';

import React, { useState, createContext, useContext, ReactNode } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { FiHome, FiBox, FiUsers, FiArchive, FiDollarSign, FiClipboard, FiTrendingUp, FiBookOpen, FiGrid, FiShoppingCart, FiBed, FiCalendar } from 'react-icons/fi';

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
  const { user } = useAuth();

  const menuItems = [
    { name: 'inicio', label: 'Inicio', icon: FiHome },
    { name: 'productos', label: 'Productos', icon: FiBox },
    { name: 'clientes', label: 'Clientes', icon: FiUsers },
    { name: 'inventario', label: 'Inventario', icon: FiArchive },
    { name: 'costos', label: 'Costos', icon: FiDollarSign },
    { name: 'recursos', label: 'Recursos', icon: FiClipboard },
    { name: 'reglas-precio', label: 'Reglas de Precios', icon: FiTrendingUp },
    { name: 'reservas', label: 'Reservas', icon: FiCalendar },
  ];

  const restauranteItems = [
    { name: 'menu-restaurante', label: 'Menú Restaurante', icon: FiBookOpen },
    { name: 'mesas', label: 'Gestión de Mesas', icon: FiGrid },
    { name: 'pedidos', label: 'Pedidos (TPV)', icon: FiShoppingCart },
  ];

  const hotelItems = [
      { name: 'habitaciones', label: 'Habitaciones', icon: FiBed },
  ];

  // Lógica para mostrar menús según el tipo de prestador (a futuro)
  const isRestaurante = true; // Placeholder
  const isHotel = true; // Placeholder

  return (
    <div className="w-64 bg-gray-800 text-white p-4 flex flex-col h-full">
      <h2 className="text-xl font-bold mb-6">Panel de Prestador</h2>
      <nav>
        <p className="px-2 text-xs uppercase text-gray-400 mb-2">General</p>
        <ul>
          {menuItems.map((item) => (
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
        {isRestaurante && (
            <>
            <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Restaurante</p>
            <ul>
            {restauranteItems.map((item) => (
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
            </>
        )}
        {isHotel && (
            <>
            <p className="px-2 mt-4 text-xs uppercase text-gray-400 mb-2">Hotel</p>
            <ul>
            {hotelItems.map((item) => (
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
    <DashboardProvider>
      <div className="flex flex-1 h-full bg-gray-50">
        <Sidebar />
        <main className="flex-1 p-8 overflow-y-auto">
          {children}
        </main>
      </div>
    </DashboardProvider>
  )
}