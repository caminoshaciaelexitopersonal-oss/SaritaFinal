'use client';

import React, { useEffect, useState } from 'react';
import api from '@/services/api';
import { toast } from 'react-hot-toast';
import { FiDollarSign, FiTrendingUp, FiUsers, FiPieChart } from 'react-icons/fi';

export default function RentabilidadPage() {
  const [data, setData] = useState<any>(null);
  const [roiData, setRoiData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const [summaryRes, roiRes] = await Promise.all([
        api.get('/admin/finanzas/dashboard/'),
        api.get('/admin/finanzas/dashboard/roi_analysis/')
      ]);
      setData(summaryRes.data);
      setRoiData(roiRes.data);
    } catch (error) {
      toast.error("Error al cargar métricas financieras.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (loading) return <div className="p-8 text-center">Calculando ROI sistémico...</div>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-8 flex items-center gap-2">
        <FiDollarSign className="text-green-600" />
        Gobierno Financiero (ROI / CAC / LTV)
      </h1>

      <div className="grid md:grid-cols-3 gap-6 mb-10">
        <div className="bg-white p-6 rounded-xl shadow-md border-b-4 border-blue-500">
          <p className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">Conversaciones</p>
          <h2 className="text-3xl font-black">{data?.summary.total_sessions}</h2>
          <p className="text-sm text-gray-500 mt-2 flex items-center gap-1">
            <FiUsers /> Leads por voz
          </p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-md border-b-4 border-red-500">
          <p className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">Costo Adquisición (Total)</p>
          <h2 className="text-3xl font-black text-red-600">${data?.summary.total_adq_costs.toFixed(2)}</h2>
          <p className="text-sm text-gray-500 mt-2 flex items-center gap-1">
             Gasto acumulado en IA
          </p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-md border-b-4 border-green-500">
          <p className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">CAC Promedio</p>
          <h2 className="text-3xl font-black text-green-600">${data?.summary.avg_cac.toFixed(2)}</h2>
          <p className="text-sm text-gray-500 mt-2 flex items-center gap-1">
            <FiPieChart /> Por sesión de voz
          </p>
        </div>
      </div>

      <h3 className="text-lg font-bold mb-4">Análisis de Rentabilidad por Segmento (ROI)</h3>
      <div className="grid gap-4">
        {roiData.map((roi, i) => (
          <div key={i} className="bg-white p-5 rounded-lg shadow-sm border border-gray-100 flex justify-between items-center">
            <div>
              <p className="font-bold text-gray-800">{roi.dimension}</p>
              <div className="flex gap-4 mt-1 text-xs text-gray-500">
                <span>CAC: ${roi.cac}</span>
                <span>LTV: ${roi.ltv}</span>
              </div>
            </div>
            <div className="text-right">
              <span className={`text-xl font-black ${roi.roi > 5 ? 'text-green-600' : 'text-orange-500'}`}>
                {roi.roi}x
              </span>
              <p className="text-[10px] uppercase font-bold text-gray-400">ROI Proyectado</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
