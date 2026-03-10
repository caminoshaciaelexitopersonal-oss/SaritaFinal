import React from 'react';
import { designTokens } from '../tokens/design-tokens';
import { spacing } from '../tokens/spacing';

interface CardProps {
  children: React.ReactNode;
  padding?: keyof typeof spacing;
}

export const Card: React.FC<CardProps> = ({ children, padding = 'md' }) => {
  return (
    <div style={{
      backgroundColor: designTokens.colors.card,
      borderRadius: designTokens.borderRadius.lg,
      padding: spacing[padding],
      boxShadow: designTokens.shadows.sm,
      border: `1px solid ${designTokens.colors.border}`,
    }}>
      {children}
    </div>
  );
};
