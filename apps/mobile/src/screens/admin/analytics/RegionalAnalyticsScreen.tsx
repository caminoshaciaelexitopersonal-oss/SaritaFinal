import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

export const RegionalAnalyticsScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Analítica Territorial</Text>
      <Text style={styles.subtitle}>Impacto regional en tiempo real</Text>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Ocupación Hotelera</Text>
        <View style={styles.chartPlaceholder}>
          <Text>Gráfico de Ocupación</Text>
        </View>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Flujo Turístico</Text>
        <View style={styles.chartPlaceholder}>
          <Text>Gráfico de Flujo</Text>
        </View>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Impacto Económico</Text>
        <View style={styles.chartPlaceholder}>
          <Text>Métricas Financieras</Text>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f9f9f9',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 4,
    color: '#1a1a1a',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 24,
  },
  card: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 12,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 12,
  },
  chartPlaceholder: {
    height: 150,
    backgroundColor: '#eee',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  }
});
