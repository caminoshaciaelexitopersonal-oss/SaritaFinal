'use client';

import React, { useState, useEffect } from 'react';
import { getConversationalKPIs, getStrategyProposals } from '@/services/intelligence';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { FiMessageSquare, FiTrendingUp, FiTarget, FiZap } from 'react-icons/fi';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

export default function EstadisticasNegocioPage() {
  const [kpis, setKpis] = useState<any[]>([]);
  const [proposals, setProposals] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      getConversationalKPIs(),
      getStrategyProposals()
    ]).then(([kpiRes, propRes]) => {
      setKpis(kpiRes);
      setProposals(propRes);
      setLoading(false);
    });
  }, []);

  if (loading) return <div className="p-10 text-center animate-pulse font-black uppercase text-slate-400">Analizando métricas del negocio...</div>;

  return (
    <div className="space-y-8 p-6 animate-in fade-in duration-500 max-w-6xl mx-auto">
      <div>
        <h1 className="text-3xl font-black text-slate-900 tracking-tight">Estadísticas e Inteligencia</h1>
        <p className="text-slate-500">Analítica real basada en tus interacciones y proyecciones de SADI.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card className="border-none shadow-sm bg-indigo-600 text-white">
          <CardContent className="p-6">
            <FiMessageSquare size={32} className="mb-4 opacity-50" />
            <p className="text-xs font-bold uppercase tracking-widest opacity-70">Calidad de Respuesta</p>
            <h3 className="text-4xl font-black mt-1">{(kpis[0]?.response_rate * 100 || 0).toFixed(0)}%</h3>
            <p className="text-xs mt-2 font-medium">Basado en chat con turistas</p>
          </CardContent>
        </Card>
        <Card className="border-none shadow-sm bg-white">
          <CardContent className="p-6">
            <FiTrendingUp size={32} className="mb-4 text-emerald-500" />
            <p className="text-xs font-bold uppercase tracking-widest text-slate-400">Demanda Estimada</p>
            <h3 className="text-4xl font-black text-slate-900 mt-1">+15%</h3>
            <p className="text-xs mt-2 text-slate-500">Proyección para el próximo mes</p>
          </CardContent>
        </Card>
        <Card className="border-none shadow-sm bg-white border-l-4 border-amber-500">
          <CardContent className="p-6">
            <FiZap size={32} className="mb-4 text-amber-500" />
            <p className="text-xs font-bold uppercase tracking-widest text-slate-400">Oportunidades IA</p>
            <h3 className="text-4xl font-black text-slate-900 mt-1">{proposals.length}</h3>
            <p className="text-xs mt-2 text-slate-500">Acciones sugeridas por el sistema</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <Card className="border-none shadow-xl rounded-[2rem] bg-white overflow-hidden">
          <CardHeader className="p-8 border-b">
            <CardTitle className="text-lg font-black uppercase">Interacciones por Período</CardTitle>
          </CardHeader>
          <CardContent className="p-8 h-[350px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={kpis}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                <XAxis dataKey="period" axisLine={false} tickLine={false} />
                <YAxis axisLine={false} tickLine={false} />
                <Tooltip cursor={{fill: '#f8fafc'}} />
                <Bar dataKey="total_chats" fill="#6366f1" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card className="border-none shadow-xl rounded-[2rem] bg-slate-900 text-white overflow-hidden">
          <CardHeader className="p-8 border-b border-slate-800">
            <CardTitle className="text-lg font-black uppercase text-indigo-400">Estrategias de Optimización</CardTitle>
          </CardHeader>
          <CardContent className="p-8">
            <div className="space-y-6">
              {proposals.length > 0 ? proposals.map((p: any) => (
                <div key={p.id} className="p-4 bg-slate-800 rounded-2xl border border-slate-700">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-[10px] font-black uppercase tracking-tighter bg-indigo-500/20 text-indigo-300 px-2 py-1 rounded">IA Suggestion</span>
                    <span className="text-[10px] text-slate-500 font-bold">{p.created_at.split('T')[0]}</span>
                  </div>
                  <p className="text-sm font-bold mb-1">{p.oportunidad_detectada}</p>
                  <p className="text-xs text-slate-400 leading-relaxed">{p.impacto_estimado}</p>
                </div>
              )) : (
                <div className="text-center py-10 opacity-30 italic">No hay propuestas estratégicas pendientes.</div>
              )}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
