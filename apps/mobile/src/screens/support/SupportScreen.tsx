import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const SupportScreen = () => (
  <ScrollView style={styles.container}>
    <Text style={styles.title}>Centro de Ayuda</Text>

    <Card style={styles.card}>
      <Text style={styles.faqTitle}>¿Cómo cancelo una reserva?</Text>
      <Text style={styles.faqText}>Puedes hacerlo desde el detalle de la reserva hasta 24 horas antes del tour.</Text>
    </Card>

    <Card style={styles.card}>
      <Text style={styles.faqTitle}>Métodos de pago aceptados</Text>
      <Text style={styles.faqText}>Aceptamos tarjetas de crédito, débito y pagos vía PSE.</Text>
    </Card>

    <Button title="Contactar Soporte en Vivo" onPress={() => {}} style={styles.btn} />
  </ScrollView>
);

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  card: { marginBottom: 15, padding: 15 },
  faqTitle: { fontWeight: 'bold', color: '#111827' },
  faqText: { color: '#4b5563', marginTop: 5 },
  btn: { marginTop: 20, backgroundColor: '#4b5563' }
});
