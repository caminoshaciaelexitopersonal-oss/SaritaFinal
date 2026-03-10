import React from 'react';
import { View, Text as RNText, TouchableOpacity, StyleSheet, Platform } from 'react-native';

interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  onClick?: () => void;
  onPress?: () => void;
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  label,
  variant = 'primary',
  onClick,
  onPress,
  disabled
}) => {
  const handlePress = onPress || onClick;

  if (Platform.OS === 'web') {
    const getBg = () => {
       if (disabled) return '#cccccc';
       if (variant === 'primary') return '#1e40af';
       if (variant === 'secondary') return '#64748b';
       if (variant === 'danger') return '#ef4444';
       return 'transparent';
    };
    return (
      <button onClick={handlePress} disabled={disabled} style={{
        backgroundColor: getBg(),
        color: '#fff',
        padding: '10px 20px',
        borderRadius: '8px',
        border: variant === 'ghost' ? '1px solid #1e40af' : 'none',
        cursor: 'pointer'
      }}>{label}</button>
    );
  }

  return (
    <TouchableOpacity style={[styles.base, styles[variant]]} onPress={handlePress} disabled={disabled}>
      <RNText style={{color: '#fff', fontWeight: 'bold'}}>{label}</RNText>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  base: { padding: 12, borderRadius: 8, alignItems: 'center' },
  primary: { backgroundColor: '#1e40af' },
  secondary: { backgroundColor: '#64748b' },
  danger: { backgroundColor: '#ef4444' },
  ghost: { backgroundColor: 'transparent', borderWidth: 1, borderColor: '#1e40af' }
});
