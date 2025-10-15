'use client';

import React from 'react';
import { useDashboard } from '@/components/dashboard/DashboardLayout';

// --- Importar vistas genéricas ---
import Perfil from './prestador/Perfil';
import Productos from './prestador/Productos';
import Clientes from './prestador/Clientes';
import Reservas from './prestador/Reservas';
import Valoraciones from './prestador/Valoraciones';
import Certificaciones from './prestador/Certificaciones';

// --- Importar vistas específicas ---
import Habitaciones from './prestador/hotel/Habitaciones';
import Menu from './prestador/restaurante/Menu';
import Mesas from './prestador/restaurante/Mesas';
import Pedidos from './prestador/restaurante/Pedidos';
import Vehiculos from './prestador/Vehiculos';
import Paquetes from './prestador/Paquetes';
import RutasGuias from './prestador/RutasGuias';


// --- Componentes placeholder para vistas no implementadas ---
const NotImplemented = ({ name }: { name: string }) => (
    <div><h1 className="text-2xl font-bold">{name}</h1><p>Este módulo aún no ha sido implementado.</p></div>
);
const Inventario = () => <NotImplemented name="Inventario" />;
const Costos = () => <NotImplemented name="Costos" />;
const Recursos = () => <NotImplemented name="Recursos" />;
const ReglasPrecio = () => <NotImplemented name="Reglas de Precio" />;


const InicioDashboard = () => (
  <div>
    <h1 className="text-2xl font-bold">Bienvenido a tu Panel de Control</h1>
    <p className="mt-2">Selecciona un módulo del menú de la izquierda para comenzar a gestionar tu negocio.</p>
  </div>
);

const DashboardPage = () => {
  const { activeView } = useDashboard();

  // Mapa de todas las vistas disponibles
  const views: { [key: string]: React.ComponentType } = {
    // Genéricas
    'inicio': InicioDashboard,
    'perfil': Perfil,
    'productos': Productos,
    'clientes': Clientes,
    'reservas': Reservas,
    'valoraciones': Valoraciones,
    'certificaciones': Certificaciones,
    'inventario': Inventario,
    'costos': Costos,
    'recursos': Recursos,
    'reglas-precio': ReglasPrecio,

    // Específicas de Hotel
    'habitaciones': Habitaciones,

    // Específicas de Restaurante
    'menu-restaurante': Menu,
    'mesas': Mesas,
    'pedidos': Pedidos,

    // Específicas de Guía
    'rutas-guias': RutasGuias,

    // Específicas de Transporte
    'vehiculos': Vehiculos,

    // Específicas de Agencia
    'paquetes': Paquetes,
  };

  const ActiveComponent = views[activeView] || InicioDashboard;

  return <ActiveComponent />;
};

export default DashboardPage;