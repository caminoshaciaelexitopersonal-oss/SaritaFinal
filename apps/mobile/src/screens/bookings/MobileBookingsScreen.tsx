import React, { useEffect, useState } from 'react';
import { View, FlatList, StyleSheet, ActivityIndicator } from 'react-native';
import { ReservationCard, Text, Button, StatCard } from '@sarita/shared-ui';
import { ReservationService, ReservationData } from '@sarita/shared-sdk';

export const MobileBookingsScreen = () => {
  const [bookings, setBookings] = useState<ReservationData[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchBookings = async () => {
    setLoading(true);
    try {
      // Usando mock para la demo de paridad
      const data: ReservationData[] = [
        { id: '1', client: 'Carlos Ruiz', service: 'Tour Río Manacacías', startDate: '2026-03-20', endDate: '2026-03-20', status: 'CONFIRMADA', price: '$150,000' },
        { id: '2', client: 'Elena Gómez', service: 'Hospedaje 2 Noches', startDate: '2026-03-21', endDate: '2026-03-23', status: 'PENDIENTE', price: '$450,000' }
      ];
      setBookings(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBookings();
  }, []);

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text variant="headingM">Gestión de Reservas</Text>
        <Button label="+" variant="primary" onPress={() => {}} />
      </View>

      <View style={styles.statsRow}>
        <StatCard title="Hoy" value={bookings.length} trend="Operativo" trendDirection="up" />
        <StatCard title="Pendientes" value="1" trend="Urgente" trendDirection="down" />
      </View>

      {loading ? (
        <ActivityIndicator style={{ marginTop: 40 }} />
      ) : (
        <FlatList
          data={bookings}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <ReservationCard reservation={item} />
          )}
          contentContainerStyle={styles.list}
          onRefresh={fetchBookings}
          refreshing={loading}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderBottomColor: '#eee'
  },
  statsRow: { flexDirection: 'row', gap: 12, padding: 16 },
  list: { padding: 16 }
});
