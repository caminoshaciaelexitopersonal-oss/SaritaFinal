import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const SustainabilityDashboard = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Impacto Ambiental y Sostenibilidad</Text>

      <Card style={styles.mainCard}>
        <Text style={styles.label}>Tu Huella de Carbono del Viaje</Text>
        <Text style={styles.value}>12.5 kg CO2</Text>
        <View style={styles.badge}><Text style={styles.badgeText}>Bajo Impacto ✓</Text></View>
      </Card>

      <Text style={styles.sectionTitle}>Recomendaciones Eco-Friendly</Text>
      <Card style={styles.ecoCard}>
        <Text style={styles.ecoTitle}>Usa transporte público regional</Text>
        <Text style={styles.ecoDesc}>Reduce tu huella en un 30% reservando el bus turístico de SARITA.</Text>
      </Card>

      <Card style={styles.ecoCard}>
        <Text style={styles.ecoTitle}>Tour de Reforestación</Text>
        <Text style={styles.ecoDesc}>Compensa tu huella participando en el tour de siembra local.</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f0fdf4', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#166534', marginBottom: 20 },
  mainCard: { padding: 30, backgroundColor: '#fff', alignItems: 'center' },
  label: { color: '#166534', fontSize: 14, opacity: 0.7 },
  value: { fontSize: 32, fontWeight: 'bold', color: '#166534', marginVertical: 10 },
  badge: { backgroundColor: '#dcfce7', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20 },
  badgeText: { color: '#166534', fontWeight: 'bold', fontSize: 12 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#166534', marginVertical: 20 },
  ecoCard: { marginBottom: 15, padding: 20 },
  ecoTitle: { fontWeight: 'bold', color: '#1e3a8a' },
  ecoDesc: { color: '#4b5563', marginTop: 5, fontSize: 13 }
});
