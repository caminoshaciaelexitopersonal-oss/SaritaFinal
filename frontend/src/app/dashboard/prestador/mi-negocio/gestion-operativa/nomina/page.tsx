'use client';

import React, { useEffect, useState } from 'react';
import { useMiNegocioApi } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import {
  FiUsers,
  FiPlus,
  FiFileText,
  FiTrendingUp,
  FiCheckCircle,
  FiCalendar
} from 'react-icons/fi';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Badge } from '@/components/ui/Badge';

export default function NominaPage() {
  const { isLoading } = useMiNegocioApi();

  const employees = [
    { name: 'Juan Perez', role: 'Operativo', salary: '$1,200', status: 'ACTIVE', joinDate: '2023-01-10' },
    { name: 'Maria Lopez', role: 'Administrativo', salary: '$1,800', status: 'ACTIVE', joinDate: '2022-05-15' },
  ];

  return (
    <div className="space-y-8 animate-in fade-in duration-700">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">Gestión de Nómina y Talento</h1>
          <p className="text-slate-500 dark:text-slate-400 mt-1">Administración de contratos, salarios y prestaciones sociales.</p>
        </div>
        <Button className="bg-brand hover:bg-brand-light text-white font-black px-8 py-6 rounded-2xl shadow-lg shadow-brand/20 transition-all">
           <FiPlus className="mr-2" /> Vincular Empleado
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8 group cursor-default">
            <div className="flex justify-between items-start mb-6">
               <div className="p-4 bg-brand/10 text-brand rounded-2xl group-hover:scale-110 transition-transform">
                  <FiUsers size={24} />
               </div>
               <Badge variant="outline" className="text-[10px] font-black uppercase tracking-tighter">Total</Badge>
            </div>
            <p className="text-slate-400 font-bold uppercase tracking-widest text-[10px] mb-1">Colaboradores</p>
            <h3 className="text-3xl font-black text-slate-900 dark:text-white">08</h3>
         </Card>

         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8 group cursor-default">
            <div className="flex justify-between items-start mb-6">
               <div className="p-4 bg-emerald-50 text-emerald-600 rounded-2xl group-hover:scale-110 transition-transform">
                  <FiCheckCircle size={24} />
               </div>
            </div>
            <p className="text-slate-400 font-bold uppercase tracking-widest text-[10px] mb-1">Estatus PILA</p>
            <h3 className="text-3xl font-black text-slate-900 dark:text-white">Al Día</h3>
         </Card>

         <Card className="border-none shadow-sm bg-brand text-white p-8 overflow-hidden relative">
            <div className="absolute right-[-20%] bottom-[-20%] opacity-20">
               <FiTrendingUp size={150} />
            </div>
            <p className="text-white/60 font-bold uppercase tracking-widest text-[10px] mb-2">Costo Laboral Mes</p>
            <h3 className="text-3xl font-black">$4.2M</h3>
            <p className="mt-4 text-xs font-medium text-white/80">Incluyendo aportes de ley.</p>
         </Card>
      </div>

      <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/10 overflow-hidden">
         <CardHeader className="p-6 border-b border-slate-50 dark:border-white/5 flex flex-row items-center justify-between bg-white dark:bg-black/40">
            <CardTitle className="text-lg font-bold flex items-center gap-2 italic">
               <FiFileText className="text-brand" /> Registro de Personal
            </CardTitle>
            <Button variant="ghost" className="text-xs font-black text-brand uppercase tracking-widest">Descargar Planilla</Button>
         </CardHeader>
         <CardContent className="p-0">
            <Table>
               <TableHeader className="bg-slate-50 dark:bg-black/20">
                  <TableRow>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest">Colaborador</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest">Cargo / Función</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest">Vinculación</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest">Asignación</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest text-center">Estado</TableHead>
                  </TableRow>
               </TableHeader>
               <TableBody>
                  {employees.map((emp, i) => (
                    <TableRow key={i} className="hover:bg-slate-50 dark:hover:bg-white/5 transition-colors border-slate-50 dark:border-white/5">
                       <TableCell>
                          <div className="flex items-center gap-3">
                             <div className="w-8 h-8 rounded-full bg-slate-100 dark:bg-white/10 flex items-center justify-center font-bold text-xs text-slate-400 uppercase">
                                {emp.name.charAt(0)}
                             </div>
                             <span className="font-bold text-slate-700 dark:text-slate-200">{emp.name}</span>
                          </div>
                       </TableCell>
                       <TableCell className="text-sm text-slate-500 font-medium">{emp.role}</TableCell>
                       <TableCell className="text-xs text-slate-400 font-bold uppercase tracking-widest">{emp.joinDate}</TableCell>
                       <TableCell className="font-black text-slate-900 dark:text-white">{emp.salary}</TableCell>
                       <TableCell className="text-center">
                          <Badge className="bg-emerald-100 text-emerald-700 border-none font-bold text-[9px]">ACTIVO</Badge>
                       </TableCell>
                    </TableRow>
                  ))}
               </TableBody>
            </Table>
            <div className="p-12 text-center bg-slate-50/50 dark:bg-black/20 border-t border-slate-50 dark:border-white/5">
               <FiCalendar size={32} className="mx-auto text-slate-200 mb-4" />
               <p className="text-sm font-bold text-slate-400 uppercase tracking-widest">Próximo Pago: 30 de Agosto</p>
            </div>
         </CardContent>
      </Card>
    </div>
  );
}
