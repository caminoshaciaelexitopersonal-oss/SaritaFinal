'use client';
import React, { useEffect, useState } from 'react';
import { useMiNegocioApi, BankAccount } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';

export default function GestionFinancieraPage() {
  const { getBankAccounts, isLoading } = useMiNegocioApi();
  const [cuentas, setCuentas] = useState<BankAccount[]>([]);

  useEffect(() => {
    const fetchCuentas = async () => {
      const data = await getBankAccounts();
      if (data && data.results) {
        setCuentas(data.results);
      }
    };
    fetchCuentas();
  }, [getBankAccounts]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Cuentas Bancarias</CardTitle>
      </CardHeader>
      <CardContent>
        {isLoading && cuentas.length === 0 ? (
          <p>Cargando cuentas bancarias...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Banco</TableHead>
                <TableHead>Número de Cuenta</TableHead>
                <TableHead>Titular</TableHead>
                <TableHead>Saldo</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {cuentas.map((cuenta) => (
                <TableRow key={cuenta.id}>
                  <TableCell>{cuenta.bank_name}</TableCell>
                  <TableCell>{cuenta.account_number}</TableCell>
                  <TableCell>{cuenta.account_holder}</TableCell>
                  <TableCell>${cuenta.balance}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
