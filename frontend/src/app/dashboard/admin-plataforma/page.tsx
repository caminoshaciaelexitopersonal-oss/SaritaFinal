'use client';

import React from 'react';
import useSWR from 'swr';
import { getStatistics } from '@/services/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import {
  FiShield,
  FiTrendingUp,
  FiUsers,
  FiActivity,
  FiAlertTriangle,
  FiZap,
  FiGlobe,
  FiArrowUpRight
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import { Button } from '@/components/ui/Button';

export default function AdminPlataformaPage() {
  const { data: stats, isLoading } = useSWR('admin-statistics', getStatistics);

  const systemicAlerts = [
    { title: 'CAC Elevado detectado', domain: 'Marketing', severity: 'HIGH', msg: 'El costo de adquisición en el nodo Meta superó el LTV proyectado.' },
    { title: 'Nueva propuesta de optimización', domain: 'Finanzas', severity: 'MEDIUM', msg: 'SADI propone ajuste de tasas de comisión para prestadores nivel Oro.' },
    { title: 'Bloqueo Soberano Activo', domain: 'Global', severity: 'CRITICAL', msg: 'Operaciones comerciales restringidas en sector Puerto Gaitán por auditoría.' },
  ];

  const mainKpis = [
    { label: 'Total Usuarios Sistema', value: stats?.total_usuarios || '0', trend: 'Global', icon: FiUsers, color: 'text-blue-600' },
    { label: 'Prestadores Activos', value: stats?.total_prestadores || '0', trend: 'Vía 2', icon: FiActivity, color: 'text-indigo-600' },
    { label: 'Publicaciones Totales', value: stats?.total_publicaciones || '0', trend: 'Contenido', icon: FiGlobe, color: 'text-emerald-600' },
    { label: 'Índice de Confianza IA', value: stats?.trust_index || '98.2%', trend: 'Estable', icon: FiZap, color: 'text-amber-600' },
  ];

  return (
    <div className="space-y-10 animate-in fade-in duration-1000">
      {/* Header de Soberanía */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 border-b border-gray-100 pb-8">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="bg-slate-900 text-white p-2 rounded-lg">
              <FiShield size={24} />
            </div>
            <h1 className="text-4xl font-black text-slate-900 tracking-tighter uppercase">Centro de Soberanía Sistémica</h1>
          </div>
          <p className="text-slate-500 text-lg">Autoridad Suprema sobre el Ecosistema Sarita.</p>
        </div>
        <div className="flex gap-4">
           <div className="px-6 py-3 bg-emerald-50 border border-emerald-100 rounded-2xl flex items-center gap-3">
              <div className="w-3 h-3 bg-emerald-500 rounded-full animate-pulse" />
              <span className="text-sm font-black text-emerald-700 tracking-widest uppercase">Kernel Online</span>
           </div>
           <Button className="bg-slate-900 text-white font-bold px-8 py-6 rounded-2xl hover:bg-slate-800 transition-all">
              Intervención Manual
           </Button>
        </div>
      </div>

      {/* Grid de KPIs Maestros */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
         {mainKpis.map((kpi, i) => (
           <Card key={i} className="border-none shadow-sm hover:shadow-md transition-all bg-white group cursor-default">
              <CardContent className="p-8">
                 <div className="flex justify-between items-start mb-6">
                    <div className={`p-4 rounded-2xl bg-gray-50 ${kpi.color} group-hover:scale-110 transition-transform`}>
                       <kpi.icon size={28} />
                    </div>
                    <Badge className="bg-slate-100 text-slate-600 border-none font-bold">{kpi.trend}</Badge>
                 </div>
                 <p className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-1">{kpi.label}</p>
                 <h3 className="text-3xl font-black text-slate-900">{kpi.value}</h3>
              </CardContent>
           </Card>
         ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
         {/* Monitoreo de Inteligencia de Decisión */}
         <Card className="lg:col-span-2 border-none shadow-sm overflow-hidden bg-white">
            <CardHeader className="bg-slate-50/50 p-6 border-b border-gray-100">
               <CardTitle className="text-xl font-black flex items-center gap-2">
                  <FiActivity className="text-indigo-600" /> Monitor de Salud del Ecosistema
               </CardTitle>
            </CardHeader>
            <CardContent className="p-8">
               <div className="space-y-12">
                  {/* Gráficos / Barras de progreso visuales */}
                  <div>
                     <div className="flex justify-between items-end mb-4">
                        <div>
                           <h4 className="font-bold text-slate-800">Rentabilidad Promedio (ROI)</h4>
                           <p className="text-xs text-slate-400">Objetivo sistémico: 4.0x</p>
                        </div>
                        <span className="text-2xl font-black text-indigo-600 italic">3.4x</span>
                     </div>
                     <div className="h-4 bg-gray-100 rounded-full overflow-hidden">
                        <div className="h-full bg-indigo-500 w-[85%] shadow-inner" />
                     </div>
                  </div>

                  <div>
                     <div className="flex justify-between items-end mb-4">
                        <div>
                           <h4 className="font-bold text-slate-800">Costo de Adquisición vs LTV</h4>
                           <p className="text-xs text-slate-400">Eficiencia de Marketing Voz</p>
                        </div>
                        <span className="text-2xl font-black text-emerald-600 italic">0.22</span>
                     </div>
                     <div className="h-4 bg-gray-100 rounded-full overflow-hidden">
                        <div className="h-full bg-emerald-500 w-[45%] shadow-inner" />
                     </div>
                  </div>

                  <div className="grid grid-cols-3 gap-6 pt-4">
                     <div className="bg-slate-50 p-6 rounded-2xl text-center">
                        <p className="text-xs font-bold text-slate-400 uppercase mb-2">Churn Rate</p>
                        <p className="text-xl font-black text-slate-900">1.2%</p>
                     </div>
                     <div className="bg-slate-50 p-6 rounded-2xl text-center">
                        <p className="text-xs font-bold text-slate-400 uppercase mb-2">ARPPU</p>
                        <p className="text-xl font-black text-slate-900">$48.5</p>
                     </div>
                     <div className="bg-slate-50 p-6 rounded-2xl text-center border-2 border-indigo-100">
                        <p className="text-xs font-bold text-indigo-600 uppercase mb-2">Health Score</p>
                        <p className="text-xl font-black text-indigo-900">92/100</p>
                     </div>
                  </div>
               </div>
            </CardContent>
         </Card>

         {/* Alertas de Gobernanza */}
         <Card className="border-none shadow-xl bg-slate-900 text-white overflow-hidden">
            <CardHeader className="p-8 border-b border-white/10">
               <CardTitle className="text-xl font-black flex items-center gap-2">
                  <FiAlertTriangle className="text-amber-400" /> Alertas de Gobernanza
               </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
               <div className="divide-y divide-white/5">
                  {systemicAlerts.map((alert, i) => (
                    <div key={i} className="p-8 hover:bg-white/5 transition-colors cursor-pointer group">
                       <div className="flex justify-between items-start mb-3">
                          <span className="text-[10px] font-black uppercase tracking-[0.2em] text-indigo-400">{alert.domain}</span>
                          <Badge className={
                             alert.severity === 'CRITICAL' ? 'bg-red-500' :
                             alert.severity === 'HIGH' ? 'bg-orange-500' : 'bg-blue-500'
                          }>
                             {alert.severity}
                          </Badge>
                       </div>
                       <h4 className="font-bold text-lg mb-2 group-hover:text-indigo-300 transition-colors">{alert.title}</h4>
                       <p className="text-slate-400 text-sm leading-relaxed">{alert.msg}</p>
                    </div>
                  ))}
               </div>
               <div className="p-8 bg-indigo-600 hover:bg-indigo-700 transition-colors text-center cursor-pointer font-black uppercase tracking-widest text-sm">
                  Ver Auditoría Global
               </div>
            </CardContent>
         </Card>
      </div>
    </div>
  );
}
