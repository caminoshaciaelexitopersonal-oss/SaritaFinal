import React from 'react';
import { View, Text, ScrollView } from 'react-native';
import { MobileLayout, Button, KpiCard } from '@sarita/shared-ui';

export default function MobilePOS() {
  return (
    <MobileLayout>
      <ScrollView className="p-4">
        <Text className="text-2xl font-bold mb-6">POS Portátil</Text>
        <View className="mb-6">
          <KpiCard title="Caja Actual" value="20.00" />
        </View>
        <Button className="mb-4">Escanear Producto</Button>
        <Button variant="outline">Ver Resumen</Button>

        <View className="mt-12 bg-white p-6 rounded-2xl border border-slate-100">
          <Text className="font-bold mb-2">Impresión Bluetooth</Text>
          <Text className="text-slate-500 text-sm">Estado: Conectado a BTP-M200</Text>
        </View>
      </ScrollView>
    </MobileLayout>
  );
}
