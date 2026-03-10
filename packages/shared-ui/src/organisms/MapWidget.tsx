import React from 'react';
import { designTokens } from '../tokens/design-tokens';
import { Text } from '../atoms/Text';

interface MapWidgetProps {
  regionName: string;
  dataPoints: Array<{ id: string; label: string; value: number }>;
}

export const MapWidget: React.FC<MapWidgetProps> = ({ regionName, dataPoints }) => {
  return (
    <div style={{
      height: '400px',
      backgroundColor: '#f0f0f0',
      borderRadius: designTokens.borderRadius.lg,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      position: 'relative',
      border: `1px solid ${designTokens.colors.border}`,
    }}>
      <Text variant="headingM">Mapa de {regionName}</Text>
      <div style={{ marginTop: '20px' }}>
        {dataPoints.map(point => (
          <div key={point.id} style={{ display: 'flex', alignItems: 'center', marginBottom: '8px' }}>
            <div style={{
              width: '8px',
              height: '8px',
              backgroundColor: designTokens.colors.primary,
              borderRadius: '50%',
              marginRight: '8px'
            }} />
            <Text variant="caption">{point.label}: {point.value}</Text>
          </div>
        ))}
      </div>
    </div>
  );
};
