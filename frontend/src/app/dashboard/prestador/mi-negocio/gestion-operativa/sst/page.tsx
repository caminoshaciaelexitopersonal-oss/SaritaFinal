'use client';

import React, { useEffect, useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import {
  FiShield,
  FiPlus,
  FiAlertTriangle,
  FiActivity,
  FiCheckCircle,
  FiFileText,
  FiTrendingUp
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { useMiNegocioApi } from '../../hooks/useMiNegocioApi';

export default function SG_SST_Page() {
  const { getSSTRisks, getSSTIncidents, isLoading } = useMiNegocioApi();
  const [risks, setRisks] = useState<any[]>([]);
  const [incidents, setIncidents] = useState<any[]>([]);

  useEffect(() => {
    const loadData = async () => {
      const [r, i] = await Promise.all([getSSTRisks(), getSSTIncidents()]);
      if (r) setRisks(r);
      if (i) setIncidents(i);
    };
    loadData();
  }, [getSSTRisks, getSSTIncidents]);

  return (
    <div className="space-y-10 animate-in fade-in duration-700">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight uppercase italic leading-none mb-2">Sistema de Gestión SST</h1>
          <p className="text-slate-500 dark:text-slate-400 text-lg">Seguridad y Salud en el Trabajo. Cumplimiento normativo y prevención de riesgos.</p>
        </div>
        <div className="flex gap-4">
           <Button variant="outline" className="border-slate-200 dark:border-white/5 font-black text-xs uppercase tracking-widest px-8">
              Autoevaluación
           </Button>
           <Button className="bg-brand text-white font-black px-8 py-6 rounded-2xl shadow-xl shadow-brand/20">
              <FiPlus className="mr-2" /> Reportar Incidente
           </Button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8 overflow-hidden relative">
            <div className="absolute right-0 top-0 p-8 opacity-5 text-brand">
               <FiActivity size={120} />
            </div>
            <p className="text-slate-400 font-bold uppercase tracking-widest text-xs mb-2 italic">Índice de Accidentalidad</p>
            <h3 className="text-4xl font-black text-slate-900 dark:text-white">0.0%</h3>
            <p className="mt-4 text-xs text-emerald-600 font-bold uppercase tracking-widest flex items-center gap-2">
               <FiCheckCircle /> Cumplimiento Óptimo
            </p>
         </Card>

         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8 overflow-hidden relative">
            <div className="absolute right-0 top-0 p-8 opacity-5 text-indigo-600">
               <FiShield size={120} />
            </div>
            <p className="text-slate-400 font-bold uppercase tracking-widest text-xs mb-2 italic">Riesgos Identificados</p>
            <h3 className="text-4xl font-black text-slate-900 dark:text-white">12</h3>
            <p className="mt-4 text-xs text-amber-600 font-bold uppercase tracking-widest">3 Requieren intervención</p>
         </Card>

         <Card className="border-none shadow-xl bg-slate-900 text-white p-8">
            <p className="text-brand-light font-black uppercase tracking-widest text-[10px] mb-4 italic">Alerta de Capacitación</p>
            <h3 className="text-2xl font-black leading-tight italic">SADI recomienda brigada de primeros auxilios para Agosto.</h3>
            <Button className="w-full bg-brand hover:bg-brand-light font-black py-4 mt-6 rounded-xl">Programar</Button>
         </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
         {/* Matriz de Riesgos */}
         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/10 overflow-hidden">
            <CardHeader className="p-8 border-b border-slate-50 dark:border-white/5 bg-white dark:bg-black/40">
               <CardTitle className="text-xl font-bold flex items-center gap-3 italic text-brand">
                  <FiAlertTriangle /> Matriz de Riesgos Prioritaria
               </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
               <Table>
                  <TableHeader className="bg-slate-50 dark:bg-black/20">
                     <TableRow>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest px-8">Área / Proceso</TableHead>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest">Factor de Riesgo</TableHead>
                        <TableHead className="font-bold text-[10px] uppercase tracking-widest text-center">Nivel</TableHead>
                     </TableRow>
                  </TableHeader>
                  <TableBody>
                     {risks.map((risk, i) => (
                       <TableRow key={i} className="hover:bg-slate-50 dark:hover:bg-white/5 transition-colors border-slate-50 dark:border-white/5">
                          <TableCell className="px-8 font-bold text-slate-700 dark:text-slate-200 uppercase tracking-tighter italic">{risk.clasificacion}</TableCell>
                          <TableCell className="text-sm text-slate-500 font-medium">{risk.peligro_descripcion}</TableCell>
                          <TableCell className="text-center">
                             <Badge className={risk.nivel_riesgo > 10 ? 'bg-red-100 text-red-700' : risk.nivel_riesgo > 5 ? 'bg-amber-100 text-amber-700' : 'bg-blue-100 text-blue-700'}>
                                {risk.nivel_riesgo}
                             </Badge>
                          </TableCell>
                       </TableRow>
                     ))}
                  </TableBody>
               </Table>
            </CardContent>
         </Card>

         {/* Registro de Incidentes */}
         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/10 overflow-hidden">
            <CardHeader className="p-8 border-b border-slate-50 dark:border-white/5 bg-white dark:bg-black/40">
               <CardTitle className="text-xl font-bold flex items-center gap-3 italic text-brand">
                  <FiFileText /> Libro de Incidentes
               </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
               <div className="divide-y divide-slate-50 dark:divide-white/5">
                  {incidents.map((inc, i) => (
                    <div key={i} className="p-8 hover:bg-slate-50 dark:hover:bg-white/5 transition-all flex items-center justify-between">
                       <div>
                          <div className="flex items-center gap-3 mb-1">
                             <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">{new Date(inc.fecha_hora).toLocaleDateString()}</span>
                             <Badge variant="outline" className="text-[8px] font-black">{inc.tipo}</Badge>
                             <Badge className={inc.gravedad === 'MORTAL' ? 'bg-black text-white' : inc.gravedad === 'GRAVE' ? 'bg-red-600 text-white' : 'bg-amber-500 text-white'}>{inc.gravedad}</Badge>
                          </div>
                          <p className="font-bold text-slate-800 dark:text-slate-200">{inc.descripcion_hechos}</p>
                       </div>
                       <Badge className={inc.estado_investigacion === 'CERRADA' ? 'bg-emerald-100 text-emerald-700' : 'bg-amber-100 text-amber-700'}>
                          {inc.estado_investigacion}
                       </Badge>
                    </div>
                  ))}
                  {incidents.length === 0 && (
                    <div className="p-20 text-center text-slate-400 italic text-sm">No se registran incidentes laborales.</div>
                  )}
               </div>
            </CardContent>
         </Card>
      </div>

      <Card className="border-none shadow-xl bg-indigo-600 text-white p-10 rounded-[2.5rem] relative overflow-hidden">
         <div className="absolute -left-10 -bottom-10 opacity-20 group-hover:scale-125 transition-transform duration-700">
            <FiTrendingUp size={250} />
         </div>
         <h3 className="text-2xl font-black mb-4 italic italic">Auditoría SST Lista para Pasar</h3>
         <p className="text-indigo-100 max-w-2xl leading-relaxed font-medium">Has completado el 94% de los requisitos del estándar mínimo. Genera el reporte para el Ministerio del Trabajo o para la autoridad gubernamental.</p>
         <Button className="bg-white text-indigo-600 font-black py-4 px-10 mt-10 rounded-xl">Generar Reporte Maestro</Button>
      </Card>
    </div>
  );
}
