import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import MapView, { Marker } from 'react-native-maps';

export const OrderTrackingScreen = () => (
  <View style={styles.container}>
    <MapView style={styles.map} initialRegion={{ latitude: 4.313, longitude: -72.081, latitudeDelta: 0.01, longitudeDelta: 0.01 }}>
      <Marker coordinate={{ latitude: 4.315, longitude: -72.083 }} title="Repartidor" pinColor="green" />
    </MapView>
    <View style={styles.statusBox}>
      <Text style={styles.statusTitle}>Tu pedido está en camino</Text>
      <Text style={styles.statusSub}>Repartidor: Juan Pérez | 5 min restantes</Text>
    </View>
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { flex: 1 },
  statusBox: { position: 'absolute', bottom: 30, left: 20, right: 20, backgroundColor: '#fff', padding: 20, borderRadius: 10, elevation: 5 },
  statusTitle: { fontWeight: 'bold', fontSize: 16 },
  statusSub: { color: '#6b7280', marginTop: 5 }
});
