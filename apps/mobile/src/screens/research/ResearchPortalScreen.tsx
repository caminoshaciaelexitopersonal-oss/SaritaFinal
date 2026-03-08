import React from 'react';
import { View, Text, StyleSheet, FlatList, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const ResearchPortalScreen = () => {
  const datasets = [
    { id: '1', name: 'Tendencias Turismo Rural 2026', type: 'Predictivo', status: 'Publicado' },
    { id: '2', name: 'Impacto Ambiental Safari Meta', type: 'Simulación', status: 'En Revisión' },
  ];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Research & Open Research Portal</Text>
      <Text style={styles.subtitle}>Datos abiertos para universidades y centros de investigación.</Text>

      <Card style={styles.promoCard}>
        <Text style={styles.promoTitle}>Potencia tu tesis con SARITA Data</Text>
        <Text style={styles.promoText}>Accede a patrones de comportamiento de más de 2M de viajeros.</Text>
        <Button title="Solicitar Acceso API Research" onPress={() => {}} style={styles.accBtn} />
      </Card>

      <Text style={styles.sectionTitle}>Datasets Destacados</Text>
      {datasets.map(d => (
        <Card key={d.id} style={styles.dataCard}>
          <Text style={styles.dataName}>{d.name}</Text>
          <Text style={styles.dataType}>Categoría: {d.type}</Text>
          <Text style={styles.status}>Estatus: {d.status}</Text>
          <Button title="Explorar Datos" onPress={() => {}} style={styles.viewBtn} />
        </Card>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#1e3a8a' },
  subtitle: { color: '#6b7280', marginVertical: 10, fontSize: 13 },
  promoCard: { padding: 25, backgroundColor: '#1e3a8a', marginBottom: 25 },
  promoTitle: { color: '#fff', fontSize: 18, fontWeight: 'bold' },
  promoText: { color: 'rgba(255,255,255,0.7)', marginTop: 10, lineHeight: 20 },
  accBtn: { marginTop: 20, backgroundColor: '#f59e0b' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginBottom: 15 },
  dataCard: { padding: 20, marginBottom: 15 },
  dataName: { fontWeight: 'bold', fontSize: 16 },
  dataType: { color: '#1e3a8a', fontSize: 12, marginTop: 5 },
  status: { color: '#10b981', fontSize: 10, fontWeight: 'bold', marginTop: 3 },
  viewBtn: { marginTop: 15, backgroundColor: '#334155' }
});
