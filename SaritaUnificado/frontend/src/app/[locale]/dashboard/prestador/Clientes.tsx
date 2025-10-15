 'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';

interface Cliente {
  id: number;
  pais_origen: string;
  cantidad: number;
  fecha_registro: string;
}

type FormInputs = Omit<Cliente, 'id'>;

const Clientes = () => {
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingCliente, setEditingCliente] = useState<Cliente | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormInputs>();

  const fetchClientes = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/empresa/clientes/');
      setClientes(response.data.results || []);
    } catch (err: any) {
      setError('No se pudieron cargar los clientes. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchClientes();
  }, [fetchClientes]);

  const openModalForCreate = () => {
    reset({
      pais_origen: '',
      cantidad: 1,
      fecha_registro: new Date().toISOString().split('T')[0],
    });
    setEditingCliente(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (cliente: Cliente) => {
    setEditingCliente(cliente);
    setValue('pais_origen', cliente.pais_origen);
    setValue('cantidad', cliente.cantidad);
    setValue('fecha_registro', cliente.fecha_registro);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingCliente(null);
    reset();
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      if (editingCliente) {
        await api.patch(`/empresa/clientes/${editingCliente.id}/`, data);
        toast.success('Registro de cliente actualizado con éxito');
      } else {
        await api.post('/empresa/clientes/', data);
        toast.success('Registro de cliente creado con éxito');
      }
      closeModal();
      fetchClientes();
    } catch (err: any) {
      toast.error('Error al guardar el registro: ' + (err.response?.data?.detail || err.message));
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este registro?')) {
      try {
        await api.delete(`/empresa/clientes/${id}/`);
        toast.success('Registro eliminado con éxito');
        fetchClientes();
      } catch (err: any) {
        toast.error('Error al eliminar el registro: ' + (err.response?.data?.detail || err.message));
      }
    }
  };

  if (isLoading) return <div>Cargando clientes...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Clientes</h1>
        <button
          onClick={openModalForCreate}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Añadir Registro
        </button>
      </div>

      <Modal
        isOpen={isModalOpen}
        onClose={closeModal}
        title={editingCliente ? 'Editar Registro' : 'Nuevo Registro'}
      >
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label htmlFor="pais_origen" className="block text-sm font-medium text-gray-700">
              País de Origen
            </label>
            <input
              id="pais_origen"
              {...register('pais_origen', { required: true })}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
            />
          </div>
          <div>
            <label htmlFor="cantidad" className="block text-sm font-medium text-gray-700">
              Cantidad
            </label>
            <input
              id="cantidad"
              type="number"
              {...register('cantidad', { required: true, valueAsNumber: true, min: 1 })}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
            />
          </div>
          <div>
            <label htmlFor="fecha_registro" className="block text-sm font-medium text-gray-700">
              Fecha de Registro
            </label>
            <input
              id="fecha_registro"
              type="date"
              {...register('fecha_registro', { required: true })}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
            />
          </div>
          <div className="flex justify-end space-x-2">
            <button
              type="button"
              onClick={closeModal}
              className="px-4 py-2 bg-gray-200 rounded"
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="px-4 py-2 bg-blue-600 text-white rounded"
            >
              Guardar
            </button>
          </div>
        </form>
      </Modal>

      {clientes.length === 0 ? (
        <p>No tienes clientes registrados.</p>
      ) : (
        <table className="min-w-full bg-white">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b text-left">País de Origen</th>
              <th className="py-2 px-4 border-b text-left">Cantidad</th>
              <th className="py-2 px-4 border-b text-left">Fecha de Registro</th>
              <th className="py-2 px-4 border-b text-left">Acciones</th>
            </tr>
          </thead>
          <tbody>
            {clientes.map((cliente) => (
              <tr key={cliente.id}>
                <td className="py-2 px-4 border-b">{cliente.pais_origen}</td>
                <td className="py-2 px-4 border-b">{cliente.cantidad}</td>
                <td className="py-2 px-4 border-b">{cliente.fecha_registro}</td>
                <td className="py-2 px-4 border-b">
                  <button
                    onClick={() => openModalForEdit(cliente)}
                    className="text-blue-500 hover:underline mr-2"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(cliente.id)}
                    className="text-red-500 hover:underline"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Clientes;