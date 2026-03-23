import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, Alert } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { walletService } from '../../services/walletService';

export const WalletTopUpScreen = () => {
  const [amount, setAmount] = useState('');
  const [loading, setLoading] = useState(false);

  const handleTopUp = async () => {
    if (!amount) return;
    try {
      setLoading(true);
      await walletService.topUp(parseFloat(amount), 'credit_card');
      Alert.alert('¡Éxito!', 'Tu recarga ha sido procesada correctamente.');
    } catch (error) {
      Alert.alert('Error', 'No se pudo procesar la recarga.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Recargar Billetera</Text>
      <Card style={styles.card}>
        <Text style={styles.label}>Monto a Recargar (USD)</Text>
        <TextInput
          style={styles.input}
          value={amount}
          onChangeText={setAmount}
          keyboardType="numeric"
          placeholder="0.00"
        />
        <Button title="Confirmar Recarga" onPress={handleTopUp} loading={loading} />
      </Card>

      <Text style={styles.info}>El saldo se verá reflejado inmediatamente en tu cuenta SARITA.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  card: { padding: 20 },
  label: { fontSize: 14, color: '#64748b', marginBottom: 10 },
  input: { borderBottomWidth: 2, borderColor: '#1e3a8a', fontSize: 24, fontWeight: 'bold', marginBottom: 30, paddingVertical: 10 },
  info: { marginTop: 20, color: '#94a3b8', fontSize: 12, textAlign: 'center' }
});
