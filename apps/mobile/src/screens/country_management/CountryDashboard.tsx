import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const CountryDashboard = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Panel Nacional de Turismo</Text>

      <Card style={styles.summaryCard}>
        <Text style={styles.label}>Flujo de Visitantes Nacionales</Text>
        <Text style={styles.value}>842,500</Text>
      </Card>

      <Text style={styles.sectionTitle}>Motor de Equilibrio Turístico</Text>
      <Card style={styles.balanceCard}>
        <Text style={styles.balanceTitle}>Control de Saturación: ACTIVADO</Text>
        <Text style={styles.balanceText}>Se están redistribuyendo flujos de Caño Cristales hacia destinos emergentes en el Guaviare para proteger el ecosistema.</Text>
        <View style={styles.progressBar}><View style={[styles.progress, { width: '65%' }]} /></View>
        <Text style={styles.progressLabel}>Carga de Destinos Principales: 65%</Text>
      </Card>

      <Text style={styles.sectionTitle}>Acciones Gubernamentales</Text>
      <Button title="Promover Destinos Emergentes" onPress={() => {}} style={styles.govBtn} />
      <Button title="Ver Reporte Sostenibilidad País" onPress={() => {}} style={[styles.govBtn, { backgroundColor: '#065f46' }]} />

      <Text style={styles.sectionTitle}>Colaboración Global (Fase 08)</Text>
      <Card style={styles.collabCard}>
        <Text style={styles.collabText}>✓ Sincronización con Red Global SARITA</Text>
        <Text style={styles.collabText}>✓ Intercambio de Datos Open Data Activo</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f8fafc', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  summaryCard: { padding: 25, backgroundColor: '#1e3a8a', alignItems: 'center' },
  label: { color: 'rgba(255,255,255,0.7)', fontSize: 14 },
  value: { color: '#fff', fontSize: 36, fontWeight: 'bold', marginTop: 10 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  balanceCard: { padding: 20 },
  balanceTitle: { fontWeight: 'bold', color: '#f59e0b', marginBottom: 10 },
  balanceText: { color: '#475569', lineHeight: 20 },
  progressBar: { height: 8, backgroundColor: '#e2e8f0', borderRadius: 4, marginTop: 15 },
  progress: { height: '100%', backgroundColor: '#f59e0b', borderRadius: 4 },
  progressLabel: { fontSize: 10, color: '#94a3b8', marginTop: 5, textAlign: 'right' },
  govBtn: { marginTop: 10, backgroundColor: '#334155' },
  collabCard: { padding: 15, backgroundColor: '#f1f5f9' },
  collabText: { fontSize: 12, color: '#1e3a8a', marginBottom: 5, fontWeight: 'bold' }
});
