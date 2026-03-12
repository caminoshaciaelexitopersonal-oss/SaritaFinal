import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessServicesScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Mis Servicios Turísticos</Text>
    <FlatList
      data={[
        { id: '1', name: 'Safari Río Meta', status: 'Activo' },
        { id: '2', name: 'Cabalgata Atardecer', status: 'Pausado' },
      ]}
      renderItem={({ item }) => (
        <Card style={styles.card}>
          <Text style={styles.name}>{item.name}</Text>
          <Text style={styles.status}>Estado: {item.status}</Text>
        </Card>
      )}
      contentContainerStyle={{ padding: 20 }}
    />
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 20, fontWeight: 'bold', margin: 20 },
  card: { padding: 15, marginBottom: 10, flexDirection: 'row', justifyContent: 'space-between' },
  name: { fontWeight: '600' },
  status: { color: '#10b981' }
});
