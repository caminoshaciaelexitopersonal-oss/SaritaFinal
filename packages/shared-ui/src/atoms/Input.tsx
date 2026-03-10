import React from 'react';
import { designTokens } from '../tokens/design-tokens';

interface InputProps {
  placeholder?: string;
  value?: string;
  onChange?: (val: string) => void;
  type?: string;
}

export const Input: React.FC<InputProps> = ({ placeholder, value, onChange, type = 'text' }) => {
  return (
    <input
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={(e) => onChange?.(e.target.value)}
      style={{
        padding: '12px 16px',
        borderRadius: designTokens.borderRadius.md,
        border: `1px solid ${designTokens.colors.border}`,
        fontSize: '16px',
        width: '100%',
        boxSizing: 'border-box',
        outline: 'none',
      }}
    />
  );
};
