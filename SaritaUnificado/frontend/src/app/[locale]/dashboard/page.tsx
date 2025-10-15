'use client';

import React from 'react';
import { useDashboard } from '@/components/dashboard/DashboardLayout';

// Importar todas las vistas posibles
import Productos from './prestador/Productos';
import Clientes from './prestador/Clientes';
import Inventario from './prestador/Inventario';
import Costos from './prestador/Costos';
import Recursos from './prestador/Recursos';
import ReglasPrecio from './prestador/ReglasPrecio';
import Menu from './prestador/restaurante/Menu';
import Mesas from './prestador/restaurante/Mesas';
import Pedidos from './prestador/restaurante/Pedidos';
import Habitaciones from './prestador/hotel/Habitaciones';
import Reservas from './prestador/Reservas';

const InicioDashboard = () => (
  <div>
    <h1 className="text-2xl font-bold">Bienvenido a tu Panel de Control</h1>
    <p className="mt-2">Selecciona un módulo del menú de la izquierda para comenzar a gestionar tu negocio.</p>
  </div>
);

const DashboardPage = () => {
  const { activeView } = useDashboard();

  const views: { [key: string]: React.ComponentType } = {
    'inicio': InicioDashboard,
    'productos': Productos,
    'clientes': Clientes,
    'inventario': Inventario,
    'costos': Costos,
    'recursos': Recursos,
    'reglas-precio': ReglasPrecio,
    'menu-restaurante': Menu,
    'mesas': Mesas,
    'pedidos': Pedidos,
    'habitaciones': Habitaciones,
    'reservas': Reservas,
  };

  const ActiveComponent = views[activeView] || InicioDashboard;

  return <ActiveComponent />;
};

export default DashboardPage;