import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { autonomousService } from '../../services/autonomousService';

export const GlobalAlertsScreen = () => {
  const [alerts, setAlerts] = useState<any[]>([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const response = await autonomousService.getGlobalAlerts();
        setAlerts(response.data || []);
      } catch (error) {
        setAlerts([
          { id: '1', type: 'CLIMATE', title: 'Fenómeno de El Niño', desc: 'Afectación del 30% en rutas fluviales del Meta.', severity: 'High' },
          { id: '2', type: 'FLOW', title: 'Saturación en Centro Histórico', desc: 'Se recomienda desviar grupos hacia zonas de ecoturismo.', severity: 'Medium' },
        ]);
      }
    };
    fetchAlerts();
  }, []);

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Alertas Turísticas Globales</Text>
        <Text style={styles.subtitle}>Detección proactiva de eventos que afectan al ecosistema.</Text>
      </View>

      <FlatList
        data={alerts}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={[styles.alertCard, item.severity === 'High' && styles.highSeverity]}>
            <View style={styles.row}>
              <View style={[styles.typeBadge, item.severity === 'High' && styles.highBadge]}>
                <Text style={styles.badgeText}>{item.type}</Text>
              </View>
              <Text style={styles.severityText}>Nivel: {item.severity}</Text>
            </View>
            <Text style={styles.alertTitle}>{item.title}</Text>
            <Text style={styles.alertDesc}>{item.desc}</Text>
            <TouchableOpacity style={styles.actionBtn}>
              <Text style={styles.actionText}>ACTIVAR PROTOCOLO DE RESPUESTA</Text>
            </TouchableOpacity>
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { padding: 30, backgroundColor: '#1e293b' },
  title: { fontSize: 22, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: 'rgba(255,255,255,0.6)', fontSize: 13, marginTop: 5 },
  alertCard: { marginBottom: 15, padding: 20, borderLeftWidth: 5, borderColor: '#f59e0b' },
  highSeverity: { borderColor: '#ef4444', backgroundColor: '#fef2f2' },
  row: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  typeBadge: { backgroundColor: '#e2e8f0', paddingHorizontal: 10, paddingVertical: 4, borderRadius: 5 },
  highBadge: { backgroundColor: '#ef4444' },
  badgeText: { fontSize: 10, fontWeight: 'bold', color: '#475569' },
  severityText: { fontSize: 10, color: '#64748b', fontWeight: 'bold' },
  alertTitle: { fontSize: 18, fontWeight: 'bold', color: '#1e3a8a' },
  alertDesc: { color: '#475569', marginTop: 5, lineHeight: 20 },
  actionBtn: { marginTop: 15, padding: 12, backgroundColor: '#0f172a', borderRadius: 8, alignItems: 'center' },
  actionText: { color: '#fff', fontSize: 10, fontWeight: 'bold' }
});
