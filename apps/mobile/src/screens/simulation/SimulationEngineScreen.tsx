import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const SimulationEngineScreen = () => {
  const [scenario, setScenario] = useState('none');

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Motor de Simulación Turística</Text>
      <Text style={styles.subtitle}>Prueba escenarios futuros y mide el impacto en el destino.</Text>

      <Text style={styles.label}>Selecciona Escenario a Simular:</Text>
      <TouchableOpacity onPress={() => setScenario('airport')} style={[styles.option, scenario === 'airport' && styles.activeOption]}>
        <Text style={[styles.optionText, scenario === 'airport' && styles.activeText]}>Nuevo Aeropuerto Regional (+50% flujo)</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={() => setScenario('festival')} style={[styles.option, scenario === 'festival' && styles.activeOption]}>
        <Text style={[styles.optionText, scenario === 'festival' && styles.activeText]}>Festival Internacional (3 días masivos)</Text>
      </TouchableOpacity>

      <Button title="Correr Simulación en Cloud AWS" onPress={() => {}} style={styles.runBtn} />

      {scenario !== 'none' && (
        <View style={styles.results}>
          <Text style={styles.sectionTitle}>Resultados de la Simulación</Text>
          <Card style={styles.resCard}>
            <Text style={styles.resTitle}>Alerta: Saturación de Hospedaje</Text>
            <Text style={styles.resDesc}>Se requiere incrementar la oferta hotelera en un 25% antes del despliegue.</Text>
          </Card>
          <Card style={styles.resCard}>
            <Text style={styles.resTitle}>Riesgo Ambiental: Alto</Text>
            <Text style={styles.resDesc}>La huella de carbono regional aumentará un 18%. Se recomiendan medidas de compensación.</Text>
          </Card>
        </View>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fdf4ff', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#701a75' },
  subtitle: { color: '#a21caf', fontSize: 13, marginVertical: 10 },
  label: { fontWeight: 'bold', marginTop: 20, marginBottom: 15, color: '#4a044e' },
  option: { padding: 20, backgroundColor: '#fff', borderRadius: 10, marginBottom: 10, borderWidth: 1, borderColor: '#d8b4fe' },
  activeOption: { backgroundColor: '#701a75', borderColor: '#701a75' },
  optionText: { color: '#701a75', fontWeight: '600' },
  activeText: { color: '#fff' },
  runBtn: { marginTop: 20, backgroundColor: '#701a75' },
  results: { marginTop: 30 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#701a75', marginBottom: 15 },
  resCard: { marginBottom: 12, padding: 20, borderLeftWidth: 5, borderColor: '#ef4444' },
  resTitle: { fontWeight: 'bold', fontSize: 16, color: '#991b1b' },
  resDesc: { color: '#4b5563', marginTop: 5, fontSize: 13 }
});
