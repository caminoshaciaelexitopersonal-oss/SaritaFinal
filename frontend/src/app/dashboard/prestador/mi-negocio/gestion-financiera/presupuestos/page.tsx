'use client';

import React, { useEffect, useState } from 'react';
import { useMiNegocioApi } from '../hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Button } from '@/components/ui/Button';
import { FiPlus, FiTarget, FiAlertTriangle } from 'react-icons/fi';

export default function PresupuestosPage() {
  const { getPresupuestos, isLoading } = useMiNegocioApi();
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    const load = async () => {
      const res = await getPresupuestos();
      if (res) setData(res);
    };
    load();
  }, [getPresupuestos]);

  return (
    <div className="space-y-8 py-8">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-black text-slate-900 tracking-tight">Presupuestos</h1>
          <p className="text-slate-500">Planificación y control de ejecución por centro de costo.</p>
        </div>
        <Button className="bg-brand text-white font-black"><FiPlus className="mr-2"/> Nuevo Presupuesto Anual</Button>
      </div>

      <div className="grid grid-cols-1 gap-6">
        {data.map((p: any) => {
          const progress = (parseFloat(p.total_ejecutado) / parseFloat(p.total_estimado)) * 100;
          return (
            <Card key={p.id} className="border-none shadow-sm overflow-hidden bg-white">
              <CardHeader className="flex flex-row items-center justify-between border-b bg-slate-50/30">
                <div>
                  <CardTitle className="text-xl font-black">{p.nombre}</CardTitle>
                  <p className="text-xs font-bold text-slate-400 uppercase tracking-widest">Año Fiscal {p.año}</p>
                </div>
                <div className="text-right">
                  <p className="text-[10px] font-black text-slate-400 uppercase">Ejecución Total</p>
                  <p className="text-xl font-black text-brand">{progress.toFixed(1)}%</p>
                </div>
              </CardHeader>
              <CardContent className="p-8">
                <div className="h-4 bg-slate-100 rounded-full overflow-hidden mb-8 shadow-inner">
                  <div
                    style={{ width: `${Math.min(progress, 100)}%` }}
                    className={`h-full transition-all duration-1000 ${progress > 90 ? 'bg-red-500' : progress > 70 ? 'bg-amber-500' : 'bg-brand'}`}
                  />
                </div>

                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead>Concepto</TableHead>
                      <TableHead className="text-right">Presupuestado</TableHead>
                      <TableHead className="text-right">Ejecutado</TableHead>
                      <TableHead className="text-right">Disponible</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {p.lineas?.map((l: any) => (
                      <TableRow key={l.id}>
                        <TableCell className="font-bold">{l.nombre_item}</TableCell>
                        <TableCell className="text-right font-mono">${parseFloat(l.monto_presupuestado).toLocaleString()}</TableCell>
                        <TableCell className="text-right font-mono text-red-500">${parseFloat(l.monto_ejecutado).toLocaleString()}</TableCell>
                        <TableCell className="text-right font-mono font-black text-slate-900">${(parseFloat(l.monto_presupuestado) - parseFloat(l.monto_ejecutado)).toLocaleString()}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </CardContent>
            </Card>
          );
        })}

        {data.length === 0 && (
           <div className="py-32 text-center bg-white rounded-3xl border-2 border-dashed border-slate-100 flex flex-col items-center">
              <FiTarget size={64} className="text-slate-100 mb-4" />
              <p className="text-xl font-black text-slate-300 uppercase tracking-tighter">Sin presupuestos activos</p>
              <p className="text-sm text-slate-400 mt-1">Defina sus metas financieras para comenzar el seguimiento.</p>
           </div>
        )}
      </div>
    </div>
  );
}
