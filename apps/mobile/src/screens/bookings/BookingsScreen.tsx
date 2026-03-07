import React from 'react';
import { View, Text, FlatList, StyleSheet, ActivityIndicator } from 'react-native';
import { usePagination } from '../../hooks/usePagination';
import { Card } from '../../components/Card';

export const BookingsScreen = () => {
  const { data, loading, loadMore } = usePagination('/reservations');

  const getStatusStyle = (status: string) => {
    switch (status) {
      case 'confirmed': return { color: '#10b981' };
      case 'pending': return { color: '#f59e0b' };
      case 'cancelled': return { color: '#ef4444' };
      default: return { color: '#6b7280' };
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Card style={styles.bookingCard}>
            <View style={styles.header}>
              <Text style={styles.tourName}>{item.tour_id}</Text>
              <Text style={[styles.status, getStatusStyle(item.status)]}>
                {item.status.toUpperCase()}
              </Text>
            </View>
            <Text style={styles.date}>Fecha: {item.date}</Text>
            <Text style={styles.total}>Total: ${item.total_price || 0} COP</Text>
          </Card>
        )}
        contentContainerStyle={styles.list}
        onEndReached={loadMore}
        ListFooterComponent={loading ? <ActivityIndicator /> : null}
        ListEmptyComponent={!loading ? <Text style={styles.empty}>No tienes reservas aún.</Text> : null}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  list: { padding: 15 },
  bookingCard: { marginBottom: 12 },
  header: { flexDirection: 'row', justifyContent: 'space-between' },
  tourName: { fontSize: 16, fontWeight: 'bold' },
  status: { fontSize: 12, fontWeight: 'bold' },
  date: { color: '#6b7280', marginTop: 5 },
  total: { marginTop: 10, fontWeight: '600', color: '#111827' },
  empty: { textAlign: 'center', marginTop: 50, color: '#6b7280' }
});
