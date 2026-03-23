import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessFinanceScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Gestión Financiera (ERP)</Text>

      <Card style={styles.mainCard}>
        <Text style={styles.label}>Flujo de Caja Neto</Text>
        <Text style={styles.value}>$12.450.000 COP</Text>
      </Card>

      <View style={styles.row}>
        <Card style={styles.miniCard}>
          <Text style={styles.miniLabel}>Ingresos</Text>
          <Text style={[styles.miniValue, { color: '#10b981' }]}>$15.2M</Text>
        </Card>
        <Card style={styles.miniCard}>
          <Text style={styles.miniLabel}>Egresos</Text>
          <Text style={[styles.miniValue, { color: '#ef4444' }]}>$2.75M</Text>
        </Card>
      </View>

      <Text style={styles.sectionTitle}>Cuentas por Cobrar</Text>
      <Card style={styles.itemCard}>
        <Text style={styles.itemName}>Reserva #1290 - Safari</Text>
        <Text style={styles.itemValue}>$450.000 COP</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  mainCard: { padding: 30, backgroundColor: '#1e3a8a', alignItems: 'center' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  value: { color: '#fff', fontSize: 32, fontWeight: 'bold', marginTop: 10 },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginTop: 20 },
  miniCard: { flex: 0.48, padding: 15 },
  miniLabel: { fontSize: 12, color: '#64748b' },
  miniValue: { fontSize: 18, fontWeight: 'bold', marginTop: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  itemCard: { padding: 15, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  itemName: { fontWeight: '500' },
  itemValue: { fontWeight: 'bold', color: '#1e3a8a' }
});
