import React from 'react';
import { View, Platform, StyleSheet } from 'react-native';
import { StatGrid } from '../organisms/StatGrid';
import { StatCard } from '../molecules/StatCard';
import { MapWidget } from '../organisms/MapWidget';
import { spacing } from '../tokens/spacing';

interface TerritorialAnalyticsProps {
  stats: {
    totalUsers: number;
    activeProviders: number;
    totalRevenue: string;
    occupancyRate: string;
  };
  regionData: Array<{ id: string; label: string; value: number }>;
  isMobile?: boolean;
}

export const TerritorialAnalytics: React.FC<TerritorialAnalyticsProps> = ({
  stats,
  regionData,
  isMobile = false
}) => {
  if (Platform.OS === 'web') {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
        <StatGrid columns={isMobile ? 1 : 4}>
          <StatCard title="Usuarios Totales" value={stats.totalUsers} trend="+12%" trendDirection="up" />
          <StatCard title="Prestadores Activos" value={stats.activeProviders} trend="+5%" trendDirection="up" />
          <StatCard title="Ingresos Regionales" value={stats.totalRevenue} trend="+8%" trendDirection="up" />
          <StatCard title="Ocupación" value={stats.occupancyRate} trend="-2%" trendDirection="down" />
        </StatGrid>

        <MapWidget regionName="Puerto Gaitán" dataPoints={regionData} />
      </div>
    );
  }

  return (
    <View style={styles.nativeContainer}>
      <StatGrid columns={1}>
        <StatCard title="Usuarios Totales" value={stats.totalUsers} trend="+12%" trendDirection="up" />
        <StatCard title="Prestadores Activos" value={stats.activeProviders} trend="+5%" trendDirection="up" />
        <StatCard title="Ingresos Regionales" value={stats.totalRevenue} trend="+8%" trendDirection="up" />
        <StatCard title="Ocupación" value={stats.occupancyRate} trend="-2%" trendDirection="down" />
      </StatGrid>

      <MapWidget regionName="Puerto Gaitán" dataPoints={regionData} />
    </View>
  );
};

const styles = StyleSheet.create({
  nativeContainer: { gap: 16 }
});
