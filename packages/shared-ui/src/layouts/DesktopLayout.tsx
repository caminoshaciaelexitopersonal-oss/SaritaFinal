import React from 'react';

export function DesktopLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-slate-100 grid grid-cols-[250px_1fr]">
      <aside className="bg-slate-900 text-white p-6">
        <div className="font-bold text-2xl mb-12">SARITA POS</div>
        {/* Sidebar Mock */}
      </aside>
      <main className="p-10 overflow-y-auto">
        <div className="max-w-6xl mx-auto">
          {children}
        </div>
      </main>
    </div>
  );
}
