'use client';
import React, { useEffect, useState, useCallback } from 'react';
import { useMiNegocioApi, BankAccount } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Button } from '@/components/ui/Button';
import { toast } from 'react-toastify';
import Link from 'next/link';
import Modal from '@/components/ui/Modal';
import CuentaBancariaForm from './components/CuentaBancariaForm';
import { Input } from '@/components/ui/Input';

type FormValues = {
  banco: string;
  numero_cuenta: string;
  titular: string;
  tipo_cuenta: 'AHORROS' | 'CORRIENTE';
};

export default function GestionFinancieraPage() {
  const { getBankAccounts, createBankAccount, updateBankAccount, deleteBankAccount, isLoading } = useMiNegocioApi();
  const [cuentas, setCuentas] = useState<BankAccount[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedAccount, setSelectedAccount] = useState<BankAccount | null>(null);
  const [searchTerm, setSearchTerm] = useState('');

  const filteredCuentas = cuentas.filter(cuenta =>
    cuenta.bank_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    cuenta.account_holder.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const fetchCuentas = useCallback(async () => {
    const data = await getBankAccounts();
    if (data) {
      setCuentas(data.results || []);
    }
  }, [getBankAccounts]);

  useEffect(() => {
    fetchCuentas();
  }, [fetchCuentas]);

  const handleOpenModal = (cuenta: BankAccount | null = null) => {
    setSelectedAccount(cuenta);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setSelectedAccount(null);
    setIsModalOpen(false);
  };

  const handleSubmit = async (values: FormValues) => {
    const apiData = {
        bank_name: values.banco,
        account_number: values.numero_cuenta,
        account_holder: values.titular,
        account_type: values.tipo_cuenta,
    };

    let success;
    if (selectedAccount) {
      success = await updateBankAccount(selectedAccount.id, apiData);
    } else {
      success = await createBankAccount(apiData);
    }

    if (success) {
      fetchCuentas();
      handleCloseModal();
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar esta cuenta?')) {
      const success = await deleteBankAccount(id);
      if (success) {
        fetchCuentas();
      }
    }
  };

  return (
    <>
      <Card>
        <CardHeader className="flex flex-row items-center justify-between">
          <CardTitle>Cuentas Bancarias</CardTitle>
          <Button onClick={() => handleOpenModal()}>
            Nueva Cuenta
          </Button>
        </CardHeader>
        <CardContent>
          <div className="mb-4">
            <Input
              placeholder="Buscar por banco o titular..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
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
                  <TableHead>Acciones</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {filteredCuentas.map((cuenta) => (
                  <TableRow key={cuenta.id}>
                    <TableCell>{cuenta.bank_name}</TableCell>
                    <TableCell>
                      <Link href={`/dashboard/prestador/mi-negocio/gestion-financiera/${cuenta.id}`} className="text-blue-600 hover:underline">
                        {cuenta.account_number}
                      </Link>
                    </TableCell>
                    <TableCell>{cuenta.account_holder}</TableCell>
                    <TableCell>${cuenta.balance}</TableCell>
                    <TableCell>
                      <div className="flex space-x-2">
                         <Button variant="outline" size="sm" onClick={() => handleOpenModal(cuenta)}>
                           Editar
                         </Button>
                         <Button variant="destructive" size="sm" onClick={() => handleDelete(cuenta.id)}>
                           Eliminar
                         </Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          )}
        </CardContent>
      </Card>

      {isModalOpen && (
        <Modal title={selectedAccount ? 'Editar Cuenta Bancaria' : 'Nueva Cuenta Bancaria'} isOpen={isModalOpen} onClose={handleCloseModal}>
          <CuentaBancariaForm
            onSubmit={handleSubmit}
            initialData={selectedAccount || undefined}
            isSubmitting={isLoading}
          />
        </Modal>
      )}
    </>
  );
}
