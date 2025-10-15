'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';

interface Reserva {
  id: number;
  cliente_nombre: string;
  nombre_cliente_externo: string;
  fecha_inicio: string;
  fecha_fin: string;
  estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
}

type FormInputs = Omit<Reserva, 'id' | 'cliente_nombre'>;

const Reservas = () => {
  const [reservas, setReservas] = useState<Reserva[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingReserva, setEditingReserva] = useState<Reserva | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormInputs>();

  const fetchReservas = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/turismo/reservas/');
      setReservas(response.data.results || []);
    } catch (err: any) {
      setError('No se pudieron cargar las reservas. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchReservas();
  }, [fetchReservas]);

  const openModalForCreate = () => {
    reset({ nombre_cliente_externo: '', fecha_inicio: '', fecha_fin: '', estado: 'PENDIENTE' });
    setEditingReserva(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (reserva: Reserva) => {
    setEditingReserva(reserva);
    setValue('nombre_cliente_externo', reserva.nombre_cliente_externo);
    setValue('fecha_inicio', reserva.fecha_inicio.slice(0, 16));
    setValue('fecha_fin', reserva.fecha_fin.slice(0, 16));
    setValue('estado', reserva.estado);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingReserva(null);
    reset();
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      if (editingReserva) {
        await api.patch(`/turismo/reservas/${editingReserva.id}/`, data);
        toast.success('Reserva actualizada con éxito');
      } else {
        await api.post('/turismo/reservas/', data);
        toast.success('Reserva creada con éxito');
      }
      closeModal();
      fetchReservas();
    } catch (err: any) {
      toast.error('Error al guardar la reserva: ' + (err.response?.data?.detail || err.message));
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar esta reserva?')) {
      try {
        await api.delete(`/turismo/reservas/${id}/`);
        toast.success('Reserva eliminada con éxito');
        fetchReservas();
      } catch (err: any) {
        toast.error('Error al eliminar la reserva: ' + (err.response?.data?.detail || err.message));
      }
    }
  };

  if (isLoading) return <div>Cargando reservas...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Reservas</h1>
        <button onClick={openModalForCreate} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Añadir Reserva
        </button>
      </div>

      <Modal isOpen={isModalOpen} onClose={closeModal} title={editingReserva ? 'Editar Reserva' : 'Nueva Reserva'}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label>Nombre del Cliente</label>
            <input {...register('nombre_cliente_externo', { required: true })} className="mt-1 block w-full" />
          </div>
          <div>
            <label>Fecha y Hora de Inicio</label>
            <input type="datetime-local" {...register('fecha_inicio', { required: true })} className="mt-1 block w-full" />
          </div>
          <div>
            <label>Fecha y Hora de Fin</label>
            <input type="datetime-local" {...register('fecha_fin', { required: true })} className="mt-1 block w-full" />
          </div>
          <div>
            <label>Estado</label>
            <select {...register('estado')} className="mt-1 block w-full">
              <option value="PENDIENTE">Pendiente</option>
              <option value="CONFIRMADA">Confirmada</option>
              <option value="CANCELADA">Cancelada</option>
              <option value="COMPLETADA">Completada</option>
            </select>
          </div>
          <div className="flex justify-end">
            <button type="submit">Guardar</button>
          </div>
        </form>
      </Modal>

      <table className="min-w-full bg-white">
        <thead>
          <tr>
            <th className="py-2 px-4 border-b text-left">Cliente</th>
            <th className="py-2 px-4 border-b text-left">Desde</th>
            <th className="py-2 px-4 border-b text-left">Hasta</th>
            <th className="py-2 px-4 border-b text-left">Estado</th>
            <th className="py-2 px-4 border-b text-left">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {reservas.map((reserva) => (
            <tr key={reserva.id}>
              <td className="py-2 px-4 border-b">{reserva.cliente_nombre || reserva.nombre_cliente_externo}</td>
              <td className="py-2 px-4 border-b">{new Date(reserva.fecha_inicio).toLocaleString()}</td>
              <td className="py-2 px-4 border-b">{new Date(reserva.fecha_fin).toLocaleString()}</td>
              <td className="py-2 px-4 border-b">{reserva.estado}</td>
              <td className="py-2 px-4 border-b">
                <button onClick={() => openModalForEdit(reserva)} className="text-blue-500 hover:underline mr-2">Editar</button>
                <button onClick={() => handleDelete(reserva.id)} className="text-red-500 hover:underline">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Reservas;