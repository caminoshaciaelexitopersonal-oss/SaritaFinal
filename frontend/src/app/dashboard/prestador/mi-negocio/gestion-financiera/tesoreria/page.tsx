'use client';

import React, { useEffect, useState } from 'react';
import { useMiNegocioApi } from '../hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Button } from '@/components/ui/Button';
import { FiPlus, FiFilter, FiDownload, FiDollarSign } from 'react-icons/fi';

export default function TesoreriaPage() {
  const { getTesoreria, getCashTransactions, isLoading } = useMiNegocioApi();
  const [data, setData] = useState<any>(null);
  const [transactions, setTransactions] = useState<any[]>([]);

  useEffect(() => {
    const load = async () => {
      const [t, txs] = await Promise.all([getTesoreria(), getCashTransactions()]);
      if (t) setData(t[0]);
      if (txs) setTransactions(txs);
    };
    load();
  }, [getTesoreria, getCashTransactions]);

  return (
    <div className="space-y-8 py-8">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-black text-slate-900 tracking-tight">Tesorería Central</h1>
          <p className="text-slate-500">Gestión de efectivo, bancos y flujo de caja real.</p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline"><FiDownload className="mr-2"/> Movimientos</Button>
          <Button className="bg-brand text-white font-black"><FiPlus className="mr-2"/> Nuevo Movimiento</Button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card className="border-none shadow-sm bg-white p-6">
          <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Disponible</p>
          <p className="text-3xl font-black text-slate-900">${data ? parseFloat(data.liquidez_disponible).toLocaleString() : '0.00'}</p>
        </Card>
        <Card className="border-none shadow-sm bg-white p-6">
          <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">En Reservas</p>
          <p className="text-3xl font-black text-slate-900">${data ? parseFloat(data.reservas_totales).toLocaleString() : '0.00'}</p>
        </Card>
        <Card className="border-none shadow-sm bg-white p-6">
          <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Custodia Total</p>
          <p className="text-3xl font-black text-brand">${data ? parseFloat(data.saldo_total_custodia).toLocaleString() : '0.00'}</p>
        </Card>
      </div>

      <Card className="border-none shadow-sm overflow-hidden bg-white">
        <CardHeader className="border-b bg-slate-50/50">
          <CardTitle className="text-lg font-bold flex items-center gap-2">
            <FiDollarSign className="text-brand" /> Órdenes de Pago Recientes
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Fecha</TableHead>
                <TableHead>Concepto</TableHead>
                <TableHead>Beneficiario</TableHead>
                <TableHead className="text-right">Monto</TableHead>
                <TableHead>Estado</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {transactions.map((tx: any) => (
                <TableRow key={tx.id}>
                  <TableCell className="text-xs">{new Date(tx.fecha_pago).toLocaleDateString()}</TableCell>
                  <TableCell className="font-bold">{tx.concepto}</TableCell>
                  <TableCell className="text-xs text-slate-500">{tx.beneficiario_id || 'N/A'}</TableCell>
                  <TableCell className="text-right font-mono font-bold">${parseFloat(tx.monto).toLocaleString()}</TableCell>
                  <TableCell>
                    <span className={`px-2 py-1 rounded-full text-[10px] font-black uppercase ${tx.estado === 'PAGADA' ? 'bg-green-100 text-green-700' : 'bg-amber-100 text-amber-700'}`}>
                      {tx.estado}
                    </span>
                  </TableCell>
                </TableRow>
              ))}
              {transactions.length === 0 && (
                <TableRow>
                  <TableCell colSpan={5} className="text-center py-20 opacity-30 italic">No hay órdenes de pago registradas.</TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
