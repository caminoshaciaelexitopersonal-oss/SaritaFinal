import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export const RegionalAnalyticsScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Analítica Regional (Stub)</Text>
      <Text>Este módulo está alineado con la arquitectura unificada.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 20, fontWeight: 'bold' }
});
