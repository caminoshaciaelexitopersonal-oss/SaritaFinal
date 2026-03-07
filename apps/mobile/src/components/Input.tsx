import React from 'react';
import { TextInput, StyleSheet } from 'react-native';

export const Input = (props: any) => (
  <TextInput style={styles.input} placeholderTextColor="#9ca3af" {...props} />
);

const styles = StyleSheet.create({
  input: { borderBottomWidth: 1, borderColor: '#d1d5db', paddingVertical: 10, fontSize: 16, marginBottom: 20 }
});
