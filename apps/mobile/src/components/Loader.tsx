import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export const Loader = () => (
  <View style={styles.container}>
    <Text style={styles.text}>Cargando SARITA...</Text>
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#fff' },
  text: { marginTop: 10, color: '#1e3a8a', fontWeight: '600' }
});
