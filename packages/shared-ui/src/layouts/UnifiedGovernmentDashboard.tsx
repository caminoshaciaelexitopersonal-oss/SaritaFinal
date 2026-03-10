import React from 'react';
import { DashboardLayout } from '../layouts/DashboardLayout';
import { TerritorialAnalytics } from '../organisms/TerritorialAnalytics';
import { AlertSystem } from '../organisms/AlertSystem';
import { ProviderMonitoring } from '../organisms/ProviderMonitoring';
import { InstitutionalReports } from '../organisms/InstitutionalReports';
import { TrendGraph } from '../organisms/TrendGraph';
import { DataExporter } from '../organisms/DataExporter';
import { spacing } from '../tokens/spacing';
import { Text } from '../atoms/Text';
import { View, Platform } from 'react-native';

interface UnifiedGovernmentDashboardProps {
  platform: 'web' | 'mobile' | 'desktop';
  data: any; // Mock data for all modules
}

export const UnifiedGovernmentDashboard: React.FC<UnifiedGovernmentDashboardProps> = ({
  platform,
  data
}) => {
  const isMobile = platform === 'mobile';
  const isWeb = Platform.OS === 'web';

  const content = (
    <View style={isWeb ? { display: 'flex', flexDirection: 'column', gap: spacing.xxl } : { gap: 32 }}>
      {/* KPIs Principales */}
      <View>
        <TerritorialAnalytics
          stats={data.stats}
          regionData={data.regionData}
          isMobile={isMobile}
        />
      </View>

      {/* Gráficos de Tendencia */}
      <View style={platform === 'desktop' || platform === 'web' ? {
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: spacing.lg
      } : { gap: 16 }}>
        <TrendGraph
          title="Crecimiento de Reservas (Mensual)"
          data={data.trends?.bookings || []}
        />
        <TrendGraph
          title="Impacto Económico Regional (MRR)"
          data={data.trends?.revenue || []}
          color="#10b981"
        />
      </View>

      {/* Monitoreo y Alertas */}
      <View style={platform === 'desktop' || platform === 'web' ? {
        display: 'grid',
        gridTemplateColumns: '2fr 1fr',
        gap: spacing.lg
      } : { gap: 16 }}>
        <ProviderMonitoring
          providers={data.providers}
          viewMode={isMobile ? 'list' : 'table'}
        />
        <AlertSystem alerts={data.alerts} />
      </View>

      {/* Reportes y Exportación */}
      <View>
        <Text variant="headingM" style={{ marginBottom: spacing.md }}>Reportes e Inteligencia</Text>
        <View style={isWeb ? { display: 'flex', flexDirection: 'column', gap: spacing.md } : { gap: 12 }}>
          <DataExporter
            reportName="Análisis de Impacto Económico Consolidado 2026"
            onExport={(format) => console.log(`Exporting in ${format}`)}
          />
          <InstitutionalReports
            reports={data.reports}
            onDownload={(id) => console.log('Downloading', id)}
          />
        </View>
      </View>
    </View>
  );

  return (
    <DashboardLayout title="Torre de Control - Gobierno" sidebar={!isMobile && isWeb ? <div style={{ padding: '20px' }}>Menu Admin</div> : undefined}>
      {content}
    </DashboardLayout>
  );
};
