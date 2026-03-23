import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, Platform, StyleSheet } from 'react-native';

interface Column {
  key: string;
  header: string;
}

interface ReportTableProps {
  title: string;
  columns: Column[];
  data: any[];
}

export const ReportTable: React.FC<ReportTableProps> = ({ title, columns, data }) => {
  const isWeb = Platform.OS === 'web';

  if (isWeb) {
    return (
      <Card style={{ padding: 0, overflow: 'hidden' }}>
        <div style={{ padding: '16px', borderBottom: '1px solid #eee' }}>
          <Text variant="headingS">{title}</Text>
        </div>
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ backgroundColor: '#f9fafb', textAlign: 'left' }}>
                {columns.map(col => (
                  <th key={col.key} style={{ padding: '12px', fontSize: '12px', color: '#6b7280' }}>{col.header}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, i) => (
                <tr key={i} style={{ borderTop: '1px solid #f3f4f6' }}>
                  {columns.map(col => (
                    <td key={col.key} style={{ padding: '12px', fontSize: '14px' }}>{row[col.key]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    );
  }

  return (
    <Card>
      <Text variant="headingS" style={{ marginBottom: 16 }}>{title}</Text>
      <View style={styles.nativeContainer}>
        {data.map((row, i) => (
          <View key={i} style={styles.nativeRow}>
            {columns.map(col => (
              <View key={col.key} style={{ flex: 1 }}>
                <Text variant="small" color="textSecondary">{col.header}</Text>
                <Text variant="body">{row[col.key]}</Text>
              </View>
            ))}
          </View>
        ))}
      </View>
    </Card>
  );
};

const styles = StyleSheet.create({
  nativeContainer: { gap: 12 },
  nativeRow: { padding: 8, borderBottomWidth: 1, borderBottomColor: '#f3f4f6' }
});
