import React, { useState } from 'react';
import { View, Text, StyleSheet, Alert } from 'react-native';
import { useRoute, useNavigation } from '@react-navigation/native';
import { api } from '../../services/api';
import { Button } from '../../components/Button';
import { Input } from '../../components/Input';

export const BookingScreen = () => {
  const route = useRoute<any>();
  const navigation = useNavigation<any>();
  const [guests, setGuests] = useState('1');
  const [date, setDate] = useState('2026-04-20');
  const [loading, setLoading] = useState(false);

  const handleBooking = async () => {
    try {
      setLoading(true);
      await api.post('/reservations/', {
        tour_id: route.params.tourId,
        date: date,
        guests: parseInt(guests),
      });
      Alert.alert('¡Éxito!', 'Tu reserva ha sido creada correctamente.');
      navigation.navigate('BookingsTab');
    } catch (error) {
      console.error('Error creating reservation:', error);
      Alert.alert('Error', 'No se pudo crear la reserva.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Finalizar Reserva</Text>
      <Text style={styles.label}>Fecha (AAAA-MM-DD)</Text>
      <Input value={date} onChangeText={setDate} />
      <Text style={styles.label}>Cantidad de Personas</Text>
      <Input
        value={guests}
        onChangeText={setGuests}
        keyboardType="numeric"
      />
      <Button
        title="Confirmar Reserva"
        onPress={handleBooking}
        loading={loading}
        style={styles.button}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 30 },
  label: { fontSize: 16, color: '#4b5563', marginBottom: 5 },
  button: { marginTop: 20 }
});
