'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiGrid, FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Mesa {
  id: number;
  numero_mesa: string;
  capacidad: number;
  estado: 'DISPONIBLE' | 'OCUPADA' | 'RESERVADA';
}

type FormData = Omit<Mesa, 'id' | 'estado'>;

const MesasManager = () => {
  const [mesas, setMesas] = useState<Mesa[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingMesa, setEditingMesa] = useState<Mesa | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormData>();

  const fetchMesas = async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/restaurante/mesas/');
      setMesas(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar las mesas.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchMesas();
  }, []);

  const openModalForCreate = () => {
    reset();
    setEditingMesa(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (mesa: Mesa) => {
    setEditingMesa(mesa);
    setValue('numero_mesa', mesa.numero_mesa);
    setValue('capacidad', mesa.capacidad);
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<FormData> = async (data) => {
    const apiCall = editingMesa
      ? api.patch(`/restaurante/mesas/${editingMesa.id}/`, data)
      : api.post('/restaurante/mesas/', data);

    try {
      await apiCall;
      toast.success(`Mesa ${editingMesa ? 'actualizada' : 'creada'} con éxito.`);
      fetchMesas();
      setIsModalOpen(false);
    } catch (error) {
      toast.error('Error al guardar la mesa.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar esta mesa?')) {
        try {
            await api.delete(`/restaurante/mesas/${id}/`);
            toast.success('Mesa eliminada.');
            fetchMesas();
        } catch (error) {
            toast.error('No se pudo eliminar la mesa.');
        }
    }
  }

  const estadoEstilos = {
    DISPONIBLE: 'bg-green-100 text-green-800',
    OCUPADA: 'bg-red-100 text-red-800',
    RESERVADA: 'bg-yellow-100 text-yellow-800',
  };

  if (isLoading) {
    return <div>Cargando mesas...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Mesas</h1>
        <button onClick={openModalForCreate} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          <FiPlus className="mr-2" />
          Añadir Mesa
        </button>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
        {mesas.length > 0 ? mesas.map(mesa => (
            <div key={mesa.id} className={`p-4 border rounded-lg shadow-sm text-center ${estadoEstilos[mesa.estado]}`}>
                <p className="font-bold text-2xl">{mesa.numero_mesa}</p>
                <p className="text-sm">Capacidad: {mesa.capacidad}</p>
                <p className="text-xs font-semibold mt-1">{mesa.estado}</p>
                <div className="flex justify-center space-x-2 mt-3">
                    <button onClick={() => openModalForEdit(mesa)} className="p-2 hover:bg-gray-200 rounded-full"><FiEdit /></button>
                    <button onClick={() => handleDelete(mesa.id)} className="p-2 hover:bg-gray-200 rounded-full"><FiTrash2 /></button>
                </div>
            </div>
        )) : (
            <p className="col-span-full text-center text-gray-500">No hay mesas registradas.</p>
        )}
      </div>

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingMesa ? "Editar Mesa" : "Crear Nueva Mesa"}>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <div>
                    <label>Número o Nombre de la Mesa</label>
                    <input {...register('numero_mesa', { required: true })} className="w-full mt-1 p-2 border rounded"/>
                </div>
                <div>
                    <label>Capacidad (personas)</label>
                    <input type="number" {...register('capacidad', { required: true, valueAsNumber: true, min: 1 })} className="w-full mt-1 p-2 border rounded"/>
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

const MesasPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <MesasManager />
        </AuthGuard>
    )
}

export default MesasPage;