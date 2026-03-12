import React from 'react';

export function MobileLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      <header className="bg-white p-4 border-b border-slate-200">
        <div className="font-bold text-lg text-primary">SARITA Mobile</div>
      </header>
      <main className="flex-1 p-4">
        {children}
      </main>
      <nav className="bg-white border-t border-slate-200 p-3 flex justify-around">
        {/* Tab Bar Mock */}
        <span className="text-xs">Inicio</span>
        <span className="text-xs">Reservas</span>
        <span className="text-xs">Perfil</span>
      </nav>
    </div>
  );
}
