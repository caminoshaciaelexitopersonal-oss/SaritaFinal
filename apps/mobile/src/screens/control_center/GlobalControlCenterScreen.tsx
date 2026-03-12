import React from 'react';
import { View, Text, StyleSheet, ScrollView, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const GlobalControlCenterScreen = () => {
  const alerts = [
    { id: '1', level: 'CRITICAL', msg: 'Saturación detectada en Venecia, Italia. Activando desvío.', time: 'Justo ahora' },
    { id: '2', level: 'WARNING', msg: 'Tormenta tropical en el Caribe afecta 12 rutas.', time: 'Hace 5 min' },
  ];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Global Control Center</Text>
      <Text style={styles.subtitle}>Gobernanza y monitoreo del turismo mundial.</Text>

      <Card style={styles.mainMetrics}>
        <Text style={styles.metricLabel}>Viajeros SARITA en Tránsito Global</Text>
        <Text style={styles.metricValue}>1.42M</Text>
        <Text style={styles.metricSub}>Sincronización Cloud AWS Multi-Región</Text>
      </Card>

      <Text style={styles.sectionTitle}>Alertas de Gobernanza</Text>
      {alerts.map(a => (
        <Card key={a.id} style={[styles.alertCard, a.level === 'CRITICAL' && styles.criticalBorder]}>
          <Text style={[styles.alertLevel, a.level === 'CRITICAL' && styles.criticalText]}>{a.level}</Text>
          <Text style={styles.alertMsg}>{a.msg}</Text>
          <Text style={styles.alertTime}>{a.time}</Text>
        </Card>
      ))}

      <Text style={styles.sectionTitle}>Estatus de Coordinación</Text>
      <Card style={styles.statusCard}>
        <Text style={styles.statusText}>✓ Alianza con OMT: Sincronizada</Text>
        <Text style={styles.statusText}>✓ Protocolos de Crisis: Standby</Text>
        <Text style={styles.statusText}>✓ Datos OpenResearch: Publicando</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0f172a', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: '#94a3b8', fontSize: 13, marginTop: 5 },
  mainMetrics: { padding: 30, backgroundColor: '#1e293b', borderBottomWidth: 5, borderColor: '#3b82f6', marginTop: 20 },
  metricLabel: { color: '#94a3b8', fontSize: 12 },
  metricValue: { color: '#fff', fontSize: 42, fontWeight: 'bold', marginVertical: 10 },
  metricSub: { color: '#3b82f6', fontSize: 10, fontWeight: 'bold' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#fff', marginVertical: 20 },
  alertCard: { padding: 15, marginBottom: 12, backgroundColor: '#1e293b' },
  criticalBorder: { borderColor: '#ef4444', borderWidth: 1 },
  alertLevel: { fontWeight: 'bold', color: '#f59e0b', fontSize: 12 },
  criticalText: { color: '#ef4444' },
  alertMsg: { color: '#e2e8f0', marginTop: 5, lineHeight: 20 },
  alertTime: { color: '#64748b', fontSize: 10, marginTop: 10 },
  statusCard: { padding: 20, backgroundColor: '#1e293b' },
  statusText: { color: '#10b981', fontWeight: 'bold', marginBottom: 5 }
});
