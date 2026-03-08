import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { orchestrationService } from '../../services/orchestrationService';
import { Card } from '../../components/Card';
import * as Location from 'expo-location';

export const ContextualExperiencesScreen = () => {
  const [experiences, setExperiences] = useState<any[]>([]);

  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status === 'granted') {
        const loc = await Location.getCurrentPositionAsync({});
        const response = await orchestrationService.getContextualRecommendations(loc.coords.latitude, loc.coords.longitude);
        setExperiences(response.data || []);
      }
    })();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Experiencias Cerca de Ti</Text>
      <Text style={styles.subtitle}>Basado en tu ubicación, hora y clima actual.</Text>

      <FlatList
        data={experiences}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <Card style={styles.expCard}>
            <Text style={styles.expTitle}>{item.name}</Text>
            <Text style={styles.expContext}>{item.context_reason}</Text>
            <Text style={styles.expDist}>A {item.distance} metros</Text>
          </Card>
        )}
        ListEmptyComponent={<Text style={styles.empty}>Buscando mejores experiencias para ti...</Text>}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', marginHorizontal: 20, marginTop: 30 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20 },
  expCard: { marginBottom: 15, padding: 20, borderLeftWidth: 5, borderColor: '#f59e0b' },
  expTitle: { fontSize: 18, fontWeight: 'bold' },
  expContext: { color: '#1e3a8a', fontSize: 12, marginVertical: 5, fontWeight: '600' },
  expDist: { fontSize: 10, color: '#9ca3af' },
  empty: { textAlign: 'center', marginTop: 50, color: '#9ca3af' }
});
