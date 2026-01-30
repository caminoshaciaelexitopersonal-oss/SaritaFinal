'use client';

import React from 'react';
import Link from 'next/link';
import { useComercialApi } from './hooks/useComercialApi';
import { Button } from '@/components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import {
  FiPlus,
  FiDollarSign,
  FiFileText,
  FiTrendingUp,
  FiBarChart,
  FiZap
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';

export default function GestionComercialPage() {
  const { facturas, isLoading, isError } = useComercialApi();

  if (isError) {
    return (
        <Card className="border-red-100 bg-red-50">
            <CardContent className="p-12 text-center">
                <h2 className="text-xl font-bold text-red-700">Error de Conexión</h2>
                <p className="text-red-600 mt-2">No se pudieron cargar las facturas. Por favor, intente de nuevo más tarde.</p>
            </CardContent>
        </Card>
    );
  }

  return (
    <div className="space-y-8 animate-in fade-in slide-in-from-top-4 duration-700">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Gestión Comercial y Ventas</h1>
          <p className="text-gray-500 mt-1">Facturación electrónica, seguimiento de leads y funnel de ventas.</p>
        </div>
        <div className="flex gap-3">
          <Link href="/dashboard/prestador/mi-negocio/gestion-comercial/ventas/nueva" passHref>
            <Button className="bg-indigo-600 hover:bg-indigo-700 shadow-indigo-200 shadow-lg">
              <FiPlus className="mr-2" /> Nueva Factura
            </Button>
          </Link>
          <Button variant="outline" className="border-gray-200">
            <FiBarChart className="mr-2" /> Analytics
          </Button>
        </div>
      </div>

      {/* Sales Analytics Summary */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
         <Card className="border-none shadow-sm bg-gradient-to-br from-indigo-600 to-violet-700 text-white">
            <CardContent className="p-8">
               <div className="flex justify-between items-start">
                  <div>
                     <p className="text-indigo-100 text-sm font-medium">Ventas del Mes</p>
                     <h3 className="text-3xl font-black mt-1">$0.00</h3>
                  </div>
                  <FiTrendingUp size={32} className="text-indigo-300" />
               </div>
               <p className="mt-6 text-xs text-indigo-200 font-bold uppercase tracking-widest">Meta Mensual: 0% alcanzado</p>
            </CardContent>
         </Card>

         <Card className="border-none shadow-sm bg-white">
            <CardContent className="p-8">
               <div className="flex justify-between items-start">
                  <div>
                     <p className="text-gray-500 text-sm font-medium">Facturas Pendientes</p>
                     <h3 className="text-3xl font-black mt-1 text-slate-900">0</h3>
                  </div>
                  <div className="p-3 bg-amber-50 text-amber-600 rounded-2xl">
                     <FiFileText size={24} />
                  </div>
               </div>
               <p className="mt-6 text-xs text-amber-600 font-bold">Requieren atención inmediata</p>
            </CardContent>
         </Card>

         <Card className="border-none shadow-sm bg-white">
            <CardContent className="p-8">
               <div className="flex justify-between items-start">
                  <div>
                     <p className="text-gray-500 text-sm font-medium">Conversión de Lead</p>
                     <h3 className="text-3xl font-black mt-1 text-slate-900">0%</h3>
                  </div>
                  <div className="p-3 bg-emerald-50 text-emerald-600 rounded-2xl">
                     <FiZap size={24} />
                  </div>
               </div>
               <p className="mt-6 text-xs text-emerald-600 font-bold">SADI está optimizando tu funnel</p>
            </CardContent>
         </Card>
      </div>

      {/* Main Content Area */}
      <Card className="border-none shadow-sm overflow-hidden">
        <CardHeader className="flex flex-row items-center justify-between border-b border-gray-50 bg-white p-6">
          <CardTitle className="text-lg font-bold flex items-center gap-2">
             <FiDollarSign className="text-indigo-600" /> Historial de Facturación
          </CardTitle>
          <div className="flex gap-2">
             <Badge variant="outline" className="rounded-md">Todos</Badge>
             <Badge variant="outline" className="rounded-md opacity-50">Pagados</Badge>
             <Badge variant="outline" className="rounded-md opacity-50">Pendientes</Badge>
          </div>
        </CardHeader>
        <CardContent className="p-0">
          {isLoading && facturas.length === 0 ? (
            <div className="p-12 space-y-4">
               {[...Array(3)].map((_, i) => <div key={i} className="h-12 bg-gray-50 rounded-xl animate-pulse" />)}
            </div>
          ) : (
            <div className="overflow-x-auto">
              <Table>
                <TableHeader className="bg-gray-50/50">
                  <TableRow>
                    <TableHead className="font-bold">N° Factura</TableHead>
                    <TableHead className="font-bold">Cliente</TableHead>
                    <TableHead className="font-bold">Fecha Emisión</TableHead>
                    <TableHead className="font-bold text-right">Monto Total</TableHead>
                    <TableHead className="font-bold text-center">Estado</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {facturas.map((factura) => (
                    <TableRow key={factura.id} className="hover:bg-gray-50/50 transition-colors border-gray-50">
                      <TableCell className="font-bold text-indigo-600">{factura.numero_factura}</TableCell>
                      <TableCell className="font-medium text-slate-700">{factura.cliente_nombre}</TableCell>
                      <TableCell className="text-slate-500 text-sm">{new Date(factura.fecha_emision).toLocaleDateString()}</TableCell>
                      <TableCell className="text-right font-black text-slate-900">${parseFloat(factura.total).toLocaleString()}</TableCell>
                      <TableCell className="text-center">
                        <Badge className={factura.estado === 'PAGADA' ? 'bg-emerald-100 text-emerald-700' : 'bg-amber-100 text-amber-700'}>
                          {factura.estado_display}
                        </Badge>
                      </TableCell>
                    </TableRow>
                  ))}
                  {facturas.length === 0 && (
                    <TableRow>
                       <TableCell colSpan={5} className="text-center py-24">
                          <div className="flex flex-col items-center opacity-20">
                             <FiFileText size={64} />
                             <p className="mt-4 font-black text-xl">No hay registros comerciales.</p>
                             <p className="text-sm">Tus facturas de venta aparecerán aquí.</p>
                          </div>
                       </TableCell>
                    </TableRow>
                  )}
                </TableBody>
              </Table>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
