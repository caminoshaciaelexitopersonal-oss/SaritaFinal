'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipado para el nuevo modelo Cliente (CRM)
type Cliente = {
  id: number;
  nombre: string;
  email: string | null;
  telefono: string | null;
  notas: string | null;
};

type ClienteFormInputs = Omit<Cliente, 'id'>;

const Clientes = () => {
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingCliente, setEditingCliente] = useState<Cliente | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors },
  } = useForm<ClienteFormInputs>();

  const fetchClientes = async () => {
    try {
      setIsLoading(true);
      // Usamos el nuevo endpoint para el CRM de clientes
      const response = await api.get<Cliente[]>('/empresa/gestion-clientes/');
      setClientes(response.data);
      setError(null);
    } catch (err) {
      setError('No se pudieron cargar los clientes.');
      toast.error('Error al cargar clientes.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchClientes();
  }, []);

  const openCreateModal = () => {
    setEditingCliente(null);
    reset({ nombre: '', email: '', telefono: '', notas: '' });
    setIsModalOpen(true);
  };

  const openEditModal = (cliente: Cliente) => {
    setEditingCliente(cliente);
    reset(cliente);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingCliente(null);
  };

  const onSubmit: SubmitHandler<ClienteFormInputs> = async (data) => {
    try {
      if (editingCliente) {
        await api.put(`/empresa/gestion-clientes/${editingCliente.id}/`, data);
        toast.success('¡Cliente actualizado con éxito!');
      } else {
        await api.post('/empresa/gestion-clientes/', data);
        toast.success('¡Cliente creado con éxito!');
      }
      fetchClientes();
      closeModal();
    } catch (err: any) {
        const errorMsg = err.response?.data?.email?.[0] || 'Ocurrió un error al guardar el cliente.';
        toast.error(errorMsg);
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este cliente?')) {
      try {
        await api.delete(`/empresa/gestion-clientes/${id}/`);
        toast.success('Cliente eliminado con éxito.');
        fetchClientes();
      } catch (err) {
        toast.error('No se pudo eliminar el cliente.');
      }
    }
  };

  if (isLoading) return <div>Cargando clientes...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Clientes (CRM)</h1>
        <button
          onClick={openCreateModal}
          className="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-full flex items-center"
        >
          <FiPlus className="mr-2" /> Añadir Cliente
        </button>
      </div>

      {clientes.length === 0 ? (
        <p>No tienes clientes registrados en tu CRM.</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Email</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Teléfono</th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {clientes.map((cliente) => (
                <tr key={cliente.id}>
                  <td className="px-6 py-4">{cliente.nombre}</td>
                  <td className="px-6 py-4">{cliente.email || 'N/A'}</td>
                  <td className="px-6 py-4">{cliente.telefono || 'N/A'}</td>
                  <td className="px-6 py-4 text-right">
                    <button onClick={() => openEditModal(cliente)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(cliente.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal title={editingCliente ? 'Editar Cliente' : 'Nuevo Cliente'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <input {...register('nombre', { required: true })} placeholder="Nombre completo" />
            <input type="email" {...register('email')} placeholder="Correo electrónico" />
            <input {...register('telefono')} placeholder="Teléfono" />
            <textarea {...register('notas')} placeholder="Notas adicionales..." />
            <div className="flex justify-end space-x-2">
              <button type="button" onClick={closeModal} className="bg-gray-200 text-gray-800 font-bold py-2 px-4 rounded">Cancelar</button>
              <button type="submit" disabled={isSubmitting} className="bg-indigo-600 text-white font-bold py-2 px-4 rounded">
                {isSubmitting ? 'Guardando...' : 'Guardar'}
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default Clientes;