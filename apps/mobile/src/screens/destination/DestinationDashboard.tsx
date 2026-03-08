import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, Dimensions } from 'react-native';
import { Card } from '../../components/Card';
import { cityService } from '../../services/cityService';

export const DestinationDashboard = () => {
  const [data, setData] = useState<any>({ visitor_count: 0, active_events: 0 });

  useEffect(() => {
    const fetchCityData = async () => {
      try {
        const response = await cityService.getCityTourismData('puerto-gaitan');
        setData(response.data);
      } catch (error) {}
    };
    fetchCityData();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.cityTitle}>Puerto Gaitán, Meta</Text>
        <Text style={styles.citySubtitle}>Gestión de Destino Inteligente</Text>
      </View>

      <Card style={styles.statsCard}>
        <Text style={styles.label}>Turistas en la Región (Tiempo Real)</Text>
        <Text style={styles.visitorValue}>{data.visitor_count?.toLocaleString() || '1,240'}</Text>
        <View style={styles.badge}><Text style={styles.badgeText}>+12% vs ayer</Text></View>
      </Card>

      <View style={styles.row}>
        <Card style={styles.miniCard}>
          <Text style={styles.miniLabel}>Eventos Activos</Text>
          <Text style={styles.miniValue}>{data.active_events || 4}</Text>
        </Card>
        <Card style={styles.miniCard}>
          <Text style={styles.miniLabel}>Ocupación Hotelera</Text>
          <Text style={styles.miniValue}>85%</Text>
        </Card>
      </View>

      <Text style={styles.sectionTitle}>Tendencias de Búsqueda</Text>
      <Card style={styles.trendCard}>
        <Text style={styles.trendText}>1. Safari Río Manacacías</Text>
        <Text style={styles.trendText}>2. Festival de la Cachama</Text>
        <Text style={styles.trendText}>3. Atardeceres de Altillanura</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6' },
  header: { padding: 30, backgroundColor: '#065f46' },
  cityTitle: { fontSize: 28, fontWeight: 'bold', color: '#fff' },
  citySubtitle: { color: 'rgba(255,255,255,0.8)', fontSize: 14 },
  statsCard: { margin: 20, padding: 25, alignItems: 'center' },
  label: { color: '#6b7280', fontSize: 14 },
  visitorValue: { fontSize: 42, fontWeight: 'bold', color: '#065f46', marginVertical: 10 },
  badge: { backgroundColor: '#d1fae5', paddingHorizontal: 10, paddingVertical: 5, borderRadius: 15 },
  badgeText: { color: '#065f46', fontSize: 12, fontWeight: 'bold' },
  row: { flexDirection: 'row', justifyContent: 'space-between', paddingHorizontal: 20 },
  miniCard: { flex: 0.48, padding: 15, alignItems: 'center' },
  miniLabel: { fontSize: 12, color: '#6b7280' },
  miniValue: { fontSize: 20, fontWeight: 'bold', marginTop: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', margin: 20 },
  trendCard: { marginHorizontal: 20, padding: 20 },
  trendText: { fontSize: 16, marginBottom: 10, color: '#374151' }
});
