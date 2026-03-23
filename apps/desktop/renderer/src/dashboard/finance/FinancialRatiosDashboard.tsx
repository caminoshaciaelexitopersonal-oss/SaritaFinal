import React from 'react';
import { Card } from '../../components/Card';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from 'recharts';

export const FinancialRatiosDashboard = ({ ratios, cashflow }: { ratios: any, cashflow: any }) => {
  // Datos simulados para tendencias (en un sistema real vendrían del backend)
  const trendData = [
    { name: 'Ene', rentabilidad: 0.12, liquidez: 1.4 },
    { name: 'Feb', rentabilidad: 0.15, liquidez: 1.6 },
    { name: 'Mar', rentabilidad: 0.18, liquidez: 1.8 },
  ];

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
      <Card>
        <h3 className="text-lg font-bold mb-6">Tendencia de Ratios</h3>
        <div className="h-[300px]">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={trendData}>
              <CartGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="rentabilidad" stroke="#1e3a8a" strokeWidth={2} name="Rentabilidad" />
              <Line type="monotone" dataKey="liquidez" stroke="#f59e0b" strokeWidth={2} name="Liquidez" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </Card>

      <Card>
        <h3 className="text-lg font-bold mb-6">Análisis de Flujo de Caja</h3>
        <div className="space-y-4">
          <div className="flex justify-between p-4 bg-gray-50 rounded-lg">
            <span className="text-gray-600 font-medium">Actividades Operativas</span>
            <span className="font-bold text-green-600">${cashflow?.operating_activities?.net_income?.toLocaleString()}</span>
          </div>
          <div className="flex justify-between p-4 bg-gray-50 rounded-lg">
            <span className="text-gray-600 font-medium">Actividades de Inversión</span>
            <span className="font-bold text-gray-800">$0</span>
          </div>
          <div className="flex justify-between p-4 bg-gray-50 rounded-lg">
            <span className="text-gray-600 font-medium">Actividades de Financiación</span>
            <span className="font-bold text-gray-800">$0</span>
          </div>
          <div className="flex justify-between p-6 bg-primary/10 rounded-lg mt-4">
            <span className="text-primary font-bold">Aumento Neto de Efectivo</span>
            <span className="text-xl font-bold text-primary">${cashflow?.net_increase_cash?.toLocaleString()}</span>
          </div>
        </div>
      </Card>
    </div>
  );
};
