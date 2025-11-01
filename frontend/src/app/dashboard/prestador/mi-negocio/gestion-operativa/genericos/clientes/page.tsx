'use client';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useMiNegocioApi, Cliente } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Button } from '@/components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { PlusCircle } from 'lucide-react';

export default function ClientesPage() {
  const { getClientes, isLoading } = useMiNegocioApi();
  const [clientes, setClientes] = useState<Cliente[]>([]);

  useEffect(() => {
    const fetchClientes = async () => {
      const data = await getClientes();
      if (data) {
        setClientes(data);
      }
    };
    fetchClientes();
  }, [getClientes]);

  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle>Gestión de Clientes</CardTitle>
        <Link href="/dashboard/prestador/mi-negocio/gestion-operativa/genericos/clientes/nuevo" passHref>
          <Button>
            <PlusCircle className="mr-2 h-4 w-4" />
            Nuevo Cliente
          </Button>
        </Link>
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <p>Cargando clientes...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Nombre</TableHead>
                <TableHead>Email</TableHead>
                <TableHead>Teléfono</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {clientes.map((cliente) => (
                <TableRow key={cliente.id}>
                  <TableCell>{cliente.nombre}</TableCell>
                  <TableCell>{cliente.email}</TableCell>
                  <TableCell>{cliente.telefono || 'N/A'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
