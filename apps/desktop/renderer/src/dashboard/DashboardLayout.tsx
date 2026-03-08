import React from 'react';
import { Sidebar } from './Sidebar';

export const DashboardLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex bg-gray-100 min-h-screen">
      <Sidebar />
      <main className="flex-1 p-8 overflow-y-auto">
        <header className="flex justify-between items-center mb-10">
          <h1 className="text-3xl font-bold text-gray-800 uppercase tracking-tight">Panel de Control</h1>
          <div className="flex items-center gap-4">
            <div className="text-right">
              <p className="font-bold">Admin SARITA</p>
              <p className="text-xs text-gray-500">Super Usuario</p>
            </div>
            <div className="w-10 h-10 rounded-full bg-primary flex items-center justify-center text-white">A</div>
          </div>
        </header>
        {children}
      </main>
    </div>
  );
};
