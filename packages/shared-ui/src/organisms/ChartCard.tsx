import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, Platform, StyleSheet } from 'react-native';

interface ChartData {
  label: string;
  value: number;
  color?: string;
}

interface ChartCardProps {
  title: string;
  data: ChartData[];
  type: 'bar' | 'pie' | 'line';
}

export const ChartCard: React.FC<ChartCardProps> = ({ title, data, type }) => {
  const isWeb = Platform.OS === 'web';

  const renderChart = () => {
    if (isWeb) {
      // Simplificación para la demostración - en producción usaría Recharts o similar
      const maxValue = Math.max(...data.map(d => d.value), 1);
      return (
        <div style={{ display: 'flex', alignItems: 'flex-end', height: '150px', gap: '10px', marginTop: '20px' }}>
          {data.map((d, i) => (
            <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <div style={{
                width: '100%',
                height: `${(d.value / maxValue) * 100}%`,
                backgroundColor: d.color || '#1e40af',
                borderRadius: '4px 4px 0 0'
              }} />
              <span style={{ fontSize: '10px', marginTop: '4px', whiteSpace: 'nowrap' }}>{d.label}</span>
            </div>
          ))}
        </div>
      );
    }

    // Native Placeholder
    return (
      <View style={styles.nativeChart}>
        {data.map((d, i) => (
          <View key={i} style={styles.nativeBarContainer}>
            <View style={[styles.nativeBar, { height: `${(d.value / 100) * 100}%`, backgroundColor: d.color || '#1e40af' }]} />
            <Text variant="small" style={{ fontSize: 8 }}>{d.label}</Text>
          </View>
        ))}
      </View>
    );
  };

  return (
    <Card>
      <Text variant="headingS">{title}</Text>
      {renderChart()}
    </Card>
  );
};

const styles = StyleSheet.create({
  nativeChart: { flexDirection: 'row', alignItems: 'flex-end', height: 120, gap: 8, marginTop: 16 },
  nativeBarContainer: { flex: 1, alignItems: 'center' },
  nativeBar: { width: '100%', borderRadius: 2 }
});
