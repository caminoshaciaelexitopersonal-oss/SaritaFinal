import React, { useEffect, useState } from 'react';
import { StyleSheet, View, Text, ActivityIndicator } from 'react-native';
import MapView, { Marker, Polyline } from 'react-native-maps';
import * as Location from 'expo-location';
import { api } from '../../services/api';

export const TourTrackingScreen = () => {
  const [userLocation, setUserLocation] = useState<any>(null);
  const [operatorLocation, setOperatorLocation] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initTracking = async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status === 'granted') {
        const loc = await Location.getCurrentPositionAsync({});
        setUserLocation(loc.coords);
      }

      // Simulación de polling de ubicación del operador
      const interval = setInterval(async () => {
        // En real: const response = await api.get(`/tracking/${reservationId}`);
        setOperatorLocation({
          latitude: (userLocation?.latitude || 4.313) + 0.005,
          longitude: (userLocation?.longitude || -72.081) + 0.005,
        });
      }, 5000);

      setLoading(false);
      return () => clearInterval(interval);
    };
    initTracking();
  }, []);

  // Geofencing: Detectar llegada al punto (radio 500m)
  useEffect(() => {
    if (userLocation && operatorLocation) {
      const dist = Math.sqrt(
        Math.pow(userLocation.latitude - operatorLocation.latitude, 2) +
        Math.pow(userLocation.longitude - operatorLocation.longitude, 2)
      );
      if (dist < 0.005) { // Aprox 500m
        console.log('SARITA: Usuario ha llegado al punto de encuentro.');
      }
    }
  }, [userLocation, operatorLocation]);

  if (loading) return <ActivityIndicator style={{ flex: 1 }} />;

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: userLocation?.latitude || 4.313,
          longitude: userLocation?.longitude || -72.081,
          latitudeDelta: 0.01,
          longitudeDelta: 0.01,
        }}
        showsUserLocation
      >
        {operatorLocation && (
          <Marker
            coordinate={operatorLocation}
            title="Tu Guía"
            description="Llanos Adventures"
            pinColor="blue"
          />
        )}
      </MapView>
      <View style={styles.statusBox}>
        <Text style={styles.statusText}>El guía está a 5 minutos de tu ubicación</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { width: '100%', height: '100%' },
  statusBox: { position: 'absolute', bottom: 30, left: 20, right: 20, backgroundColor: '#fff', padding: 15, borderRadius: 10, elevation: 5 },
  statusText: { fontWeight: 'bold', textAlign: 'center', color: '#1e3a8a' }
});
