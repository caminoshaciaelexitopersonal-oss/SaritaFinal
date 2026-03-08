import React, { useState } from 'react';
import { View, Text, StyleSheet, Alert } from 'react-native';
import { useRoute, useNavigation } from '@react-navigation/native';
import { api } from '../../services/api';
import { Button } from '../../components/Button';
import { Input } from '../../components/Input';

export const ReviewScreen = () => {
  const route = useRoute<any>();
  const navigation = useNavigation<any>();
  const [rating, setRating] = useState('5');
  const [comment, setComment] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    try {
      setLoading(true);
      await api.post('/reviews/', {
        tour_id: route.params.tourId,
        rating: parseInt(rating),
        comment: comment
      });
      Alert.alert('¡Gracias!', 'Tu opinión nos ayuda a mejorar.');
      navigation.goBack();
    } catch (error) {
      Alert.alert('Error', 'No se pudo enviar la reseña.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Califica tu Experiencia</Text>
      <Text style={styles.label}>Puntuación (1-5)</Text>
      <Input value={rating} onChangeText={setRating} keyboardType="numeric" />
      <Text style={styles.label}>Comentario</Text>
      <Input
        value={comment}
        onChangeText={setComment}
        multiline
        numberOfLines={4}
        style={styles.textArea}
      />
      <Button title="Enviar Reseña" onPress={handleSubmit} loading={loading} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#fff' },
  title: { fontSize: 20, fontWeight: 'bold', marginBottom: 20 },
  label: { fontSize: 14, color: '#4b5563', marginBottom: 5 },
  textArea: { height: 100, textAlignVertical: 'top' }
});
