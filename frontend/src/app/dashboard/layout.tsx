"use client";

import '../globals.css'; // Importación explícita de los estilos globales
import React, { useState, useEffect } from 'react';
import Sidebar from '@/components/Sidebar';
import Header from '@/components/Header';
import { useAuth } from '@/contexts/AuthContext';
import { useRouter, usePathname } from 'next/navigation';

// Componente interno para el layout autenticado
// Esto asegura que los hooks solo se usen dentro de un contexto autenticado y renderizado
const AuthenticatedLayout = ({ children }: { children: React.ReactNode }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // Hook para bloquear el scroll del body cuando el sidebar móvil está abierto
  useEffect(() => {
    if (isSidebarOpen) {
      document.body.classList.add('overflow-hidden');
    } else {
      document.body.classList.remove('overflow-hidden');
    }
    // Limpieza al desmontar
    return () => {
      document.body.classList.remove('overflow-hidden');
    };
  }, [isSidebarOpen]);

  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar para Desktop */}
      <div className="hidden lg:flex lg:flex-shrink-0">
        <Sidebar />
      </div>

      {/* Sidebar para Móvil (Drawer) */}
      <div
        className={`lg:hidden fixed inset-0 z-50 transition-transform transform ${
          isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
        role="dialog"
        aria-modal="true"
      >
        <div
          className="fixed inset-0 bg-black/60"
          aria-hidden="true"
          onClick={() => setIsSidebarOpen(false)}
        ></div>
        <div className="relative bg-white h-full w-64 shadow-xl">
          <Sidebar />
        </div>
      </div>

      <div className="flex flex-col flex-1 w-0 lg:overflow-x-hidden">
        <Header isSidebarOpen={isSidebarOpen} setIsSidebarOpen={setIsSidebarOpen} />
        <main className="flex-1 relative z-0 focus:outline-none p-4 sm:p-6 lg:p-8">
          {children}
        </main>
      </div>
    </div>
  );
};

// Layout principal que maneja la lógica de enrutamiento y autenticación
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { user, isLoading, isAuthenticated } = useAuth();
  const router = useRouter();
  const pathname = usePathname();

  // Mover todas las comprobaciones condicionales que retornan temprano al principio
  // sin llamar a hooks después de ellas.

  // Si estamos en páginas públicas, no se necesita el layout autenticado.
  if (pathname.startsWith('/dashboard/login') || pathname.startsWith('/dashboard/registro')) {
    return <>{children}</>;
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <p className="text-xl text-gray-600">Verificando acceso...</p>
      </div>
    );
  }

  if (!isAuthenticated && !pathname.startsWith('/dashboard/login') && !pathname.startsWith('/dashboard/registro')) {
    // Redirige al login si no está autenticado y no está ya en una página pública del dashboard
    router.push('/dashboard/login');
    return null; // O un componente de carga mientras redirige
  }

  if (user?.role === 'TURISTA') {
    router.push('/mi-viaje');
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <p className="text-xl text-gray-600">Acceso denegado. Redirigiendo...</p>
      </div>
    );
  }

  // Si todas las comprobaciones pasan, renderiza el layout autenticado.
  // Todos los hooks (useState, useEffect) están ahora dentro de este componente.
  return <AuthenticatedLayout>{children}</AuthenticatedLayout>;
}