import React, { useEffect, useState } from 'react';
import { UnifiedGovernmentDashboard, RiskHeatmap } from '@sarita/shared-ui';
import { ControlTowerService } from '@sarita/shared-sdk';

export const AdminDashboard = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [stats, alerts, providers] = await Promise.all([
          ControlTowerService.getGlobalStats(),
          ControlTowerService.getSystemAlerts(),
          ControlTowerService.getProviderMonitoring()
        ]);

        setData({
          stats,
          alerts,
          providers,
          regionData: [
            { id: '1', label: 'Centro', value: 85 },
            { id: '2', label: 'Norte', value: 42 }
          ],
          trends: {
            bookings: [{ label: 'Q1', value: 2400 }],
            revenue: [{ label: 'Q1', value: 1250000 }]
          },
          reports: [
            { id: '1', name: 'Auditoría Anual 2026', lastGenerated: '2026-03-01', type: 'institutional' }
          ],
          riskZones: [
            { label: 'Ciberseguridad', level: 12 },
            { label: 'Cumplimiento Legal', level: 5 },
            { label: 'Disponibilidad Cloud', level: 95 }
          ]
        });
      } catch (error) {
        console.error("Error loading admin data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div className="p-8 font-bold animate-pulse">Sincronizando con la Torre de Control...</div>;

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <UnifiedGovernmentDashboard
        platform="desktop"
        data={data}
      />

      <section className="bg-white p-6 rounded-lg border border-gray-200 shadow-sm">
        <h2 className="text-xl font-bold mb-4 text-gray-800">Auditoría Sistémica de Riesgo (Desktop Mode)</h2>
        <RiskHeatmap zones={data.riskZones} />
      </section>
    </div>
  );
};
