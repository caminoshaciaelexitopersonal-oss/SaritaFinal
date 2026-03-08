import React from 'react';
import { View, ActivityIndicator, StyleSheet, Text } from 'react-native';

interface LoaderProps {
  message?: string;
  fullScreen?: boolean;
}

export const Loader: React.FC<LoaderProps> = ({ message, fullScreen = false }) => {
  const content = (
    <View style={[styles.container, fullScreen && styles.fullScreen]}>
      <ActivityIndicator size="large" color="#1e3a8a" />
      {message && <Text style={styles.message}>{message}</Text>}
    </View>
  );

  return content;
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
  fullScreen: {
    flex: 1,
    backgroundColor: 'rgba(255,255,255,0.8)',
  },
  message: {
    marginTop: 10,
    color: '#1e3a8a',
    fontWeight: '500',
  },
});
