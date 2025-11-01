"use client";

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiPlus, FiEdit, FiTrash2, FiLoader } from 'react-icons/fi';
import { toast } from 'react-toastify';
import api from '@/services/api';
import Modal from '@/components/shared/Modal';
import FormField from '@/components/ui/FormField';
import { useAuth } from '@/contexts/AuthContext';

// --- Tipos de Datos ---
interface Vacante {
  id: number;
  titulo: string;
  descripcion: string;
  tipo_contrato: 'TIEMPO_COMPLETO' | 'MEDIO_TIEMPO' | 'POR_HORAS' | 'TEMPORAL' | 'PRACTICAS';
  ubicacion: string;
  salario?: string;
  activa: boolean;
}

type FormInputs = Omit<Vacante, 'id' | 'activa'>;

// --- Componente Principal ---
export default function VacantesManager() {
  const { user } = useAuth();
  const [vacantes, setVacantes] = useState<Vacante[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingVacante, setEditingVacante] = useState<Vacante | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormInputs>();

  const fetchVacantes = useCallback(async () => {
    setIsLoading(true);
    try {
      const response = await api.get<Vacante[]>('/vacantes/');
      setVacantes(response.data);
    } catch (error) {
      toast.error('Error al cargar las vacantes.');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    if (user?.role === 'PRESTADOR') {
        fetchVacantes();
    }
  }, [user, fetchVacantes]);

  const openModalForCreate = () => {
    reset({
      titulo: '',
      descripcion: '',
      tipo_contrato: 'TIEMPO_COMPLETO',
      ubicacion: '',
      salario: '',
    });
    setEditingVacante(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (vacante: Vacante) => {
    setEditingVacante(vacante);
    reset({
        titulo: vacante.titulo,
        descripcion: vacante.descripcion,
        tipo_contrato: vacante.tipo_contrato,
        ubicacion: vacante.ubicacion,
        salario: vacante.salario || '',
    });
    setIsModalOpen(true);
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar esta vacante?')) {
      try {
        await api.delete(`/vacantes/${id}/`);
        toast.success('Vacante eliminada con éxito.');
        fetchVacantes();
      } catch (error) {
        toast.error('Error al eliminar la vacante.');
      }
    }
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      if (editingVacante) {
        await api.put(`/vacantes/${editingVacante.id}/`, data);
        toast.success('Vacante actualizada con éxito.');
      } else {
        await api.post('/vacantes/', data);
        toast.success('Vacante creada con éxito.');
      }
      fetchVacantes();
      setIsModalOpen(false);
    } catch (error) {
        const errorMsg = 'Ocurrió un error.';
        toast.error(`Error: ${errorMsg}`);
    }
  };

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-64">
        <FiLoader className="animate-spin text-4xl text-blue-500" />
      </div>
    );
  }

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Vacantes</h1>
        <button
          onClick={openModalForCreate}
          className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
        >
          <FiPlus className="mr-2" />
          Crear Vacante
        </button>
      </div>

      <div className="bg-white shadow rounded-lg overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-100">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Título</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Ubicación</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Tipo Contrato</th>
              <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {vacantes.length > 0 ? (
              vacantes.map((vacante) => (
                <tr key={vacante.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{vacante.titulo}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">{vacante.ubicacion}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">{vacante.tipo_contrato.replace('_', ' ')}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <button onClick={() => openModalForEdit(vacante)} className="text-indigo-600 hover:text-indigo-900 mr-4">
                      <FiEdit />
                    </button>
                    <button onClick={() => handleDelete(vacante.id)} className="text-red-600 hover:text-red-900">
                      <FiTrash2 />
                    </button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={4} className="px-6 py-4 text-center text-sm text-gray-500">
                  No has creado ninguna vacante todavía.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingVacante ? 'Editar Vacante' : 'Crear Nueva Vacante'}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <FormField name="titulo" label="Título de la Vacante" register={register} errors={errors} required />
          <FormField name="descripcion" label="Descripción del Puesto" type="textarea" register={register} errors={errors} required />
          <FormField name="ubicacion" label="Ubicación" register={register} errors={errors} required />
          <FormField name="salario" label="Salario o Rango Salarial (Opcional)" register={register} errors={errors} />
          <div>
            <label htmlFor="tipo_contrato" className="block text-sm font-medium text-gray-700">Tipo de Contrato</label>
            <select
              id="tipo_contrato"
              {...register('tipo_contrato', { required: true })}
              className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="TIEMPO_COMPLETO">Tiempo Completo</option>
              <option value="MEDIO_TIEMPO">Medio Tiempo</option>
              <option value="POR_HORAS">Por Horas</option>
              <option value="TEMPORAL">Temporal</option>
              <option value="PRACTICAS">Prácticas / Pasantía</option>
            </select>
          </div>
          <div className="flex justify-end pt-4">
            <button type="button" onClick={() => setIsModalOpen(false)} className="mr-2 px-4 py-2 text-gray-700 bg-gray-200 rounded-lg hover:bg-gray-300">
              Cancelar
            </button>
            <button type="submit" disabled={isSubmitting} className="px-4 py-2 text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-blue-400">
              {isSubmitting ? 'Guardando...' : 'Guardar'}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
}