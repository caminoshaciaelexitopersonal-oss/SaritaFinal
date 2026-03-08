import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessCustomersScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Directorio de Clientes</Text>
    <FlatList
      data={[
        { id: '1', name: 'Andrés Viajero', purchases: 12 },
        { id: '2', name: 'Laura Exploradora', purchases: 5 },
      ]}
      renderItem={({ item }) => (
        <Card style={styles.card}>
          <Text style={styles.name}>{item.name}</Text>
          <Text style={styles.sub}>{item.purchases} reservas completadas</Text>
        </Card>
      )}
      contentContainerStyle={{ padding: 20 }}
    />
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 20, fontWeight: 'bold', margin: 20 },
  card: { padding: 15, marginBottom: 10 },
  name: { fontWeight: 'bold' },
  sub: { fontSize: 12, color: '#6b7280', marginTop: 3 }
});
