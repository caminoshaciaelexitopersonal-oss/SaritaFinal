import React from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';

export const UrbanServicesScreen = () => {
  const services = [
    { id: '1', name: 'Alquiler de Bicicletas', icon: '🚲', status: 'Disponible' },
    { id: '2', name: 'Transporte Público Local', icon: '🚌', status: 'En servicio' },
    { id: '3', name: 'Entradas Museos', icon: '🏛️', status: 'Abierto' },
  ];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Servicios Urbanos Inteligentes</Text>
      <Text style={styles.subtitle}>Conectando con la infraestructura de la ciudad.</Text>

      <FlatList
        data={services}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity>
            <Card style={styles.serviceCard}>
              <Text style={styles.icon}>{item.icon}</Text>
              <View style={styles.info}>
                <Text style={styles.name}>{item.name}</Text>
                <Text style={styles.status}>Estado: {item.status}</Text>
              </View>
              <Text style={styles.arrow}>→</Text>
            </Card>
          </TouchableOpacity>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 22, fontWeight: 'bold', marginTop: 30, marginHorizontal: 20 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20 },
  serviceCard: { marginBottom: 15, padding: 20, flexDirection: 'row', alignItems: 'center' },
  icon: { fontSize: 30, marginRight: 20 },
  info: { flex: 1 },
  name: { fontSize: 16, fontWeight: 'bold' },
  status: { fontSize: 12, color: '#10b981', marginTop: 3 },
  arrow: { fontSize: 20, color: '#9ca3af' }
});
