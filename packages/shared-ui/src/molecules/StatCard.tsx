import React from 'react';
import { Card } from './Card';
import { Text } from '../atoms/Text';
import { spacing } from '../tokens/spacing';

interface StatCardProps {
  title: string;
  value: string | number;
  trend?: string;
  trendDirection?: 'up' | 'down';
}

export const StatCard: React.FC<StatCardProps> = ({ title, value, trend, trendDirection }) => {
  return (
    <Card>
      <div style={{ marginBottom: spacing.xs }}>
        <Text variant="caption" color="textSecondary">{title}</Text>
      </div>
      <div style={{ marginBottom: spacing.xs }}>
        <Text variant="headingL">{value}</Text>
      </div>
      {trend && (
        <Text variant="small" color={trendDirection === 'up' ? 'success' : 'danger'}>
          {trend}
        </Text>
      )}
    </Card>
  );
};
