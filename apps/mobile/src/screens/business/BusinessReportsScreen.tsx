import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const BusinessReportsScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Reportes de Negocio</Text>

      <Card style={styles.reportCard}>
        <Text style={styles.reportTitle}>Ventas por Categoría</Text>
        <View style={styles.chartPlaceholder}>
          <Text style={styles.chartText}>[ Gráfico de Torta: 60% Safari, 30% Hospedaje, 10% Otros ]</Text>
        </View>
      </Card>

      <Card style={styles.reportCard}>
        <Text style={styles.reportTitle}>Crecimiento de Clientes</Text>
        <View style={styles.chartPlaceholder}>
          <Text style={styles.chartText}>[ Gráfico de Líneas: +12% este mes ]</Text>
        </View>
      </Card>

      <Card style={styles.reportCard}>
        <Text style={styles.reportTitle}>Servicios más Vendidos</Text>
        <Text style={styles.item}>1. Safari Río Meta (45 reservas)</Text>
        <Text style={styles.item}>2. Cabalgata Atardecer (22 reservas)</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  reportCard: { marginBottom: 20, padding: 20 },
  reportTitle: { fontWeight: 'bold', fontSize: 16, marginBottom: 15, color: '#1e3a8a' },
  chartPlaceholder: { height: 150, backgroundColor: '#f8fafc', borderRadius: 10, justifyContent: 'center', alignItems: 'center', borderStyle: 'dashed', borderWidth: 1, borderColor: '#cbd5e1' },
  chartText: { fontSize: 12, color: '#94a3b8', textAlign: 'center' },
  item: { fontSize: 14, color: '#475569', marginBottom: 5 }
});
