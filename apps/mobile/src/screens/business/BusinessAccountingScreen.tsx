import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessAccountingScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Libro Mayor y Contabilidad</Text>

      <Card style={styles.ledgerCard}>
        <Text style={styles.ledgerTitle}>Asientos Recientes</Text>
        {[
          { id: 'J-001', date: '2026-03-07', desc: 'Venta Tour Safari', debit: 120.00, credit: 0 },
          { id: 'J-002', date: '2026-03-07', desc: 'Pago Comisión SARITA', debit: 0, credit: 18.00 },
        ].map(j => (
          <View key={j.id} style={styles.entry}>
            <Text style={styles.entryDesc}>{j.desc}</Text>
            <Text style={styles.entryVal}>{j.debit > 0 ? `+${j.debit}` : `-${j.credit}`} USD</Text>
          </View>
        ))}
      </Card>

      <Text style={styles.sectionTitle}>Balance General Simulado</Text>
      <Card style={styles.balanceCard}>
        <View style={styles.row}><Text>Activos Circulantes</Text><Text style={styles.bold}>$15.250 USD</Text></View>
        <View style={styles.row}><Text>Pasivos</Text><Text style={styles.bold}>$2.100 USD</Text></View>
        <View style={styles.row}><Text>Patrimonio Neto</Text><Text style={styles.bold}>$13.150 USD</Text></View>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f8fafc', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20, color: '#0f172a' },
  ledgerCard: { padding: 20, marginBottom: 20 },
  ledgerTitle: { fontWeight: 'bold', marginBottom: 15, fontSize: 16 },
  entry: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 10, borderBottomWidth: 1, borderColor: '#f1f5f9' },
  entryDesc: { fontSize: 13, color: '#475569' },
  entryVal: { fontWeight: 'bold' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 15 },
  balanceCard: { padding: 20 },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 10 },
  bold: { fontWeight: 'bold', color: '#1e3a8a' }
});
