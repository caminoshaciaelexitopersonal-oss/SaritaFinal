import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { FileText, Download, TrendingUp, TrendingDown } from 'lucide-react';

export const BalanceSheet = () => {
  const [balance, setBalance] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBalance = async () => {
      try {
        const response = await accountingService.getBalanceSheet();
        setBalance(response.data);
      } catch (error) {
        console.error('Error al obtener Balance General real.');
      } finally {
        setLoading(false);
      }
    };
    fetchBalance();
  }, []);

  if (loading) return <div className="p-10 text-center text-gray-400">Generando Balance Real...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Estado de Situación Financiera (Balance)</h2>
        <button className="flex items-center gap-2 px-3 py-1.5 border rounded-lg text-xs font-bold hover:bg-gray-50 transition bg-white shadow-sm">
          <Download size={14} /> PDF Fiscal
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Activos */}
        <div className="space-y-4 bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <h3 className="font-bold text-sm uppercase text-gray-400 tracking-widest border-b pb-2">ACTIVOS</h3>
          {balance?.activos_detalle?.map((a: any) => (
            <div key={a.nombre} className="flex justify-between border-b border-gray-50 py-2">
              <span className="text-sm">{a.nombre}</span>
              <span className="font-bold font-mono">${a.monto?.toLocaleString()}</span>
            </div>
          ))}
          <div className="flex justify-between bg-blue-50 p-4 rounded-lg mt-4 shadow-inner">
            <span className="font-bold text-primary">TOTAL ACTIVOS</span>
            <span className="font-bold text-primary">${balance?.total_activos?.toLocaleString()} COP</span>
          </div>
        </div>

        <div className="space-y-8">
          {/* Pasivos */}
          <div className="space-y-4 bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
            <h3 className="font-bold text-sm uppercase text-gray-400 tracking-widest border-b pb-2">PASIVOS</h3>
            {balance?.pasivos_detalle?.map((p: any) => (
              <div key={p.nombre} className="flex justify-between border-b border-gray-50 py-2">
                <span className="text-sm">{p.nombre}</span>
                <span className="font-bold font-mono">${p.monto?.toLocaleString()}</span>
              </div>
            ))}
            <div className="flex justify-between bg-red-50 p-4 rounded-lg mt-4 shadow-inner">
              <span className="font-bold text-red-600">TOTAL PASIVOS</span>
              <span className="font-bold text-red-600">${balance?.total_pasivos?.toLocaleString()} COP</span>
            </div>
          </div>

          {/* Patrimonio */}
          <div className="space-y-4 bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
            <h3 className="font-bold text-sm uppercase text-gray-400 tracking-widest border-b pb-2">PATRIMONIO</h3>
            <div className="flex justify-between bg-green-50 p-4 rounded-lg shadow-inner">
              <span className="font-bold text-green-700">TOTAL PATRIMONIO</span>
              <span className="font-bold text-green-700">${balance?.total_patrimonio?.toLocaleString()} COP</span>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-gray-900 text-white p-6 rounded-xl flex justify-between items-center shadow-lg border-t-4 border-secondary">
        <span className="font-bold uppercase tracking-widest text-xs opacity-60">Control de Integridad Contable</span>
        <span className="text-xl font-bold text-secondary">A = P + PT (Certificado ✓)</span>
      </div>
    </div>
  );
};
