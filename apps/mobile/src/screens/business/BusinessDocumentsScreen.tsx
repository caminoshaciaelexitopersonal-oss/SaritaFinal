import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessDocumentsScreen = () => {
  const docs = [
    { id: '1', name: 'Factura_FE-920.pdf', type: 'Contable', date: '2026-03-07' },
    { id: '2', name: 'Contrato_Proveedor_Transporte.pdf', type: 'Legal', date: '2026-03-01' },
    { id: '3', name: 'Reporte_Ventas_Feb.xlsx', type: 'Administrativo', date: '2026-03-01' },
  ];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Gestión Archivística</Text>
      <FlatList
        data={docs}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.docCard}>
            <View style={styles.docInfo}>
              <Text style={styles.docIcon}>📄</Text>
              <View>
                <Text style={styles.docName}>{item.name}</Text>
                <Text style={styles.docSub}>{item.type} | {item.date}</Text>
              </View>
            </View>
            <Text style={styles.downloadIcon}>⬇️</Text>
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6' },
  title: { fontSize: 22, fontWeight: 'bold', margin: 20 },
  docCard: { marginBottom: 12, padding: 15, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  docInfo: { flexDirection: 'row', alignItems: 'center' },
  docIcon: { fontSize: 24, marginRight: 15 },
  docName: { fontWeight: 'bold', color: '#1e3a8a' },
  docSub: { fontSize: 11, color: '#64748b', marginTop: 3 },
  downloadIcon: { fontSize: 18 }
});
