import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, StyleSheet } from 'react-native';

interface KPIWidgetProps {
  label: string;
  value: string | number;
  trend?: string;
  isPositive?: boolean;
}

export const KPIWidget: React.FC<KPIWidgetProps> = ({ label, value, trend, isPositive }) => {
  return (
    <Card style={styles.card}>
      <Text variant="caption" color="textSecondary">{label}</Text>
      <View style={styles.valueRow}>
        <Text variant="headingM">{value}</Text>
        {trend && (
          <Text
            variant="small"
            style={{
              color: isPositive ? '#10b981' : '#ef4444',
              marginLeft: 8,
              fontWeight: 'bold'
            }}
          >
            {trend}
          </Text>
        )}
      </View>
    </Card>
  );
};

const styles = StyleSheet.create({
  card: { padding: 16, minWidth: 150 },
  valueRow: { flexDirection: 'row', alignItems: 'baseline', marginTop: 4 }
});
