'use client';

import { useAuth } from '@/contexts/AuthContext';
import { FiChevronDown, FiChevronRight, FiHome, FiSettings, FiBox, FiDollarSign, FiArchive, FiTrendingDown, FiBarChart2, FiUsers, FiFileText, FiMonitor } from 'react-icons/fi';
import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import api from '../services/api'; // Corregido: Importar con ruta relativa

// --- Tipos ---
interface NavLink {
  title: string;
  href: string;
  icon?: React.ElementType;
}

interface NavSection {
  title: string;
  children?: NavLink[];
  href?: string;
  icon?: React.ElementType;
}

// --- Icon Mapping ---
const iconMap: { [key: string]: React.ElementType } = {
  Inicio: FiHome,
  "Mi Negocio": FiBox,
  "Gestión Operativa": FiSettings,
  "Gestión Comercial": FiDollarSign,
  "Gestión Archivística": FiArchive,
  "Gestión Contable": FiFileText,
  "Análisis Financiero": FiTrendingDown,
  "Plataforma Sarita": FiMonitor,
  "Planes": FiDollarSign,
  "Gestión Web": FiMonitor,
  "Administración": FiUsers,
  "Usuarios": FiUsers,
  "Config. del Sitio": FiSettings,
  default: FiBox,
};

const getIcon = (title: string) => iconMap[title] || iconMap.default;

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
  const Icon = link.icon || getIcon(link.title);

  return (
    <Link href={link.href} passHref>
      <div
        className={`w-full flex items-center pl-10 pr-4 py-2.5 text-sm font-medium rounded-lg transition-colors text-left cursor-pointer ${
          isActive
            ? 'bg-blue-100 text-blue-700'
            : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
        }`}
      >
        {Icon && <Icon className="mr-3 h-5 w-5 flex-shrink-0" />}
        <span className="truncate">{link.title}</span>
      </div>
    </Link>
  );
};

const CollapsibleNavSection = ({ section }: { section: NavSection }) => {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);

  const isSectionActive = section.children?.some(link => pathname.startsWith(link.href)) || false;

  useEffect(() => {
    if (isSectionActive) {
      setIsOpen(true);
    }
  }, [isSectionActive]);

  if (!section.children) {
    return <SidebarLink link={{ href: section.href || '#', title: section.title, icon: section.icon }} />;
  }

  const Icon = section.icon || getIcon(section.title);

  return (
    <div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center justify-between w-full px-4 py-2.5 text-sm font-medium text-left rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        <span className="flex items-center font-semibold">
          {Icon && <Icon className="mr-3 h-5 w-5 flex-shrink-0" />}
          {section.title}
        </span>
        {isOpen ? <FiChevronDown className="h-5 w-5" /> : <FiChevronRight className="h-5 w-5" />}
      </button>
      {isOpen && (
        <div className="mt-2 space-y-1">
          {section.children.map((link) => (
            <SidebarLink key={link.href} link={link} />
          ))}
        </div>
      )}
    </div>
  );
};

// --- Componente Principal del Sidebar ---
export default function Sidebar() {
  const { user, isLoading: isAuthLoading } = useAuth();
  const [menuData, setMenuData] = useState<NavSection[]>([]);
  const [isMenuLoading, setIsMenuLoading] = useState(true);

  useEffect(() => {
    const fetchMenu = async () => {
      if (user) {
        setIsMenuLoading(true);
        try {
          const response = await api.get<NavSection[]>('/config/dashboard-menu/');
          setMenuData(response.data);
        } catch (error) {
          console.error("Failed to fetch menu data:", error);
          // Opcional: setear un menú por defecto en caso de error
          setMenuData([]);
        } finally {
          setIsMenuLoading(false);
        }
      }
    };

    fetchMenu();
  }, [user]);

  if (isAuthLoading || (user && isMenuLoading)) return <SidebarSkeleton />;
  if (!user) return <aside className="w-64 flex-shrink-0 bg-white border-r border-gray-200" />;

  return (
    <aside className="w-64 flex-shrink-0 bg-white border-r border-gray-200 flex flex-col">
      <div className="p-4 border-b">
        <h2 className="text-xl font-bold text-gray-800 truncate">SITYC</h2>
        <p className="text-sm text-gray-500 truncate" title={user.email}>
          {user.username}
        </p>
      </div>
      <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
        {menuData.map((section) => (
          <CollapsibleNavSection key={section.title} section={section} />
        ))}
      </nav>
    </aside>
  );
}