import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, FlatList, Image } from 'react-native';
import { aiService } from '../services/aiService';
import { Card } from '../components/Card';
import { useNavigation } from '@react-navigation/native';

const RecommendationItem = React.memo(({ item }: { item: any }) => (
  <Card style={styles.recCard}>
    <Image
      source={{ uri: item.image_url || 'https://via.placeholder.com/150' }}
      style={styles.recImage}
      resizeMode="cover"
    />
    <Text style={styles.recName} numberOfLines={1}>{item.name}</Text>
    <Text style={styles.recScore}>★ {Math.round(item.score * 100)}% Coincidencia</Text>
  </Card>
));

export const HomeScreen = () => {
  const [recommendations, setRecommendations] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const navigation = useNavigation<any>();

  useEffect(() => {
    const fetchHomeData = async () => {
      try {
        const recs = await aiService.getRecommendations();
        setRecommendations(recs);
      } finally {
        setLoading(false);
      }
    };
    fetchHomeData();
  }, []);

  const renderRecommendation = React.useCallback(({ item }: { item: any }) => (
    <RecommendationItem item={item} />
  ), []);

  if (loading) {
    return (
      <View style={styles.container}>
        <View style={styles.header}>
          <View style={[styles.skeleton, { width: '60%', height: 30 }]} />
          <View style={[styles.skeleton, { width: '40%', height: 20, marginTop: 10, opacity: 0.5 }]} />
        </View>
        <Text style={styles.sectionTitle}>Recomendado por IA SARITA</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={{ paddingLeft: 20 }}>
          {[1, 2, 3].map(i => (
            <View key={i} style={[styles.recCard, styles.skeleton, { height: 160 }]} />
          ))}
        </ScrollView>
      </View>
    );
  }

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
        renderItem={renderRecommendation}
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={{ paddingLeft: 20 }}
        initialNumToRender={5}
        maxToRenderPerBatch={5}
        windowSize={10}
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
  promoText: { color: '#fff', fontSize: 18, fontWeight: 'bold', textAlign: 'center' },
  skeleton: { backgroundColor: '#e5e7eb', borderRadius: 8 },
});
