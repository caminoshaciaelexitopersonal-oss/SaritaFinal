import React from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const DigitalTwinScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Gemelo Digital del Turismo</Text>
      <Text style={styles.subtitle}>Representación virtual de flujos y capacidades en tiempo real.</Text>

      <Card style={styles.viewerCard}>
        <Image source={{ uri: 'https://via.placeholder.com/600x400' }} style={styles.twinImage} />
        <Text style={styles.overlayText}>Visualización: Caño Cristales (Réplica 3D)</Text>
      </Card>

      <View style={styles.statsRow}>
        <Card style={styles.miniCard}>
          <Text style={styles.label}>Capacidad Actual</Text>
          <Text style={styles.value}>45%</Text>
        </Card>
        <Card style={styles.miniCard}>
          <Text style={styles.label}>Flujo Simulado</Text>
          <Text style={styles.value}>+15%</Text>
        </Card>
      </View>

      <Text style={styles.sectionTitle}>Análisis de Impacto (Twin Engine)</Text>
      <Card style={styles.infoCard}>
        <Text style={styles.infoText}>✓ Integridad del Ecosistema: Estable</Text>
        <Text style={styles.infoText}>✓ Carga del Sendero: Óptima</Text>
        <Text style={styles.infoText}>✓ Regeneración Hídrica: Activa</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f0f9ff', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#0369a1' },
  subtitle: { color: '#0ea5e9', fontSize: 13, marginVertical: 10 },
  viewerCard: { padding: 0, overflow: 'hidden', height: 300, marginBottom: 20 },
  twinImage: { width: '100%', height: '100%', opacity: 0.8 },
  overlayText: { position: 'absolute', bottom: 15, left: 15, color: '#fff', fontWeight: 'bold', backgroundColor: 'rgba(0,0,0,0.5)', padding: 5, borderRadius: 5 },
  statsRow: { flexDirection: 'row', justifyContent: 'space-between' },
  miniCard: { flex: 0.48, padding: 15, alignItems: 'center' },
  label: { fontSize: 12, color: '#64748b' },
  value: { fontSize: 24, fontWeight: 'bold', color: '#0369a1', marginTop: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#0369a1', marginVertical: 20 },
  infoCard: { padding: 20 },
  infoText: { fontSize: 14, color: '#334155', marginBottom: 8, fontWeight: '500' }
});
