'use client';

import { useAuth } from '@/contexts/AuthContext';
import {
  FiChevronDown, FiChevronRight, FiBox, FiStar, FiAward, FiMap, FiTruck,
  FiBriefcase, FiImage, FiBookOpen, FiGrid, FiShoppingCart, FiUser, FiArchive,
  FiTrendingDown, FiDollarSign, FiHome, FiUsers, FiFileText, FiMapPin, FiSettings,
  FiBarChart2, FiShield, FiFolder, FiCamera, FiEdit, FiCalendar, FiClipboard, FiCheckSquare, FiMonitor, FiDownload,
  FiActivity
} from 'react-icons/fi';
import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

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
  isSubSection?: boolean;
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

// --- Enlace del Sidebar ---
const SidebarLink = ({ link, isSubSection }: { link: NavLink, isSubSection?: boolean }) => {
  const pathname = usePathname();
  const isActive = pathname === link.href;
  const Icon = link.icon;
  const paddingClass = isSubSection ? 'pl-14' : 'pl-10';

  return (
    <Link href={link.href} passHref>
      <div
        className={`w-full flex items-center pr-4 py-2.5 text-sm font-medium rounded-lg transition-colors text-left cursor-pointer ${paddingClass} ${
          isActive
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

// --- Estructura de Navegación "Mi Negocio" ---
const miNegocioNav: NavSection[] = [
  {
    title: 'Gestión Operativa',
    isSubSection: true,
    links: [
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/perfil', label: 'Mi Perfil', icon: FiUser },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/productos-servicios', label: 'Productos/Servicios', icon: FiBox },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/clientes', label: 'Clientes', icon: FiUsers },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/reservas', label: 'Reservas', icon: FiCalendar },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/valoraciones', label: 'Valoraciones', icon: FiStar },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/documentos', label: 'Documentos', icon: FiAward },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/galeria', label: 'Galería', icon: FiImage },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/estadisticas', label: 'Estadísticas', icon: FiBarChart2 },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/genericos/costos', label: 'Costos', icon: FiTrendingDown },
    ],
  },
  {
    title: 'Módulos Especializados',
    isSubSection: true,
    links: [
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/hoteles/habitaciones', label: 'Habitaciones', icon: FiBriefcase, prestadorCategoria: 'hotel' },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/restaurantes/menu', label: 'Menú/Carta', icon: FiBookOpen, prestadorCategoria: 'restaurante' },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/restaurantes/mesas', label: 'Gestión de Mesas', icon: FiGrid, prestadorCategoria: 'restaurante' },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/restaurantes/pedidos', label: 'Pedidos (TPV)', icon: FiShoppingCart, prestadorCategoria: 'restaurante' },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/guias', label: 'Mis Rutas', icon: FiMap, prestadorCategoria: 'guía' },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/transporte', label: 'Vehículos', icon: FiTruck, prestadorCategoria: 'transporte' },
      { href: '/dashboard/prestador/mi-negocio/gestion-operativa/especializados/agencias', label: 'Paquetes Turísticos', icon: FiBriefcase, prestadorCategoria: 'agencia' },
    ],
  },
  {
    title: 'Gestión Comercial',
    isSubSection: true,
    links: [
      { href: '/dashboard/prestador/mi-negocio/comercial', label: 'Facturación de Ventas', icon: FiDollarSign },
    ],
  },
  { title: 'Gestión Archivística', isSubSection: true, links: [{ href: '/dashboard/prestador/mi-negocio/gestion-archivistica', label: 'Ver Módulo', icon: FiArchive }] },
  { title: 'Análisis Financiero', isSubSection: true, links: [{ href: '/dashboard/prestador/mi-negocio/financiera', label: 'Ver Módulo', icon: FiTrendingDown }] },
];

// --- Sección Colapsable ---
const CollapsibleNavSection = ({
  section,
  userRole,
  prestadorCategoria,
}: {
  section: NavSection;
  userRole: string;
  prestadorCategoria?: string;
}) => {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);

  const filteredLinks = section.links.filter((link) => {
    if (link.allowedRoles && !link.allowedRoles.includes(userRole)) return false;
    if (link.prestadorCategoria) {
      if (userRole !== 'PRESTADOR' || !prestadorCategoria) return false;
      return prestadorCategoria.toLowerCase().includes(link.prestadorCategoria);
    }
    return true;
  });

  const isSectionActive = filteredLinks.some((link) => pathname.startsWith(link.href));
  useEffect(() => {
    if (isSectionActive) setIsOpen(true);
  }, [isSectionActive]);

  if (filteredLinks.length === 0) return null;

  const paddingClass = section.isSubSection ? 'pl-8' : 'px-4';

  return (
    <div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`flex items-center justify-between w-full py-2.5 text-sm font-medium text-left rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 ${paddingClass}`}
      >
        <span className="font-semibold">{section.title}</span>
        {isOpen ? <FiChevronDown className="h-5 w-5" /> : <FiChevronRight className="h-5 w-5" />}
      </button>
      {isOpen && (
        <div className="mt-2 space-y-1">
          {filteredLinks.map((link) => (
            <SidebarLink key={link.href} link={link} isSubSection={section.isSubSection} />
          ))}
        </div>
      )}
    </div>
  );
};

// --- Componente Principal del Sidebar ---
export default function Sidebar() {
  const { user, isLoading } = useAuth();
  const [isMiNegocioOpen, setIsMiNegocioOpen] = useState(true);

  if (isLoading) return <SidebarSkeleton />;
  // Si la carga ha terminado y no hay usuario, retorna un componente vacío
  // que mantiene el espacio en el layout para evitar el parpadeo (flicker).
  if (!user) return <aside className="w-64 flex-shrink-0 bg-white border-r border-gray-200" />;

  const prestadorCategoria = user.perfil_prestador?.categoria?.nombre;

  const adminNavSections: NavSection[] = [
    {
      title: 'ERP SISTÉMICO',
      links: [
        { href: '/dashboard/admin_plataforma/gestion-comercial', label: 'Gestión Comercial', icon: FiDollarSign },
        { href: '/dashboard/admin_plataforma/operativa', label: 'Gestión Operativa', icon: FiGrid },
        { href: '/dashboard/admin_plataforma/contable', label: 'Gestión Contable', icon: FiBookOpen },
        { href: '/dashboard/admin_plataforma/financiera', label: 'Gestión Financiera', icon: FiTrendingDown },
        { href: '/dashboard/admin_plataforma/archivistica', label: 'Gestión Archivística', icon: FiArchive },
      ],
    },
    {
      title: 'Plataforma Sarita',
      links: [
        { href: '/dashboard/admin_plataforma/inteligencia', label: 'Inteligencia IA', icon: FiActivity },
        { href: '/dashboard/admin_plataforma/planes', label: 'Planes', icon: FiDollarSign },
        { href: '/dashboard/admin_plataforma/web-content', label: 'Gestión Web', icon: FiMonitor },
        { href: '/dashboard/admin_plataforma/downloads', label: 'Descargas', icon: FiDownload },
      ],
    },
    {
      title: 'Gestión de Contenido',
      links: [
        { href: '/dashboard/publicaciones', label: 'Publicaciones', icon: FiFileText },
        { href: '/dashboard/atractivos', label: 'Atractivos', icon: FiMapPin },
        { href: '/dashboard/rutas', label: 'Rutas Turísticas', icon: FiMapPin },
      ],
    },
    {
      title: 'Administración',
      links: [
        { href: '/dashboard/admin/users', label: 'Usuarios', icon: FiUsers },
        { href: '/dashboard/admin/site-config', label: 'Config. del Sitio', icon: FiSettings },
        { href: '/dashboard/admin/formularios', label: 'Formularios', icon: FiClipboard },
        { href: '/dashboard/admin/verificacion', label: 'Verificaciones', icon: FiCheckSquare },
        { href: '/dashboard/admin/scoring', label: 'Puntuación', icon: FiAward },
      ],
    },
  ];

  return (
    <aside className="w-64 flex-shrink-0 bg-white border-r border-gray-200 flex flex-col">
      <div className="p-4 border-b">
        <h2 className="text-xl font-bold text-gray-800 truncate">SITYC</h2>
        <p className="text-sm text-gray-500 truncate" title={user.email}>
          {user.username}
        </p>
      </div>
      <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
        <SidebarLink link={{ href: '/dashboard', label: 'Inicio', icon: FiHome }} />

        {user.role === 'PRESTADOR' && (
          <div>
            <button
              onClick={() => setIsMiNegocioOpen(!isMiNegocioOpen)}
              className="flex items-center justify-between w-full px-4 py-2.5 text-sm font-medium text-left rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <span className="font-semibold text-lg">Mi Negocio</span>
              {isMiNegocioOpen ? <FiChevronDown className="h-5 w-5" /> : <FiChevronRight className="h-5 w-5" />}
            </button>
            {isMiNegocioOpen && (
              <div className="mt-2 space-y-1">
                {miNegocioNav.map((section) => (
                  <CollapsibleNavSection
                    key={section.title}
                    section={section}
                    userRole={user.role}
                    prestadorCategoria={prestadorCategoria}
                  />
                ))}
              </div>
            )}
          </div>
        )}

        {(user.role === 'ADMIN' || user.role === 'FUNCIONARIO_DIRECTIVO') &&
          adminNavSections.map((section) => (
            <CollapsibleNavSection key={section.title} section={section} userRole={user.role} />
          ))}
      </nav>
    </aside>
  );
}