"use client";
import { useState, useEffect } from 'react';

export function useKpiData(apiEndpoint: string) {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulamos llamada a API
    const fetchData = async () => {
      setLoading(true);
      // await axios.get(apiEndpoint)
      setData({
        todaySales: ',240',
        activeBookings: 14,
        occupancy: '82%',
        alerts: 2
      });
      setLoading(false);
    };
    fetchData();
  }, [apiEndpoint]);

  return { data, loading };
}
