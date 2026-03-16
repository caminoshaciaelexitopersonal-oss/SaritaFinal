import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView, FlatList } from 'react-native';
import { MobileLayout, KpiCard } from '@sarita/shared-ui';
import { governanceService } from '../../services/governanceService';

export const GovernmentDashboard = () => {
  const [officials, setOfficials] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    governanceService.getOfficials()
      .then(res => {
        setOfficials(res.data.results || []);
      })
      .catch(err => console.error("Error loading officials:", err))
      .finally(() => setLoading(false));
  }, []);

  return (
    <MobileLayout title="Gobernanza Móvil">
      <ScrollView className="p-4">
        <View className="flex-row justify-between mb-6">
          <KpiCard title="Funcionarios" value={officials.length.toString()} unit="Activos" />
          <KpiCard title="Entidades" value="3" unit="Niveles" />
        </View>

        <Text className="text-xl font-bold mb-4 text-slate-800">Directorio de Funcionarios</Text>

        {officials.map((item: any) => (
          <View key={item.id} className="bg-white p-4 rounded-xl mb-3 shadow-sm border border-slate-100">
            <Text className="font-bold text-slate-900">{item.user_name}</Text>
            <Text className="text-slate-500 text-sm">{item.cargo} • {item.nivel}</Text>
          </View>
        ))}

        {officials.length === 0 && !loading && (
          <Text className="text-slate-400 italic text-center mt-10">No hay funcionarios registrados.</Text>
        )}
      </ScrollView>
    </MobileLayout>
  );
};
