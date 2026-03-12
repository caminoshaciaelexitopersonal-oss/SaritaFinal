import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { api } from '../../services/api';

export const PassportScreen = () => {
  const [passport, setPassport] = useState<any>({ stamps: [], achievements: [] });

  useEffect(() => {
    const fetchPassport = async () => {
      try {
        const response = await api.get('/passport/');
        setPassport(response.data);
      } catch (error) {}
    };
    fetchPassport();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <Card style={styles.headerCard}>
        <Text style={styles.label}>Nivel de Viajero</Text>
        <Text style={styles.level}>NOMAD</Text>
      </Card>

      <Text style={styles.sectionTitle}>Tus Sellos de Destino</Text>
      <View style={styles.stampsGrid}>
        {['Meta', 'Vichada', 'Guaviare', 'Casanare'].map(s => (
          <View key={s} style={styles.stamp}>
            <Text style={styles.stampText}>{s.toUpperCase()}</Text>
          </View>
        ))}
      </View>

      <Text style={styles.sectionTitle}>Logros Desbloqueados</Text>
      {['Primer Safari', 'Explorador del Río', 'Héroe Local'].map(a => (
        <Card key={a} style={styles.achievementCard}>
          <Text style={styles.achievementName}>{a} ✓</Text>
        </Card>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  headerCard: { padding: 30, alignItems: 'center', backgroundColor: '#1e3a8a' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  level: { color: '#fff', fontSize: 32, fontWeight: 'bold' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  stampsGrid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between' },
  stamp: { width: '45%', height: 100, backgroundColor: '#fff', borderRadius: 50, borderWidth: 2, borderColor: '#f59e0b', borderStyle: 'dashed', justifyContent: 'center', alignItems: 'center', marginBottom: 15 },
  stampText: { fontSize: 10, fontWeight: 'bold', color: '#f59e0b' },
  achievementCard: { padding: 15, marginBottom: 10 },
  achievementName: { fontWeight: 'bold', color: '#10b981' }
});
