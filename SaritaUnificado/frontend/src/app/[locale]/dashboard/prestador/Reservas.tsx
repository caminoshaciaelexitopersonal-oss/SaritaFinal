'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipado para el cliente (necesario para el dropdown)
type Cliente = {
  id: number;
  nombre: string;
};

// Tipado para la reserva
type Reserva = {
  id: number;
  cliente: number;
  cliente_info: Cliente;
  fecha_reserva: string;
  numero_personas: number;
  estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
  notas_reserva: string | null;
};

type ReservaFormInputs = {
    cliente: number;
    fecha_reserva: string;
    numero_personas: number;
    estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
    notas_reserva: string;
};

const estadoChoices = ['PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'COMPLETADA'];

const Reservas = () => {
  const [reservas, setReservas] = useState<Reserva[]>([]);
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingReserva, setEditingReserva] = useState<Reserva | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors },
  } = useForm<ReservaFormInputs>();

  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const [reservasRes, clientesRes] = await Promise.all([
          api.get<Reserva[]>('/turismo/reservas/'),
          api.get<Cliente[]>('/empresa/gestion-clientes/')
        ]);
        setReservas(reservasRes.data);
        setClientes(clientesRes.data);
        setError(null);
      } catch (err) {
        setError('No se pudieron cargar los datos de reservas o clientes.');
        toast.error('Error al cargar datos.');
      } finally {
        setIsLoading(false);
      }
    };
    fetchData();
  }, []);

  const openCreateModal = () => {
    setEditingReserva(null);
    reset({
      cliente: clientes[0]?.id,
      fecha_reserva: new Date().toISOString().slice(0, 16), // Formato para datetime-local
      numero_personas: 1,
      estado: 'PENDIENTE',
      notas_reserva: '',
    });
    setIsModalOpen(true);
  };

  const openEditModal = (reserva: Reserva) => {
    setEditingReserva(reserva);
    reset({
        cliente: reserva.cliente,
        fecha_reserva: new Date(reserva.fecha_reserva).toISOString().slice(0, 16),
        numero_personas: reserva.numero_personas,
        estado: reserva.estado,
        notas_reserva: reserva.notas_reserva || ''
    });
    setIsModalOpen(true);
  };

  const closeModal = () => setIsModalOpen(false);

  const onSubmit: SubmitHandler<ReservaFormInputs> = async (data) => {
    try {
      if (editingReserva) {
        await api.put(`/turismo/reservas/${editingReserva.id}/`, data);
        toast.success('¡Reserva actualizada!');
      } else {
        await api.post('/turismo/reservas/', data);
        toast.success('¡Reserva creada!');
      }
      const res = await api.get<Reserva[]>('/turismo/reservas/');
      setReservas(res.data);
      closeModal();
    } catch (err) {
      toast.error('Ocurrió un error al guardar la reserva.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Seguro que quieres eliminar esta reserva?')) {
      try {
        await api.delete(`/turismo/reservas/${id}/`);
        toast.success('Reserva eliminada.');
        setReservas(reservas.filter(r => r.id !== id));
      } catch (err) {
        toast.error('No se pudo eliminar la reserva.');
      }
    }
  };

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Reservas</h1>
        <button onClick={openCreateModal} disabled={clientes.length === 0} className="bg-cyan-600 hover:bg-cyan-700 text-white font-bold py-2 px-4 rounded-full flex items-center disabled:bg-gray-400">
          <FiPlus className="mr-2" /> Nueva Reserva
        </button>
      </div>
       {clientes.length === 0 && <p className="text-yellow-600 bg-yellow-100 p-2 rounded-md">Debe añadir al menos un cliente en el módulo de Clientes (CRM) para poder crear una reserva.</p>}

      {reservas.length === 0 ? (
        <p className="mt-4">No tienes reservas registradas.</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden mt-4">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Cliente</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Fecha</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Personas</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Estado</th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {reservas.map((reserva) => (
                <tr key={reserva.id}>
                  <td className="px-6 py-4">{reserva.cliente_info?.nombre || 'Cliente eliminado'}</td>
                  <td className="px-6 py-4">{new Date(reserva.fecha_reserva).toLocaleString()}</td>
                  <td className="px-6 py-4">{reserva.numero_personas}</td>
                  <td className="px-6 py-4">{reserva.estado}</td>
                  <td className="px-6 py-4 text-right">
                    <button onClick={() => openEditModal(reserva)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(reserva.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal title={editingReserva ? 'Editar Reserva' : 'Nueva Reserva'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
                <label htmlFor="cliente">Cliente</label>
                <select id="cliente" {...register('cliente', {valueAsNumber: true})}>
                    {clientes.map(c => <option key={c.id} value={c.id}>{c.nombre}</option>)}
                </select>
            </div>
            <input type="datetime-local" {...register('fecha_reserva', { required: true })} />
            <input type="number" {...register('numero_personas', { required: true, valueAsNumber: true, min: 1 })} placeholder="Nº de personas"/>
            <select {...register('estado')}>
                {estadoChoices.map(e => <option key={e} value={e}>{e}</option>)}
            </select>
            <textarea {...register('notas_reserva')} placeholder="Notas adicionales..." />
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

export default Reservas;