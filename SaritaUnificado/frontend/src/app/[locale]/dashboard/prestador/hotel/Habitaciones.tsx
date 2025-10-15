'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';

interface Habitacion {
  id: number;
  nombre_o_numero: string;
  tipo_habitacion: 'INDIVIDUAL' | 'DOBLE' | 'SUITE' | 'FAMILIAR';
  capacidad: number;
  precio_por_noche: string;
  disponible: boolean;
}

type FormInputs = Omit<Habitacion, 'id'>;

const Habitaciones = () => {
  const [habitaciones, setHabitaciones] = useState<Habitacion[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingHabitacion, setEditingHabitacion] = useState<Habitacion | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormInputs>();

  const fetchHabitaciones = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/turismo/habitaciones/');
      setHabitaciones(response.data.results || []);
    } catch (err: any) {
      setError('No se pudieron cargar las habitaciones. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchHabitaciones();
  }, [fetchHabitaciones]);

  const openModalForCreate = () => {
    reset({ nombre_o_numero: '', tipo_habitacion: 'INDIVIDUAL', capacidad: 1, precio_por_noche: '0.00', disponible: true });
    setEditingHabitacion(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (habitacion: Habitacion) => {
    setEditingHabitacion(habitacion);
    setValue('nombre_o_numero', habitacion.nombre_o_numero);
    setValue('tipo_habitacion', habitacion.tipo_habitacion);
    setValue('capacidad', habitacion.capacidad);
    setValue('precio_por_noche', habitacion.precio_por_noche);
    setValue('disponible', habitacion.disponible);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingHabitacion(null);
    reset();
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      if (editingHabitacion) {
        await api.patch(`/turismo/habitaciones/${editingHabitacion.id}/`, data);
        toast.success('Habitación actualizada con éxito');
      } else {
        await api.post('/turismo/habitaciones/', data);
        toast.success('Habitación creada con éxito');
      }
      closeModal();
      fetchHabitaciones();
    } catch (err: any) {
      toast.error('Error al guardar la habitación: ' + (err.response?.data?.detail || err.message));
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar esta habitación?')) {
      try {
        await api.delete(`/turismo/habitaciones/${id}/`);
        toast.success('Habitación eliminada con éxito');
        fetchHabitaciones();
      } catch (err: any) {
        toast.error('Error al eliminar la habitación: ' + (err.response?.data?.detail || err.message));
      }
    }
  };

  if (isLoading) return <div>Cargando habitaciones...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Habitaciones</h1>
        <button onClick={openModalForCreate} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Añadir Habitación
        </button>
      </div>

      <Modal isOpen={isModalOpen} onClose={closeModal} title={editingHabitacion ? 'Editar Habitación' : 'Nueva Habitación'}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label>Nombre o Número</label>
            <input {...register('nombre_o_numero', { required: true })} className="mt-1 block w-full" />
          </div>
          <div>
            <label>Tipo de Habitación</label>
            <select {...register('tipo_habitacion')} className="mt-1 block w-full">
              <option value="INDIVIDUAL">Individual</option>
              <option value="DOBLE">Doble</option>
              <option value="SUITE">Suite</option>
              <option value="FAMILIAR">Familiar</option>
            </select>
          </div>
          <div>
            <label>Capacidad</label>
            <input type="number" {...register('capacidad', { required: true, min: 1 })} className="mt-1 block w-full" />
          </div>
          <div>
            <label>Precio por Noche</label>
            <input type="number" step="0.01" {...register('precio_por_noche', { required: true })} className="mt-1 block w-full" />
          </div>
          <div className="flex items-center">
            <input type="checkbox" {...register('disponible')} />
            <label className="ml-2">Disponible</label>
          </div>
          <div className="flex justify-end">
            <button type="submit">Guardar</button>
          </div>
        </form>
      </Modal>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {habitaciones.map((habitacion) => (
          <div key={habitacion.id} className="bg-white p-4 rounded shadow relative">
            <div onClick={() => openModalForEdit(habitacion)} className="cursor-pointer">
              <h3 className="font-bold">{habitacion.nombre_o_numero}</h3>
              <p>{habitacion.tipo_habitacion}</p>
              <p>${habitacion.precio_por_noche} / noche</p>
              <p>{habitacion.disponible ? 'Disponible' : 'No Disponible'}</p>
            </div>
            <button onClick={() => handleDelete(habitacion.id)} className="absolute top-2 right-2 text-red-500 hover:text-red-700">X</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Habitaciones;