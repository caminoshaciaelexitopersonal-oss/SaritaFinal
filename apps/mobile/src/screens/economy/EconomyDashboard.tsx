import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const EconomyDashboard = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Tu Monedero Turístico</Text>

      <Card style={styles.walletCard}>
        <Text style={styles.label}>Créditos SARITA Disponibles</Text>
        <Text style={styles.value}>$150.00 USD</Text>
        <Button title="Recargar Créditos" onPress={() => {}} style={styles.topupBtn} />
      </Card>

      <Text style={styles.sectionTitle}>Conversión Multi-moneda (Fase 08)</Text>
      <Card style={styles.infoCard}>
        <Text style={styles.currencyRow}>100 USD = 390.000 COP</Text>
        <Text style={styles.currencyRow}>100 USD = 92 EUR</Text>
      </Card>

      <Text style={styles.sectionTitle}>Economía de Experiencias</Text>
      <Card style={styles.infoCard}>
        <Text style={styles.infoTitle}>Gana Dinero como Creador</Text>
        <Text style={styles.infoText}>Publica tus rutas y guías, y recibe créditos cuando otros viajeros las utilicen.</Text>
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  walletCard: { padding: 30, backgroundColor: '#1e3a8a', alignItems: 'center' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  value: { color: '#fff', fontSize: 36, fontWeight: 'bold', marginVertical: 10 },
  topupBtn: { backgroundColor: '#f59e0b', width: '100%', marginTop: 10 },
  currencyRow: { fontSize: 16, fontWeight: 'bold', color: '#1e3a8a', marginBottom: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  infoCard: { padding: 20 },
  infoTitle: { fontWeight: 'bold', marginBottom: 5 },
  infoText: { color: '#4b5563' }
});
