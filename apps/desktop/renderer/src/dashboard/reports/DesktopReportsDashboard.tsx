import React, { useEffect, useState } from 'react';
import { KPIWidget, ChartCard, ReportTable, Text, DataExporter } from '@sarita/shared-ui';

export const DesktopReportsDashboard = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulando carga de datos analíticos densos
    setTimeout(() => {
      setData({
        financialKPIs: [
          { label: 'Ingresos Totales', value: '$452.8M', trend: '+12.5%', pos: true },
          { label: 'Utilidad Neta', value: '$84.2M', trend: '+8.1%', pos: true },
          { label: 'EBITDA', value: '22.4%', trend: '+1.2%', pos: true },
          { label: 'Runway', value: '18 Meses', trend: 'Estable', pos: true }
        ],
        revenueChart: [
          { label: 'Ene', value: 380, color: '#3b82f6' },
          { label: 'Feb', value: 420, color: '#3b82f6' },
          { label: 'Mar', value: 550, color: '#10b981' }
        ],
        operationalTable: [
          { date: '2026-03-10', type: 'Venta Directa', amount: '$1.2M', status: 'Sincronizado' },
          { date: '2026-03-11', type: 'Reserva Online', amount: '$2.5M', status: 'Sincronizado' },
          { date: '2026-03-12', type: 'Pago QR', amount: '$0.8M', status: 'Pendiente' }
        ]
      });
      setLoading(false);
    }, 800);
  }, []);

  if (loading) return <div className="p-10 font-bold animate-pulse">Generando Inteligencia de Negocio...</div>;

  return (
    <div className="p-8 space-y-10 animate-in fade-in duration-700">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold text-gray-900">Centro Analítico Empresarial</h1>
          <p className="text-gray-500">Reportes consolidados y auditoría financiera SARITA ERP.</p>
        </div>
        <DataExporter
          reportName="Cierre de Mes - Consolidado"
          onExport={(format) => console.log(`Exporting desktop report as ${format}`)}
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {data.financialKPIs.map((kpi: any, i: number) => (
          <KPIWidget key={i} label={kpi.label} value={kpi.value} trend={kpi.trend} isPositive={kpi.pos} />
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <ChartCard
            title="Evolución de Ingresos (Mensual)"
            data={data.revenueChart}
            type="line"
          />
        </div>
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <h3 className="font-bold mb-4">Exportación Masiva</h3>
          <ul className="space-y-4">
            <li className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span className="text-sm font-medium">Libro Mayor .xlsx</span>
              <button className="text-blue-600 font-bold text-xs">DESCARGAR</button>
            </li>
            <li className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span className="text-sm font-medium">Estado P&L .pdf</span>
              <button className="text-blue-600 font-bold text-xs">DESCARGAR</button>
            </li>
          </ul>
        </div>
      </div>

      <ReportTable
        title="Últimas Operaciones Sincronizadas"
        columns={[
          { key: 'date', header: 'Fecha' },
          { key: 'type', header: 'Tipo de Operación' },
          { key: 'amount', header: 'Monto' },
          { key: 'status', header: 'Estado' }
        ]}
        data={data.operationalTable}
      />
    </div>
  );
};
