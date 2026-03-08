import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, TextInput, KeyboardAvoidingView, Platform } from 'react-native';
import { aiService } from '../../services/aiService';
import { Button } from '../../components/Button';
import { Card } from '../../components/Card';
import { useNavigation } from '@react-navigation/native';

export const AISearchScreen = () => {
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const navigation = useNavigation<any>();

  const handleSearch = async () => {
    if (!query.trim()) return;
    setLoading(true);
    const results = await aiService.askAssistant(query);
    setSuggestions(results);
    setLoading(false);
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      keyboardVerticalOffset={100}
    >
      <View style={styles.header}>
        <Text style={styles.title}>Agente Turístico IA</Text>
        <Text style={styles.subtitle}>Dime qué experiencia buscas y te la encontraré.</Text>
      </View>

      <FlatList
        data={suggestions}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity onPress={() => navigation.navigate('TourDetail', { id: item.tour_id })}>
            <Card style={styles.suggestionCard}>
              <Text style={styles.tourName}>{item.name}</Text>
              <Text style={styles.matchText}>✓ Recomendado para ti</Text>
            </Card>
          </TouchableOpacity>
        )}
        contentContainerStyle={{ padding: 20 }}
        ListEmptyComponent={!loading ? <Text style={styles.empty}>Prueba con: "Quiero un tour de cascadas en Meta"</Text> : null}
      />

      <View style={styles.inputArea}>
        <TextInput
          style={styles.input}
          value={query}
          onChangeText={setQuery}
          placeholder="¿A dónde vamos hoy?"
        />
        <Button title="Consultar" onPress={handleSearch} loading={loading} style={styles.btn} />
      </View>
    </KeyboardAvoidingView>
  );
};

// Importar TouchableOpacity para los items
import { TouchableOpacity } from 'react-native';

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { padding: 30, backgroundColor: '#1e3a8a' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#fff' },
  subtitle: { color: 'rgba(255,255,255,0.8)', fontSize: 14, marginTop: 5 },
  suggestionCard: { marginBottom: 15, padding: 20, borderLeftWidth: 4, borderColor: '#f59e0b' },
  tourName: { fontSize: 18, fontWeight: 'bold' },
  matchText: { color: '#10b981', fontSize: 12, marginTop: 5 },
  empty: { textAlign: 'center', marginTop: 50, color: '#9ca3af' },
  inputArea: { flexDirection: 'row', padding: 20, borderTopWidth: 1, borderColor: '#e5e7eb', alignItems: 'center' },
  input: { flex: 1, height: 45, backgroundColor: '#f3f4f6', borderRadius: 25, paddingHorizontal: 20, marginRight: 10 },
  btn: { paddingVertical: 10, paddingHorizontal: 20 }
});
