import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator, Alert } from 'react-native';
import { orchestrationService } from '../../services/orchestrationService';
import { Button } from '../../components/Button';
import { Input } from '../../components/Input';
import { Card } from '../../components/Card';

export const TravelOrchestratorScreen = () => {
  const [destination, setDestination] = useState('Meta, Colombia');
  const [days, setDays] = useState('3');
  const [budget, setBudget] = useState('500000');
  const [loading, setLoading] = useState(false);
  const [itinerary, setItinerary] = useState<any>(null);

  const handleOrchestration = async () => {
    try {
      setLoading(true);
      const response = await orchestrationService.orchestrateTrip(destination, parseInt(days), parseInt(budget));
      setItinerary(response.data);
      Alert.alert('¡Viaje Orquestado!', 'Hemos reservado automáticamente los mejores servicios para ti.');
    } catch (error) {
      Alert.alert('Error', 'No se pudo generar el itinerario autónomo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Orquestador de Viajes Autónomo</Text>
      <Text style={styles.subtitle}>Define tu destino y presupuesto, SARITA hace el resto.</Text>

      <Card style={styles.formCard}>
        <Text style={styles.label}>Destino</Text>
        <Input value={destination} onChangeText={setDestination} />

        <View style={styles.row}>
          <View style={{ flex: 1, marginRight: 10 }}>
            <Text style={styles.label}>Días</Text>
            <Input value={days} onChangeText={setDays} keyboardType="numeric" />
          </View>
          <View style={{ flex: 1 }}>
            <Text style={styles.label}>Presupuesto (COP)</Text>
            <Input value={budget} onChangeText={setBudget} keyboardType="numeric" />
          </View>
        </View>

        <Button title="Orquestar mi Viaje" onPress={handleOrchestration} loading={loading} style={styles.btn} />
      </Card>

      {itinerary && (
        <View style={styles.itineraryResult}>
          <Text style={styles.sectionTitle}>Tu Itinerario Inteligente</Text>
          {itinerary.steps?.map((step: any, index: number) => (
            <Card key={index} style={styles.stepCard}>
              <Text style={styles.stepTime}>{step.time}</Text>
              <Text style={styles.stepTitle}>{step.activity}</Text>
              <Text style={styles.stepStatus}>Estado: Reservado ✓</Text>
            </Card>
          ))}
        </View>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', color: '#1e3a8a', marginBottom: 5 },
  subtitle: { fontSize: 14, color: '#6b7280', marginBottom: 20 },
  formCard: { padding: 20 },
  label: { fontSize: 12, color: '#9ca3af', marginBottom: 5, fontWeight: 'bold' },
  row: { flexDirection: 'row' },
  btn: { marginTop: 10, backgroundColor: '#1e3a8a' },
  itineraryResult: { marginTop: 30 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginBottom: 15 },
  stepCard: { marginBottom: 10, borderLeftWidth: 4, borderColor: '#10b981', padding: 15 },
  stepTime: { fontSize: 12, color: '#1e3a8a', fontWeight: 'bold' },
  stepTitle: { fontSize: 16, fontWeight: '600', marginVertical: 5 },
  stepStatus: { fontSize: 12, color: '#10b981', fontWeight: 'bold' }
});
