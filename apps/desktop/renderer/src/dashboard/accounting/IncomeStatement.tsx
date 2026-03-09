import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Landmark, TrendingUp, TrendingDown, FileText } from 'lucide-react';

export const IncomeStatement = () => {
  const [pnl, setPnl] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPnL = async () => {
      try {
        const response = await accountingService.getIncomeStatement();
        setPnl(response.data);
      } catch (error) {
        console.error('Error al obtener Estado de Resultados real.');
      } finally {
        setLoading(false);
      }
    };
    fetchPnL();
  }, []);

  if (loading) return <div className="p-10 text-center text-gray-400">Calculando Utilidad Neta Real...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Estado de Resultados (P&L)</h2>
        <span className="text-xs font-bold text-gray-400 uppercase tracking-widest bg-gray-100 px-3 py-1 rounded-full border">Periodo Fiscal Actual</span>
      </div>

      <div className="bg-white p-10 rounded-2xl shadow-xl border border-gray-100 max-w-3xl mx-auto space-y-8 relative overflow-hidden">
        <div className="absolute top-0 right-0 p-4 text-gray-100 opacity-20"><Landmark size={80} /></div>

        <div className="space-y-4">
          <div className="flex justify-between text-xl font-bold border-b pb-4 text-gray-800">
            <span className="flex items-center gap-2"><TrendingUp className="text-green-500" /> INGRESOS OPERACIONALES</span>
            <span>${pnl?.total_ingresos?.toLocaleString()} COP</span>
          </div>
          {pnl?.ingresos_detalle?.map((i: any) => (
            <div key={i.nombre} className="flex justify-between text-sm text-gray-500 pl-4 italic">
              <span>{i.nombre}</span>
              <span>${i.monto?.toLocaleString()}</span>
            </div>
          ))}
        </div>

        <div className="space-y-4 border-t pt-8">
          <div className="flex justify-between text-xl font-bold text-red-600 border-b pb-4">
            <span className="flex items-center gap-2"><TrendingDown /> COSTOS Y GASTOS</span>
            <span>(${pnl?.total_gastos?.toLocaleString()}) COP</span>
          </div>
          {pnl?.gastos_detalle?.map((g: any) => (
            <div key={g.nombre} className="flex justify-between text-sm text-gray-500 pl-4 italic">
              <span>{g.nombre}</span>
              <span>(${g.monto?.toLocaleString()})</span>
            </div>
          ))}
        </div>

        <div className="border-t-4 border-primary pt-10 flex justify-between items-center bg-gray-50 p-6 rounded-xl border border-gray-100 shadow-inner">
          <div className="flex flex-col">
            <span className="text-xs font-bold text-gray-400 uppercase tracking-tighter">Resultado del Ejercicio</span>
            <span className="text-2xl font-bold text-primary">UTILIDAD NETA FISCAL</span>
          </div>
          <span className="text-3xl font-bold text-green-600">${pnl?.utilidad_neta?.toLocaleString()} COP</span>
        </div>
      </div>
    </div>
  );
};
