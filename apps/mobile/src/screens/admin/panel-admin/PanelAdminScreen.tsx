import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export const PanelAdminMobileStub = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Panel Admin - Gobierno</Text>
    <View style={styles.grid}>
      <Text style={styles.item}>Analytics</Text>
      <Text style={styles.item}>Prestadores</Text>
      <Text style={styles.item}>Informes</Text>
      <Text style={styles.item}>Monitoreo</Text>
    </View>
  </View>
);

const styles = StyleSheet.create({
  container: { padding: 20 },
  title: { fontSize: 18, fontWeight: 'bold' },
  grid: { flexDirection: 'row', flexWrap: 'wrap', marginTop: 10 },
  item: { width: '45%', padding: 15, margin: '2.5%', backgroundColor: '#f0f7ff' }
});
