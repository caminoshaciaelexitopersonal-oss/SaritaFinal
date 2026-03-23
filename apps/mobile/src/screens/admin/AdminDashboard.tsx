import React from 'react';
import { View, Text, ScrollView } from 'react-native';
import { MobileLayout, KpiCard } from '@sarita/shared-ui';

export default function AdminDashboardScreen() {
  return (
    <MobileLayout>
      <ScrollView>
        <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 20 }}>Gobernanza Móvil</Text>
        <View style={{ gap: 12 }}>
          <KpiCard title="Ingresos" value="2.5k" />
          <KpiCard title="Alertas" value="2" />
          <KpiCard title="Sincronización" value="99%" />
        </View>
      </ScrollView>
    </MobileLayout>
  );
}
