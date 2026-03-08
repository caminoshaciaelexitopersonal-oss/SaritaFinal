import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { orchestrationService } from '../../services/orchestrationService';
import { Card } from '../../components/Card';

export const LiveExperiencesScreen = () => {
  const [liveExps, setLiveExps] = useState<any[]>([]);

  useEffect(() => {
    const fetchLive = async () => {
      try {
        const response = await orchestrationService.getLiveExperiences();
        setLiveExps(response.data || []);
      } catch (error) {
        setLiveExps([
          { id: '1', name: 'Tour Nocturno Inmediato', time_left: '25 min', price: 85000 },
          { id: '2', name: 'Clase de Pesca en Vivo', time_left: '45 min', price: 60000 },
        ]);
      }
    };
    fetchLive();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Experiencias en Tiempo Real</Text>
      <Text style={styles.subtitle}>Ofertas de último minuto y actividades disponibles ahora.</Text>

      <FlatList
        data={liveExps}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity>
            <Card style={styles.liveCard}>
              <View style={styles.badge}><Text style={styles.badgeText}>QUEDAN: {item.time_left}</Text></View>
              <Text style={styles.expName}>{item.name}</Text>
              <Text style={styles.price}>${item.price.toLocaleString()} COP</Text>
              <Text style={styles.bookNow}>RESERVAR YA →</Text>
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
  liveCard: { marginBottom: 15, padding: 20, borderLeftWidth: 5, borderColor: '#ef4444' },
  badge: { backgroundColor: '#fee2e2', paddingHorizontal: 10, paddingVertical: 5, borderRadius: 5, alignSelf: 'flex-start', marginBottom: 10 },
  badgeText: { color: '#ef4444', fontSize: 10, fontWeight: 'bold' },
  expName: { fontSize: 18, fontWeight: 'bold' },
  price: { color: '#1e3a8a', marginTop: 5, fontWeight: '600' },
  bookNow: { marginTop: 15, color: '#ef4444', fontWeight: 'bold', fontSize: 12 }
});
