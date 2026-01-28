// frontend/src/components/Header.tsx
import React from 'react';
import { Menu, Bell, User } from 'lucide-react';

interface HeaderProps {
  isSidebarOpen: boolean;
  setIsSidebarOpen: (isOpen: boolean) => void;
}

 
const Header: React.FC<HeaderProps> = ({ isSidebarOpen, setIsSidebarOpen }) => {
 
  return (
    <header className="bg-white shadow-sm">
      <div className="mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Botón para menú móvil */}
          <button
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            className="lg:hidden text-gray-500 hover:text-gray-700"
            aria-label="Abrir menú"
          >
            <Menu className="h-6 w-6" />
          </button>

          {/* Espaciador para centrar el título o dejarlo vacío */}
          <div className="flex-1"></div>

          {/* Iconos de la derecha */}
          <div className="flex items-center space-x-4">
            <button className="text-gray-500 hover:text-gray-700">
              <Bell className="h-6 w-6" />
            </button>
            <button className="text-gray-500 hover:text-gray-700">
              <User className="h-6 w-6" />
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
