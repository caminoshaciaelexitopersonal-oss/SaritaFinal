import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const ReputationScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Reputación y Confianza</Text>

      <Card style={styles.mainScoreCard}>
        <Text style={styles.label}>Puntuación Global del Operador</Text>
        <Text style={styles.score}>4.9</Text>
        <Text style={styles.ratingText}>Excelente ✓</Text>
      </Card>

      <Text style={styles.sectionTitle}>Métricas Detalladas</Text>
      <Card style={styles.metricCard}>
        <Text style={styles.metricLabel}>Puntualidad</Text>
        <Text style={styles.metricValue}>98%</Text>
      </Card>

      <Card style={styles.metricCard}>
        <Text style={styles.metricLabel}>Calidad del Servicio</Text>
        <Text style={styles.metricValue}>4.9/5</Text>
      </Card>

      <Card style={styles.metricCard}>
        <Text style={styles.metricLabel}>Tasa de Respuesta Chat</Text>
        <Text style={styles.metricValue}>15 min</Text>
      </Card>

      <View style={styles.trustBadge}>
        <Text style={styles.trustText}>Sello de Confianza SARITA Nivel PLATINUM</Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  mainScoreCard: { padding: 30, alignItems: 'center', backgroundColor: '#1e3a8a' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  score: { fontSize: 64, fontWeight: 'bold', color: '#fff', marginVertical: 10 },
  ratingText: { color: '#10b981', fontWeight: 'bold' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  metricCard: { marginBottom: 10, padding: 15, flexDirection: 'row', justifyContent: 'space-between' },
  metricLabel: { color: '#64748b' },
  metricValue: { fontWeight: 'bold', color: '#1e3a8a' },
  trustBadge: { marginTop: 30, padding: 20, backgroundColor: '#fef3c7', borderRadius: 10, borderWidth: 1, borderColor: '#f59e0b' },
  trustText: { textAlign: 'center', fontWeight: 'bold', color: '#92400e' }
});
