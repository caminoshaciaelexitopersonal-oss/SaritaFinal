import React, { useEffect, useState } from 'react';
import { View, FlatList, StyleSheet, ActivityIndicator } from 'react-native';
import { ReservationCard, Text, Button, StatCard } from '@sarita/shared-ui';
import { ReservationData } from '@sarita/shared-sdk';
import { bookingService } from '../../services/bookingService';

export const MobileBookingsScreen = () => {
  const [bookings, setBookings] = useState<ReservationData[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchBookings = async () => {
    setLoading(true);
    try {
      const response = await bookingService.getReservations();
      // Map API data to UI model if needed
      const mappedData = (response.data.results || []).map((item: any) => ({
         id: item.id,
         client: item.customer_name || 'Turista',
         service: item.service_name || 'Servicio',
         startDate: item.start_date,
         endDate: item.end_date,
         status: item.status,
         price: `$${item.total_price}`
      }));
      setBookings(mappedData);
    } catch (err) {
      console.error("Mobile Bookings Error:", err);
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
