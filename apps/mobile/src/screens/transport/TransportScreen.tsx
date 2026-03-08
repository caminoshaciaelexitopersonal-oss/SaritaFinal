import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const TransportScreen = () => {
  const [transportOptions] = useState([
    { id: '1', type: 'Bus Turístico', route: 'Puerto Gaitán - Villavicencio', price: 45000, time: '08:00 AM' },
    { id: '2', type: 'Transporte Privado', route: 'Traslado al Safari', price: 120000, time: 'Disponible 24/7' },
  ]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Transporte Turístico</Text>
      <FlatList
        data={transportOptions}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.transportCard}>
            <View style={styles.header}>
              <Text style={styles.type}>{item.type}</Text>
              <Text style={styles.price}>${item.price.toLocaleString()} COP</Text>
            </View>
            <Text style={styles.route}>{item.route}</Text>
            <Text style={styles.time}>{item.time}</Text>
            <Button title="Reservar Traslado" onPress={() => {}} style={styles.btn} />
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', margin: 20 },
  transportCard: { marginBottom: 15, padding: 20 },
  header: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 10 },
  type: { fontWeight: 'bold', fontSize: 16 },
  price: { color: '#1e3a8a', fontWeight: 'bold' },
  route: { color: '#4b5563', marginBottom: 5 },
  time: { color: '#9ca3af', fontSize: 12, marginBottom: 15 },
  btn: { paddingVertical: 10 }
});
