import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { businessService } from '../../services/businessService';

export const BusinessDashboard = () => {
  const [stats, setStats] = useState<any>({ revenue: 0, orders: 0 });

  useEffect(() => {
    const fetchBusinessData = async () => {
      try {
        const response = await businessService.getOperativaDashboard();
        setStats(response.data);
      } catch (error) {
        console.error("Mobile Business Dashboard Error:", error);
      }
    };
    fetchBusinessData();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>ERP Mi Negocio</Text>

      <Card style={styles.mainCard}>
        <Text style={styles.label}>Ventas Brutas</Text>
        <Text style={styles.value}>${stats?.total_sales?.toLocaleString() || 0} COP</Text>
        <View style={styles.badge}><Text style={styles.badgeText}>Flujo Real</Text></View>
      </Card>

      <View style={styles.grid}>
        <TouchableOpacity style={styles.gridItem}>
          <Card style={styles.itemCard}><Text style={styles.icon}>📋</Text><Text style={styles.itemLabel}>Servicios</Text></Card>
        </TouchableOpacity>
        <TouchableOpacity style={styles.gridItem}>
          <Card style={styles.itemCard}><Text style={styles.icon}>💰</Text><Text style={styles.itemLabel}>Finanzas</Text></Card>
        </TouchableOpacity>
        <TouchableOpacity style={styles.gridItem}>
          <Card style={styles.itemCard}><Text style={styles.icon}>🧾</Text><Text style={styles.itemLabel}>Contabilidad</Text></Card>
        </TouchableOpacity>
        <TouchableOpacity style={styles.gridItem}>
          <Card style={styles.itemCard}><Text style={styles.icon}>📂</Text><Text style={styles.itemLabel}>Documentos</Text></Card>
        </TouchableOpacity>
      </View>

      <Text style={styles.sectionTitle}>Operaciones Recientes</Text>
      <Card style={styles.opCard}>
        <Text style={styles.opTitle}>Saldo Monedero</Text>
        <Text style={[styles.opStatus, { color: '#4f46e5' }]}>${stats?.wallet_balance?.toLocaleString() || 0} Disponible</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  mainCard: { padding: 30, backgroundColor: '#0f172a', alignItems: 'center' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  value: { color: '#fff', fontSize: 32, fontWeight: 'bold', marginVertical: 10 },
  badge: { backgroundColor: '#10b981', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20 },
  badgeText: { color: '#fff', fontWeight: 'bold', fontSize: 10 },
  grid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between', marginTop: 20 },
  gridItem: { width: '48%', marginBottom: 15 },
  itemCard: { padding: 20, alignItems: 'center' },
  icon: { fontSize: 24, marginBottom: 10 },
  itemLabel: { fontWeight: 'bold', color: '#1e3a8a' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  opCard: { padding: 20 },
  opTitle: { fontWeight: 'bold' },
  opStatus: { color: '#f59e0b', fontSize: 12, marginTop: 5, fontWeight: 'bold' }
});
