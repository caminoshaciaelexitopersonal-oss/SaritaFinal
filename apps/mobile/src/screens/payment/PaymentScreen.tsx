import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ActivityIndicator, Alert } from 'react-native';
import { useRoute, useNavigation } from '@react-navigation/native';
import { paymentService } from '../../services/paymentService';
import { Button } from '../../components/Button';
import { Input } from '../../components/Input';
import { Card } from '../../components/Card';

export const PaymentScreen = () => {
  const route = useRoute<any>();
  const navigation = useNavigation<any>();
  const [loading, setLoading] = useState(false);
  const [clientSecret, setClientSecret] = useState('');
  const reservationId = route.params?.reservationId;

  useEffect(() => {
    const initPayment = async () => {
      try {
        const data = await paymentService.createPaymentIntent(reservationId);
        setClientSecret(data.client_secret);
      } catch (error) {
        Alert.alert('Error', 'No se pudo inicializar el pago.');
      }
    };
    if (reservationId) initPayment();
  }, [reservationId]);

  const handlePayment = async () => {
    try {
      setLoading(true);
      // Simulación de confirmación de pago (en real se usaría Stripe SDK)
      await new Promise(resolve => setTimeout(resolve, 2000));
      await paymentService.confirmPayment('pi_fake_123');

      Alert.alert('¡Pago Exitoso!', 'Tu reserva ha sido confirmada.', [
        { text: 'Ver Ticket', onPress: () => navigation.navigate('Ticket', { reservationId }) }
      ]);
    } catch (error) {
      Alert.alert('Error', 'Hubo un problema al procesar el pago.');
    } finally {
      setLoading(false);
    }
  };

  if (!clientSecret && !loading) return <ActivityIndicator style={{ flex: 1 }} />;

  return (
    <View style={styles.container}>
      <Card style={styles.card}>
        <Text style={styles.title}>Pasarela de Pago Segura</Text>
        <Text style={styles.subtitle}>Reserva: {reservationId}</Text>

        <View style={styles.inputContainer}>
          <Text style={styles.label}>Número de Tarjeta</Text>
          <Input placeholder="XXXX XXXX XXXX XXXX" keyboardType="numeric" />
        </View>

        <View style={styles.row}>
          <View style={{ flex: 1, marginRight: 10 }}>
            <Text style={styles.label}>Vencimiento</Text>
            <Input placeholder="MM/AA" />
          </View>
          <View style={{ flex: 1 }}>
            <Text style={styles.label}>CVV</Text>
            <Input placeholder="123" secureTextEntry keyboardType="numeric" />
          </View>
        </View>

        <Button
          title="Pagar Ahora"
          onPress={handlePayment}
          loading={loading}
          style={styles.payBtn}
        />
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f9fafb', justifyContent: 'center' },
  card: { padding: 20 },
  title: { fontSize: 20, fontWeight: 'bold', textAlign: 'center', marginBottom: 5 },
  subtitle: { textAlign: 'center', color: '#6b7280', marginBottom: 20 },
  inputContainer: { marginBottom: 15 },
  label: { fontSize: 14, color: '#4b5563', marginBottom: 5 },
  row: { flexDirection: 'row', marginBottom: 20 },
  payBtn: { backgroundColor: '#10b981', marginTop: 10 }
});
