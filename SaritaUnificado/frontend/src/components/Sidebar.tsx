'use client';

import { useAuth } from '@/contexts/AuthContext';
import { FiChevronDown, FiChevronRight, FiBox, FiStar, FiBed, FiAward, FiMap, FiTruck, FiBriefcase, FiImage, FiBookOpen, FiGrid, FiShoppingCart, FiUser } from 'react-icons/fi';
import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
  FiHome, FiUsers, FiFileText, FiMapPin, FiSettings, FiBarChart2,
  FiShield, FiFolder, FiCamera, FiEdit, FiCalendar, FiArchive, FiTrendingDown
} from 'react-icons/fi';

// --- Tipos ---
interface NavLink {
  href: string;
  label: string;
  icon: React.ElementType;
  allowedRoles?: string[];
  prestadorCategoria?: string;
}

interface NavSection {
  title: string;
  links: NavLink[];
}

// --- Componentes de UI ---
const SidebarSkeleton = () => (
  <div className="p-4 animate-pulse">
    <div className="h-8 bg-gray-200 rounded-md w-3/4 mb-6"></div>
    <div className="space-y-4">
      {[...Array(4)].map((_, i) => (
        <div key={i}>
          <div className="h-6 bg-gray-200 rounded-md w-1/2 mb-3"></div>
          <div className="space-y-2 pl-4">
            <div className="h-5 bg-gray-200 rounded-md w-5/6"></div>
            <div className="h-5 bg-gray-200 rounded-md w-4/6"></div>
          </div>
        </div>
      ))}
    </div>
  </div>
);

const SidebarLink = ({ link }: { link: NavLink }) => {
  const pathname = usePathname();
  const isActive = pathname === link.href;
  const Icon = link.icon;

  return (
    <Link href={link.href} passHref>
      <div
        className={`w-full flex items-center pl-10 pr-4 py-2.5 text-sm font-medium rounded-lg transition-colors text-left cursor-pointer
          ${isActive
            ? 'bg-blue-100 text-blue-700'
            : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
          }`}
      >
        {Icon && <Icon className="mr-3 h-5 w-5 flex-shrink-0" />}
        <span className="truncate">{link.label}</span>
      </div>
    </Link>
  );
};

// --- Estructura de Navegación Completa ---
const navSections: NavSection[] = [
  {
    title: 'Principal',
    links: [
      { href: '/dashboard', label: 'Inicio', icon: FiHome, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO', 'FUNCIONARIO_PROFESIONAL', 'PRESTADOR', 'ARTESANO'] },
      { href: '/dashboard/ai-config', label: 'Configuración AI', icon: FiSettings, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO', 'FUNCIONARIO_PROFESIONAL', 'PRESTADOR', 'ARTESANO'] },
    ],
  },
  {
    title: 'Panel de Prestador',
    links: [
        { href: '/dashboard/prestador/perfil', label: 'Mi Perfil', icon: FiUser, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/productos', label: 'Productos/Servicios', icon: FiBox, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/clientes', label: 'Clientes', icon: FiUsers, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/reservas', label: 'Reservas', icon: FiCalendar, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/valoraciones', label: 'Valoraciones', icon: FiStar, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/certificaciones', label: 'Documentos', icon: FiAward, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/galeria', label: 'Galería', icon: FiImage, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/estadisticas', label: 'Estadísticas', icon: FiBarChart2, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/inventario', label: 'Inventario', icon: FiArchive, allowedRoles: ['PRESTADOR'] },
        { href: '/dashboard/prestador/costos', label: 'Costos', icon: FiTrendingDown, allowedRoles: ['PRESTADOR'] },
    ],
  },
  {
      title: 'Módulos Específicos',
      links: [
        { href: '/dashboard/prestador/hotel/habitaciones', label: 'Habitaciones', icon: FiBed, prestadorCategoria: 'hotel' },
        { href: '/dashboard/prestador/restaurante/menu', label: 'Menú/Carta', icon: FiBookOpen, prestadorCategoria: 'restaurante' },
        { href: '/dashboard/prestador/restaurante/mesas', label: 'Gestión de Mesas', icon: FiGrid, prestadorCategoria: 'restaurante' },
        { href: '/dashboard/prestador/restaurante/pedidos', label: 'Pedidos (TPV)', icon: FiShoppingCart, prestadorCategoria: 'restaurante' },
        { href: '/dashboard/prestador/guias', label: 'Mis Rutas', icon: FiMap, prestadorCategoria: 'guía' },
        { href: '/dashboard/prestador/transporte', label: 'Vehículos', icon: FiTruck, prestadorCategoria: 'transporte' },
        { href: '/dashboard/prestador/agencias', label: 'Paquetes Turísticos', icon: FiBriefcase, prestadorCategoria: 'agencia' },
      ]
  },
  {
    title: 'Gestión de Contenido',
    links: [
      { href: '/dashboard/publicaciones', label: 'Publicaciones', icon: FiFileText, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO'] },
      { href: '/dashboard/atractivos', label: 'Atractivos', icon: FiMapPin, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO'] },
      { href: '/dashboard/rutas', label: 'Rutas Turísticas', icon: FiMapPin, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO'] },
    ],
  },
  {
    title: 'Administración',
    links: [
      { href: '/dashboard/admin/users', label: 'Usuarios', icon: FiUsers, allowedRoles: ['ADMIN'] },
      { href: '/dashboard/admin/site-config', label: 'Config. del Sitio', icon: FiSettings, allowedRoles: ['ADMIN'] },
    ],
  },
];

const CollapsibleNavSection = ({ section, userRole, prestadorCategoria }: { section: NavSection; userRole: string; prestadorCategoria?: string }) => {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);

  const filteredLinks = section.links.filter(link => {
    if (link.allowedRoles && !link.allowedRoles.includes(userRole)) {
      return false;
    }
    if (link.prestadorCategoria) {
      if (userRole !== 'PRESTADOR' || !prestadorCategoria) return false;
      return prestadorCategoria.toLowerCase().includes(link.prestadorCategoria);
    }
    return true;
  });

  const isSectionActive = filteredLinks.some(link => pathname.startsWith(link.href));

  useEffect(() => {
    if (isSectionActive) {
      setIsOpen(true);
    }
  }, [isSectionActive]);

  if (filteredLinks.length === 0) {
    return null;
  }

  return (
    <div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center justify-between w-full px-4 py-2.5 text-sm font-medium text-left rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        <span className="font-semibold">{section.title}</span>
        {isOpen ? <FiChevronDown className="h-5 w-5" /> : <FiChevronRight className="h-5 w-5" />}
      </button>
      {isOpen && (
        <div className="mt-2 space-y-1">
          {filteredLinks.map((link) => (
            <SidebarLink key={link.href} link={link} />
          ))}
        </div>
      )}
    </div>
  );
};

// --- Componente Principal del Sidebar ---
export default function Sidebar() {
  const { user } = useAuth();

  if (!user) {
    return <SidebarSkeleton />;
  }

  const prestadorCategoria = user.perfil_prestador?.categoria?.nombre;

  return (
    <aside className="w-64 flex-shrink-0 bg-white border-r border-gray-200 flex flex-col">
      <div className="p-4 border-b">
        <h2 className="text-xl font-bold text-gray-800 truncate">SITYC</h2>
        <p className="text-sm text-gray-500 truncate" title={user.email}>{user.username}</p>
      </div>
      <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
        {navSections.map((section) => (
          <CollapsibleNavSection
            key={section.title}
            section={section}
            userRole={user.role}
            prestadorCategoria={prestadorCategoria}
          />
        ))}
      </nav>
    </aside>
  );
}