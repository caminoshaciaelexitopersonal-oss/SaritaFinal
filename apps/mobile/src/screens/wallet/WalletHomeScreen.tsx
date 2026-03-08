import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { walletService } from '../../services/walletService';

export const WalletHomeScreen = () => {
  const [balance, setBalance] = useState(0);

  useEffect(() => {
    const fetchBalance = async () => {
      try {
        const response = await walletService.getBalance();
        setBalance(response.data.balance);
      } catch (error) {
        setBalance(150.50); // Fallback mock
      }
    };
    fetchBalance();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <Card style={styles.balanceCard}>
        <Text style={styles.label}>Saldo Disponible</Text>
        <Text style={styles.balance}>${balance.toLocaleString()} USD</Text>
        <View style={styles.actions}>
          <Button title="Recargar" onPress={() => {}} style={styles.actionBtn} />
          <Button title="Enviar" onPress={() => {}} style={[styles.actionBtn, { backgroundColor: '#334155' }]} />
        </View>
      </Card>

      <Text style={styles.sectionTitle}>Transacciones Recientes</Text>
      {[
        { id: '1', title: 'Pago Tour Safari', amount: -120, date: 'Hoy' },
        { id: '2', title: 'Recarga Tarjeta', amount: 50, date: 'Ayer' },
      ].map(t => (
        <Card key={t.id} style={styles.txCard}>
          <View style={styles.row}>
            <Text style={styles.txTitle}>{t.title}</Text>
            <Text style={[styles.txAmount, t.amount < 0 ? styles.negative : styles.positive]}>
              {t.amount < 0 ? '' : '+'}{t.amount} USD
            </Text>
          </View>
          <Text style={styles.txDate}>{t.date}</Text>
        </Card>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  balanceCard: { padding: 30, backgroundColor: '#1e3a8a', alignItems: 'center' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  balance: { color: '#fff', fontSize: 36, fontWeight: 'bold', marginVertical: 15 },
  actions: { flexDirection: 'row', gap: 10, width: '100%' },
  actionBtn: { flex: 1, backgroundColor: '#f59e0b' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  txCard: { marginBottom: 10, padding: 15 },
  row: { flexDirection: 'row', justifyContent: 'space-between' },
  txTitle: { fontWeight: 'bold' },
  txAmount: { fontWeight: 'bold' },
  negative: { color: '#ef4444' },
  positive: { color: '#10b981' },
  txDate: { fontSize: 12, color: '#9ca3af', marginTop: 5 }
});
