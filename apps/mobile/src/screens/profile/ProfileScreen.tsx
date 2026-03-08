import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, Image, ScrollView, TouchableOpacity } from 'react-native';
import { useAuth } from '../../context/AuthContext';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { orchestrationService } from '../../services/orchestrationService';

/**
 * Identidad Digital del Viajero (Fase 07.2)
 * Perfil global que unifica historial, preferencias y nivel.
 */

export const ProfileScreen = () => {
  const { user, signOut } = useAuth();
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await orchestrationService.getTravelerProfile();
        setProfile(response.data);
      } catch (error) {
        setProfile({
          level: 'Adventurer',
          trips_completed: 14,
          total_points: 2450,
          preferences: ['Naturaleza', 'Aventura', 'Fotografía']
        });
      }
    };
    fetchProfile();
  }, []);

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Image source={{ uri: 'https://via.placeholder.com/120' }} style={styles.avatar} />
        <Text style={styles.name}>{user?.first_name} {user?.last_name}</Text>
        <View style={styles.levelBadge}>
          <Text style={styles.levelText}>{profile?.level?.toUpperCase() || 'EXPLORER'}</Text>
        </View>
      </View>

      <View style={styles.statsRow}>
        <View style={styles.statBox}>
          <Text style={styles.statVal}>{profile?.trips_completed || 0}</Text>
          <Text style={styles.statLab}>Viajes</Text>
        </View>
        <View style={styles.statBox}>
          <Text style={styles.statVal}>{profile?.total_points || 0}</Text>
          <Text style={styles.statLab}>Puntos</Text>
        </View>
        <View style={styles.statBox}>
          <Text style={styles.statVal}>4.8</Text>
          <Text style={styles.statLab}>Rating</Text>
        </View>
      </View>

      <Text style={styles.sectionTitle}>Preferencias de Viaje</Text>
      <View style={styles.tagContainer}>
        {profile?.preferences?.map((p: string) => (
          <View key={p} style={styles.tag}><Text style={styles.tagText}>{p}</Text></View>
        ))}
      </View>

      <Text style={styles.sectionTitle}>Mi Pasaporte Digital</Text>
      <Card style={styles.passportCard}>
        <Text style={styles.passportText}>Has desbloqueado 4 sellos en el Meta.</Text>
        <TouchableOpacity><Text style={styles.linkText}>Ver sellos y logros →</Text></TouchableOpacity>
      </Card>

      <Button title="Cerrar Sesión" onPress={signOut} style={styles.logoutBtn} />
      <Text style={styles.version}>SARITA Super App v1.0.0 | Global ID: {user?.id?.substring(0,8)}</Text>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { alignItems: 'center', padding: 30, backgroundColor: '#f8fafc' },
  avatar: { width: 100, height: 100, borderRadius: 50, marginBottom: 15, borderWidth: 3, borderColor: '#1e3a8a' },
  name: { fontSize: 22, fontWeight: 'bold', color: '#1e293b' },
  levelBadge: { backgroundColor: '#f59e0b', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20, marginTop: 10 },
  levelText: { color: '#fff', fontSize: 12, fontWeight: 'bold' },
  statsRow: { flexDirection: 'row', justifyContent: 'space-around', padding: 20, borderBottomWidth: 1, borderColor: '#f1f5f9' },
  statBox: { alignItems: 'center' },
  statVal: { fontSize: 20, fontWeight: 'bold', color: '#1e3a8a' },
  statLab: { fontSize: 12, color: '#64748b', marginTop: 3 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', margin: 20, marginBottom: 10 },
  tagContainer: { flexDirection: 'row', flexWrap: 'wrap', paddingHorizontal: 20 },
  tag: { backgroundColor: '#e2e8f0', paddingHorizontal: 12, paddingVertical: 6, borderRadius: 15, marginRight: 8, marginBottom: 8 },
  tagText: { fontSize: 12, color: '#475569' },
  passportCard: { marginHorizontal: 20, padding: 20, backgroundColor: '#1e3a8a' },
  passportText: { color: '#fff', fontWeight: '600' },
  linkText: { color: '#f59e0b', marginTop: 10, fontWeight: 'bold' },
  logoutBtn: { margin: 20, backgroundColor: '#ef4444', marginTop: 40 },
  version: { textAlign: 'center', fontSize: 10, color: '#94a3b8', marginBottom: 30 }
});
