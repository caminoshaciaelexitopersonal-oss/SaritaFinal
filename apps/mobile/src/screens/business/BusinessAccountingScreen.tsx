import React from 'react';
import { InventoryWidget, PayrollSnapshot, StatCard, StatGrid } from '@sarita/shared-ui';
import { ScrollView, View, StyleSheet } from 'react-native';

const PRESTADOR_MOCK = {
  inventory: [
    { id: '1', name: 'Toallas Blancas', stock: 15, minStock: 20, unit: 'unidades' },
    { id: '2', name: 'Jabón Biodegradable', stock: 50, minStock: 10, unit: 'litros' }
  ],
  payroll: {
    totalEmployees: 12,
    totalPayable: "$8,500,000",
    nextPaymentDate: "30 Mar 2026",
    pendingLiquidations: 1
  },
  stats: {
    revenue: "$45.2M",
    bookings: 85,
    satisfaction: "4.8/5"
  }
};

export const BusinessAccountingScreen = () => {
  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <StatGrid columns={1}>
        <StatCard title="Ingresos Mes" value={PRESTADOR_MOCK.stats.revenue} trend="+12%" trendDirection="up" />
        <StatCard title="Reservas Activas" value={PRESTADOR_MOCK.stats.bookings} trend="+5%" trendDirection="up" />
      </StatGrid>

      <View style={{ marginVertical: 20 }}>
        <PayrollSnapshot data={PRESTADOR_MOCK.payroll} />
      </View>

      <InventoryWidget items={PRESTADOR_MOCK.inventory} />
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  content: { padding: 16 }
});
