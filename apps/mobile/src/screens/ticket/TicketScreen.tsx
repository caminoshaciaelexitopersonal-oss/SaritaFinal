import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import { useRoute } from '@react-navigation/native';
import { api } from '../../services/api';
import { Card } from '../../components/Card';

// En un entorno real, instalaríamos react-native-qrcode-svg
// Aquí simulamos el contenedor del QR para la Fase 03
const QRCodePlaceholder = ({ value }: { value: string }) => (
  <View style={styles.qrContainer}>
    <View style={styles.qrBox}>
      <Text style={{ fontSize: 10, textAlign: 'center' }}>QR: {value}</Text>
    </View>
  </View>
);

export const TicketScreen = () => {
  const route = useRoute<any>();
  const [ticket, setTicket] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTicket = async () => {
      try {
        const response = await api.get(`/reservations/${route.params.id || route.params.reservationId}/ticket/`);
        setTicket(response.data);
      } catch (error) {
        console.error('Error fetching ticket:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchTicket();
  }, [route.params.reservationId]);

  if (loading) return <ActivityIndicator style={{ flex: 1 }} />;
  if (!ticket) return <View style={styles.container}><Text>No se encontró el ticket.</Text></View>;

  return (
    <View style={styles.container}>
      <Card style={styles.ticketCard}>
        <Text style={styles.confirmedBadge}>RESERVA CONFIRMADA</Text>
        <Text style={styles.tourName}>{ticket.tour_name || 'Safari Río Meta'}</Text>

        <View style={styles.divider} />

        <View style={styles.infoRow}>
          <View>
            <Text style={styles.label}>Fecha</Text>
            <Text style={styles.value}>{ticket.date || '20-04-2026'}</Text>
          </View>
          <View>
            <Text style={styles.label}>Hora</Text>
            <Text style={styles.value}>08:30 AM</Text>
          </View>
        </View>

        <QRCodePlaceholder value={`SARITA-${ticket.reservation_id}`} />

        <Text style={styles.footerNote}>Presenta este QR al operador al iniciar el tour.</Text>
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f3f4f6', justifyContent: 'center' },
  ticketCard: { padding: 30, alignItems: 'center', borderStyle: 'dashed', borderWidth: 1, borderColor: '#d1d5db' },
  confirmedBadge: { backgroundColor: '#d1fae5', color: '#065f46', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20, fontSize: 12, fontWeight: 'bold', marginBottom: 20 },
  tourName: { fontSize: 24, fontWeight: 'bold', textAlign: 'center' },
  divider: { width: '100%', height: 1, backgroundColor: '#e5e7eb', marginVertical: 20 },
  infoRow: { flexDirection: 'row', justifyContent: 'space-between', width: '100%', marginBottom: 30 },
  label: { fontSize: 12, color: '#6b7280', textTransform: 'uppercase' },
  value: { fontSize: 16, fontWeight: 'bold' },
  qrContainer: { marginVertical: 20 },
  qrBox: { width: 150, height: 150, backgroundColor: '#fff', borderWidth: 10, borderColor: '#000', justifyContent: 'center', alignItems: 'center' },
  footerNote: { color: '#9ca3af', fontSize: 12, textAlign: 'center', marginTop: 10 }
});
