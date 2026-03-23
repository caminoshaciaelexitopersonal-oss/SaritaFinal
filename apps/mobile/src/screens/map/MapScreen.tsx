import React, { useEffect, useState } from 'react';
import { StyleSheet, View, Text, ActivityIndicator } from 'react-native';
import MapView, { Marker, Callout } from 'react-native-maps';
import * as Location from 'expo-location';
import { api } from '../../services/api';
import { useNavigation } from '@react-navigation/native';

export const MapScreen = () => {
  const [location, setLocation] = useState<any>(null);
  const [tours, setTours] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const navigation = useNavigation<any>();

  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        console.error('Permiso de ubicación denegado');
        setLoading(false);
        return;
      }

      let userLocation = await Location.getCurrentPositionAsync({});
      setLocation(userLocation.coords);

      try {
        const response = await api.get('/tours', {
          params: { lat: userLocation.coords.latitude, lng: userLocation.coords.longitude }
        });
        setTours(response.data.results || []);
      } catch (error) {
        console.error('Error fetching nearby tours:', error);
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  if (loading) return <ActivityIndicator style={{ flex: 1 }} />;

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: location?.latitude || 4.313,
          longitude: location?.longitude || -72.081,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421,
        }}
        showsUserLocation
      >
        {tours.map((tour) => (
          <Marker
            key={tour.id}
            coordinate={{
              latitude: tour.location.latitude,
              longitude: tour.location.longitude,
            }}
          >
            <Callout onPress={() => navigation.navigate('TourDetail', { id: tour.id })}>
              <View style={styles.callout}>
                <Text style={styles.calloutTitle}>{tour.name}</Text>
                <Text>${tour.price} COP</Text>
              </View>
            </Callout>
          </Marker>
        ))}
      </MapView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { width: '100%', height: '100%' },
  callout: { padding: 10, minWidth: 150 },
  calloutTitle: { fontWeight: 'bold', marginBottom: 5 }
});
