import React from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
import { Button } from '../../components/Button';

export const ProductDetailsScreen = () => (
  <View style={styles.container}>
    <Image source={{ uri: 'https://via.placeholder.com/400x300' }} style={styles.image} />
    <View style={styles.content}>
      <Text style={styles.name}>Plato Típico</Text>
      <Text style={styles.price}>$25.000 COP</Text>
      <Text style={styles.desc}>Una descripción deliciosa del producto local.</Text>
      <Button title="Agregar" onPress={() => {}} style={styles.btn} />
    </View>
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  image: { width: '100%', height: 250 },
  content: { padding: 20 },
  name: { fontSize: 22, fontWeight: 'bold' },
  price: { fontSize: 18, color: '#1e3a8a', marginVertical: 10 },
  desc: { color: '#6b7280', lineHeight: 20 },
  btn: { marginTop: 30 }
});
