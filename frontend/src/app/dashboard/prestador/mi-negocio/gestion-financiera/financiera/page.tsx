'use client';
import React from 'react';
import { useFinancieraApi } from '@/app/dashboard/prestador/mi-negocio/hooks/useFinancieraApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Badge } from '@/components/ui/Badge';
import { format } from 'date-fns';

const FinancieraPage = () => {
    const {
        bankAccounts, bankAccountsLoading,
        cashTransactions, cashTransactionsLoading
    } = useFinancieraApi();

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Módulo Financiero</h1>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div className="lg:col-span-1">
                    <Card>
                        <CardHeader><CardTitle>Cuentas Bancarias</CardTitle></CardHeader>
                        <CardContent>
                            {bankAccountsLoading && <p>Cargando...</p>}
                            <div className="space-y-4">
                                {bankAccounts.map(account => (
                                    <div key={account.id} className="p-3 bg-gray-50 rounded-lg">
                                        <p className="font-semibold">{account.name}</p>
                                        <p className="text-sm text-gray-600">{account.bank_name} - {account.account_number}</p>
                                    </div>
                                ))}
                            </div>
                        </CardContent>
                    </Card>
                </div>

                <div className="lg:col-span-2">
                    <Card>
                        <CardHeader><CardTitle>Últimos Movimientos</CardTitle></CardHeader>
                        <CardContent>
                            {cashTransactionsLoading && <p>Cargando...</p>}
                            <Table>
                                <TableHeader><TableRow><TableHead>Fecha</TableHead><TableHead>Descripción</TableHead><TableHead>Tipo</TableHead><TableHead className="text-right">Monto</TableHead></TableRow></TableHeader>
                                <TableBody>
                                    {cashTransactions.slice(0, 10).map(tx => (
                                        <TableRow key={tx.id}>
                                            <TableCell>{format(new Date(tx.transaction_date), 'dd/MM/yyyy')}</TableCell>
                                            <TableCell>{tx.description}</TableCell>
                                            <TableCell>
                                                <Badge variant={tx.transaction_type === 'INFLOW' ? 'default' : 'destructive'}>
                                                    {tx.transaction_type}
                                                </Badge>
                                            </TableCell>
                                            <TableCell className="text-right font-mono">${parseFloat(tx.amount).toLocaleString('es-CO')}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </CardContent>
                    </Card>
                </div>
            </div>
        </div>
    );
};

export default FinancieraPage;
