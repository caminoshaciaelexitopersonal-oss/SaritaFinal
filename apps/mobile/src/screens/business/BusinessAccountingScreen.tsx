import React, { useState, useEffect } from 'react';
import { InventoryWidget, PayrollSnapshot, StatCard, StatGrid } from '@sarita/shared-ui';
import { ScrollView, View, StyleSheet, ActivityIndicator } from 'react-native';
import { api } from '../../services/api';

export const BusinessAccountingScreen = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAccounting = async () => {
      try {
        const [payrollRes, inventoryRes, statsRes] = await Promise.all([
          api.get('/payroll/dashboard/'),
          api.get('/mi-negocio/operativa/inventario/'),
          api.get('/mi-negocio/financiera/indicadores/')
        ]);
        setData({
          payroll: payrollRes.data,
          inventory: inventoryRes.data.results,
          stats: statsRes.data
        });
      } catch (err) {
        console.error('Mobile Accounting Error:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchAccounting();
  }, []);

  if (loading) {
    return (
      <View style={[styles.container, { justifyContent: 'center' }]}>
        <ActivityIndicator size="large" color="#1a1a1a" />
      </View>
    );
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <StatGrid columns={1}>
        <StatCard title="Ingresos Mes" value={`$${data?.stats?.revenue || 0}`} trend="+12%" trendDirection="up" />
        <StatCard title="Reservas Activas" value={data?.stats?.active_bookings || 0} trend="+5%" trendDirection="up" />
      </StatGrid>

      <View style={{ marginVertical: 20 }}>
        <PayrollSnapshot data={{
          totalEmployees: data?.payroll?.total_employees,
          totalPayable: `$${data?.payroll?.total_payable}`,
          nextPaymentDate: data?.payroll?.next_payment_date,
          pendingLiquidations: data?.payroll?.pending_liquidations
        }} />
      </View>

      <InventoryWidget items={data?.inventory?.map((i: any) => ({
        id: i.id,
        name: i.nombre,
        stock: i.stock_actual,
        minStock: i.stock_minimo,
        unit: i.unidad_medida
      })) || []} />
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  content: { padding: 16 }
});
