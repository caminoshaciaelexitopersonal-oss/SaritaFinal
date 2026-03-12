import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessOrdersScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Pedidos Recibidos (ERP)</Text>
    <FlatList
      data={[
        { id: 'ORD-101', total: 125.00, customer: 'Andrés V.' },
        { id: 'ORD-102', total: 45.50, customer: 'María L.' },
      ]}
      renderItem={({ item }) => (
        <Card style={styles.card}>
          <Text style={styles.id}>{item.id}</Text>
          <Text>{item.customer}</Text>
          <Text style={styles.total}>${item.total} USD</Text>
        </Card>
      )}
      contentContainerStyle={{ padding: 20 }}
    />
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 20, fontWeight: 'bold', margin: 20 },
  card: { padding: 15, marginBottom: 10, flexDirection: 'row', justifyContent: 'space-between' },
  id: { fontWeight: 'bold', color: '#1e3a8a' },
  total: { fontWeight: 'bold' }
});
