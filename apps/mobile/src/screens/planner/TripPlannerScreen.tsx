import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const TripPlannerScreen = () => {
  const [itinerary, setItinerary] = useState<any[]>([]);

  const addToTrip = (tour: any) => {
    setItinerary([...itinerary, { ...tour, time: '09:00 AM' }]);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Planeador de Viajes Inteligente</Text>
      <Text style={styles.subtitle}>Crea tu itinerario perfecto en Puerto Gaitán</Text>

      <FlatList
        data={itinerary}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item, index }) => (
          <View style={styles.timelineItem}>
            <View style={styles.timelinePoint} />
            <Card style={styles.tourCard}>
              <Text style={styles.timeText}>{item.time}</Text>
              <Text style={styles.tourName}>{item.name || 'Safari Río Manacacías'}</Text>
            </Card>
          </View>
        )}
        ListEmptyComponent={
          <View style={styles.emptyContainer}>
            <Text style={styles.emptyText}>Tu itinerario está vacío.</Text>
            <Button title="Explorar Tours para Agregar" onPress={() => {}} style={styles.addBtn} />
          </View>
        }
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', marginTop: 30, marginHorizontal: 20 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20 },
  timelineItem: { flexDirection: 'row', marginBottom: 15 },
  timelinePoint: { width: 12, height: 12, borderRadius: 6, backgroundColor: '#1e3a8a', marginTop: 25, marginRight: 15 },
  tourCard: { flex: 1, padding: 15 },
  timeText: { fontSize: 12, color: '#1e3a8a', fontWeight: 'bold' },
  tourName: { fontSize: 16, fontWeight: '600', marginTop: 5 },
  emptyContainer: { alignItems: 'center', marginTop: 100 },
  emptyText: { color: '#9ca3af', marginBottom: 20 },
  addBtn: { width: '80%' }
});
