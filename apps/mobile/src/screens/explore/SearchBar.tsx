import React from 'react';
import { View, TextInput, StyleSheet } from 'react-native';

export const SearchBar = ({ value, onChangeText }: any) => (
  <View style={styles.container}>
    <TextInput
      style={styles.input}
      placeholder="Buscar tours, destinos..."
      value={value}
      onChangeText={onChangeText}
    />
  </View>
);

const styles = StyleSheet.create({
  container: { padding: 15, backgroundColor: '#fff' },
  input: { backgroundColor: '#f3f4f6', borderRadius: 25, paddingHorizontal: 20, paddingVertical: 12, fontSize: 16 }
});
