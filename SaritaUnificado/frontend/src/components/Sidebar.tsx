"use client";

import { useAuth } from '@/contexts/AuthContext';
import { FiChevronDown, FiChevronRight, FiAlertCircle } from 'react-icons/fi';
import React, { useState, useEffect, useCallback } from 'react';
import api from '@/services/api';
import { useDashboard } from '@/contexts/DashboardContext'; // Importar el hook del contexto

// --- Definición de Tipos y Componentes Internos ---

export interface NavLink {
  href: string; // Se usará como identificador de la vista
  label: string;
  icon: React.ElementType;
  allowedRoles: string[];
}

export interface NavSection {
  title: string;
  links: NavLink[];
}

import {
  FiHome, FiUsers, FiFileText, FiMapPin, FiSettings, FiBarChart2,
  FiShield, FiFolder, FiAward, FiCamera, FiEdit
} from 'react-icons/fi';

// Mapeo de strings de iconos a componentes de React Icons
const iconMap: { [key: string]: React.ElementType } = {
  FiHome, FiUsers, FiFileText, FiMapPin, FiSettings, FiBarChart2,
  FiShield, FiFolder, FiAward, FiCamera, FiEdit
};

// Componente para el estado de carga (esqueleto)
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

import Link from 'next/link';
import { usePathname } from 'next/navigation';

// Componente para un enlace individual en el menú, ahora usa next/link
const SidebarLink = ({ link }: { link: NavLink }) => {
  const pathname = usePathname();
  const isActive = pathname === link.href;
  const Icon = typeof link.icon === 'string' ? iconMap[link.icon] : link.icon;

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

// --- Estructura de Menú Estática ---
const staticNavSections: NavSection[] = [
    {
        title: 'Principal',
        links: [
            { href: '/dashboard', label: 'Inicio', icon: FiHome, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO', 'FUNCIONARIO_PROFESIONAL', 'PRESTADOR', 'ARTESANO'] },
            { href: '/dashboard/ai-config', label: 'Configuración AI', icon: FiSettings, allowedRoles: ['ADMIN', 'FUNCIONARIO_DIRECTIVO', 'FUNCIONARIO_PROFESIONAL', 'PRESTADOR', 'ARTESANO'] },
        ],
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
        title: 'Gestión de Prestador',
        links: [
            { href: '/dashboard/prestador', label: 'Mi Panel', icon: FiHome, allowedRoles: ['PRESTADOR'] },
            { href: '/dashboard/prestador/productos', label: 'Productos', icon: FiBox, allowedRoles: ['PRESTADOR'] },
            { href: '/dashboard/prestador/clientes', label: 'Clientes', icon: FiUsers, allowedRoles: ['PRESTADOR'] },
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


// Componente para una sección de navegación colapsable
const CollapsibleNavSection = ({ section, userRole }: { section: NavSection; userRole: string }) => {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);

  const filteredLinks = section.links.filter(link =>
    link.allowedRoles.includes(userRole)
  );

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

  return (
    <aside className="w-64 flex-shrink-0 bg-white border-r border-gray-200 flex flex-col">
      <div className="p-4 border-b">
        <h2 className="text-xl font-bold text-gray-800 truncate">SITYC</h2>
        <p className="text-sm text-gray-500 truncate" title={user.email}>{user.username}</p>
      </div>
      <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
        {staticNavSections.map((section) => (
          <CollapsibleNavSection key={section.title} section={section} userRole={user.role} />
        ))}
      </nav>
    </aside>
  );
}