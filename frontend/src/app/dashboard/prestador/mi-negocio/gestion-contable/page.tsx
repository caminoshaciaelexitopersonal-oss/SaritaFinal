'use client';
import React, { useEffect, useState } from 'react';
import { useMiNegocioApi, ChartOfAccount } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';

export default function GestionContablePage() {
  const { getChartOfAccounts, isLoading } = useMiNegocioApi();
  const [cuentas, setCuentas] = useState<ChartOfAccount[]>([]);

  useEffect(() => {
    const fetchCuentas = async () => {
      const data = await getChartOfAccounts();
      if (data && data.results) {
        setCuentas(data.results);
      }
    };
    fetchCuentas();
  }, [getChartOfAccounts]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Plan de Cuentas</CardTitle>
      </CardHeader>
      <CardContent>
        {isLoading && cuentas.length === 0 ? (
          <p>Cargando plan de cuentas...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Número de Cuenta</TableHead>
                <TableHead>Nombre</TableHead>
                <TableHead>Tipo</TableHead>
                <TableHead>Activa</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {cuentas.map((cuenta) => (
                <TableRow key={cuenta.id}>
                  <TableCell>{cuenta.account_number}</TableCell>
                  <TableCell>{cuenta.name}</TableCell>
                  <TableCell>{cuenta.account_type}</TableCell>
                  <TableCell>{cuenta.is_active ? 'Sí' : 'No'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
