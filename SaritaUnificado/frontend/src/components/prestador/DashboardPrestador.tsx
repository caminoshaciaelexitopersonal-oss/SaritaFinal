'use client';

import React from 'react';
import Link from 'next/link';
import { FiGrid, FiPlusCircle, FiUserPlus, FiBarChart2, FiSettings, FiDollarSign, FiCalendar, FiBox, FiHome, FiKey, FiBookOpen } from 'react-icons/fi';

// Hook para obtener datos del prestador (simulado por ahora)
const usePrestadorData = () => {
  // En el futuro, esto vendrá de una llamada a la API, ej: api.get('/profile/prestador/')
  return {
    isLoading: false,
    error: null,
    prestador: {
      nombre_negocio: 'Hotel Paraíso Tropical',
      categoria: {
        slug: 'hoteles', // 'restaurantes', 'agencias-de-viajes'
      },
    },
    stats: {
      clientes: [
        { pais: 'Colombia', total: 120 },
        { pais: 'Estados Unidos', total: 15 },
        { pais: 'España', total: 8 },
      ],
    },
  };
};

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
  const { prestador, stats, isLoading, error } = usePrestadorData();

  if (isLoading) {
    return <div>Cargando panel...</div>;
  }

  if (error) {
    return <div className="text-red-500">Error al cargar los datos del prestador.</div>;
  }

  const getCategoriaAccesos = () => {
    switch (prestador?.categoria?.slug) {
      case 'hoteles':
        return (
          <>
            <ShortcutCard title="Gestionar Habitaciones" href="/dashboard/prestador/habitaciones" icon={FiHome} />
            <ShortcutCard title="Gestionar Reservas" href="/dashboard/prestador/reservas" icon={FiCalendar} />
          </>
        );
      case 'restaurantes':
         return (
          <>
            <ShortcutCard title="Gestionar Menús" href="/dashboard/prestador/menus" icon={FiBookOpen} />
            <ShortcutCard title="Gestionar Mesas" href="/dashboard/prestador/mesas" icon={FiGrid} />
            <ShortcutCard title="Terminal Punto de Venta (TPV)" href="/dashboard/prestador/tpv" icon={FiDollarSign} />
          </>
        );
      case 'agencias-de-viajes':
         return (
          <>
            <ShortcutCard title="Gestionar Paquetes" href="/dashboard/prestador/paquetes" icon={FiBox} />
            <ShortcutCard title="Gestionar Reservas" href="/dashboard/prestador/reservas-agencia" icon={FiKey} />
          </>
        );
      default:
        return null;
    }
  };


  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold text-gray-900">Panel de Control</h1>
      <p className="text-lg text-gray-600 mb-6">Bienvenido, {prestador?.nombre_negocio || 'Prestador'}</p>

      {/* Sección de Estadísticas */}
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
        <StatCard title="Clientes Registrados (Mes)" value={stats.clientes.reduce((acc, c) => acc + c.total, 0)} icon={FiUserPlus} />
        <StatCard title="Productos Activos" value="12" icon={FiGrid} />
        <StatCard title="Reservas Pendientes" value="3" icon={FiCalendar} />
        <StatCard title="Ingresos del Mes" value="$1,250,000" icon={FiDollarSign} />
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