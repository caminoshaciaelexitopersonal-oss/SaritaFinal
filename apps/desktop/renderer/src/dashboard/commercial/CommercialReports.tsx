import React from 'react';
import { BarChart3, PieChart, TrendingUp, Download } from 'lucide-react';

export const CommercialReports = () => {
  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Reportes y Analítica</h2>
        <button className="flex items-center gap-2 px-4 py-2 border rounded-lg text-gray-600 hover:bg-gray-50 transition font-bold text-sm">
          <Download size={18} /> Exportar Datos (Excel/PDF)
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <div className="flex items-center gap-3 mb-6">
            <BarChart3 className="text-primary" />
            <h3 className="font-bold">Crecimiento de Ventas Mensuales</h3>
          </div>
          <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center border border-dashed border-gray-200">
            <span className="text-gray-400 text-sm italic">[ Gráfico de Barras: Evolución de Ingresos ]</span>
          </div>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <div className="flex items-center gap-3 mb-6">
            <PieChart className="text-primary" />
            <h3 className="font-bold">Distribución de Clientes por Segmento</h3>
          </div>
          <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center border border-dashed border-gray-200">
            <span className="text-gray-400 text-sm italic">[ Gráfico de Torta: VIP vs Recurrente vs Nuevo ]</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          { label: 'Valor Promedio Venta', value: '$85.50 USD', delta: '+12%' },
          { label: 'Tasa de Conversión', value: '18.4%', delta: '+5%' },
          { label: 'Retención de Clientes', value: '42%', delta: '+3%' },
        ].map(kpi => (
          <div key={kpi.label} className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
            <p className="text-xs text-gray-500 font-bold uppercase tracking-wider">{kpi.label}</p>
            <div className="flex items-end gap-3 mt-4">
              <span className="text-2xl font-bold">{kpi.value}</span>
              <span className="text-green-500 text-sm font-bold flex items-center"><TrendingUp size={14} /> {kpi.delta}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
