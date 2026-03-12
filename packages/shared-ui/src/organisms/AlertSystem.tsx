import React from 'react';
import { View, Platform, StyleSheet } from 'react-native';
import { AlertCard } from '../molecules/AlertCard';
import { Text } from '../atoms/Text';
import { spacing } from '../tokens/spacing';

interface Alert {
  id: string;
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high' | 'critical';
  timestamp: string;
}

interface AlertSystemProps {
  alerts: Alert[];
}

export const AlertSystem: React.FC<AlertSystemProps> = ({ alerts }) => {
  if (Platform.OS === 'web') {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
        <Text variant="headingM">Alertas del Sistema</Text>
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
          {alerts.map(alert => (
            <AlertCard
              key={alert.id}
              title={alert.title}
              description={alert.description}
              priority={alert.priority}
              timestamp={alert.timestamp}
            />
          ))}
        </div>
        {alerts.length === 0 && (
          <Text color="textSecondary">No hay alertas críticas en este momento.</Text>
        )}
      </div>
    );
  }

  return (
    <View style={styles.nativeContainer}>
      <Text variant="headingM" style={{ marginBottom: 16 }}>Alertas del Sistema</Text>
      <View style={{ gap: 8 }}>
        {alerts.map(alert => (
          <AlertCard
            key={alert.id}
            title={alert.title}
            description={alert.description}
            priority={alert.priority}
            timestamp={alert.timestamp}
          />
        ))}
      </View>
      {alerts.length === 0 && (
        <Text color="textSecondary">No hay alertas críticas en este momento.</Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  nativeContainer: { paddingVertical: 12 }
});
