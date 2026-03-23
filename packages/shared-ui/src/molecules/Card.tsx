import React from 'react';
import { View, Platform, StyleSheet } from 'react-native';
import { designTokens } from '../tokens/design-tokens';
import { spacing } from '../tokens/spacing';

interface CardProps {
  children: React.ReactNode;
  padding?: keyof typeof spacing;
  style?: any;
}

export const Card: React.FC<CardProps> = ({ children, padding = 'md', style }) => {
  if (Platform.OS === 'web') {
    return (
      <div style={{
        backgroundColor: designTokens.colors.card,
        borderRadius: designTokens.borderRadius.lg,
        padding: spacing[padding],
        boxShadow: designTokens.shadows.sm,
        border: `1px solid ${designTokens.colors.border}`,
        ...style
      }}>
        {children}
      </div>
    );
  }

  return (
    <View style={[nativeStyles.card, { padding: spacing[padding] }, style]}>
      {children}
    </View>
  );
};

const nativeStyles = StyleSheet.create({
  card: {
    backgroundColor: designTokens.colors.card,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: designTokens.colors.border,
    // iOS shadow
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    // Android shadow
    elevation: 3,
  }
});
