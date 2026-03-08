import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, Image, TouchableOpacity, TextInput } from 'react-native';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';

export const CommunityScreen = () => {
  const [posts] = useState([
    { id: '1', user: 'Laura Viajera', content: 'Acabo de llegar al muelle de Puerto Gaitán, ¡el clima está increíble!', likes: 12, comments: 3 },
    { id: '2', user: 'Carlos Explorador', content: '¿Alguien para compartir tour de pesca mañana temprano?', likes: 8, comments: 5 },
  ]);

  return (
    <View style={styles.container}>
      <View style={styles.postBox}>
        <TextInput placeholder="¿Qué quieres compartir con la comunidad?" multiline style={styles.input} />
        <Button title="Publicar" onPress={() => {}} style={styles.postBtn} />
      </View>

      <FlatList
        data={posts}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.postCard}>
            <View style={styles.header}>
              <View style={styles.avatarPlaceholder} />
              <Text style={styles.userName}>{item.user}</Text>
            </View>
            <Text style={styles.content}>{item.content}</Text>
            <View style={styles.footer}>
              <Text style={styles.actionText}>❤️ {item.likes} Me gusta</Text>
              <Text style={styles.actionText}>💬 {item.comments} Comentarios</Text>
            </View>
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6' },
  postBox: { padding: 20, backgroundColor: '#fff', borderBottomWidth: 1, borderColor: '#e5e7eb' },
  input: { backgroundColor: '#f9fafb', borderRadius: 10, padding: 15, height: 80, textAlignVertical: 'top' },
  postBtn: { marginTop: 10, alignSelf: 'flex-end', paddingHorizontal: 20 },
  postCard: { marginBottom: 15, padding: 15 },
  header: { flexDirection: 'row', alignItems: 'center', marginBottom: 10 },
  avatarPlaceholder: { width: 30, height: 30, borderRadius: 15, backgroundColor: '#1e3a8a', marginRight: 10 },
  userName: { fontWeight: 'bold' },
  content: { color: '#374151', lineHeight: 20 },
  footer: { flexDirection: 'row', marginTop: 15, borderTopWidth: 1, borderColor: '#f3f4f6', paddingTop: 10 },
  actionText: { marginRight: 20, fontSize: 12, color: '#6b7280' }
});
