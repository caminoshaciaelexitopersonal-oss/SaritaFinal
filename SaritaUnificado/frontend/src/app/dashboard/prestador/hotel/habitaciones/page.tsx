'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiBed, FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Habitacion {
  id: number;
  nombre_o_numero: string;
  tipo_habitacion: 'INDIVIDUAL' | 'DOBLE' | 'SUITE' | 'FAMILIAR';
  capacidad: number;
  precio_por_noche: string;
  disponible: boolean;
}

type FormData = Omit<Habitacion, 'id'>;

const HabitacionesManager = () => {
  const [habitaciones, setHabitaciones] = useState<Habitacion[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingHabitacion, setEditingHabitacion] = useState<Habitacion | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormData>();

  const fetchHabitaciones = async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/turismo/hotel/habitaciones/');
      setHabitaciones(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar las habitaciones.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchHabitaciones();
  }, []);

  const openModalForCreate = () => {
    reset();
    setEditingHabitacion(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (hab: Habitacion) => {
    setEditingHabitacion(hab);
    setValue('nombre_o_numero', hab.nombre_o_numero);
    setValue('tipo_habitacion', hab.tipo_habitacion);
    setValue('capacidad', hab.capacidad);
    setValue('precio_por_noche', hab.precio_por_noche);
    setValue('disponible', hab.disponible);
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<FormData> = async (data) => {
    const apiCall = editingHabitacion
      ? api.patch(`/turismo/hotel/habitaciones/${editingHabitacion.id}/`, data)
      : api.post('/turismo/hotel/habitaciones/', data);

    try {
      await apiCall;
      toast.success(`Habitación ${editingHabitacion ? 'actualizada' : 'creada'} con éxito.`);
      fetchHabitaciones();
      setIsModalOpen(false);
    } catch (error) {
      toast.error('Error al guardar la habitación.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar esta habitación?')) {
        try {
            await api.delete(`/turismo/hotel/habitaciones/${id}/`);
            toast.success('Habitación eliminada.');
            fetchHabitaciones();
        } catch (error) {
            toast.error('No se pudo eliminar la habitación.');
        }
    }
  }

  if (isLoading) {
    return <div>Cargando habitaciones...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Habitaciones</h1>
        <button onClick={openModalForCreate} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          <FiPlus className="mr-2" />
          Añadir Habitación
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {habitaciones.length > 0 ? habitaciones.map(hab => (
            <div key={hab.id} className="p-4 border rounded-lg shadow-sm">
                <div className="flex justify-between items-start">
                    <h3 className="font-bold text-xl text-gray-800">{hab.nombre_o_numero}</h3>
                    <span className={`px-2 py-1 text-xs font-semibold rounded-full ${hab.disponible ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                        {hab.disponible ? 'Disponible' : 'No Disponible'}
                    </span>
                </div>
                <p className="text-sm text-gray-600">{hab.tipo_habitacion}</p>
                <p className="text-lg font-semibold text-gray-900 mt-2">${hab.precio_por_noche} / noche</p>
                <p className="text-sm text-gray-500">Capacidad: {hab.capacidad} personas</p>
                <div className="flex justify-end space-x-2 mt-4">
                    <button onClick={() => openModalForEdit(hab)} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                    <button onClick={() => handleDelete(hab.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                </div>
            </div>
        )) : (
            <p className="col-span-full text-center text-gray-500">No hay habitaciones registradas.</p>
        )}
      </div>

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingHabitacion ? "Editar Habitación" : "Crear Nueva Habitación"}>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <div>
                    <label>Nombre o Número</label>
                    <input {...register('nombre_o_numero', { required: true })} className="w-full mt-1 p-2 border rounded"/>
                </div>
                <div>
                    <label>Tipo de Habitación</label>
                    <select {...register('tipo_habitacion', { required: true })} className="w-full mt-1 p-2 border rounded">
                        <option value="INDIVIDUAL">Individual</option>
                        <option value="DOBLE">Doble</option>
                        <option value="SUITE">Suite</option>
                        <option value="FAMILIAR">Familiar</option>
                    </select>
                </div>
                <div>
                    <label>Capacidad</label>
                    <input type="number" {...register('capacidad', { required: true, valueAsNumber: true })} className="w-full mt-1 p-2 border rounded"/>
                </div>
                <div>
                    <label>Precio por Noche</label>
                    <input type="text" {...register('precio_por_noche', { required: true })} className="w-full mt-1 p-2 border rounded"/>
                </div>
                <div className="flex items-center">
                    <input type="checkbox" {...register('disponible')} className="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"/>
                    <label className="ml-2 block text-sm text-gray-900">Disponible</label>
                </div>
                <div className="text-right">
                    <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">Guardar</button>
                </div>
            </form>
        </Modal>
      )}
    </div>
  );
};

const HabitacionesPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <HabitacionesManager />
        </AuthGuard>
    )
}

export default HabitacionesPage;