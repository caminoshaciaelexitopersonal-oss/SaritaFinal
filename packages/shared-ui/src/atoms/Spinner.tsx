import React from 'react';
import { designTokens } from '../tokens/design-tokens';

export const Spinner: React.FC = () => {
  return (
    <div style={{
      width: '24px',
      height: '24px',
      border: `3px solid ${designTokens.colors.border}`,
      borderTop: `3px solid ${designTokens.colors.primary}`,
      borderRadius: '50%',
      animation: 'spin 1s linear infinite',
    }} />
  );
};

// CSS for spinner would be handled via a global inject or CSS-in-JS library in a real scenario
