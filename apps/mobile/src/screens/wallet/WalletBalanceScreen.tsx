import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Card } from '../../components/Card';

export const WalletBalanceScreen = () => (
  <View style={styles.container}>
    <Card style={styles.card}>
      <Text style={styles.label}>Desglose de Saldo</Text>
      <Text style={styles.amount}>$150.50 USD</Text>
      <View style={styles.divider} />
      <Text style={styles.sub}>Saldo Contable: $150.50</Text>
      <Text style={styles.sub}>Saldo Disponible: $150.50</Text>
    </Card>
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f9fafb' },
  card: { padding: 20 },
  label: { fontSize: 14, color: '#64748b' },
  amount: { fontSize: 32, fontWeight: 'bold', marginVertical: 10 },
  divider: { height: 1, backgroundColor: '#e2e8f0', marginVertical: 15 },
  sub: { fontSize: 14, color: '#475569', marginBottom: 5 }
});
