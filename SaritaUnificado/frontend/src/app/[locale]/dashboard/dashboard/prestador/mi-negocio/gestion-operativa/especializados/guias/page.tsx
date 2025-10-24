'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiMap, FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Ruta {
  id: number;
  nombre: string;
  slug: string;
  descripcion: string;
  imagen_principal: string | null;
  es_publicado: boolean;
}

type FormData = Omit<Ruta, 'id' | 'slug' | 'imagen_principal'> & {
    imagen_principal_file?: FileList;
};

const RutasManager = () => {
  const [rutas, setRutas] = useState<Ruta[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingRuta, setEditingRuta] = useState<Ruta | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormData>();

  const fetchRutas = async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/turismo/rutas-turisticas/');
      setRutas(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar las rutas.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchRutas();
  }, []);

  const openModalForCreate = () => {
    reset();
    setEditingRuta(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (ruta: Ruta) => {
    setEditingRuta(ruta);
    setValue('nombre', ruta.nombre);
    setValue('descripcion', ruta.descripcion);
    setValue('es_publicado', ruta.es_publicado);
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<FormData> = async (data) => {
    const formData = new FormData();
    formData.append('nombre', data.nombre);
    formData.append('descripcion', data.descripcion);
    formData.append('es_publicado', String(data.es_publicado));
    if (data.imagen_principal_file && data.imagen_principal_file.length > 0) {
        formData.append('imagen_principal', data.imagen_principal_file[0]);
    }

    const apiCall = editingRuta
      ? api.patch(`/turismo/rutas-turisticas/${editingRuta.id}/`, formData, { headers: { 'Content-Type': 'multipart/form-data' } })
      : api.post('/turismo/rutas-turisticas/', formData, { headers: { 'Content-Type': 'multipart/form-data' } });

    try {
      await apiCall;
      toast.success(`Ruta ${editingRuta ? 'actualizada' : 'creada'} con éxito.`);
      fetchRutas();
      setIsModalOpen(false);
    } catch (error) {
      toast.error('Error al guardar la ruta.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar esta ruta?')) {
        try {
            await api.delete(`/turismo/rutas-turisticas/${id}/`);
            toast.success('Ruta eliminada.');
            fetchRutas();
        } catch (error) {
            toast.error('No se pudo eliminar la ruta.');
        }
    }
  }

  if (isLoading) {
    return <div>Cargando mis rutas...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Mis Rutas Turísticas</h1>
        <button onClick={openModalForCreate} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          <FiPlus className="mr-2" />
          Crear Ruta
        </button>
      </div>

      <div className="space-y-4">
        {rutas.length > 0 ? rutas.map(ruta => (
            <div key={ruta.id} className="p-4 border rounded-lg flex items-center justify-between">
                <div className="flex items-center">
                    {ruta.imagen_principal && <img src={ruta.imagen_principal} alt={ruta.nombre} className="h-16 w-16 rounded-md object-cover mr-4" />}
                    <div>
                        <h3 className="font-bold text-xl text-gray-800">{ruta.nombre}</h3>
                        <p className="text-sm text-gray-600">{ruta.descripcion.substring(0, 100)}...</p>
                    </div>
                </div>
                <div className="flex items-center space-x-2">
                    <span className={`px-2 py-1 text-xs font-semibold rounded-full ${ruta.es_publicado ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                        {ruta.es_publicado ? 'Publicada' : 'Borrador'}
                    </span>
                    <button onClick={() => openModalForEdit(ruta)} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                    <button onClick={() => handleDelete(ruta.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                </div>
            </div>
        )) : (
            <p className="text-center text-gray-500 py-8">No has creado ninguna ruta turística.</p>
        )}
      </div>

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingRuta ? "Editar Ruta" : "Crear Nueva Ruta"}>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <div>
                    <label>Nombre de la Ruta</label>
                    <input {...register('nombre', { required: true })} className="w-full mt-1 p-2 border rounded"/>
                </div>
                <div>
                    <label>Descripción</label>
                    <textarea {...register('descripcion', { required: true })} rows={4} className="w-full mt-1 p-2 border rounded"/>
                </div>
                <div>
                    <label>Imagen Principal</label>
                    <input type="file" {...register('imagen_principal_file')} className="w-full mt-1"/>
                </div>
                <div className="flex items-center">
                    <input type="checkbox" {...register('es_publicado')} className="h-4 w-4 text-blue-600"/>
                    <label className="ml-2">Publicar esta ruta</label>
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

const RutasPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <RutasManager />
        </AuthGuard>
    )
}

export default RutasPage;