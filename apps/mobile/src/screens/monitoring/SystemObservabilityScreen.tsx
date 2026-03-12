import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const SystemObservabilityScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Observabilidad del Sistema</Text>

      <Card style={styles.healthCard}>
        <Text style={styles.healthLabel}>Estado de Infraestructura AWS</Text>
        <Text style={styles.healthStatus}>OPERATIVO ✓</Text>
        <Text style={styles.healthDetail}>Latencia Global: 45ms | Uptime: 99.99%</Text>
      </Card>

      <Text style={styles.sectionTitle}>Tráfico en Tiempo Real</Text>
      <Card style={styles.metricCard}>
        <Text style={styles.metricLabel}>Peticiones / min</Text>
        <Text style={styles.metricValue}>12.4K</Text>
      </Card>

      <Card style={styles.metricCard}>
        <Text style={styles.metricLabel}>Usuarios Activos Globales</Text>
        <Text style={styles.metricValue}>4,820</Text>
      </Card>

      <View style={styles.sentryBox}>
        <Text style={styles.sentryText}>Sentry & Datadog: Monitoreo Activo</Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0f172a', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#fff', marginBottom: 20 },
  healthCard: { padding: 25, backgroundColor: '#1e293b', borderLeftWidth: 5, borderColor: '#10b981' },
  healthLabel: { color: '#94a3b8', fontSize: 12 },
  healthStatus: { color: '#10b981', fontSize: 24, fontWeight: 'bold', marginVertical: 5 },
  healthDetail: { color: '#64748b', fontSize: 10 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#fff', marginVertical: 20 },
  metricCard: { padding: 20, backgroundColor: '#1e293b', marginBottom: 12 },
  metricLabel: { color: '#94a3b8', fontSize: 12 },
  metricValue: { color: '#fff', fontSize: 20, fontWeight: 'bold', marginTop: 5 },
  sentryBox: { marginTop: 30, padding: 15, backgroundColor: 'rgba(255,255,255,0.05)', borderRadius: 10 },
  sentryText: { color: '#94a3b8', fontSize: 10, textAlign: 'center' }
});
