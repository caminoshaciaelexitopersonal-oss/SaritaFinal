import React, { useState } from 'react';
import { View, ScrollView } from 'react-native';
import { MobileLayout, KpiCard, DataTable, Button } from '@sarita/shared-ui';

export default function BusinessInvoicingScreen() {
  const [invoices, setInvoices] = useState([
    { id: 'INV-001', client: 'Juan Pérez', total: '20.00', status: 'Pagada' },
    { id: 'INV-002', client: 'Maria Lopez', total: '5.50', status: 'Pendiente' }
  ]);

  const handleCreate = () => {
    // Logic to call BillingService via SharedSDK
    console.log("Creating invoice...");
  };

  return (
    <MobileLayout>
      <ScrollView className="p-4">
        <h2 className="text-2xl font-bold mb-4">Gestión de Facturas</h2>
        <div className="grid grid-cols-2 gap-4 mb-6">
          <KpiCard title="Total Mes" value=",520" />
          <KpiCard title="Pendientes" value="3" />
        </div>
        <Button onClick={handleCreate} className="mb-6">Nueva Factura</Button>
        <DataTable
          columns={[{header: 'ID', accessor: 'id'}, {header: 'Cliente', accessor: 'client'}, {header: 'Total', accessor: 'total'}]}
          data={invoices}
        />
      </ScrollView>
    </MobileLayout>
  );
}
