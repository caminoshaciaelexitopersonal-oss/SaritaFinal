import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import { usePagination } from '../../hooks/usePagination';
import { Card } from '../../components/Card';

export const HistoryScreen = () => {
  const { data, loading } = usePagination('/history');

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.historyCard}>
            <Text style={styles.tourName}>{item.tour_name}</Text>
            <Text style={styles.date}>{item.date}</Text>
            <Text style={styles.price}>${item.amount} COP</Text>
          </Card>
        )}
        ListEmptyComponent={<Text style={styles.empty}>No tienes viajes pasados.</Text>}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 15 },
  historyCard: { marginBottom: 10 },
  tourName: { fontWeight: 'bold', fontSize: 16 },
  date: { color: '#6b7280', fontSize: 12 },
  price: { marginTop: 5, color: '#1e3a8a' },
  empty: { textAlign: 'center', marginTop: 50, color: '#9ca3af' }
});
