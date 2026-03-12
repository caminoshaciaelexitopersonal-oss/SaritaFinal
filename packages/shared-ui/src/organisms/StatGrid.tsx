import React from 'react';
import { View, Platform, StyleSheet } from 'react-native';
import { spacing } from '../tokens/spacing';

interface StatGridProps {
  children: React.ReactNode;
  columns?: number;
}

export const StatGrid: React.FC<StatGridProps> = ({ children, columns = 4 }) => {
  if (Platform.OS === 'web') {
    return (
      <div style={{
        display: 'grid',
        gridTemplateColumns: `repeat(${columns}, 1fr)`,
        gap: spacing.md,
        width: '100%',
      }}>
        {children}
      </div>
    );
  }

  return (
    <View style={styles.nativeGrid}>
      {children}
    </View>
  );
};

const styles = StyleSheet.create({
  nativeGrid: {
    flexDirection: 'column',
    gap: 12,
    width: '100%',
  }
});
