'use client';

import React, { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// Tipos de datos
type SummaryStats = {
  total_reservas_confirmadas: number;
  total_clientes: number;
  ingresos_ultimo_mes: string;
};

type ReservasPorEstado = {
  estado: string;
  count: number;
};

type AnalyticsData = {
  summary: SummaryStats;
  reservas_por_estado: ReservasPorEstado[];
};

const Estadisticas = () => {
  const [data, setData] = useState<AnalyticsData | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        setIsLoading(true);
        const response = await api.get<AnalyticsData>('/profile/prestador/analytics/');
        setData(response.data);
      } catch (error) {
        toast.error("No se pudieron cargar las estadísticas.");
      } finally {
        setIsLoading(false);
      }
    };
    fetchAnalytics();
  }, []);

  if (isLoading) return <div>Cargando estadísticas...</div>;
  if (!data) return <div>No hay datos de estadísticas disponibles.</div>;

  const chartData = data.reservas_por_estado.map(item => ({
      name: item.estado,
      Reservas: item.count
  }));

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Reportes y Estadísticas</h1>

      {/* Tarjetas de Resumen */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-xl font-semibold text-gray-600">Reservas Confirmadas</h3>
          <p className="text-4xl font-bold mt-2">{data.summary.total_reservas_confirmadas}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-xl font-semibold text-gray-600">Total de Clientes</h3>
          <p className="text-4xl font-bold mt-2">{data.summary.total_clientes}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-xl font-semibold text-gray-600">Ingresos (Últ. 30 días)</h3>
          <p className="text-4xl font-bold mt-2">${data.summary.ingresos_ultimo_mes}</p>
        </div>
      </div>

      {/* Gráfico de Reservas */}
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h3 className="text-xl font-semibold mb-4">Distribución de Reservas por Estado</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="Reservas" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default Estadisticas;