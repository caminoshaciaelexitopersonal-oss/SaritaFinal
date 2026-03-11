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
        // En un entorno real, llamaríamos a ReportingService.getAnalyticsSummary()
        // Simulamos la respuesta para la paridad funcional
        const mockData = {
          kpis: [
            { label: 'Ingresos Hoy', value: '$1.2M', trend: '+5%', pos: true },
            { label: 'Ocupación', value: '82%', trend: '+2%', pos: true },
            { label: 'Alertas', value: '3', trend: '-1', pos: true }
          ],
          touristChart: [
            { label: 'Ene', value: 45 },
            { label: 'Feb', value: 62 },
            { label: 'Mar', value: 88 }
          ],
          topProviders: [
            { name: 'Hotel Sol', cat: 'Hospedaje', score: '4.9' },
            { name: 'EcoPark', cat: 'Aventura', score: '4.7' }
          ]
        };
        setData(mockData);
      } catch (err) {
        console.error(err);
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
