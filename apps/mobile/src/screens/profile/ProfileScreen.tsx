import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, Alert } from 'react-native';
import { useAuth } from '../../context/AuthContext';
import { Button } from '../../components/Button';
import { Input } from '../../components/Input';
import { api } from '../../services/api';

export const ProfileScreen = () => {
  const { user, signOut } = useAuth();
  const [editing, setEditing] = useState(false);
  const [name, setName] = useState(user?.first_name || '');

  const handleUpdate = async () => {
    try {
      await api.put('/me/', { first_name: name });
      Alert.alert('Éxito', 'Perfil actualizado.');
      setEditing(false);
    } catch (error) {
      Alert.alert('Error', 'No se pudo actualizar el perfil.');
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Image source={{ uri: 'https://via.placeholder.com/100' }} style={styles.avatar} />
        <Text style={styles.email}>{user?.email}</Text>
      </View>

      <View style={styles.content}>
        <Text style={styles.label}>Nombre</Text>
        <Input
          value={name}
          onChangeText={setName}
          editable={editing}
        />

        {editing ? (
          <Button title="Guardar Cambios" onPress={handleUpdate} style={styles.saveBtn} />
        ) : (
          <Button title="Editar Perfil" onPress={() => setEditing(true)} style={styles.editBtn} />
        )}

        <Button
          title="Cerrar Sesión"
          onPress={signOut}
          style={styles.logoutBtn}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { alignItems: 'center', padding: 40, backgroundColor: '#f9fafb' },
  avatar: { width: 100, height: 100, borderRadius: 50, marginBottom: 15 },
  email: { fontSize: 16, color: '#6b7280' },
  content: { padding: 20 },
  label: { fontSize: 14, color: '#4b5563', marginBottom: 5 },
  editBtn: { backgroundColor: '#4b5563', marginTop: 20 },
  saveBtn: { backgroundColor: '#10b981', marginTop: 20 },
  logoutBtn: { backgroundColor: '#ef4444', marginTop: 50 },
});
