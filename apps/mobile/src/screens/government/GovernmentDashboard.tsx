import React from 'react';
import { View, Text, ScrollView } from 'react-native';
import { MobileLayout, KpiCard } from '@sarita/shared-ui';

export const GovernmentDashboard = () => {
  return (
    <MobileLayout title="Gobernanza Móvil">
      <ScrollView>
        <KpiCard title="Funcionarios" value="12" unit="Activos" />
        <KpiCard title="Presupuesto Ejecutado" value="45" unit="%" />
      </ScrollView>
    </MobileLayout>
  );
};
