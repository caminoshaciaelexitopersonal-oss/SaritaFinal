import React from 'react';
import { View, Platform, StyleSheet } from 'react-native';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { spacing } from '../tokens/spacing';

interface Provider {
  id: string;
  name: string;
  category: string;
  status: 'active' | 'inactive';
  lastActivity: string;
}

interface ProviderMonitoringProps {
  providers: Provider[];
  viewMode: 'table' | 'list';
}

export const ProviderMonitoring: React.FC<ProviderMonitoringProps> = ({ providers, viewMode }) => {
  const isWeb = Platform.OS === 'web';

  if (isWeb && viewMode === 'table') {
    return (
      <table style={{ width: '100%', borderCollapse: 'collapse', backgroundColor: '#fff' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid #eaeaea', textAlign: 'left' }}>
            <th style={{ padding: spacing.sm }}>Nombre</th>
            <th style={{ padding: spacing.sm }}>Categoría</th>
            <th style={{ padding: spacing.sm }}>Estado</th>
            <th style={{ padding: spacing.sm }}>Última Actividad</th>
          </tr>
        </thead>
        <tbody>
          {providers.map(p => (
            <tr key={p.id} style={{ borderBottom: '1px solid #eee' }}>
              <td style={{ padding: spacing.sm }}><Text>{p.name}</Text></td>
              <td style={{ padding: spacing.sm }}><Text variant="caption">{p.category}</Text></td>
              <td style={{ padding: spacing.sm }}>
                <Text color={p.status === 'active' ? 'success' : 'danger'}>{p.status}</Text>
              </td>
              <td style={{ padding: spacing.sm }}><Text variant="small">{p.lastActivity}</Text></td>
            </tr>
          </tbody>
        </table>
    );
  }

  if (isWeb) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
        {providers.map(p => (
          <Card key={p.id} padding="sm">
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <Text variant="headingM">{p.name}</Text>
              <Text variant="small" color={p.status === 'active' ? 'success' : 'danger'}>
                {p.status.toUpperCase()}
              </Text>
            </div>
            <Text variant="caption">{p.category}</Text>
          </Card>
        ))}
      </div>
    );
  }

  return (
    <View style={styles.nativeContainer}>
      <Text variant="headingM" style={{ marginBottom: 12 }}>Monitoreo de Prestadores</Text>
      <View style={{ gap: 8 }}>
        {providers.map(p => (
          <Card key={p.id} padding="sm" style={styles.nativeCard}>
            <View style={styles.row}>
              <Text variant="headingM" style={{ fontSize: 16 }}>{p.name}</Text>
              <Text variant="small" color={p.status === 'active' ? 'success' : 'danger'}>
                {p.status.toUpperCase()}
              </Text>
            </View>
            <Text variant="caption">{p.category}</Text>
          </Card>
        ))}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  nativeContainer: { paddingVertical: 12 },
  nativeCard: { padding: 12 },
  row: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }
});
