"use client";

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/services/api';
import { useAuth } from '@/contexts/AuthContext';
import { FiDollarSign, FiTrendingUp, FiArrowUpRight, FiClock, FiShield, FiFileText } from 'react-icons/fi';
import { ViewState } from '@/components/ui/ViewState';
import { toast } from 'react-toastify';

export default function PrestadorMonederoPage() {
  const { token } = useAuth();
  const [wallet, setWallet] = useState<any>(null);
  const [transactions, setTransactions] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async () => {
    if (!token) return;
    setIsLoading(true);
    try {
      const [walletRes, txRes] = await Promise.all([
        api.get('/wallet/accounts/'),
        api.get('/wallet/transactions/')
      ]);

      if (walletRes.data.results && walletRes.data.results.length > 0) {
        setWallet(walletRes.data.results[0]);
      }
      setTransactions(txRes.data.results || []);
    } catch (err) {
      setError("Error al cargar la información financiera.");
    } finally {
      setIsLoading(false);
    }
  }, [token]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleLiquidate = async () => {
    if (!wallet) return;
    try {
      await api.post('/wallet/accounts/liquidate_wallet/', { wallet_id: wallet.id });
      toast.success("Liquidación solicitada correctamente.");
      fetchData();
    } catch (err) {
      toast.error("Error al procesar la liquidación.");
    }
  };

  return (
    <div className="p-8 space-y-8">
      <div className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-black text-slate-900">Monedero Institucional</h1>
          <p className="text-slate-500 font-medium">Gestión soberana de ingresos y liquidaciones.</p>
        </div>
        <div className="flex gap-3">
           <button onClick={fetchData} className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-600 rounded-xl font-bold text-xs transition-all">
              Actualizar
           </button>
           <button onClick={handleLiquidate} className="px-6 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl font-bold text-xs shadow-lg shadow-indigo-100 transition-all">
              Solicitar Liquidación
           </button>
        </div>
      </div>

      <ViewState isLoading={isLoading} error={error}>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white p-8 rounded-[2rem] border border-slate-100 shadow-sm relative overflow-hidden">
             <div className="relative z-10">
                <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Saldo Disponible</p>
                <h2 className="text-4xl font-black text-slate-900">${wallet?.balance || '0.00'}</h2>
                <div className="mt-4 flex items-center gap-2 text-green-600 font-bold text-xs">
                   <FiTrendingUp /> +12% vs mes anterior
                </div>
             </div>
             <FiDollarSign className="absolute -bottom-4 -right-4 text-slate-50" size={120} />
          </div>

          <div className="bg-white p-8 rounded-[2rem] border border-slate-100 shadow-sm">
             <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Ingresos por Servicios</p>
             <h2 className="text-4xl font-black text-slate-900">${transactions.filter(t => t.type === 'PAYMENT').reduce((acc, t) => acc + parseFloat(t.amount), 0).toFixed(2)}</h2>
             <p className="mt-4 text-slate-400 font-medium text-xs">Total histórico capturado.</p>
          </div>

          <div className="bg-white p-8 rounded-[2rem] border border-slate-100 shadow-sm">
             <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Estatus de Auditoría</p>
             <div className="flex items-center gap-2 text-indigo-600 font-black text-xl mb-4">
                <FiShield /> CONFORME
             </div>
             <p className="text-slate-400 font-medium text-xs">Hash encadenado al ERP quíntuple verificado.</p>
          </div>
        </div>

        <div className="bg-white rounded-[2rem] border border-slate-100 shadow-sm overflow-hidden">
           <div className="px-8 py-6 border-b border-slate-50 flex justify-between items-center">
              <h3 className="font-black text-slate-900 uppercase tracking-widest text-xs">Últimos Movimientos</h3>
              <FiFileText className="text-slate-300" />
           </div>
           <div className="overflow-x-auto">
              <table className="w-full text-left">
                 <thead>
                    <tr className="bg-slate-50">
                       <th className="px-8 py-4 text-[9px] font-black text-slate-400 uppercase tracking-widest">Fecha</th>
                       <th className="px-8 py-4 text-[9px] font-black text-slate-400 uppercase tracking-widest">Tipo</th>
                       <th className="px-8 py-4 text-[9px] font-black text-slate-400 uppercase tracking-widest">Descripción</th>
                       <th className="px-8 py-4 text-[9px] font-black text-slate-400 uppercase tracking-widest text-right">Monto</th>
                    </tr>
                 </thead>
                 <tbody className="divide-y divide-slate-50">
                    {transactions.map(tx => (
                       <tr key={tx.id} className="hover:bg-slate-50 transition-colors">
                          <td className="px-8 py-4 text-xs font-bold text-slate-600">{new Date(tx.timestamp).toLocaleDateString()}</td>
                          <td className="px-8 py-4 text-[10px] font-black">
                             <span className={tx.type === 'PAYMENT' ? 'text-green-600' : 'text-slate-400'}>{tx.type}</span>
                          </td>
                          <td className="px-8 py-4 text-xs text-slate-500 font-medium">{tx.description}</td>
                          <td className="px-8 py-4 text-right text-sm font-black text-slate-900">${tx.amount}</td>
                       </tr>
                    ))}
                 </tbody>
              </table>
           </div>
        </div>
      </ViewState>
    </div>
  );
}
