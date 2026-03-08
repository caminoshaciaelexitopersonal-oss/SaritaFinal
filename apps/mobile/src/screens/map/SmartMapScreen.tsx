import React, { useEffect, useState } from 'react';
import { StyleSheet, View, Text, ActivityIndicator, TouchableOpacity, ScrollView } from 'react-native';
import MapView, { Marker, Polyline } from 'react-native-maps';
import * as Location from 'expo-location';
import { api } from '../../services/api';

export const SmartMapScreen = () => {
  const [filter, setFilter] = useState('tours'); // tours, restaurants, events
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchItems = async (type: string) => {
    try {
      const response = await api.get(`/discovery/?type=${type}`);
      setItems(response.data.results || []);
    } catch (error) {}
  };

  useEffect(() => {
    fetchItems(filter);
    setLoading(false);
  }, [filter]);

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: 4.313,
          longitude: -72.081,
          latitudeDelta: 0.05,
          longitudeDelta: 0.05,
        }}
        showsUserLocation
      >
        {items.map(item => (
          <Marker
            key={item.id}
            coordinate={item.location}
            pinColor={filter === 'tours' ? 'red' : filter === 'restaurants' ? 'green' : 'blue'}
          >
            <View style={styles.markerContainer}>
              <Text style={styles.markerText}>{item.name}</Text>
            </View>
          </Marker>
        ))}
      </MapView>

      <View style={styles.filterBar}>
        <ScrollView horizontal showsHorizontalScrollIndicator={false}>
          {['tours', 'restaurantes', 'eventos', 'rutas'].map(f => (
            <TouchableOpacity
              key={f}
              style={[styles.filterBtn, filter === f && styles.activeFilter]}
              onPress={() => setFilter(f)}
            >
              <Text style={[styles.filterText, filter === f && styles.activeText]}>{f.toUpperCase()}</Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { width: '100%', height: '100%' },
  filterBar: { position: 'absolute', top: 50, left: 0, right: 0, paddingHorizontal: 15 },
  filterBtn: { backgroundColor: 'rgba(255,255,255,0.9)', paddingHorizontal: 15, paddingVertical: 10, borderRadius: 20, marginRight: 10, elevation: 5 },
  activeFilter: { backgroundColor: '#1e3a8a' },
  filterText: { fontSize: 12, fontWeight: 'bold', color: '#1e3a8a' },
  activeText: { color: '#fff' },
  markerContainer: { backgroundColor: 'rgba(255,255,255,0.8)', padding: 5, borderRadius: 5, borderBottomWidth: 2, borderColor: '#000' },
  markerText: { fontSize: 8, fontWeight: 'bold' }
});
