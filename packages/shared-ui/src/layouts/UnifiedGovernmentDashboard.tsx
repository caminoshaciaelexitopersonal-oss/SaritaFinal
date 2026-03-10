import React from 'react';
import { DashboardLayout } from '../layouts/DashboardLayout';
import { TerritorialAnalytics } from '../organisms/TerritorialAnalytics';
import { AlertSystem } from '../organisms/AlertSystem';
import { ProviderMonitoring } from '../organisms/ProviderMonitoring';
import { InstitutionalReports } from '../organisms/InstitutionalReports';
import { spacing } from '../tokens/spacing';

interface UnifiedGovernmentDashboardProps {
  platform: 'web' | 'mobile' | 'desktop';
  data: any; // Mock data for all modules
}

export const UnifiedGovernmentDashboard: React.FC<UnifiedGovernmentDashboardProps> = ({
  platform,
  data
}) => {
  const isMobile = platform === 'mobile';

  return (
    <DashboardLayout title="Torre de Control - Gobierno" sidebar={!isMobile ? <div style={{ padding: '20px' }}>Menu Admin</div> : undefined}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xxl }}>
        <section>
          <TerritorialAnalytics
            stats={data.stats}
            regionData={data.regionData}
            isMobile={isMobile}
          />
        </section>

        <section style={{
          display: 'grid',
          gridTemplateColumns: platform === 'desktop' || platform === 'web' ? '2fr 1fr' : '1fr',
          gap: spacing.lg
        }}>
          <ProviderMonitoring
            providers={data.providers}
            viewMode={isMobile ? 'list' : 'table'}
          />
          <AlertSystem alerts={data.alerts} />
        </section>

        <section>
          <InstitutionalReports
            reports={data.reports}
            onDownload={(id) => console.log('Downloading', id)}
          />
        </section>
      </div>
    </DashboardLayout>
  );
};
