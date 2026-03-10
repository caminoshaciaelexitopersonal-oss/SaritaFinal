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

  const [useWallet, setUseWallet] = useState(false);

  const handlePayment = async () => {
    try {
      setLoading(true);

      let result;
      if (useWallet) {
        // Pago vía Wallet SARITA (Integración Fase 4)
        result = await paymentService.payWithWallet(reservationId);
      } else {
        // Integración con pasarela externa (Stripe/Wompi)
        result = await paymentService.confirmPayment(clientSecret);
      }

      if (result.success || result.data?.status === 'succeeded') {
        Alert.alert('¡Pago Exitoso!', 'Tu reserva ha sido confirmada.', [
          { text: 'Ver Ticket', onPress: () => navigation.navigate('Ticket', { reservationId }) }
        ]);
      } else {
        throw new Error(result.message || 'Pago no procesado correctamente');
      }
    } catch (error: any) {
      Alert.alert('Error', error.message || 'Hubo un problema al procesar el pago.');
    } finally {
      setLoading(false);
    }
  };

  if (!clientSecret && !loading) return <ActivityIndicator style={{ flex: 1 }} />;

  return (
    <View style={styles.container}>
      <Card style={styles.card}>
        <Text style={styles.title}>Método de Pago</Text>
        <Text style={styles.subtitle}>Reserva: {reservationId}</Text>

        <View style={styles.paymentMethods}>
           <TouchableOpacity
             style={[styles.methodOption, !useWallet && styles.methodActive]}
             onPress={() => setUseWallet(false)}
           >
             <Text style={[styles.methodText, !useWallet && styles.methodTextActive]}>Tarjeta</Text>
           </TouchableOpacity>
           <TouchableOpacity
             style={[styles.methodOption, useWallet && styles.methodActive]}
             onPress={() => setUseWallet(true)}
           >
             <Text style={[styles.methodText, useWallet && styles.methodTextActive]}>SARITA Wallet</Text>
           </TouchableOpacity>
        </View>

        {!useWallet ? (
          <>
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

          </>
        ) : (
          <View style={styles.walletInfo}>
            <Text style={styles.walletLabel}>Paga usando tu saldo acumulado en SARITA.</Text>
            <Text style={styles.walletNote}>Rápido, seguro y sin comisiones extras.</Text>
          </View>
        )}

        <Button
          title={useWallet ? "Pagar con Wallet" : "Confirmar Pago"}
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
  paymentMethods: { flexDirection: 'row', gap: 10, marginBottom: 20 },
  methodOption: { flex: 1, padding: 12, borderRadius: 10, borderWidth: 1, borderColor: '#e5e7eb', alignItems: 'center' },
  methodActive: { borderColor: '#1e3a8a', backgroundColor: '#eff6ff' },
  methodText: { fontWeight: 'bold', color: '#6b7280' },
  methodTextActive: { color: '#1e3a8a' },
  inputContainer: { marginBottom: 15 },
  label: { fontSize: 14, color: '#4b5563', marginBottom: 5 },
  row: { flexDirection: 'row', marginBottom: 20 },
  walletInfo: { padding: 20, backgroundColor: '#f3f4f6', borderRadius: 12, marginBottom: 20 },
  walletLabel: { textAlign: 'center', fontWeight: 'bold', color: '#374151' },
  walletNote: { textAlign: 'center', fontSize: 12, color: '#6b7280', marginTop: 5 },
  payBtn: { backgroundColor: '#10b981', marginTop: 10 }
});
