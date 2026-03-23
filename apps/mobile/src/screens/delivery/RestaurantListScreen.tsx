import React from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';

export const RestaurantListScreen = () => {
  const categories = ['Pescados', 'Carnes', 'Comida Rápida', 'Postres'];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Restaurantes Aliados</Text>
      <FlatList
        horizontal
        showsHorizontalScrollIndicator={false}
        data={categories}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.catBadge}><Text style={styles.catText}>{item}</Text></TouchableOpacity>
        )}
        style={styles.catList}
      />

      <FlatList
        data={[
          { id: '1', name: 'El Asador Llanero', dist: '1.2 km', rating: 4.9 },
          { id: '2', name: 'Pescadería del Puerto', dist: '0.8 km', rating: 4.7 },
        ]}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.resCard}>
            <Text style={styles.resName}>{item.name}</Text>
            <Text style={styles.resInfo}>{item.rating} ★ | {item.dist}</Text>
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', margin: 20 },
  catList: { maxHeight: 50, paddingLeft: 20 },
  catBadge: { backgroundColor: '#f3f4f6', paddingHorizontal: 15, paddingVertical: 8, borderRadius: 20, marginRight: 10 },
  catText: { fontSize: 12, fontWeight: '600', color: '#1e3a8a' },
  resCard: { marginBottom: 15, padding: 15 },
  resName: { fontSize: 18, fontWeight: 'bold' },
  resInfo: { color: '#6b7280', marginTop: 5 }
});
