import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, Platform, StyleSheet } from 'react-native';

interface RoutePoint {
  label: string;
  type: string;
}

interface InteractiveRouteMapProps {
  routeName: string;
  points: RoutePoint[];
}

export const InteractiveRouteMap: React.FC<InteractiveRouteMapProps> = ({ routeName, points }) => {
  const isWeb = Platform.OS === 'web';

  if (isWeb) {
    return (
      <div style={{ padding: '24px', backgroundColor: '#eff6ff', borderRadius: '16px', border: '1px solid #bfdbfe' }}>
        <Text variant="headingS" color="primary">{routeName}</Text>
        <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {points.map((p, i) => (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{ width: '24px', height: '24px', borderRadius: '50%', backgroundColor: '#1e40af', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '12px', fontWeight: 'bold' }}>
                {i + 1}
              </div>
              <div>
                <Text variant="body" style={{ fontWeight: 'bold' }}>{p.label}</Text>
                <Text variant="small" color="textSecondary">{p.type}</Text>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <Card style={styles.nativeCard}>
      <Text variant="headingS" color="primary">{routeName}</Text>
      <View style={styles.pointsContainer}>
        {points.map((p, i) => (
          <View key={i} style={styles.pointRow}>
            <View style={styles.badge}>
              <Text variant="small" style={{ color: 'white', fontWeight: 'bold' }}>{i + 1}</Text>
            </View>
            <View>
              <Text variant="body" style={{ fontWeight: 'bold' }}>{p.label}</Text>
              <Text variant="small" color="textSecondary">{p.type}</Text>
            </View>
          </View>
        ))}
      </View>
    </Card>
  );
};

const styles = StyleSheet.create({
  nativeCard: { padding: 16, backgroundColor: '#eff6ff' },
  pointsContainer: { marginTop: 16, gap: 12 },
  pointRow: { flexDirection: 'row', alignItems: 'center', gap: 12 },
  badge: { width: 24, height: 24, borderRadius: 12, backgroundColor: '#1e40af', alignItems: 'center', justifyContent: 'center' }
});
