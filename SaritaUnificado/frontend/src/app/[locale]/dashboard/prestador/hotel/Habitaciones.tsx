'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos
type Habitacion = {
  id: number;
  nombre_o_numero: string;
  tipo_habitacion: string;
  capacidad: number;
  precio_por_noche: string;
};

type HabitacionFormInputs = Omit<Habitacion, 'id'>;

const HabitacionesPage = () => {
  const [habitaciones, setHabitaciones] = useState<Habitacion[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingHabitacion, setEditingHabitacion] = useState<Habitacion | null>(null);

  const { register, handleSubmit, reset } = useForm<HabitacionFormInputs>();

  const fetchHabitaciones = async () => {
    setIsLoading(true);
    try {
      const response = await api.get<Habitacion[]>('/turismo/habitaciones/');
      setHabitaciones(response.data.results || response.data);
    } catch (error) {
      toast.error("Error al cargar las habitaciones.");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchHabitaciones();
  }, []);

  const openCreateModal = () => {
    setEditingHabitacion(null);
    reset({ nombre_o_numero: '', tipo_habitacion: '', capacidad: 1, precio_por_noche: '0.00' });
    setIsModalOpen(true);
  };

  const openEditModal = (habitacion: Habitacion) => {
    setEditingHabitacion(habitacion);
    reset(habitacion);
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<HabitacionFormInputs> = async (data) => {
    try {
      if (editingHabitacion) {
        await api.put(`/turismo/habitaciones/${editingHabitacion.id}/`, data);
        toast.success('Habitación actualizada con éxito.');
      } else {
        await api.post('/turismo/habitaciones/', data);
        toast.success('Habitación creada con éxito.');
      }
      fetchHabitaciones();
      setIsModalOpen(false);
    } catch (error) {
      toast.error('No se pudo guardar la habitación.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro?')) {
      try {
        await api.delete(`/turismo/habitaciones/${id}/`);
        toast.success('Habitación eliminada.');
        fetchHabitaciones();
      } catch (error) {
        toast.error('No se pudo eliminar la habitación.');
      }
    }
  };

  if (isLoading) return <div>Cargando...</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Habitaciones</h1>
        <button onClick={openCreateModal} className="bg-blue-600 text-white font-bold py-2 px-4 rounded flex items-center"><FiPlus className="mr-2" />Añadir Habitación</button>
      </div>

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left">Nombre/Número</th>
                <th className="px-6 py-3 text-left">Tipo</th>
                <th className="px-6 py-3 text-left">Capacidad</th>
                <th className="px-6 py-3 text-left">Precio/Noche</th>
                <th className="px-6 py-3 text-right">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {habitaciones.map((hab) => (
                <tr key={hab.id}>
                  <td className="px-6 py-4">{hab.nombre_o_numero}</td>
                  <td className="px-6 py-4">{hab.tipo_habitacion}</td>
                  <td className="px-6 py-4">{hab.capacidad}</td>
                  <td className="px-6 py-4">${hab.precio_por_noche}</td>
                  <td className="px-6 py-4 text-right">
                    <button onClick={() => openEditModal(hab)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(hab.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {isModalOpen && (
            <Modal title={editingHabitacion ? 'Editar Habitación' : 'Nueva Habitación'} onClose={() => setIsModalOpen(false)}>
                <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 p-4">
                    <div>
                        <label>Nombre / Número</label>
                        <input {...register('nombre_o_numero', { required: true })} className="w-full p-2 border rounded" />
                    </div>
                    <div>
                        <label>Tipo (ej. Doble, Suite)</label>
                        <input {...register('tipo_habitacion', { required: true })} className="w-full p-2 border rounded" />
                    </div>
                    <div>
                        <label>Capacidad</label>
                        <input type="number" {...register('capacidad', { required: true, valueAsNumber: true, min: 1 })} className="w-full p-2 border rounded" />
                    </div>
                    <div>
                        <label>Precio por Noche</label>
                        <input type="number" step="0.01" {...register('precio_por_noche', { required: true })} className="w-full p-2 border rounded" />
                    </div>
                    <div className="flex justify-end pt-4">
                        <button type="submit" className="bg-blue-600 text-white font-bold py-2 px-4 rounded">Guardar</button>
                    </div>
                </form>
            </Modal>
        )}
    </div>
  );
};

export default HabitacionesPage;