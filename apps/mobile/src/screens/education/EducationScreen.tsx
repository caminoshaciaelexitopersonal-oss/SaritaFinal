import React from 'react';
import { View, Text, StyleSheet, ScrollView, Image } from 'react-native';
import { Card } from '../../components/Card';

export const EducationScreen = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Aula Turística SARITA</Text>
      <Text style={styles.subtitle}>Aprende sobre la biodiversidad y cultura de tus destinos.</Text>

      <Card style={styles.eduCard}>
        <Image source={{ uri: 'https://via.placeholder.com/300x150' }} style={styles.image} />
        <Text style={styles.eduTitle}>Los Tres Ríos de Puerto Gaitán</Text>
        <Text style={styles.eduText}>Una guía visual sobre el Meta, Manacacías y Yucao.</Text>
      </Card>

      <Card style={styles.eduCard}>
        <Image source={{ uri: 'https://via.placeholder.com/300x150' }} style={styles.image} />
        <Text style={styles.eduTitle}>Cultura Llanera: El Joropo</Text>
        <Text style={styles.eduText}>Historia, música y tradiciones de la región del Meta.</Text>
      </Card>

      <Card style={styles.eduCard}>
        <Image source={{ uri: 'https://via.placeholder.com/300x150' }} style={styles.image} />
        <Text style={styles.eduTitle}>Sostenibilidad en el Safari</Text>
        <Text style={styles.eduText}>Cómo interactuar de forma responsable con la fauna local.</Text>
      </Card>

      <Text style={styles.sectionTitle}>Global Learning (Fase 08)</Text>
      <Card style={styles.eduCard}>
        <Image source={{ uri: 'https://via.placeholder.com/300x150' }} style={styles.image} />
        <Text style={styles.eduTitle}>Maravillas del Mundo: Historia Global</Text>
        <Text style={styles.eduText}>Explora los patrimonios culturales conectados a la red SARITA.</Text>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', color: '#1e3a8a' },
  subtitle: { color: '#6b7280', marginVertical: 10, fontSize: 14 },
  eduCard: { marginBottom: 20, overflow: 'hidden', padding: 0 },
  image: { width: '100%', height: 150 },
  eduTitle: { fontSize: 18, fontWeight: 'bold', margin: 15, marginBottom: 5 },
  eduText: { marginHorizontal: 15, marginBottom: 15, color: '#4b5563' }
});
