import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, Image, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { deliveryService } from '../../services/deliveryService';

export const DeliveryHomeScreen = () => {
  const [restaurants, setRestaurants] = useState<any[]>([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await deliveryService.getRestaurants();
        setRestaurants(response.data || []);
      } catch (error) {
        setRestaurants([
          { id: '1', name: 'Llanos Grill', category: 'Carnes', rating: 4.8 },
          { id: '2', name: 'Sabor de Río', category: 'Pescados', rating: 4.5 },
        ]);
      }
    };
    fetchRestaurants();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Delivery SARITA</Text>
      <Text style={styles.subtitle}>Comida local directo a tu ubicación.</Text>

      <FlatList
        data={restaurants}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity>
            <Card style={styles.resCard}>
              <View style={styles.header}>
                <Text style={styles.resName}>{item.name}</Text>
                <Text style={styles.resRating}>★ {item.rating}</Text>
              </View>
              <Text style={styles.resCat}>{item.category}</Text>
              <Text style={styles.deliveryInfo}>Tiempo estimado: 30-45 min</Text>
            </Card>
          </TouchableOpacity>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginHorizontal: 20, marginTop: 30 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20 },
  resCard: { marginBottom: 15, padding: 15 },
  header: { flexDirection: 'row', justifyContent: 'space-between' },
  resName: { fontSize: 18, fontWeight: 'bold' },
  resRating: { color: '#f59e0b', fontWeight: 'bold' },
  resCat: { color: '#4b5563', marginVertical: 5 },
  deliveryInfo: { fontSize: 12, color: '#10b981', fontWeight: 'bold' }
});
