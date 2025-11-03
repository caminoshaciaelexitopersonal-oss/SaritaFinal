'use client';
import React, { useEffect, useState, useCallback } from 'react';
import Link from 'next/link';
import { useMiNegocioApi, Cliente } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Button } from '@/components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { PlusCircle, Edit, Trash2 } from 'lucide-react';
import { toast } from 'react-toastify';

export default function ClientesPage() {
  const { getClientes, deleteCliente, isLoading } = useMiNegocioApi();
  const [clientes, setClientes] = useState<Cliente[]>([]);

  const fetchClientes = useCallback(async () => {
    const data = await getClientes();
    if (data) {
      // La API devuelve un objeto con 'results', accedemos a él
      setClientes(data.results || []);
    }
  }, [getClientes]);

  useEffect(() => {
    fetchClientes();
  }, [fetchClientes]);

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este cliente?')) {
      const success = await deleteCliente(id);
      if (success) {
        toast.success('Cliente eliminado con éxito');
        fetchClientes(); // Recargar la lista de clientes
      }
    }
  };

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
        {isLoading && clientes.length === 0 ? (
          <p>Cargando clientes...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Nombre</TableHead>
                <TableHead>Email</TableHead>
                <TableHead>Teléfono</TableHead>
                <TableHead>Acciones</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {clientes.map((cliente) => (
                <TableRow key={cliente.id}>
                  <TableCell>{cliente.nombre}</TableCell>
                  <TableCell>{cliente.email}</TableCell>
                  <TableCell>{cliente.telefono || 'N/A'}</TableCell>
                  <TableCell>
                    <Link href={`/dashboard/prestador/mi-negocio/gestion-operativa/genericos/clientes/editar/${cliente.id}`} passHref>
                       <Button variant="outline" size="sm" className="mr-2">
                          <Edit className="h-4 w-4" />
                       </Button>
                    </Link>
                    <Button variant="destructive" size="sm" onClick={() => handleDelete(cliente.id)}>
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
