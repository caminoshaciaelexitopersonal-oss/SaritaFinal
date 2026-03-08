import React from 'react';
import { View, Text, StyleSheet, FlatList, Image } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const ExtensionsMarketplaceScreen = () => {
  const extensions = [
    { id: '1', name: 'Gestor Hotelero Pro', provider: 'Hotelex', description: 'Sincroniza tus reservas de SARITA con tu PMS.' },
    { id: '2', name: 'Traductor en Vivo', provider: 'PolyGlot', description: 'Traducción simultánea para guías y turistas.' },
  ];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Marketplace de Extensiones</Text>
      <Text style={styles.subtitle}>Potencia tu negocio turístico con herramientas de terceros.</Text>

      <FlatList
        data={extensions}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.extCard}>
            <View style={styles.header}>
              <Text style={styles.name}>{item.name}</Text>
              <Text style={styles.provider}>por {item.provider}</Text>
            </View>
            <Text style={styles.desc}>{item.description}</Text>
            <Button title="Instalar Extensión" onPress={() => {}} style={styles.btn} />
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  title: { fontSize: 22, fontWeight: 'bold', marginTop: 30, marginHorizontal: 20 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20 },
  extCard: { marginBottom: 15, padding: 20 },
  header: { marginBottom: 10 },
  name: { fontSize: 18, fontWeight: 'bold', color: '#1e3a8a' },
  provider: { fontSize: 12, color: '#9ca3af' },
  desc: { color: '#4b5563', marginBottom: 20 },
  btn: { backgroundColor: '#4b5563' }
});
