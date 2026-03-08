import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const OpenDataPortalScreen = () => {
  const datasets = [
    { id: '1', name: 'Flujo Turístico 2025', format: 'CSV/JSON', size: '12 MB' },
    { id: '2', name: 'Gasto Promedio por Región', format: 'JSON', size: '4.5 MB' },
    { id: '3', name: 'Tendencias de Ecoturismo', format: 'PDF/XLS', size: '8.2 MB' },
  ];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Portal de Datos Abiertos</Text>
      <Text style={styles.subtitle}>Fomentando la investigación y transparencia en el sector turístico.</Text>

      <FlatList
        data={datasets}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.dataCard}>
            <View style={styles.row}>
              <View style={styles.info}>
                <Text style={styles.dataName}>{item.name}</Text>
                <Text style={styles.dataInfo}>Formato: {item.format} | {item.size}</Text>
              </View>
              <Button title="Descargar" onPress={() => {}} style={styles.dlBtn} />
            </View>
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 22, fontWeight: 'bold', marginTop: 30, marginHorizontal: 20 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20, fontSize: 13 },
  dataCard: { marginBottom: 15, padding: 20 },
  row: { flexDirection: 'row', alignItems: 'center' },
  info: { flex: 1 },
  dataName: { fontWeight: 'bold', fontSize: 16, color: '#1e3a8a' },
  dataInfo: { fontSize: 12, color: '#9ca3af', marginTop: 5 },
  dlBtn: { paddingVertical: 8, paddingHorizontal: 15, backgroundColor: '#334155' }
});
