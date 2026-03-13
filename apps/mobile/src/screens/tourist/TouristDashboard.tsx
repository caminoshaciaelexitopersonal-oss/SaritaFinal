import React from 'react';
import { View, Text, ScrollView } from 'react-native';
import { MobileLayout, KpiCard } from '@sarita/shared-ui';

export const TouristDashboard = () => {
  return (
    <MobileLayout title="Mi Viaje (Mobile)">
      <ScrollView>
        <KpiCard title="Reservas Activas" value="3" unit="Próximas" />
        <KpiCard title="Saldo Wallet" value="150.000" unit="COP" />
      </ScrollView>
    </MobileLayout>
  );
};
