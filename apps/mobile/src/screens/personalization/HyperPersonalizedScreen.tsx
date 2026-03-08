import React from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';
import { Card } from '../../components/Card';

export const HyperPersonalizedScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Tu Identidad Turística Global</Text>
        <Text style={styles.subtitle}>Perfil único para el ecosistema SARITA</Text>
      </View>

      <Card style={styles.idCard}>
        <View style={styles.row}>
          <Image source={{ uri: 'https://via.placeholder.com/60' }} style={styles.avatar} />
          <View style={styles.userInfo}>
            <Text style={styles.userName}>Andrés Viajero</Text>
            <Text style={styles.userLevel}>Nivel: NOMAD LEGEND</Text>
          </View>
        </View>
        <View style={styles.divider} />
        <Text style={styles.prefLabel}>Preferencias Hiper-personalizadas:</Text>
        <Text style={styles.prefTags}>#Ecoturismo #Safari #GastronomíaLlanera #SinFricción</Text>
      </Card>

      <Text style={styles.sectionTitle}>Sugerencias Exclusivas para ti</Text>
      <Card style={styles.suggestionCard}>
        <Text style={styles.suggTitle}>Expedición Secreta al Río Yucao</Text>
        <Text style={styles.suggReason}>Basado en tu pasión por el Safari y tu presupuesto actual.</Text>
      </Card>

      <Card style={styles.suggestionCard}>
        <Text style={styles.suggTitle}>Cena Privada en la Altillanura</Text>
        <Text style={styles.suggReason}>Perfecto para tu horario habitual de cena y gustos gastronómicos.</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { padding: 30, backgroundColor: '#0f172a' },
  title: { fontSize: 22, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: 'rgba(255,255,255,0.6)', fontSize: 13, marginTop: 5 },
  idCard: { margin: 20, padding: 20, backgroundColor: '#f8fafc', borderLeftWidth: 5, borderColor: '#3b82f6' },
  row: { flexDirection: 'row', alignItems: 'center' },
  avatar: { width: 60, height: 60, borderRadius: 30 },
  userInfo: { marginLeft: 15 },
  userName: { fontSize: 18, fontWeight: 'bold' },
  userLevel: { color: '#3b82f6', fontSize: 12, fontWeight: 'bold', marginTop: 3 },
  divider: { height: 1, backgroundColor: '#e2e8f0', marginVertical: 15 },
  prefLabel: { fontSize: 12, fontWeight: 'bold', color: '#64748b' },
  prefTags: { fontSize: 12, color: '#1e293b', marginTop: 5 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginHorizontal: 20, marginTop: 10, marginBottom: 15 },
  suggestionCard: { marginHorizontal: 20, marginBottom: 12, padding: 20 },
  suggTitle: { fontWeight: 'bold', fontSize: 16, color: '#1e3a8a' },
  suggReason: { fontSize: 12, color: '#64748b', marginTop: 5 }
});
