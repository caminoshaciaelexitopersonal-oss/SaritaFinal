'use client';

import React, { useEffect, useState } from 'react';
import { useAxios } from '@/hooks/useAxios';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

// Tipos para los datos de la API
interface EstadisticasData {
  total_reservas: number;
  total_clientes: number;
  total_valoraciones: number;
  ingresos_totales: string;
  reservas_ultimo_mes: number;
  tendencia_reservas_anual: { mes: string; reservas: number }[];
}

const EstadisticasManager = () => {
  const { GDI, loading, error } = useAxios();
  const [data, setData] = useState<EstadisticasData | null>(null);

  useEffect(() => {
    const fetchEstadisticas = async () => {
      try {
        const response = await GDI.get<EstadisticasData>('/prestadores/mi-negocio/estadisticas/');
        setData(response.data);
      } catch (err) {
        console.error('Error al cargar las estadísticas:', err);
      }
    };

    fetchEstadisticas();
  }, [GDI]);

  if (loading) {
    return <p>Cargando estadísticas...</p>;
  }

  if (error) {
    return <p className="text-red-500">Error al cargar las estadísticas: {error.message}</p>;
  }

  if (!data) {
    return <p>No hay datos de estadísticas disponibles.</p>;
  }

  const chartData = {
    labels: data.tendencia_reservas_anual.map(item => item.mes),
    datasets: [
      {
        label: 'Reservas por Mes',
        data: data.tendencia_reservas_anual.map(item => item.reservas),
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: true,
        text: 'Tendencia de Reservas (Últimos 12 Meses)',
      },
    },
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Estadísticas de Mi Negocio</h1>

      {/* KPIs */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold text-gray-700">Ingresos Totales</h2>
          <p className="text-3xl font-bold text-green-600">${data.ingresos_totales}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold text-gray-700">Reservas Totales</h2>
          <p className="text-3xl font-bold">{data.total_reservas}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold text-gray-700">Nuevas Reservas (30 días)</h2>
          <p className="text-3xl font-bold">{data.reservas_ultimo_mes}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold text-gray-700">Clientes Registrados</h2>
          <p className="text-3xl font-bold">{data.total_clientes}</p>
        </div>
      </div>

      {/* Gráfico */}
      <div className="bg-white p-6 rounded-lg shadow">
        <Bar options={chartOptions} data={chartData} />
      </div>
    </div>
  );
};

export default EstadisticasManager;
