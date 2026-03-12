import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';

export const GlobalNetworkScreen = () => {
  const routes = [
    { id: '1', name: 'Ruta del Café y Llano', connections: ['Colombia', 'Brasil'], status: 'Activa' },
    { id: '2', name: 'Circuito Amazónico Global', connections: ['Colombia', 'Perú', 'Ecuador'], status: 'En expansión' },
  ];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Red Global de Destinos</Text>
      <Text style={styles.subtitle}>Circuitos turísticos internacionales conectados por SARITA.</Text>

      {routes.map(route => (
        <Card key={route.id} style={styles.routeCard}>
          <Text style={styles.routeName}>{route.name}</Text>
          <View style={styles.connectionRow}>
            {route.connections.map(c => (
              <View key={c} style={styles.badge}><Text style={styles.badgeText}>{c}</Text></View>
            ))}
          </View>
          <Text style={styles.status}>Estatus: {route.status}</Text>
          <TouchableOpacity style={styles.collabBtn}><Text style={styles.collabText}>Ver Alianzas Regionales</Text></TouchableOpacity>
        </Card>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f8fafc', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', color: '#0f172a' },
  subtitle: { color: '#64748b', marginVertical: 10, fontSize: 14 },
  routeCard: { marginBottom: 20, padding: 20 },
  routeName: { fontSize: 18, fontWeight: 'bold', color: '#1e3a8a' },
  connectionRow: { flexDirection: 'row', marginVertical: 10 },
  badge: { backgroundColor: '#e2e8f0', paddingHorizontal: 10, paddingVertical: 4, borderRadius: 12, marginRight: 8 },
  badgeText: { fontSize: 10, fontWeight: 'bold', color: '#475569' },
  status: { fontSize: 12, color: '#10b981', fontWeight: 'bold' },
  collabBtn: { marginTop: 15, padding: 10, backgroundColor: '#334155', borderRadius: 8, alignItems: 'center' },
  collabText: { color: '#fff', fontSize: 12, fontWeight: 'bold' }
});
