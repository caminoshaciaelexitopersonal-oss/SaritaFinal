import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const WalletTransactionsScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Historial de Transacciones</Text>
      <FlatList
        data={[
          { id: '1', type: 'Pago', amount: -45.00, date: '2026-03-07', desc: 'Cena en Llanos Grill' },
          { id: '2', type: 'Recarga', amount: 100.00, date: '2026-03-06', desc: 'Top-up Tarjeta' },
        ]}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.card}>
            <View style={styles.row}>
              <Text style={styles.desc}>{item.desc}</Text>
              <Text style={[styles.amount, item.amount < 0 ? styles.negative : styles.positive]}>
                {item.amount < 0 ? '' : '+'}{item.amount} USD
              </Text>
            </View>
            <Text style={styles.date}>{item.date} | {item.type}</Text>
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 20, fontWeight: 'bold', margin: 20 },
  card: { marginBottom: 10, padding: 15 },
  row: { flexDirection: 'row', justifyContent: 'space-between' },
  desc: { fontWeight: '600' },
  amount: { fontWeight: 'bold' },
  negative: { color: '#ef4444' },
  positive: { color: '#10b981' },
  date: { fontSize: 12, color: '#9ca3af', marginTop: 5 }
});
