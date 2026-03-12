import React, { useEffect, useState } from 'react';
import { commercialService } from './commercialService';
import { ShoppingCart, Users, Target, TrendingUp } from 'lucide-react';

export const CommercialDashboard = () => {
  const [stats, setStats] = useState<any>({ monthly_sales: 0, new_customers: 0, open_ops: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await commercialService.getCommercialAnalytics();
        setStats(response.data);
      } catch (error) {
        setStats({ monthly_sales: 12450, new_customers: 24, open_ops: 8 });
      }
    };
    fetchStats();
  }, []);

  return (
    <div className="space-y-8">
      <h2 className="text-2xl font-bold text-gray-800">Dashboard Comercial</h2>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 rounded-lg bg-green-100 flex items-center justify-center mb-4 text-green-600">
            <ShoppingCart size={24} />
          </div>
          <p className="text-gray-500 text-sm font-medium">Ventas del Mes</p>
          <p className="text-2xl font-bold mt-1">${stats.monthly_sales.toLocaleString()} USD</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center mb-4 text-blue-600">
            <Users size={24} />
          </div>
          <p className="text-gray-500 text-sm font-medium">Clientes Nuevos</p>
          <p className="text-2xl font-bold mt-1">{stats.new_customers}</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 rounded-lg bg-purple-100 flex items-center justify-center mb-4 text-purple-600">
            <Target size={24} />
          </div>
          <p className="text-gray-500 text-sm font-medium">Oportunidades</p>
          <p className="text-2xl font-bold mt-1">{stats.open_ops}</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <div className="w-12 h-12 rounded-lg bg-orange-100 flex items-center justify-center mb-4 text-orange-600">
            <TrendingUp size={24} />
          </div>
          <p className="text-gray-500 text-sm font-medium">Crecimiento</p>
          <p className="text-2xl font-bold mt-1">+15%</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6">Servicios más Vendidos</h3>
          <div className="space-y-4">
            {['Safari Río Meta', 'Cena Romántica Altillanura', 'Tour Pesca Deportiva'].map((s, i) => (
              <div key={s} className="flex justify-between items-center">
                <span className="text-gray-600">{s}</span>
                <span className="font-bold text-primary">{(100 - i * 20)}%</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6">Ingresos por Canal</h3>
          <div className="space-y-4 text-sm">
            <div className="flex justify-between"><span>App Móvil</span><span className="font-bold text-green-600">$8,450.00</span></div>
            <div className="flex justify-between"><span>Portal Web</span><span className="font-bold text-blue-600">$3,200.00</span></div>
            <div className="flex justify-between"><span>Venta Directa</span><span className="font-bold text-gray-600">$800.00</span></div>
          </div>
        </div>
      </div>
    </div>
  );
};
