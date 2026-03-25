import React, { useState, useEffect } from 'react';
import { InventoryWidget, PayrollSnapshot, StatCard, StatGrid } from '@sarita/shared-ui';
import { ScrollView, View, Text, StyleSheet, ActivityIndicator, TouchableOpacity } from 'react-native';
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

  const [chartOfAccounts, setChartOfAccounts] = useState<any[]>([]);

  useEffect(() => {
     api.get('/finance/ledger/cuentas/').then(res => setChartOfAccounts(res.data.results || []));
  }, []);

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.sectionHeader}>Resumen Financiero</Text>
      <StatGrid columns={1}>
        <StatCard title="Ingresos Mes" value={`$${data?.stats?.revenue || 0}`} trend="+12%" trendDirection="up" />
        <StatCard title="Reservas Activas" value={data?.stats?.active_bookings || 0} trend="+5%" trendDirection="up" />
      </StatGrid>

      <Text style={styles.sectionHeader}>Estructura PUC (Plan de Cuentas)</Text>
      <View style={styles.pucContainer}>
          {chartOfAccounts.slice(0, 10).map((acc: any) => (
              <TouchableOpacity key={acc.id} style={styles.accountRow}>
                  <Text style={styles.accountCode}>{acc.code}</Text>
                  <Text style={styles.accountName}>{acc.name}</Text>
                  <Text style={styles.accountType}>{acc.type}</Text>
              </TouchableOpacity>
          ))}
          {chartOfAccounts.length > 10 && <Text style={styles.moreText}>+ Ver catálogo completo</Text>}
      </View>

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
  content: { padding: 16 },
  sectionHeader: { fontSize: 14, fontWeight: '900', color: '#64748b', textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 16, marginTop: 24 },
  pucContainer: { backgroundColor: '#fff', borderRadius: 20, padding: 16, borderWith: 1, borderColor: '#f1f5f9' },
  accountRow: { flexDirection: 'row', paddingVertical: 12, borderBottomWidth: 1, borderBottomColor: '#f8fafc', alignItems: 'center' },
  accountCode: { fontWeight: 'bold', width: 60, color: '#4f46e5' },
  accountName: { flex: 1, fontSize: 13, color: '#334155' },
  accountType: { fontSize: 10, fontWeight: '900', color: '#94a3b8', backgroundColor: '#f1f5f9', paddingHorizontal: 6, paddingVertical: 2, borderRadius: 4 },
  moreText: { textAlign: 'center', marginTop: 12, fontSize: 12, color: '#6366f1', fontWeight: 'bold' }
});
