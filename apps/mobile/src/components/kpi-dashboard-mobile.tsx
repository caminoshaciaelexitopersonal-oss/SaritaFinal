import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const KPICard = ({ title, value, color }) => (
  <View style={[styles.card, { borderLeftColor: color }]}>
    <Text style={styles.cardTitle}>{title}</Text>
    <Text style={styles.cardValue}>{value}</Text>
  </View>
);

export default function KPIDashboardMobile({ stats }) {
  return (
    <View style={styles.grid}>
      <KPICard title="Ventas Hoy" value={stats?.todaySales || "-bash"} color="#4CAF50" />
      <KPICard title="Reservas" value={stats?.activeBookings || "0"} color="#2196F3" />
      <KPICard title="Ocupación" value={stats?.occupancy || "0%"} color="#FF9800" />
      <KPICard title="Alertas" value={stats?.alerts || "0"} color="#F44336" />
    </View>
  );
}

const styles = StyleSheet.create({
  grid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between', padding: 8 },
  card: { width: '48%', padding: 16, backgroundColor: '#fff', marginBottom: 12, borderRadius: 8, borderLeftWidth: 4, elevation: 2 },
  cardTitle: { fontSize: 12, color: '#666' },
  cardValue: { fontSize: 18, fontWeight: 'bold', marginTop: 4 }
});
