import React from 'react';
import { View, ScrollView, Text } from 'react-native';
import { MobileLayout, KpiCard, LineChart } from '@sarita/shared-ui';

export default function InstitutionalReportsScreen() {
  return (
    <MobileLayout>
      <ScrollView className="p-4">
        <Text className="text-2xl font-bold mb-4 text-slate-900">Reportes del Territorio</Text>
        <View className="gap-4 mb-6">
          <KpiCard title="Prestadores Activos" value="128" trend="+5" />
          <KpiCard title="Reservas Regionales" value="3,420" trend="+15%" />
        </View>
        <View className="bg-white p-4 rounded-xl shadow-sm">
          <Text className="font-bold mb-4">Tendencia de Ocupación</Text>
          <LineChart data={[{name: 'Sem 1', v: 45}, {name: 'Sem 2', v: 60}, {name: 'Sem 3', v: 85}]} dataKey="v" />
        </View>
      </ScrollView>
    </MobileLayout>
  );
}
