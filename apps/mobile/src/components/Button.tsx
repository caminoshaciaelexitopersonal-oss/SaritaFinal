import React from 'react';
import { TouchableOpacity, Text, StyleSheet, ActivityIndicator } from 'react-native';

export const Button = ({ title, onPress, loading, style }: any) => (
  <TouchableOpacity style={[styles.button, style]} onPress={onPress} disabled={loading}>
    {loading ? <ActivityIndicator color="#fff" /> : <Text style={styles.text}>{title}</Text>}
  </TouchableOpacity>
);

const styles = StyleSheet.create({
  button: { backgroundColor: '#1e3a8a', padding: 15, borderRadius: 8, alignItems: 'center' },
  text: { color: '#fff', fontWeight: 'bold', fontSize: 16 }
});
