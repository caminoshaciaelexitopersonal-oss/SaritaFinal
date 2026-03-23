import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, Alert } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { autonomousService } from '../../services/autonomousService';

export const AutonomousPlanningScreen = () => {
  const [loading, setLoading] = useState(false);
  const [plan, setPlan] = useState<any>(null);

  const handlePlanning = async () => {
    try {
      setLoading(true);
      const response = await autonomousService.generateAutonomousPlan('region-meta', { target: 'sustainable-growth' });
      setPlan(response.data);
      Alert.alert('Planificación Generada', 'El motor autónomo ha optimizado la infraestructura de la región.');
    } catch (error) {} finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Planificación Regional Autónoma</Text>
      <Text style={styles.subtitle}>SARITA gestiona automáticamente la infraestructura y flujos de tu región.</Text>

      <Button title="Lanzar Algoritmo de Planificación" onPress={handlePlanning} loading={loading} style={styles.planBtn} />

      {plan && (
        <View style={styles.planResults}>
          <Text style={styles.sectionTitle}>Acciones Ejecutadas por el Sistema</Text>
          <Card style={styles.actionCard}>
            <Text style={styles.actionTitle}>1. Distribución de Carga</Text>
            <Text style={styles.actionDesc}>Redireccionamiento del 20% del flujo turístico hacia el puerto alternativo para evitar congestión.</Text>
          </Card>
          <Card style={styles.actionCard}>
            <Text style={styles.actionTitle}>2. Optimización de Energía</Text>
            <Text style={styles.actionDesc}>Ajuste automático de luminarias en rutas turísticas basado en el flujo peatonal simulado.</Text>
          </Card>
          <Card style={styles.actionCard}>
            <Text style={styles.actionTitle}>3. Gestión de Residuos</Text>
            <Text style={styles.actionDesc}>Activación de recolección prioritaria en zonas de alta densidad de viajeros detectadas.</Text>
          </Card>
        </View>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f8fafc', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#1e293b' },
  subtitle: { color: '#64748b', fontSize: 13, marginVertical: 10 },
  planBtn: { marginTop: 20, backgroundColor: '#0f172a' },
  planResults: { marginTop: 30 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginBottom: 20 },
  actionCard: { marginBottom: 15, padding: 20, borderLeftWidth: 4, borderColor: '#3b82f6' },
  actionTitle: { fontWeight: 'bold', fontSize: 16, color: '#1e3a8a' },
  actionDesc: { color: '#475569', marginTop: 5, fontSize: 13 }
});
