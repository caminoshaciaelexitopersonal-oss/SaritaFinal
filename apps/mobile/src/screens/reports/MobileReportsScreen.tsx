import React, { useEffect, useState } from 'react';
import { View, ScrollView, StyleSheet, ActivityIndicator } from 'react-native';
import { KPIWidget, ChartCard, ReportTable, Text } from '@sarita/shared-ui';
import { ReportingService } from '@sarita/shared-sdk';

export const MobileReportsScreen = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const response = await api.get('/tourism/intelligence/intelligence/economic-impact/');
        const results = response.data.results || [];

        const kpis = [
          { label: 'Ventas Totales', value: `$${results[0]?.ventas_totales || 0}`, trend: '+5%', pos: true },
          { label: 'Ingresos Netos', value: `$${results[0]?.ingresos_turisticos_netos || 0}`, trend: '+2%', pos: true },
          { label: 'Empleo Gen.', value: results[0]?.empleo_generado_estimado || 0, trend: '+12', pos: true }
        ];

        const chartData = results.map((r: any) => ({
          label: r.periodo,
          value: parseFloat(r.ventas_totales)
        }));

        setData({
          kpis,
          touristChart: chartData,
          topProviders: [] // Marketplace integration pending
        });
      } catch (err) {
        console.error('Mobile Reports Error:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchReports();
  }, []);

  if (loading) return <ActivityIndicator style={{ flex: 1 }} />;

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text variant="headingM" style={{ marginBottom: 20 }}>Reportes Analíticos</Text>

      <View style={styles.kpiRow}>
        {data.kpis.map((kpi: any, i: number) => (
          <KPIWidget key={i} label={kpi.label} value={kpi.value} trend={kpi.trend} isPositive={kpi.pos} />
        ))}
      </View>

      <View style={{ marginVertical: 24 }}>
        <ChartCard
          title="Flujo Turístico Mensual"
          data={data.touristChart}
          type="bar"
        />
      </View>

      <ReportTable
        title="Mejores Prestadores"
        columns={[
          { key: 'name', header: 'Nombre' },
          { key: 'score', header: 'Puntaje' }
        ]}
        data={data.topProviders}
      />
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  content: { padding: 16 },
  kpiRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 12 }
});
