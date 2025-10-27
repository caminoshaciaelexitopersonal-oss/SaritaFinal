'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import useMiNegocioApi from '../../app/dashboard/prestador/mi-negocio/ganchos/useMiNegocioApi';
import FormField from '@/components/ui/FormField';
import { Button } from '@/components/ui/Button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { FiEdit, FiTrash2 } from 'react-icons/fi';

interface Cliente {
  id: number;
  nombre: string;
  email: string;
  telefono: string;
  notas: string;
}

type ClienteFormData = Omit<Cliente, 'id'>;

const ClienteManager = () => {
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [editingCliente, setEditingCliente] = useState<Cliente | null>(null);
  const { request, loading: apiLoading } = useMiNegocioApi();

  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ClienteFormData>();

  const fetchClientes = useCallback(async () => {
    try {
      const response = await request('/clientes/');
      setClientes(response.results || response);
    } catch (error) {
      toast.error('Error al cargar los clientes.');
    }
  }, [request]);

  useEffect(() => {
    fetchClientes();
  }, [fetchClientes]);

  const onSubmit: SubmitHandler<ClienteFormData> = async (data) => {
    try {
      if (editingCliente) {
        await request(`/clientes/${editingCliente.id}/`, {
          method: 'PUT',
          body: JSON.stringify(data),
        });
        toast.success('Cliente actualizado con éxito.');
      } else {
        await request('/clientes/', {
          method: 'POST',
          body: JSON.stringify(data),
        });
        toast.success('Cliente creado con éxito.');
      }
      reset();
      setEditingCliente(null);
      fetchClientes();
    } catch (error) {
      toast.error('Ocurrió un error al guardar el cliente.');
    }
  };

  const handleEdit = (cliente: Cliente) => {
    setEditingCliente(cliente);
    Object.keys(cliente).forEach((key) => {
      setValue(key as keyof ClienteFormData, cliente[key as keyof Cliente]);
    });
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este cliente?')) {
      try {
        await request(`/clientes/${id}/`, { method: 'DELETE' });
        toast.success('Cliente eliminado con éxito.');
        fetchClientes();
      } catch (error) {
        toast.error('Error al eliminar el cliente.');
      }
    }
  };

  const handleCancelEdit = () => {
    setEditingCliente(null);
    reset();
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Gestión de Clientes (CRM)</h1>

      <div className="bg-white p-6 rounded-lg shadow-md mb-8">
        <h2 className="text-xl font-semibold mb-4">{editingCliente ? 'Editar Cliente' : 'Crear Nuevo Cliente'}</h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <FormField name="nombre" label="Nombre Completo" register={register} errors={errors} required />
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <FormField name="email" label="Correo Electrónico" type="email" register={register} errors={errors} />
            <FormField name="telefono" label="Teléfono" register={register} errors={errors} />
          </div>
          <FormField name="notas" label="Notas Adicionales" type="textarea" register={register} errors={errors} />
          <div className="flex space-x-4">
            <Button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Guardando...' : (editingCliente ? 'Actualizar Cliente' : 'Crear Cliente')}
            </Button>
            {editingCliente && (
              <Button variant="outline" onClick={handleCancelEdit}>
                Cancelar Edición
              </Button>
            )}
          </div>
        </form>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">Listado de Clientes</h2>
        {apiLoading ? (
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
                  <TableCell className="font-medium">{cliente.nombre}</TableCell>
                  <TableCell>{cliente.email}</TableCell>
                  <TableCell>{cliente.telefono}</TableCell>
                  <TableCell>
                    <div className="flex space-x-2">
                      <Button variant="icon" onClick={() => handleEdit(cliente)}>
                        <FiEdit className="h-4 w-4" />
                      </Button>
                      <Button variant="icon" color="danger" onClick={() => handleDelete(cliente.id)}>
                        <FiTrash2 className="h-4 w-4" />
                      </Button>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </div>
    </div>
  );
};

export default ClienteManager;