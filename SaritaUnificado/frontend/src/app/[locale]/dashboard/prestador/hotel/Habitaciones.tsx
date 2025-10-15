'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipado para una habitación, basado en HabitacionSerializer
type Habitacion = {
  id: number;
  nombre_o_numero: string;
  tipo_habitacion: 'INDIVIDUAL' | 'DOBLE' | 'SUITE' | 'FAMILIAR';
  capacidad: number;
  precio_por_noche: string;
  disponible: boolean;
};

// Tipado para el formulario (sin el id)
type HabitacionFormInputs = Omit<Habitacion, 'id'>;

const tipoHabitacionChoices = [
    { value: 'INDIVIDUAL', label: 'Individual' },
    { value: 'DOBLE', label: 'Doble' },
    { value: 'SUITE', label: 'Suite' },
    { value: 'FAMILIAR', label: 'Familiar' },
];

const Habitaciones = () => {
  const [habitaciones, setHabitaciones] = useState<Habitacion[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingHabitacion, setEditingHabitacion] = useState<Habitacion | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors },
  } = useForm<HabitacionFormInputs>();

  const fetchHabitaciones = async () => {
    try {
      setIsLoading(true);
      const response = await api.get<Habitacion[]>('/turismo/habitaciones/');
      setHabitaciones(response.data);
      setError(null);
    } catch (err: any) {
      if(err.response && err.response.status === 404) {
          setError('No tiene un perfil de hotel configurado para gestionar habitaciones.');
          toast.warn('Perfil de hotel no encontrado.');
      } else {
          setError('No se pudieron cargar las habitaciones.');
          toast.error('Error al cargar habitaciones.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchHabitaciones();
  }, []);

  const openCreateModal = () => {
    setEditingHabitacion(null);
    reset({
      nombre_o_numero: '',
      tipo_habitacion: 'INDIVIDUAL',
      capacidad: 1,
      precio_por_noche: '0.00',
      disponible: true,
    });
    setIsModalOpen(true);
  };

  const openEditModal = (habitacion: Habitacion) => {
    setEditingHabitacion(habitacion);
    reset({
        ...habitacion,
        precio_por_noche: parseFloat(habitacion.precio_por_noche).toFixed(2),
    });
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingHabitacion(null);
  };

  const onSubmit: SubmitHandler<HabitacionFormInputs> = async (data) => {
    const payload = {
        ...data,
        precio_por_noche: data.precio_por_noche.toString(),
    };
    try {
      if (editingHabitacion) {
        await api.put(`/turismo/habitaciones/${editingHabitacion.id}/`, payload);
        toast.success('¡Habitación actualizada con éxito!');
      } else {
        await api.post('/turismo/habitaciones/', payload);
        toast.success('¡Habitación creada con éxito!');
      }
      fetchHabitaciones();
      closeModal();
    } catch (err) {
      toast.error('Ocurrió un error al guardar la habitación.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar esta habitación?')) {
      try {
        await api.delete(`/turismo/habitaciones/${id}/`);
        toast.success('Habitación eliminada con éxito.');
        fetchHabitaciones();
      } catch (err) {
        toast.error('No se pudo eliminar la habitación.');
      }
    }
  };

  if (isLoading) {
    return <div>Cargando habitaciones...</div>;
  }

  if (error) {
    return <div className="text-red-500 p-4 bg-red-100 rounded-md">{error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Habitaciones</h1>
        <button
          onClick={openCreateModal}
          className="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-full flex items-center"
        >
          <FiPlus className="mr-2" /> Añadir Habitación
        </button>
      </div>

      {habitaciones.length === 0 ? (
        <p>No tienes habitaciones registradas.</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre/Número</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tipo</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Capacidad</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Precio/Noche</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Disponible</th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {habitaciones.map((h) => (
                <tr key={h.id}>
                  <td className="px-6 py-4">{h.nombre_o_numero}</td>
                  <td className="px-6 py-4">{h.tipo_habitacion}</td>
                  <td className="px-6 py-4">{h.capacidad}</td>
                  <td className="px-6 py-4">${parseFloat(h.precio_por_noche).toFixed(2)}</td>
                  <td className="px-6 py-4">
                     <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${h.disponible ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                      {h.disponible ? 'Sí' : 'No'}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <button onClick={() => openEditModal(h)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(h.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal title={editingHabitacion ? 'Editar Habitación' : 'Crear Habitación'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label htmlFor="nombre_o_numero">Nombre o Número</label>
              <input id="nombre_o_numero" {...register('nombre_o_numero', { required: true })} />
              {errors.nombre_o_numero && <p className="text-red-500">Este campo es requerido.</p>}
            </div>
             <div>
                <label htmlFor="tipo_habitacion">Tipo de Habitación</label>
                <select id="tipo_habitacion" {...register('tipo_habitacion', { required: true })}>
                    {tipoHabitacionChoices.map(choice => (
                        <option key={choice.value} value={choice.value}>{choice.label}</option>
                    ))}
                </select>
            </div>
            <div>
              <label htmlFor="capacidad">Capacidad</label>
              <input id="capacidad" type="number" {...register('capacidad', { required: true, valueAsNumber: true, min: 1 })} />
              {errors.capacidad && <p className="text-red-500">Debe ser un número mayor a 0.</p>}
            </div>
            <div>
              <label htmlFor="precio_por_noche">Precio por Noche</label>
              <input id="precio_por_noche" type="number" step="0.01" {...register('precio_por_noche', { required: true })} />
              {errors.precio_por_noche && <p className="text-red-500">Este campo es requerido.</p>}
            </div>
            <div className="flex items-center">
                <input id="disponible" type="checkbox" {...register('disponible')} />
                <label htmlFor="disponible" className="ml-2">Disponible</label>
            </div>
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

export default Habitaciones;