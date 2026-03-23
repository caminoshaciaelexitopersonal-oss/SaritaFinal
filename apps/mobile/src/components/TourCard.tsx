import React from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import { Card } from './Card';
import { Tour } from '@sarita/shared-sdk';
import { api } from '../services/api';

interface TourCardProps {
  tour: Tour;
  onPress: (tour: Tour) => void;
}

export const TourCard: React.FC<TourCardProps> = ({ tour, onPress }) => {
  const toggleFavorite = async () => {
    try {
      await api.post('/favorites/', { tour_id: tour.id });
      Alert.alert('Favoritos', 'Tour guardado en tus favoritos.');
    } catch (error) {
      console.error('Error toggling favorite:', error);
    }
  };

  return (
    <TouchableOpacity onPress={() => onPress(tour)}>
      <Card style={styles.container}>
        <Image source={{ uri: 'https://via.placeholder.com/300x200' }} style={styles.image} />
        <TouchableOpacity style={styles.favBadge} onPress={toggleFavorite}>
          <Text style={styles.favText}>♥</Text>
        </TouchableOpacity>
        <View style={styles.info}>
          <View style={styles.header}>
            <Text style={styles.name}>{tour.name}</Text>
            <Text style={styles.rating}>★ {tour.rating}</Text>
          </View>
          <Text style={styles.location}>{tour.location.address}</Text>
          <Text style={styles.price}>${tour.price.toLocaleString()} COP</Text>
        </View>
      </Card>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: { marginBottom: 15, overflow: 'hidden', padding: 0 },
  image: { width: '100%', height: 200 },
  favBadge: { position: 'absolute', top: 10, right: 10, backgroundColor: 'rgba(255,255,255,0.8)', borderRadius: 20, width: 35, height: 35, justifyContent: 'center', alignItems: 'center' },
  favText: { color: '#ef4444', fontSize: 20 },
  info: { padding: 12 },
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  name: { fontSize: 18, fontWeight: 'bold' },
  rating: { fontSize: 14, color: '#f59e0b' },
  location: { color: '#6b7280', fontSize: 14, marginTop: 2 },
  price: { fontSize: 16, fontWeight: '600', color: '#1e3a8a', marginTop: 8 }
});
