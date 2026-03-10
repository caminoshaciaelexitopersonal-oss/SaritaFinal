import React from 'react';
import { designTokens } from '../tokens/design-tokens';

interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  onPress?: () => void;
  disabled?: boolean;
}

/**
 * Unified Button Atom.
 * Adapts between platforms via conditional rendering or cross-platform primitives.
 */
export const Button: React.FC<ButtonProps> = ({
  label,
  variant = 'primary',
  onPress,
  disabled
}) => {
  const getBackgroundColor = () => {
    if (disabled) return '#cccccc';
    switch (variant) {
      case 'primary': return designTokens.colors.primary;
      case 'secondary': return designTokens.colors.secondary;
      case 'danger': return designTokens.colors.danger;
      case 'ghost': return 'transparent';
      default: return designTokens.colors.primary;
    }
  };

  const getTextColor = () => {
    if (variant === 'ghost') return designTokens.colors.primary;
    return '#ffffff';
  };

  // Note: In a real implementation, we would use react-native-web or
  // platform-specific extensions (.web.tsx, .tsx).
  return (
    <button
      onClick={onPress}
      disabled={disabled}
      style={{
        backgroundColor: getBackgroundColor(),
        color: getTextColor(),
        padding: '10px 20px',
        borderRadius: designTokens.borderRadius.md,
        border: variant === 'ghost' ? `1px solid ${designTokens.colors.primary}` : 'none',
        cursor: disabled ? 'not-allowed' : 'pointer',
        fontSize: '16px',
        fontWeight: '600',
        transition: 'opacity 0.2s',
      }}
      onMouseOver={(e) => (e.currentTarget.style.opacity = '0.8')}
      onMouseOut={(e) => (e.currentTarget.style.opacity = '1')}
    >
      {label}
    </button>
  );
};
