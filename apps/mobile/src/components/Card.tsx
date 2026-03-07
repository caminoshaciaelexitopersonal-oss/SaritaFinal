import React from 'react';
import { View, StyleSheet } from 'react-native';

export const Card = ({ children, style }: any) => (
  <View style={[styles.card, style]}>{children}</View>
);

const styles = StyleSheet.create({
  card: { backgroundColor: '#fff', borderRadius: 10, padding: 15, elevation: 3, shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1, shadowRadius: 4 }
});
