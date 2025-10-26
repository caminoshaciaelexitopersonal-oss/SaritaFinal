'use client';

import React from 'react';
import Link from 'next/link';
import { FiGrid, FiPlusCircle, FiUserPlus, FiBarChart2, FiSettings, FiDollarSign, FiCalendar, FiBox, FiHome, FiKey, FiBookOpen } from 'react-icons/fi';

import { useAuth } from '@/contexts/AuthContext';

const StatCard = ({ title, value, icon: Icon }: { title: string; value: string | number; icon: React.ElementType }) => (
  <div className="p-4 bg-white rounded-lg shadow">
    <div className="flex items-center">
      <div className="flex-shrink-0 p-3 bg-blue-500 rounded-md">
        <Icon className="w-6 h-6 text-white" />
      </div>
      <div className="ml-4">
        <p className="text-sm font-medium text-gray-500 truncate">{title}</p>
        <p className="text-2xl font-semibold text-gray-900">{value}</p>
      </div>
    </div>
  </div>
);

const ShortcutCard = ({ title, href, icon: Icon }: { title: string; href: string; icon: React.ElementType }) => (
  <Link href={href}>
    <div className="flex flex-col items-center justify-center p-6 text-center bg-white rounded-lg shadow-md hover:shadow-lg hover:bg-gray-50 transition-all duration-200 h-full">
      <Icon className="w-10 h-10 mb-3 text-blue-600" />
      <h3 className="text-md font-semibold text-gray-800">{title}</h3>
    </div>
  </Link>
);

const DashboardPrestador = () => {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return <div>Cargando panel...</div>;
  }

  if (!user || !user.perfil_prestador) {
    return (
      <div className="p-6 text-center">
        <h2 className="text-2xl font-bold text-red-600">Error al cargar el perfil</h2>
        <p className="mt-2 text-gray-600">
          No se pudo cargar la información de tu perfil de prestador.
          Por favor, <Link href="/dashboard/prestador/perfil" className="text-blue-500 underline">completa tu perfil</Link> para continuar.
        </p>
      </div>
    );
  }

  const { perfil_prestador } = user;

  const getCategoriaAccesos = () => {
    switch (perfil_prestador?.categoria?.slug) {
      case 'hoteles':
        return (
          <>
            <ShortcutCard title="Gestionar Habitaciones" href="/dashboard/prestador/hotel/habitaciones" icon={FiHome} />
            <ShortcutCard title="Gestionar Reservas" href="/dashboard/prestador/reservas" icon={FiCalendar} />
          </>
        );
      case 'restaurantes':
         return (
          <>
            <ShortcutCard title="Gestionar Menús" href="/dashboard/prestador/restaurante/menu" icon={FiBookOpen} />
            <ShortcutCard title="Gestionar Mesas" href="/dashboard/prestador/restaurante/mesas" icon={FiGrid} />
            <ShortcutCard title="Pedidos" href="/dashboard/prestador/restaurante/pedidos" icon={FiDollarSign} />
          </>
        );
      case 'agencias-de-viajes':
         return (
          <>
            <ShortcutCard title="Gestionar Paquetes" href="/dashboard/prestador/agencias" icon={FiBox} />
            <ShortcutCard title="Ver Reservas" href="/dashboard/prestador/reservas" icon={FiKey} />
          </>
        );
      case 'guias-turisticos':
        return (
          <>
            <ShortcutCard title="Mis Rutas" href="/dashboard/prestador/guias" icon={FiBookOpen} />
            <ShortcutCard title="Ver Reservas" href="/dashboard/prestador/reservas" icon={FiKey} />
          </>
        );
      case 'transporte-turistico':
        return (
          <>
            <ShortcutCard title="Gestionar Vehículos" href="/dashboard/prestador/transporte" icon={FiBox} />
            <ShortcutCard title="Ver Reservas" href="/dashboard/prestador/reservas" icon={FiKey} />
          </>
        );
      default:
        return null;
    }
  };


  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold text-gray-900">Panel de Control</h1>
      <p className="text-lg text-gray-600 mb-6">Bienvenido, {perfil_prestador?.nombre_negocio || user.username}</p>

      {/* Sección de Estadísticas (con datos simulados temporalmente) */}
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
        <StatCard title="Clientes Registrados (Mes)" value="0" icon={FiUserPlus} />
        <StatCard title="Productos Activos" value="0" icon={FiGrid} />
        <StatCard title="Reservas Pendientes" value="0" icon={FiCalendar} />
        <StatCard title="Ingresos del Mes" value="$0" icon={FiDollarSign} />
      </div>

      {/* Sección de Accesos Directos */}
      <div>
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Accesos Directos</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
            <ShortcutCard title="Gestionar Productos" href="/dashboard/prestador/productos" icon={FiPlusCircle} />
            <ShortcutCard title="Registrar Clientes" href="/dashboard/prestador/clientes" icon={FiUserPlus} />
            <ShortcutCard title="Ver Estadísticas" href="/dashboard/prestador/estadisticas" icon={FiBarChart2} />
            <ShortcutCard title="Configuración" href="/dashboard/prestador/configuracion" icon={FiSettings} />
            {getCategoriaAccesos()}
        </div>
      </div>
    </div>
  );
};

export default DashboardPrestador;