import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, FlatList, Image } from 'react-native';
import { aiService } from '../services/aiService';
import { Card } from '../components/Card';
import { useNavigation } from '@react-navigation/native';

export const HomeScreen = () => {
  const [recommendations, setRecommendations] = useState<any[]>([]);
  const navigation = useNavigation<any>();

  useEffect(() => {
    const fetchHomeData = async () => {
      const recs = await aiService.getRecommendations();
      setRecommendations(recs);
    };
    fetchHomeData();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.welcome}>¡Hola, Viajero!</Text>
        <Text style={styles.subtitle}>Explora lo mejor de Puerto Gaitán</Text>
      </View>

      <Text style={styles.sectionTitle}>Recomendado por IA SARITA</Text>
      <FlatList
        horizontal
        data={recommendations}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.recCard}>
            <Image source={{ uri: 'https://via.placeholder.com/150' }} style={styles.recImage} />
            <Text style={styles.recName} numberOfLines={1}>{item.name}</Text>
            <Text style={styles.recScore}>★ {Math.round(item.score * 100)}% Coincidencia</Text>
          </Card>
        )}
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={{ paddingLeft: 20 }}
      />

      <View style={styles.promoBanner}>
        <Text style={styles.promoText}>Nuevas Experiencias en el Río Manacacías</Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { padding: 30, backgroundColor: '#1e3a8a' },
  welcome: { fontSize: 28, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: 'rgba(255,255,255,0.8)', fontSize: 16 },
  sectionTitle: { fontSize: 20, fontWeight: 'bold', margin: 20 },
  recCard: { width: 160, marginRight: 15, padding: 10 },
  recImage: { width: '100%', height: 100, borderRadius: 8 },
  recName: { fontWeight: 'bold', marginTop: 10 },
  recScore: { fontSize: 12, color: '#10b981', marginTop: 2 },
  promoBanner: { margin: 20, padding: 30, backgroundColor: '#f59e0b', borderRadius: 15 },
  promoText: { color: '#fff', fontSize: 18, fontWeight: 'bold', textAlign: 'center' }
});
