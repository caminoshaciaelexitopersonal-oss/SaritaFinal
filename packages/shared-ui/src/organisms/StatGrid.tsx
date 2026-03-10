import React from 'react';
import { spacing } from '../tokens/spacing';

interface StatGridProps {
  children: React.ReactNode;
  columns?: number;
}

export const StatGrid: React.FC<StatGridProps> = ({ children, columns = 4 }) => {
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
};
