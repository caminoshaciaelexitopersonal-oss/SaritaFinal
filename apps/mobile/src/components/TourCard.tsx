import React from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity } from 'react-native';
import { Card } from './Card';
import { Tour } from '@sarita/shared-sdk';

interface TourCardProps {
  tour: Tour;
  onPress: (tour: Tour) => void;
}

export const TourCard: React.FC<TourCardProps> = ({ tour, onPress }) => (
  <TouchableOpacity onPress={() => onPress(tour)}>
    <Card style={styles.container}>
      <Image source={{ uri: 'https://via.placeholder.com/300x200' }} style={styles.image} />
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

const styles = StyleSheet.create({
  container: { marginBottom: 15, overflow: 'hidden', padding: 0 },
  image: { width: '100%', height: 200 },
  info: { padding: 12 },
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  name: { fontSize: 18, fontWeight: 'bold' },
  rating: { fontSize: 14, color: '#f59e0b' },
  location: { color: '#6b7280', fontSize: 14, marginTop: 2 },
  price: { fontSize: 16, fontWeight: '600', color: '#1e3a8a', marginTop: 8 }
});
