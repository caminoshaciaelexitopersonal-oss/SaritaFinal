'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiTruck, FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Vehiculo {
  id: number;
  placa: string;
  marca: string;
  modelo: string;
  tipo_vehiculo: string;
  capacidad: number;
}

type FormData = Omit<Vehiculo, 'id'>;

const VehiculosManager = () => {
  const [vehiculos, setVehiculos] = useState<Vehiculo[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingVehiculo, setEditingVehiculo] = useState<Vehiculo | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormData>();

  const fetchVehiculos = async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/turismo/vehiculos/');
      setVehiculos(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar los vehículos.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchVehiculos();
  }, []);

  const openModalForCreate = () => {
    reset();
    setEditingVehiculo(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (vehiculo: Vehiculo) => {
    setEditingVehiculo(vehiculo);
    setValue('placa', vehiculo.placa);
    setValue('marca', vehiculo.marca);
    setValue('modelo', vehiculo.modelo);
    setValue('tipo_vehiculo', vehiculo.tipo_vehiculo);
    setValue('capacidad', vehiculo.capacidad);
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<FormData> = async (data) => {
    const apiCall = editingVehiculo
      ? api.patch(`/turismo/vehiculos/${editingVehiculo.id}/`, data)
      : api.post('/turismo/vehiculos/', data);

    try {
      await apiCall;
      toast.success(`Vehículo ${editingVehiculo ? 'actualizado' : 'creado'} con éxito.`);
      fetchVehiculos();
      setIsModalOpen(false);
    } catch (error) {
      toast.error('Error al guardar el vehículo.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este vehículo?')) {
        try {
            await api.delete(`/turismo/vehiculos/${id}/`);
            toast.success('Vehículo eliminado.');
            fetchVehiculos();
        } catch (error) {
            toast.error('No se pudo eliminar el vehículo.');
        }
    }
  }

  if (isLoading) {
    return <div>Cargando vehículos...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Flota de Vehículos</h1>
        <button onClick={openModalForCreate} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          <FiPlus className="mr-2" />
          Añadir Vehículo
        </button>
      </div>

      <div className="space-y-3">
        {vehiculos.length > 0 ? vehiculos.map(v => (
            <div key={v.id} className="p-4 border rounded-lg flex items-center justify-between">
                <div className="flex items-center">
                    <FiTruck className="h-10 w-10 text-blue-500 mr-4"/>
                    <div>
                        <p className="font-bold text-lg">{v.marca} {v.modelo}</p>
                        <p className="text-sm text-gray-700">Placa: <span className="font-mono bg-gray-100 p-1 rounded">{v.placa}</span></p>
                        <p className="text-sm text-gray-500">Tipo: {v.tipo_vehiculo} - Capacidad: {v.capacidad}</p>
                    </div>
                </div>
                <div className="flex items-center space-x-2">
                    <button onClick={() => openModalForEdit(v)} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                    <button onClick={() => handleDelete(v.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                </div>
            </div>
        )) : (
            <p className="text-center text-gray-500 py-8">No has registrado ningún vehículo.</p>
        )}
      </div>

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingVehiculo ? "Editar Vehículo" : "Añadir Nuevo Vehículo"}>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <input {...register('placa', { required: true })} placeholder="Placa" className="w-full p-2 border rounded"/>
                <input {...register('marca', { required: true })} placeholder="Marca" className="w-full p-2 border rounded"/>
                <input {...register('modelo', { required: true })} placeholder="Modelo" className="w-full p-2 border rounded"/>
                <input {...register('tipo_vehiculo', { required: true })} placeholder="Tipo (Ej: Bus, Camioneta)" className="w-full p-2 border rounded"/>
                <input type="number" {...register('capacidad', { required: true, valueAsNumber: true })} placeholder="Capacidad" className="w-full p-2 border rounded"/>
                <div className="text-right">
                    <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded-md">Guardar</button>
                </div>
            </form>
        </Modal>
      )}
    </div>
  );
};

const VehiculosPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <VehiculosManager />
        </AuthGuard>
    )
}

export default VehiculosPage;