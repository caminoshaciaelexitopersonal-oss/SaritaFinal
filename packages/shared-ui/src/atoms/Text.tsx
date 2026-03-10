import React from 'react';
import { typography } from '../tokens/typography';
import { designTokens } from '../tokens/design-tokens';

interface TextProps {
  children: React.ReactNode;
  variant?: keyof typeof typography;
  color?: keyof typeof designTokens.colors;
}

export const Text: React.FC<TextProps> = ({
  children,
  variant = 'body',
  color = 'textPrimary'
}) => {
  const styles = typography[variant];

  return (
    <span style={{
      ...styles,
      color: designTokens.colors[color],
      display: 'inline-block',
    }}>
      {children}
    </span>
  );
};
