import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, Share, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { api } from '../../services/api';
import { Button } from '../../components/Button';

export const LoyaltyScreen = () => {
  const [loyalty, setLoyalty] = useState<any>({ points: 0, level: 'Explorer' });

  useEffect(() => {
    const fetchLoyalty = async () => {
      try {
        const response = await api.get('/loyalty/');
        setLoyalty(response.data);
      } catch (error) {}
    };
    fetchLoyalty();
  }, []);

  const handleShare = async () => {
    try {
      await Share.share({
        message: '¡Únete a SARITA y explora Puerto Gaitán! Usa mi código REF-2026 para ganar puntos.',
      });
      await api.post('/referrals/', { action: 'shared' });
    } catch (error) {}
  };

  return (
    <View style={styles.container}>
      <Card style={styles.pointsCard}>
        <Text style={styles.pointsLabel}>Tus Puntos SARITA</Text>
        <Text style={styles.pointsValue}>{loyalty.points}</Text>
        <View style={styles.levelBadge}>
          <Text style={styles.levelText}>{loyalty.level.toUpperCase()}</Text>
        </View>
      </Card>

      <Text style={styles.sectionTitle}>Programa de Referidos</Text>
      <Card style={styles.referralCard}>
        <Text style={styles.referralTitle}>Gana 100 puntos por cada amigo</Text>
        <Text style={styles.referralText}>Comparte tu código y ambos recibirán beneficios exclusivos en su próxima reserva.</Text>
        <Button title="Compartir Código" onPress={handleShare} style={styles.shareBtn} />
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 20 },
  pointsCard: { padding: 30, alignItems: 'center', backgroundColor: '#1e3a8a' },
  pointsLabel: { color: 'rgba(255,255,255,0.7)', fontSize: 16 },
  pointsValue: { color: '#fff', fontSize: 48, fontWeight: 'bold', marginVertical: 10 },
  levelBadge: { backgroundColor: '#f59e0b', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 20 },
  levelText: { color: '#fff', fontSize: 12, fontWeight: 'bold' },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', marginVertical: 20 },
  referralCard: { padding: 20 },
  referralTitle: { fontWeight: 'bold', fontSize: 16, marginBottom: 10 },
  referralText: { color: '#6b7280', lineHeight: 20, marginBottom: 20 },
  shareBtn: { backgroundColor: '#10b981' }
});
