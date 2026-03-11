import React from 'react';
import { Text } from '../atoms/Text';
import { Card } from '../molecules/Card';
import { spacing } from '../tokens/spacing';

interface AlertCardProps {
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high' | 'critical';
  timestamp: string;
}

export const AlertCard: React.FC<AlertCardProps> = ({ title, description, priority, timestamp }) => {
  const getPriorityColor = () => {
    switch (priority) {
      case 'critical': return '#ff0000';
      case 'high': return '#f5a623';
      case 'medium': return '#0070f3';
      default: return '#666666';
    }
  };

  return (
    <Card padding="sm">
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: spacing.xs }}>
        <Text variant="headingM">{title}</Text>
        <div style={{
          backgroundColor: getPriorityColor(),
          width: '12px',
          height: '12px',
          borderRadius: '50%'
        }} />
      </div>
      <Text variant="body">{description}</Text>
      <div style={{ marginTop: spacing.sm, textAlign: 'right' }}>
        <Text variant="small" color="textSecondary">{timestamp}</Text>
      </div>
    </Card>
  );
};
