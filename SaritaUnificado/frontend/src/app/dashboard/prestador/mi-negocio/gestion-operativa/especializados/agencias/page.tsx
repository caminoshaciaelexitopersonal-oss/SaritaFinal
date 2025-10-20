'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiBriefcase, FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Paquete {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
  activo: boolean;
}

type FormData = Omit<Paquete, 'id'>;

const PaquetesManager = () => {
  const [paquetes, setPaquetes] = useState<Paquete[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingPaquete, setEditingPaquete] = useState<Paquete | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormData>();

  const fetchPaquetes = async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/turismo/paquetes-turisticos/');
      setPaquetes(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar los paquetes turísticos.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchPaquetes();
  }, []);

  const openModalForCreate = () => {
    reset();
    setEditingPaquete(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (paquete: Paquete) => {
    setEditingPaquete(paquete);
    setValue('nombre', paquete.nombre);
    setValue('descripcion', paquete.descripcion);
    setValue('precio', paquete.precio);
    setValue('activo', paquete.activo);
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<FormData> = async (data) => {
    const apiCall = editingPaquete
      ? api.patch(`/turismo/paquetes-turisticos/${editingPaquete.id}/`, data)
      : api.post('/turismo/paquetes-turisticos/', data);

    try {
      await apiCall;
      toast.success(`Paquete ${editingPaquete ? 'actualizado' : 'creado'} con éxito.`);
      fetchPaquetes();
      setIsModalOpen(false);
    } catch (error) {
      toast.error('Error al guardar el paquete.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este paquete turístico?')) {
        try {
            await api.delete(`/turismo/paquetes-turisticos/${id}/`);
            toast.success('Paquete eliminado.');
            fetchPaquetes();
        } catch (error) {
            toast.error('No se pudo eliminar el paquete.');
        }
    }
  }

  if (isLoading) {
    return <div>Cargando paquetes turísticos...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Paquetes Turísticos</h1>
        <button onClick={openModalForCreate} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          <FiPlus className="mr-2" />
          Crear Paquete
        </button>
      </div>

      <div className="space-y-3">
        {paquetes.length > 0 ? paquetes.map(p => (
            <div key={p.id} className="p-4 border rounded-lg flex items-center justify-between">
                <div>
                    <p className="font-bold text-lg">{p.nombre}</p>
                    <p className="text-sm text-gray-600">{p.descripcion.substring(0, 120)}...</p>
                    <p className="text-md font-semibold text-gray-900 mt-2">${p.precio}</p>
                </div>
                <div className="flex items-center space-x-2">
                    <span className={`px-2 py-1 text-xs font-semibold rounded-full ${p.activo ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                        {p.activo ? 'Activo' : 'Inactivo'}
                    </span>
                    <button onClick={() => openModalForEdit(p)} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                    <button onClick={() => handleDelete(p.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                </div>
            </div>
        )) : (
            <p className="text-center text-gray-500 py-8">No has creado ningún paquete turístico.</p>
        )}
      </div>

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingPaquete ? "Editar Paquete" : "Crear Nuevo Paquete"}>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <input {...register('nombre', { required: true })} placeholder="Nombre del Paquete" className="w-full p-2 border rounded"/>
                <textarea {...register('descripcion')} placeholder="Descripción detallada" rows={5} className="w-full p-2 border rounded"/>
                <input type="text" {...register('precio', { required: true })} placeholder="Precio" className="w-full p-2 border rounded"/>
                <div className="flex items-center">
                    <input type="checkbox" {...register('activo')} defaultChecked={true} />
                    <label className="ml-2">Paquete Activo</label>
                </div>
                <div className="text-right">
                    <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded-md">Guardar</button>
                </div>
            </form>
        </Modal>
      )}
    </div>
  );
};

const PaquetesPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <PaquetesManager />
        </AuthGuard>
    )
}

export default PaquetesPage;