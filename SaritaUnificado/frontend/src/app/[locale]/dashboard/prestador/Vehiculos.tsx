'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipado para un vehículo, basado en VehiculoTuristicoSerializer
type Vehiculo = {
  id: number;
  placa: string;
  marca: string;
  modelo: string;
  tipo_vehiculo: 'BUS' | 'BUSETA' | 'VAN' | 'AUTOMOVIL' | 'CHIVA' | 'LANCHA';
  capacidad: number;
  documentacion_al_dia: boolean;
  foto?: string; // Opcional
};

type VehiculoFormInputs = Omit<Vehiculo, 'id'>;

const tipoVehiculoChoices = [
    { value: 'BUS', label: 'Autobús' },
    { value: 'BUSETA', label: 'Buseta' },
    { value: 'VAN', label: 'Van de Turismo' },
    { value: 'AUTOMOVIL', label: 'Automóvil Particular' },
    { value: 'CHIVA', label: 'Chiva Turística' },
    { value: 'LANCHA', label: 'Lancha Fluvial' },
];

const Vehiculos = () => {
  const [vehiculos, setVehiculos] = useState<Vehiculo[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingVehiculo, setEditingVehiculo] = useState<Vehiculo | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors },
  } = useForm<VehiculoFormInputs>();

  const fetchVehiculos = async () => {
    try {
      setIsLoading(true);
      const response = await api.get<Vehiculo[]>('/turismo/vehiculos/');
      setVehiculos(response.data);
      setError(null);
    } catch (err) {
      setError('No se pudieron cargar los vehículos.');
      toast.error('Error al cargar vehículos.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchVehiculos();
  }, []);

  const openCreateModal = () => {
    setEditingVehiculo(null);
    reset({
      placa: '',
      marca: '',
      modelo: '',
      tipo_vehiculo: 'AUTOMOVIL',
      capacidad: 4,
      documentacion_al_dia: true,
    });
    setIsModalOpen(true);
  };

  const openEditModal = (vehiculo: Vehiculo) => {
    setEditingVehiculo(vehiculo);
    reset(vehiculo);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingVehiculo(null);
  };

  const onSubmit: SubmitHandler<VehiculoFormInputs> = async (data) => {
    try {
      if (editingVehiculo) {
        await api.put(`/turismo/vehiculos/${editingVehiculo.id}/`, data);
        toast.success('¡Vehículo actualizado con éxito!');
      } else {
        await api.post('/turismo/vehiculos/', data);
        toast.success('¡Vehículo añadido con éxito!');
      }
      fetchVehiculos();
      closeModal();
    } catch (err) {
      toast.error('Ocurrió un error al guardar el vehículo.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este vehículo?')) {
      try {
        await api.delete(`/turismo/vehiculos/${id}/`);
        toast.success('Vehículo eliminado con éxito.');
        fetchVehiculos();
      } catch (err) {
        toast.error('No se pudo eliminar el vehículo.');
      }
    }
  };

  if (isLoading) return <div>Cargando vehículos...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Vehículos</h1>
        <button
          onClick={openCreateModal}
          className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full flex items-center"
        >
          <FiPlus className="mr-2" /> Añadir Vehículo
        </button>
      </div>

      {vehiculos.length === 0 ? (
        <p>No tienes vehículos registrados.</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Placa</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Marca / Modelo</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tipo</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Capacidad</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Docs al día</th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {vehiculos.map((v) => (
                <tr key={v.id}>
                  <td className="px-6 py-4 font-mono text-sm">{v.placa}</td>
                  <td className="px-6 py-4">{v.marca} {v.modelo}</td>
                  <td className="px-6 py-4">{v.tipo_vehiculo}</td>
                  <td className="px-6 py-4">{v.capacidad}</td>
                  <td className="px-6 py-4">
                     <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${v.documentacion_al_dia ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                      {v.documentacion_al_dia ? 'Sí' : 'No'}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <button onClick={() => openEditModal(v)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(v.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal title={editingVehiculo ? 'Editar Vehículo' : 'Añadir Vehículo'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <input type="text" {...register('placa', { required: true })} placeholder="Placa" />
            <input type="text" {...register('marca', { required: true })} placeholder="Marca" />
            <input type="text" {...register('modelo', { required: true })} placeholder="Modelo" />
            <select {...register('tipo_vehiculo', { required: true })}>
                {tipoVehiculoChoices.map(c => <option key={c.value} value={c.value}>{c.label}</option>)}
            </select>
            <input type="number" {...register('capacidad', { required: true, valueAsNumber: true, min: 1 })} placeholder="Capacidad" />
            <div>
                <input type="checkbox" {...register('documentacion_al_dia')} id="docs" />
                <label htmlFor="docs" className="ml-2">Documentación al día</label>
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

export default Vehiculos;