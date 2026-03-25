import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Alert } from 'react-native';
import { Card } from '../../components/Card';
import { autonomousService } from '../../services/autonomousService';
import { api } from '../../services/api';

export const GlobalAIDashboard = () => {
  const [insights, setInsights] = useState<any>({ global_demand: 0, top_trend: '' });
  const [proposals, setProposals] = useState<any[]>([]);

  const loadData = async () => {
    try {
      const [aiRes, propRes] = await Promise.all([
          autonomousService.getGlobalAIInsights(),
          api.get('/governance/intelligence/proposals/')
      ]);
      setInsights(aiRes.data);
      setProposals(propRes.data || []);
    } catch (error) {}
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleApprove = async (id: string) => {
      try {
          await api.post(`/governance/intelligence/proposals/${id}/approve/`);
          Alert.alert("Éxito", "Propuesta estratégica autorizada desde móvil.");
          loadData();
      } catch (e) {
          Alert.alert("Error", "No se pudo autorizar la propuesta.");
      }
  }

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Motor Global de IA SARITA</Text>
        <Text style={styles.subtitle}>Análisis predictivo y prescriptivo de la industria mundial.</Text>
      </View>

      <Card style={styles.aiCard}>
        <Text style={styles.label}>Predicción de Demanda Mundial (Próximos 30 días)</Text>
        <Text style={styles.value}>+38.4%</Text>
        <View style={styles.badge}><Text style={styles.badgeText}>CONFIANZA IA: 98.2%</Text></View>
      </Card>

      <Text style={styles.sectionTitle}>Propuestas de Gobernanza IA</Text>
      {proposals.map((p: any) => (
          <Card key={p.id} style={styles.policyCard}>
            <View style={styles.policyHeader}>
                <Text style={styles.policyTitle}>{p.domain}</Text>
                <View style={styles.priorityBadge}><Text style={styles.priorityText}>{p.nivel_urgencia}</Text></View>
            </View>
            <Text style={styles.policyText}>{p.contexto_detectado}</Text>
            {p.status === 'PENDING' && (
                <TouchableOpacity onPress={() => handleApprove(p.id)} style={styles.approveBtn}>
                    <Text style={styles.approveBtnText}>AUTORIZAR MANDATO</Text>
                </TouchableOpacity>
            )}
            {p.status === 'APPROVED' && (
                <View style={styles.statusBadge}><Text style={styles.statusText}>✓ AUTORIZADO</Text></View>
            )}
          </Card>
      ))}
      {proposals.length === 0 && <Text style={styles.emptyText}>Sin propuestas pendientes.</Text>}

      <Text style={styles.sectionTitle}>Tendencias Detectadas por el Sistema</Text>
      {['Turismo Regenerativo', 'Nómadas Digitales 2.0', 'Expediciones Low-Carbon'].map(t => (
        <Card key={t} style={styles.trendCard}>
          <Text style={styles.trendName}>{t}</Text>
          <Text style={styles.trendStatus}>Emergiendo ✓</Text>
        </Card>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  header: { padding: 30, backgroundColor: '#1e1b4b' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: 'rgba(255,255,255,0.7)', fontSize: 13, marginTop: 5 },
  aiCard: { marginVertical: 20, marginHorizontal: 20, padding: 30, alignItems: 'center', backgroundColor: '#fff', borderRadius: 30, shadowColor: '#000', shadowOpacity: 0.1, shadowRadius: 10 },
  label: { fontSize: 12, color: '#4338ca', fontWeight: 'bold', textAlign: 'center' },
  value: { fontSize: 48, fontWeight: 'bold', color: '#1e1b4b', marginVertical: 10 },
  badge: { backgroundColor: '#e0e7ff', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20 },
  badgeText: { color: '#4338ca', fontWeight: 'bold', fontSize: 10 },
  sectionTitle: { fontSize: 14, fontWeight: '900', color: '#64748b', marginHorizontal: 20, marginVertical: 15, textTransform: 'uppercase', letterSpacing: 1 },
  policyCard: { padding: 20, marginHorizontal: 20, marginBottom: 15, backgroundColor: '#fff', borderRadius: 24 },
  policyHeader: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 10 },
  priorityBadge: { backgroundColor: '#fef2f2', paddingHorizontal: 8, paddingVertical: 4, borderRadius: 8 },
  priorityText: { color: '#ef4444', fontSize: 10, fontWeight: 'bold' },
  policyTitle: { fontWeight: '900', fontSize: 12, color: '#4338ca', textTransform: 'uppercase' },
  policyText: { color: '#334155', fontSize: 13, lineHeight: 20, fontWeight: '500' },
  approveBtn: { backgroundColor: '#1e1b4b', padding: 15, borderRadius: 15, marginTop: 15, alignItems: 'center' },
  approveBtnText: { color: '#fff', fontWeight: 'bold', fontSize: 12 },
  statusBadge: { marginTop: 15, padding: 10, backgroundColor: '#f0fdf4', borderRadius: 10, alignItems: 'center' },
  statusText: { color: '#16a34a', fontWeight: 'bold', fontSize: 11 },
  emptyText: { textAlign: 'center', color: '#94a3b8', marginTop: 20 },
  trendCard: { padding: 15, marginHorizontal: 20, marginBottom: 10, flexDirection: 'row', justifyContent: 'space-between', backgroundColor: '#fff', borderRadius: 15 },
  trendName: { fontWeight: 'bold', color: '#1e1b4b' },
  trendName: { fontWeight: '600' },
  trendStatus: { color: '#10b981', fontSize: 12 }
});
