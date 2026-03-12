import React, { useState } from 'react';
import { View, ScrollView, Text } from 'react-native';
import { MobileLayout, DataTable, Button, KpiCard } from '@sarita/shared-ui';

export default function UserManagementScreen() {
  const [users, setUsers] = useState([
    { id: '1', username: 'admin_PG', role: 'Administrador' },
    { id: '2', username: 'hotel_villas', role: 'Prestador' },
    { id: '3', username: 'guia_local', role: 'Prestador' }
  ]);

  return (
    <MobileLayout>
      <ScrollView className="p-4">
        <Text className="text-2xl font-bold mb-4">Gestión de Usuarios</Text>
        <KpiCard title="Total Usuarios" value={users.length} />
        <Button className="my-6">Crear Nuevo Usuario</Button>
        <DataTable
          columns={[
            {header: 'Usuario', accessor: 'username'},
            {header: 'Rol', accessor: 'role'}
          ]}
          data={users}
        />
      </ScrollView>
    </MobileLayout>
  );
}
