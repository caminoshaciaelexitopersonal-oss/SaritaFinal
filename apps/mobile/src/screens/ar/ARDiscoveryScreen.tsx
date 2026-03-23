import React from 'react';
import { View, Text, StyleSheet, ImageBackground } from 'react-native';

export const ARDiscoveryScreen = () => {
  return (
    <View style={styles.container}>
      <ImageBackground
        source={{ uri: 'https://via.placeholder.com/1080x1920' }}
        style={styles.cameraView}
      >
        <View style={styles.arOverlay}>
          <View style={styles.marker}>
            <Text style={styles.markerTitle}>Catedral de Puerto Gaitán</Text>
            <Text style={styles.markerDist}>A 150 metros</Text>
          </View>
        </View>

        <View style={styles.arInstructions}>
          <Text style={styles.instrText}>Apunta tu cámara a los puntos de interés</Text>
        </View>
      </ImageBackground>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1 },
  cameraView: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  arOverlay: { position: 'absolute', top: '40%' },
  marker: { backgroundColor: 'rgba(30,58,138,0.9)', padding: 15, borderRadius: 10, borderBottomWidth: 5, borderColor: '#f59e0b' },
  markerTitle: { color: '#fff', fontWeight: 'bold', fontSize: 16 },
  markerDist: { color: 'rgba(255,255,255,0.7)', fontSize: 12, marginTop: 5 },
  arInstructions: { position: 'absolute', bottom: 50, backgroundColor: 'rgba(0,0,0,0.5)', padding: 15, borderRadius: 20 },
  instrText: { color: '#fff', fontSize: 14 }
});
