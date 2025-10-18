'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { FiUserPlus, FiCalendar, FiDollarSign, FiCheckSquare, FiLoader, FiAlertTriangle } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// --- Tipos ---
interface AnalyticsSummary {
  total_reservas_confirmadas: number;
  total_clientes: number;
  ingresos_ultimo_mes: string;
}

interface ReservasPorEstado {
    estado: string;
    count: number;
}

interface AnalyticsData {
  summary: AnalyticsSummary;
  reservas_por_estado: ReservasPorEstado[];
}

// --- Componentes ---
const StatCard = ({ title, value, icon: Icon }: { title: string; value: string | number; icon: React.ElementType }) => (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex items-center">
        <div className="flex-shrink-0 p-3 bg-blue-500 rounded-md">
          <Icon className="w-6 h-6 text-white" />
        </div>
        <div className="ml-4">
          <p className="text-sm font-medium text-gray-500 truncate">{title}</p>
          <p className="text-2xl font-semibold text-gray-900">{value}</p>
        </div>
      </div>
    </div>
);

const LoadingState = () => (
    <div className="text-center py-10">
        <FiLoader className="mx-auto h-12 w-12 text-gray-400 animate-spin" />
        <p className="mt-2 text-sm font-medium text-gray-600">Cargando estadísticas...</p>
    </div>
);

const ErrorState = () => (
    <div className="text-center py-10 px-6 border-2 border-dashed border-red-300 rounded-lg bg-red-50">
        <FiAlertTriangle className="mx-auto h-12 w-12 text-red-400" />
        <p className="mt-2 text-sm font-medium text-red-700">Ocurrió un error al cargar las estadísticas. Por favor, inténtalo de nuevo más tarde.</p>
    </div>
);


const EstadisticasManager = () => {
  const [data, setData] = useState<AnalyticsData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    const fetchAnalytics = async () => {
      setIsLoading(true);
      setError(false);
      try {
        const response = await api.get('/profile/prestador/analytics/');
        setData(response.data);
      } catch (err) {
        toast.error('No se pudieron cargar los datos de estadísticas.');
        setError(true);
      } finally {
        setIsLoading(false);
      }
    };
    fetchAnalytics();
  }, []);

  if (isLoading) return <LoadingState />;
  if (error || !data) return <ErrorState />;

  const chartData = data.reservas_por_estado.map(item => ({
      name: item.estado,
      Reservas: item.count,
  }));

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Estadísticas de Rendimiento</h1>

      {/* --- Resumen General --- */}
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 mb-8">
        <StatCard title="Reservas Confirmadas" value={data.summary.total_reservas_confirmadas} icon={FiCheckSquare} />
        <StatCard title="Total de Clientes" value={data.summary.total_clientes} icon={FiUserPlus} />
        <StatCard title="Ingresos (Últimos 30 días)" value={`$${data.summary.ingresos_ultimo_mes}`} icon={FiDollarSign} />
      </div>

      {/* --- Gráfico de Reservas por Estado --- */}
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Distribución de Reservas por Estado</h2>
        {chartData.length > 0 ? (
            <ResponsiveContainer width="100%" height={300}>
                <BarChart data={chartData} margin={{ top: 5, right: 20, left: -10, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis allowDecimals={false} />
                    <Tooltip />
                    <Legend />
                    <Bar dataKey="Reservas" fill="#3B82F6" />
                </BarChart>
            </ResponsiveContainer>
        ) : (
            <p className="text-center text-gray-500">No hay datos de reservas para mostrar en el gráfico.</p>
        )}
      </div>
    </div>
  );
};

const EstadisticasPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <EstadisticasManager />
        </AuthGuard>
    )
}

export default EstadisticasPage;