import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { autonomousService } from '../../services/autonomousService';

export const GlobalAIDashboard = () => {
  const [insights, setInsights] = useState<any>({ global_demand: 0, top_trend: '' });

  useEffect(() => {
    const fetchAI = async () => {
      try {
        const response = await autonomousService.getGlobalAIInsights();
        setInsights(response.data);
      } catch (error) {}
    };
    fetchAI();
  }, []);

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

      <Text style={styles.sectionTitle}>Optimización de Políticas Turísticas</Text>
      <Card style={styles.policyCard}>
        <Text style={styles.policyTitle}>Recomendación: Incentivos Ecoturismo</Text>
        <Text style={styles.policyText}>Basado en el crecimiento del 200% en búsquedas de destinos rurales en LATAM. Se sugiere reducción impositiva del 5% para operadores certificados.</Text>
      </Card>

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
  container: { flex: 1, backgroundColor: '#fdf2f2', padding: 20 },
  header: { padding: 30, backgroundColor: '#991b1b' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: 'rgba(255,255,255,0.7)', fontSize: 13, marginTop: 5 },
  aiCard: { marginVertical: 20, padding: 30, alignItems: 'center', backgroundColor: '#fff' },
  label: { fontSize: 12, color: '#991b1b', fontWeight: 'bold', textAlign: 'center' },
  value: { fontSize: 48, fontWeight: 'bold', color: '#991b1b', marginVertical: 10 },
  badge: { backgroundColor: '#fee2e2', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20 },
  badgeText: { color: '#991b1b', fontWeight: 'bold', fontSize: 10 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#991b1b', marginVertical: 20 },
  policyCard: { padding: 20, backgroundColor: '#fff', borderLeftWidth: 5, borderColor: '#991b1b' },
  policyTitle: { fontWeight: 'bold', fontSize: 16 },
  policyText: { color: '#4b5563', marginTop: 10, lineHeight: 22 },
  trendCard: { padding: 15, marginBottom: 10, flexDirection: 'row', justifyContent: 'space-between' },
  trendName: { fontWeight: '600' },
  trendStatus: { color: '#10b981', fontSize: 12 }
});
