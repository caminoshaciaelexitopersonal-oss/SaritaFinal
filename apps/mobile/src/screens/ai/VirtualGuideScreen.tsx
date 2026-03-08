import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, Image, TouchableOpacity } from 'react-native';
import { Button } from '../../components/Button';

export const VirtualGuideScreen = () => {
  const [isNarrating, setIsNarrating] = useState(false);

  return (
    <View style={styles.container}>
      <Image source={{ uri: 'https://via.placeholder.com/600x300' }} style={styles.placeImage} />

      <ScrollView style={styles.content}>
        <Text style={styles.placeName}>Muelle de Puerto Gaitán</Text>
        <View style={styles.aiBadge}><Text style={styles.aiText}>GUÍA IA ACTIVADO</Text></View>

        <Text style={styles.description}>
          "El muelle de Puerto Gaitán es el corazón comercial y turístico de la región. Desde aquí parten las expediciones hacia el Safari de los Llanos Orientales..."
        </Text>

        <TouchableOpacity
          style={[styles.narrateBtn, isNarrating && styles.activeBtn]}
          onPress={() => setIsNarrating(!isNarrating)}
        >
          <Text style={styles.btnText}>{isNarrating ? '⏹ Detener Narración' : '▶ Escuchar Historia'}</Text>
        </TouchableOpacity>

        <Text style={styles.sectionTitle}>Curiosidades Locales</Text>
        <Card style={styles.factCard}>
          <Text style={styles.factText}>¿Sabías que aquí se encuentran tres grandes ríos: Meta, Manacacías y Yucao?</Text>
        </Card>
      </ScrollView>
    </View>
  );
};

import { Card } from '../../components/Card';

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  placeImage: { width: '100%', height: 250 },
  content: { padding: 20 },
  placeName: { fontSize: 24, fontWeight: 'bold' },
  aiBadge: { backgroundColor: '#1e3a8a', paddingHorizontal: 10, paddingVertical: 5, borderRadius: 5, alignSelf: 'flex-start', marginVertical: 10 },
  aiText: { color: '#fff', fontSize: 10, fontWeight: 'bold' },
  description: { fontSize: 16, lineHeight: 24, color: '#4b5563', marginVertical: 15 },
  narrateBtn: { backgroundColor: '#f59e0b', padding: 15, borderRadius: 10, alignItems: 'center' },
  activeBtn: { backgroundColor: '#ef4444' },
  btnText: { color: '#fff', fontWeight: 'bold' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginTop: 30, marginBottom: 15 },
  factCard: { padding: 15 },
  factText: { fontStyle: 'italic', color: '#374151' }
});
