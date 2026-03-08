import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Button } from '../../components/Button';
import { Card } from '../../components/Card';

export const CartScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Tu Carrito</Text>
    <FlatList
      data={[{ id: '1', name: 'Mamona', qty: 1, price: 35000 }]}
      renderItem={({ item }) => (
        <Card style={styles.card}>
          <Text>{item.name} x{item.qty}</Text>
          <Text>${item.price}</Text>
        </Card>
      )}
      contentContainerStyle={{ padding: 20 }}
    />
    <View style={styles.footer}>
      <Text style={styles.total}>Total: $35.000 COP</Text>
      <Button title="Proceder al Pago" onPress={() => {}} />
    </View>
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', margin: 20 },
  card: { padding: 15, marginBottom: 10, flexDirection: 'row', justifyContent: 'space-between' },
  footer: { padding: 20, borderTopWidth: 1, borderColor: '#e5e7eb' },
  total: { fontSize: 18, fontWeight: 'bold', marginBottom: 15 }
});
