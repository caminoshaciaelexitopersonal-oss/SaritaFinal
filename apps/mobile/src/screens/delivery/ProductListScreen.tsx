import React from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';

export const ProductListScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Menú del Restaurante</Text>
    <FlatList
      data={[
        { id: '1', name: 'Mamona Llanera', price: 35000 },
        { id: '2', name: 'Amarillo a la Monseñor', price: 42000 },
      ]}
      keyExtractor={item => item.id}
      renderItem={({ item }) => (
        <Card style={styles.card}>
          <View style={styles.row}>
            <Text style={styles.name}>{item.name}</Text>
            <Text style={styles.price}>${item.price.toLocaleString()}</Text>
          </View>
          <TouchableOpacity style={styles.addBtn}><Text style={styles.addText}>Añadir al Carrito</Text></TouchableOpacity>
        </Card>
      )}
      contentContainerStyle={{ padding: 20 }}
    />
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 20, fontWeight: 'bold', margin: 20 },
  card: { marginBottom: 10, padding: 15 },
  row: { flexDirection: 'row', justifyContent: 'space-between' },
  name: { fontWeight: 'bold' },
  price: { color: '#1e3a8a' },
  addBtn: { marginTop: 10, backgroundColor: '#10b981', padding: 8, borderRadius: 5, alignItems: 'center' },
  addText: { color: '#fff', fontSize: 12, fontWeight: 'bold' }
});
