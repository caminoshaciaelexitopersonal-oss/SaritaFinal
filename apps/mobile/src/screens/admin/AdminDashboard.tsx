import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { api } from '../../services/api';

export const AdminDashboard = () => {
  const [stats, setStats] = useState<any>({ total_revenue: 0, user_growth: 0 });

  useEffect(() => {
    const fetchAdminData = async () => {
      try {
        const response = await api.get('/admin/analytics/');
        setStats(response.data);
      } catch (error) {}
    };
    fetchAdminData();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Control Tower SuperAdmin</Text>

      <Card style={styles.mainCard}>
        <Text style={styles.label}>Ingresos Totales (GMV)</Text>
        <Text style={styles.value}>${stats.total_revenue?.toLocaleString()} COP</Text>
      </Card>

      <View style={styles.row}>
        <Card style={styles.miniCard}>
          <Text style={styles.miniLabel}>Nuevos Usuarios</Text>
          <Text style={styles.miniValue}>+{stats.user_growth}%</Text>
        </Card>
        <Card style={styles.miniCard}>
          <Text style={styles.miniLabel}>Tours Activos</Text>
          <Text style={styles.miniValue}>{stats.total_tours || 0}</Text>
        </Card>
      </View>

      <Text style={styles.sectionTitle}>Rendimiento por Categoría</Text>
      {['Ecoturismo', 'Aventura', 'Cultural'].map(cat => (
        <Card key={cat} style={styles.catCard}>
          <Text style={styles.catName}>{cat}</Text>
          <View style={styles.progressBar}>
            <View style={[styles.progress, { width: '70%' }]} />
          </View>
        </Card>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#1a1a1a', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#fff', marginBottom: 25 },
  mainCard: { padding: 25, backgroundColor: '#1e3a8a', borderBottomWidth: 4, borderColor: '#f59e0b' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  value: { color: '#fff', fontSize: 32, fontWeight: 'bold', marginTop: 10 },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginTop: 20 },
  miniCard: { flex: 0.48, padding: 15, backgroundColor: '#2d2d2d' },
  miniLabel: { color: '#9ca3af', fontSize: 12 },
  miniValue: { color: '#fff', fontSize: 20, fontWeight: 'bold', marginTop: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#fff', marginVertical: 20 },
  catCard: { marginBottom: 12, padding: 15, backgroundColor: '#2d2d2d' },
  catName: { color: '#fff', fontWeight: 'bold' },
  progressBar: { height: 6, backgroundColor: '#4b5563', borderRadius: 3, marginTop: 10 },
  progress: { height: '100%', backgroundColor: '#f59e0b', borderRadius: 3 }
});
