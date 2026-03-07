import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { operatorService } from '../../services/operatorService';

export const OperatorDashboard = () => {
  const [metrics, setMetrics] = useState<any>({ total_earnings: 0, active_bookings: 0 });

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await operatorService.getEarnings();
        setMetrics(response.data);
      } catch (error) {}
    };
    fetchMetrics();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Panel del Operador</Text>

      <View style={styles.metricsRow}>
        <Card style={styles.metricCard}>
          <Text style={styles.metricLabel}>Ingresos Totales</Text>
          <Text style={styles.metricValue}>${metrics.total_earnings?.toLocaleString()} COP</Text>
        </Card>
        <Card style={styles.metricCard}>
          <Text style={styles.metricLabel}>Comisión Plataforma</Text>
          <Text style={[styles.metricValue, { color: '#ef4444' }]}>
            -${metrics.platform_fee?.toLocaleString() || 0}
          </Text>
        </Card>
      </View>

      <Text style={styles.sectionTitle}>Gestión de Experiencias</Text>
      <Card style={styles.actionCard}>
        <Text style={styles.actionText}>Tours Activos: {metrics.active_tours || 0}</Text>
      </Card>

      <Card style={styles.actionCard}>
        <Text style={styles.actionText}>Reservas Pendientes: {metrics.pending_bookings || 0}</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  metricsRow: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 20 },
  metricCard: { flex: 0.48, padding: 15, alignItems: 'center' },
  metricLabel: { fontSize: 12, color: '#6b7280' },
  metricValue: { fontSize: 18, fontWeight: 'bold', color: '#10b981', marginTop: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 15 },
  actionCard: { marginBottom: 10, padding: 20 },
  actionText: { fontWeight: '600' }
});
