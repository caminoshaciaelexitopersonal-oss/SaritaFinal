import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView, Image, StyleSheet, ActivityIndicator } from 'react-native';
import { useRoute, useNavigation } from '@react-navigation/native';
import { api } from '../../services/api';
import { Button } from '../../components/Button';

export const TourDetailScreen = () => {
  const route = useRoute<any>();
  const navigation = useNavigation<any>();
  const [tour, setTour] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDetail = async () => {
      try {
        const response = await api.get(`/tours/${route.params.id}`);
        setTour(response.data);
      } catch (error) {
        console.error('Error fetching tour detail:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchDetail();
  }, [route.params.id]);

  if (loading) return <ActivityIndicator style={{ flex: 1 }} />;
  if (!tour) return <Text>Error cargando el tour</Text>;

  return (
    <ScrollView style={styles.container}>
      <Image source={{ uri: 'https://via.placeholder.com/600x400' }} style={styles.image} />
      <View style={styles.content}>
        <Text style={styles.name}>{tour.name}</Text>
        <Text style={styles.price}>${tour.price.toLocaleString()} COP</Text>
        <Text style={styles.sectionTitle}>Descripción</Text>
        <Text style={styles.description}>{tour.description || 'Sin descripción disponible.'}</Text>

        <View style={styles.stats}>
          <Text>Capacidad: {tour.capacity || 10} pers.</Text>
          <Text>Duración: {tour.duration || '3 horas'}</Text>
        </View>

        <Button
          title="Reservar ahora"
          onPress={() => navigation.navigate('Booking', { tourId: tour.id })}
          style={styles.button}
        />
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  image: { width: '100%', height: 300 },
  content: { padding: 20 },
  name: { fontSize: 24, fontWeight: 'bold' },
  price: { fontSize: 20, color: '#1e3a8a', fontWeight: '600', marginTop: 10 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginTop: 25 },
  description: { fontSize: 16, color: '#4b5563', marginTop: 10, lineHeight: 24 },
  stats: { flexDirection: 'row', justifyContent: 'space-between', marginTop: 20, padding: 15, backgroundColor: '#f3f4f6', borderRadius: 8 },
  button: { marginTop: 30 }
});
