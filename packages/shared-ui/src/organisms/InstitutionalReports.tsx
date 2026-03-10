import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { Button } from '../atoms/Button';
import { spacing } from '../tokens/spacing';

interface Report {
  id: string;
  name: string;
  lastGenerated: string;
  type: 'financial' | 'operational' | 'institutional';
}

interface InstitutionalReportsProps {
  reports: Report[];
  onDownload: (id: string) => void;
}

export const InstitutionalReports: React.FC<InstitutionalReportsProps> = ({ reports, onDownload }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
      <Text variant="headingM">Reportes Institucionales</Text>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
        gap: spacing.md
      }}>
        {reports.map(report => (
          <Card key={report.id} padding="md">
            <Text variant="headingM">{report.name}</Text>
            <div style={{ margin: `${spacing.sm}px 0` }}>
              <Text variant="caption" color="textSecondary">Tipo: {report.type.toUpperCase()}</Text>
            </div>
            <div style={{ marginBottom: spacing.md }}>
              <Text variant="small" color="textSecondary">Generado: {report.lastGenerated}</Text>
            </div>
            <Button label="Descargar PDF" variant="secondary" onPress={() => onDownload(report.id)} />
          </Card>
        ))}
      </div>
    </div>
  );
};
