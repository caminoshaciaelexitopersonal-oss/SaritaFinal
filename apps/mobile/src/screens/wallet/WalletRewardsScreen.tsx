import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const WalletRewardsScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Mis Recompensas</Text>
    <FlatList
      data={[
        { id: '1', title: '5% Descuento Delivery', points: '500 pts' },
        { id: '2', title: 'Tour Gratis (Sorteo)', points: '2000 pts' },
      ]}
      keyExtractor={item => item.id}
      renderItem={({ item }) => (
        <Card style={styles.card}>
          <Text style={styles.name}>{item.title}</Text>
          <Text style={styles.pts}>Costo: {item.points}</Text>
        </Card>
      )}
      contentContainerStyle={{ padding: 20 }}
    />
  </View>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', margin: 20 },
  card: { marginBottom: 10, padding: 15 },
  name: { fontWeight: 'bold' },
  pts: { color: '#f59e0b', fontSize: 12, marginTop: 5 }
});
