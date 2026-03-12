import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const CreatorDashboard = () => (
  <ScrollView style={styles.container}>
    <Text style={styles.title}>Panel de Creador</Text>

    <Card style={styles.statsCard}>
      <Text style={styles.label}>Tus Experiencias Publicadas</Text>
      <Text style={styles.value}>12</Text>
    </Card>

    <View style={styles.row}>
      <Card style={styles.miniCard}>
        <Text style={styles.miniLabel}>Vistas Totales</Text>
        <Text style={styles.miniValue}>45.2K</Text>
      </Card>
      <Card style={styles.miniCard}>
        <Text style={styles.miniLabel}>Seguidores</Text>
        <Text style={styles.miniValue}>1,280</Text>
      </Card>
    </View>

    <Button title="Publicar Nueva Experiencia (Video/Ruta)" onPress={() => {}} style={styles.createBtn} />

    <Text style={styles.sectionTitle}>Guías Recientes</Text>
    {['Ruta de las Cascadas', 'Mejores Atardeceres', 'Pesca en el Manacacías'].map(g => (
      <Card key={g} style={styles.guideCard}>
        <Text style={styles.guideName}>{g}</Text>
        <Text style={styles.guideStatus}>Publicado ✓</Text>
      </Card>
    ))}
  </ScrollView>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  statsCard: { padding: 30, alignItems: 'center', backgroundColor: '#1e3a8a' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  value: { color: '#fff', fontSize: 32, fontWeight: 'bold' },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginTop: 15 },
  miniCard: { flex: 0.48, padding: 15 },
  miniLabel: { color: '#6b7280', fontSize: 12 },
  miniValue: { fontSize: 20, fontWeight: 'bold' },
  createBtn: { marginTop: 20, backgroundColor: '#10b981' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  guideCard: { marginBottom: 10, padding: 15, flexDirection: 'row', justifyContent: 'space-between' },
  guideName: { fontWeight: '600' },
  guideStatus: { color: '#10b981', fontSize: 12 }
});
