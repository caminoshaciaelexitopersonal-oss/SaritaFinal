import React from 'react';
import { Text as RNText, Platform, StyleSheet } from 'react-native';

interface TextProps {
  children: React.ReactNode;
  variant?: 'body' | 'headingS' | 'headingM' | 'headingL' | 'caption' | 'small';
  color?: 'primary' | 'textPrimary' | 'textSecondary' | 'success' | 'danger';
  style?: any;
}

export const Text: React.FC<TextProps> = ({ children, variant = 'body', color = 'textPrimary', style }) => {
  if (Platform.OS === 'web') {
    const getFontSize = () => {
      if (variant === 'headingL') return '32px';
      if (variant === 'headingM') return '24px';
      if (variant === 'headingS') return '18px';
      return '16px';
    };
    return <span style={{ fontSize: getFontSize(), fontWeight: variant.startsWith('heading') ? 'bold' : 'normal', ...style }}>{children}</span>;
  }
  return <RNText style={[style, { fontSize: 16 }]}>{children}</RNText>;
};
