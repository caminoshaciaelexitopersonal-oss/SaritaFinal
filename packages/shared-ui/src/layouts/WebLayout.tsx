import React from 'react';

export function WebLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-slate-50 flex">
      <div className="w-64 bg-white border-r border-slate-200 p-4 hidden lg:block">
        <div className="font-bold text-xl text-primary mb-8">SARITA Web</div>
        {/* Navigation Mock */}
      </div>
      <main className="flex-1 p-8 container mx-auto">
        {children}
      </main>
    </div>
  );
}
