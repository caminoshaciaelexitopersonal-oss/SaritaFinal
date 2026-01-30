'use client';

import React, { useState } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import {
  FiDollarSign,
  FiMegaphone,
  FiTrendingUp,
  FiZap,
  FiLayout,
  FiActivity,
  FiSettings,
  FiFileText
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import { useComercialApi } from './hooks/useComercialApi';

// Importación de los niveles de clase mundial
import Level1_Communication from './components/Level1_Communication';
import Level2_Responses from './components/Level2_Responses';
import LevelAIStudio from './components/LevelAIStudio';
import LevelFunnels from './components/LevelFunnels';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import Link from 'next/link';

enum CommercialView {
  DASHBOARD = 'dashboard',
  MARKETING = 'marketing',
  SALES_CRM = 'sales_crm',
  AI_STUDIO = 'ai_studio',
  FUNNELS = 'funnels',
  INVOICING = 'invoicing'
}

export default function GestionComercialPage() {
  const { token } = useAuth();
  const [activeView, setActiveView] = useState<CommercialView>(CommercialView.DASHBOARD);
  const { facturas, isLoading } = useComercialApi();

  const renderContent = () => {
    switch (activeView) {
      case CommercialView.MARKETING:
        return <Level1_Communication authToken={token!} />;
      case CommercialView.SALES_CRM:
        return <Level2_Responses />;
      case CommercialView.AI_STUDIO:
        return <LevelAIStudio />;
      case CommercialView.FUNNELS:
        return <LevelFunnels authToken={token!} />;
      case CommercialView.INVOICING:
        return (
          <div className="p-8 space-y-6">
             <div className="flex justify-between items-center">
                <h2 className="text-2xl font-black text-slate-900 dark:text-white uppercase italic">Libro de Ventas y Facturación</h2>
                <Link href="/dashboard/prestador/mi-negocio/gestion-comercial/ventas/nueva">
                   <Button className="bg-brand text-white font-black px-6"><FiPlus className="mr-2"/> Emitir Factura</Button>
                </Link>
             </div>
             <Card className="border-none shadow-sm overflow-hidden">
                <CardContent className="p-0">
                  <Table>
                    <TableHeader className="bg-slate-50 dark:bg-black/20">
                      <TableRow>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest px-8">N° Factura</TableHead>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest">Cliente</TableHead>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest">Fecha</TableHead>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest text-right px-8">Monto</TableHead>
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {facturas.map((f: any) => (
                        <TableRow key={f.id} className="hover:bg-slate-50 dark:hover:bg-white/5 transition-colors border-slate-50 dark:border-white/5">
                          <TableCell className="font-mono text-xs font-black text-brand px-8">{f.numero_factura}</TableCell>
                          <TableCell className="font-bold text-slate-700 dark:text-slate-200">{f.cliente_nombre}</TableCell>
                          <TableCell className="text-xs text-slate-500">{new Date(f.fecha_emision).toLocaleDateString()}</TableCell>
                          <TableCell className="text-right font-black text-slate-900 dark:text-white px-8">${parseFloat(f.total).toLocaleString()}</TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </CardContent>
             </Card>
          </div>
        );
      case CommercialView.DASHBOARD:
      default:
        return (
          <div className="p-8 space-y-10 animate-in fade-in duration-700">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
              <div>
                <h1 className="text-4xl font-black text-slate-900 dark:text-white tracking-tighter uppercase leading-none">Crecimiento y Ventas</h1>
                <p className="text-slate-500 dark:text-slate-400 mt-2 text-lg">Centro de mando comercial del Operador Turístico.</p>
              </div>
              <div className="flex bg-slate-100 dark:bg-brand-deep/30 p-1 rounded-xl">
                 <button className="px-6 py-2 bg-white dark:bg-brand shadow-sm rounded-lg text-sm font-bold text-slate-900 dark:text-white">Snapshot</button>
                 <button className="px-6 py-2 text-sm font-bold text-slate-500 hover:text-slate-700">Historial</button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
               {[
                 { label: 'Ingresos Mes', val: '$12.4k', icon: FiDollarSign, color: 'text-brand' },
                 { label: 'Leads Nuevos', val: '24', icon: FiUsers, color: 'text-indigo-600' },
                 { label: 'Conversión', val: '18%', icon: FiZap, color: 'text-amber-500' },
                 { label: 'Tickets Activos', val: '08', icon: FiActivity, color: 'text-emerald-600' },
               ].map((kpi, i) => (
                 <Card key={i} className="border-none shadow-sm bg-white dark:bg-brand-deep/20">
                    <CardContent className="p-8 flex items-center justify-between">
                       <div>
                          <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">{kpi.label}</p>
                          <h3 className="text-3xl font-black text-slate-900 dark:text-white">{kpi.val}</h3>
                       </div>
                       <div className={`p-4 rounded-2xl bg-slate-50 dark:bg-black/20 ${kpi.color}`}>
                          <kpi.icon size={24} />
                       </div>
                    </CardContent>
                 </Card>
               ))}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
               <Card className="border-none shadow-xl bg-slate-900 text-white rounded-[2rem] p-10 overflow-hidden relative group cursor-pointer" onClick={() => setActiveView(CommercialView.FUNNELS)}>
                  <div className="absolute -right-10 -bottom-10 opacity-10 group-hover:scale-110 transition-transform duration-1000">
                     <FiLayout size={250} />
                  </div>
                  <Badge className="bg-brand-light text-brand-deep font-black mb-4">OPTIMIZADOR IA</Badge>
                  <h3 className="text-3xl font-black italic leading-tight">Arquitecto de Embudos</h3>
                  <p className="mt-4 text-slate-400 text-lg">Diseña flujos de conversión automatizados para tus paquetes turísticos.</p>
                  <Button className="mt-10 bg-white text-slate-900 font-black px-8 py-4 rounded-xl">Configurar Ahora</Button>
               </Card>

               <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 rounded-[2rem] p-10 flex flex-col justify-between" onClick={() => setActiveView(CommercialView.MARKETING)}>
                  <div>
                    <FiMegaphone className="text-brand mb-6" size={40} />
                    <h3 className="text-2xl font-black text-slate-900 dark:text-white uppercase tracking-tighter">Marketing Multicanal</h3>
                    <p className="mt-2 text-slate-500">Envía promociones por WhatsApp, Email y Redes Sociales en un solo clic.</p>
                  </div>
                  <div className="mt-10 flex items-center gap-2 text-brand font-black text-xs uppercase tracking-widest cursor-pointer group">
                     Ir al estudio <FiArrowRight className="group-hover:translate-x-2 transition-transform" />
                  </div>
               </Card>
            </div>
          </div>
        );
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-black transition-colors flex flex-col">
       {/* Sub-nav horizontal corporativo */}
       <div className="bg-white dark:bg-brand-deep/10 border-b border-slate-100 dark:border-white/5 flex items-center px-8 gap-8 overflow-x-auto no-scrollbar sticky top-0 z-30 backdrop-blur-md">
          {[
            { id: CommercialView.DASHBOARD, label: 'Resumen', icon: FiActivity },
            { id: CommercialView.MARKETING, label: 'Marketing', icon: FiMegaphone },
            { id: CommercialView.SALES_CRM, label: 'Ventas y CRM', icon: FiTrendingUp },
            { id: CommercialView.AI_STUDIO, label: 'Estudio AI', icon: FiZap },
            { id: CommercialView.FUNNELS, label: 'Arquitecto', icon: FiLayout },
            { id: CommercialView.INVOICING, label: 'Facturación', icon: FiFileText },
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveView(tab.id)}
              className={`py-6 flex items-center gap-2 text-xs font-black uppercase tracking-widest transition-all border-b-2 ${
                activeView === tab.id
                ? 'border-brand text-brand'
                : 'border-transparent text-slate-400 hover:text-slate-600 dark:hover:text-slate-200'
              }`}
            >
              <tab.icon size={16} />
              {tab.label}
            </button>
          ))}
       </div>

       <div className="flex-1 overflow-y-auto">
          {renderContent()}
       </div>
    </div>
  );
}

import { FiUsers, FiArrowRight, FiPlus } from 'react-icons/fi';
