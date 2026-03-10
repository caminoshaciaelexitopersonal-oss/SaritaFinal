import React, { useEffect, useState } from 'react';
import { UnifiedGovernmentDashboard } from '@sarita/shared-ui';
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
            { id: '1', label: 'Meta', value: 85 },
            { id: '2', label: 'Casanare', value: 42 }
          ],
          trends: {
            bookings: [{ label: 'Mar', value: 900 }],
            revenue: [{ label: 'Mar', value: 450000 }]
          },
          reports: [
            { id: '1', name: 'Impacto Regional', lastGenerated: '2026-03-01', type: 'financial' }
          ]
        });
      } catch (error) {
        console.error("Error fetching admin data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return null;

  return (
    <UnifiedGovernmentDashboard
      platform="mobile"
      data={data}
    />
  );
};
