import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import { Card } from '../../components/Card';
import { businessService } from '../../services/businessService';

export const BusinessAccountingScreen = () => {
  const [journal, setJournal] = useState<any[]>([]);
  const [balance, setBalance] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAccounting = async () => {
      try {
        const [journalRes, balanceRes] = await Promise.all([
          businessService.getContabilidadGeneral(),
          businessService.getFinancieraDashboard()
        ]);
        setJournal(journalRes.data);
        setBalance(balanceRes.data.balance_general);
      } catch (error) {
        console.error('Error al cargar datos contables reales.');
      } finally {
        setLoading(false);
      }
    };
    fetchAccounting();
  }, []);

  if (loading) return <ActivityIndicator style={{ flex: 1 }} />;

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Libro Mayor y Contabilidad ERP</Text>

      <Card style={styles.ledgerCard}>
        <Text style={styles.ledgerTitle}>Libro Diario (Asientos)</Text>
        {journal.length > 0 ? journal.map(j => (
          <View key={j.id} style={styles.entry}>
            <View>
              <Text style={styles.entryDesc}>{j.descripcion}</Text>
              <Text style={{ fontSize: 10, color: '#94a3b8' }}>{j.fecha}</Text>
            </View>
            <Text style={styles.entryVal}>
              {j.naturaleza === 'DB' ? `+${j.monto}` : `-${j.monto}`} COP
            </Text>
          </View>
        )) : <Text style={{ color: '#94a3b8' }}>No hay asientos recientes.</Text>}
      </Card>

      <Text style={styles.sectionTitle}>Situación Financiera Real</Text>
      <Card style={styles.balanceCard}>
        <View style={styles.row}><Text>Activos</Text><Text style={styles.bold}>${balance?.activos || 0} COP</Text></View>
        <View style={styles.row}><Text>Pasivos</Text><Text style={styles.bold}>${balance?.pasivos || 0} COP</Text></View>
        <View style={styles.row}><Text>Patrimonio</Text><Text style={styles.bold}>${balance?.patrimonio || 0} COP</Text></View>
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
