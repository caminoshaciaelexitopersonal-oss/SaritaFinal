'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipado para un paquete, basado en PaqueteTuristicoSerializer
type Paquete = {
  id: number;
  nombre: string;
  descripcion: string;
  servicios_incluidos: string;
  precio_por_persona: string;
  duracion_dias: number;
  es_publico: boolean;
};

type PaqueteFormInputs = Omit<Paquete, 'id'>;

const Paquetes = () => {
  const [paquetes, setPaquetes] = useState<Paquete[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingPaquete, setEditingPaquete] = useState<Paquete | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors },
  } = useForm<PaqueteFormInputs>();

  const fetchPaquetes = async () => {
    try {
      setIsLoading(true);
      const response = await api.get<Paquete[]>('/turismo/paquetes/');
      setPaquetes(response.data);
      setError(null);
    } catch (err) {
      setError('No se pudieron cargar los paquetes turísticos.');
      toast.error('Error al cargar paquetes.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchPaquetes();
  }, []);

  const openCreateModal = () => {
    setEditingPaquete(null);
    reset({
      nombre: '',
      descripcion: '',
      servicios_incluidos: '',
      precio_por_persona: '0.00',
      duracion_dias: 1,
      es_publico: false,
    });
    setIsModalOpen(true);
  };

  const openEditModal = (paquete: Paquete) => {
    setEditingPaquete(paquete);
    reset({
        ...paquete,
        precio_por_persona: parseFloat(paquete.precio_por_persona).toFixed(2),
    });
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingPaquete(null);
  };

  const onSubmit: SubmitHandler<PaqueteFormInputs> = async (data) => {
     const payload = {
        ...data,
        precio_por_persona: data.precio_por_persona.toString(),
    };
    try {
      if (editingPaquete) {
        await api.put(`/turismo/paquetes/${editingPaquete.id}/`, payload);
        toast.success('¡Paquete actualizado con éxito!');
      } else {
        await api.post('/turismo/paquetes/', payload);
        toast.success('¡Paquete creado con éxito!');
      }
      fetchPaquetes();
      closeModal();
    } catch (err) {
      toast.error('Ocurrió un error al guardar el paquete.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este paquete?')) {
      try {
        await api.delete(`/turismo/paquetes/${id}/`);
        toast.success('Paquete eliminado con éxito.');
        fetchPaquetes();
      } catch (err) {
        toast.error('No se pudo eliminar el paquete.');
      }
    }
  };

  if (isLoading) return <div>Cargando paquetes...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Paquetes Turísticos</h1>
        <button
          onClick={openCreateModal}
          className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded-full flex items-center"
        >
          <FiPlus className="mr-2" /> Crear Paquete
        </button>
      </div>

      {paquetes.length === 0 ? (
        <p>No tienes paquetes turísticos creados.</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
             <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Precio/Persona</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Duración</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Público</th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {paquetes.map((p) => (
                <tr key={p.id}>
                  <td className="px-6 py-4">{p.nombre}</td>
                  <td className="px-6 py-4">${parseFloat(p.precio_por_persona).toFixed(2)}</td>
                  <td className="px-6 py-4">{p.duracion_dias} día(s)</td>
                  <td className="px-6 py-4">
                     <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${p.es_publico ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                      {p.es_publico ? 'Sí' : 'No'}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <button onClick={() => openEditModal(p)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(p.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal title={editingPaquete ? 'Editar Paquete' : 'Crear Paquete'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <input type="text" {...register('nombre', { required: true })} placeholder="Nombre del paquete" />
            <textarea {...register('descripcion')} placeholder="Descripción detallada" />
            <textarea {...register('servicios_incluidos')} placeholder="Servicios incluidos (ej. Hotel, Guía...)" />
            <input type="number" step="0.01" {...register('precio_por_persona', { required: true })} placeholder="Precio por persona" />
            <input type="number" {...register('duracion_dias', { required: true, valueAsNumber: true, min: 1 })} placeholder="Duración en días" />
            <div>
                <input type="checkbox" {...register('es_publico')} id="es_publico" />
                <label htmlFor="es_publico" className="ml-2">Hacer público</label>
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

export default Paquetes;