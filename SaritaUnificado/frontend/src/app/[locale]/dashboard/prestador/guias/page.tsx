'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos
type Ruta = {
  id: number;
  nombre: string;
  descripcion: string;
  es_publicado: boolean;
};
type RutaForm = Omit<Ruta, 'id'>;

const RutasGuiasPage = () => {
  const [rutas, setRutas] = useState<Ruta[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingRuta, setEditingRuta] = useState<Ruta | null>(null);

  const { register, handleSubmit, reset } = useForm<RutaForm>();

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/turismo/rutas-turisticas/');
      setRutas(response.data.results || response.data);
    } catch (error) { toast.error("Error al cargar las rutas."); }
    finally { setIsLoading(false); }
  };

  useEffect(() => { fetchData(); }, []);

  const openModal = (ruta: Ruta | null = null) => {
    setEditingRuta(ruta);
    reset(ruta || { es_publicado: true });
    setModalOpen(true);
  };
  const closeModal = () => setModalOpen(false);

  const onSubmit: SubmitHandler<RutaForm> = async (data) => {
    const apiCall = editingRuta ? api.put(`/turismo/rutas-turisticas/${editingRuta.id}/`, data) : api.post('/turismo/rutas-turisticas/', data);
    try {
      await apiCall;
      toast.success(`Ruta ${editingRuta ? 'actualizada' : 'creada'}.`);
      fetchData();
      closeModal();
    } catch (error) { toast.error("Error al guardar la ruta."); }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Seguro que quieres eliminar esta ruta?")) return;
    try {
      await api.delete(`/turismo/rutas-turisticas/${id}/`);
      toast.success("Ruta eliminada.");
      fetchData();
    } catch (error) { toast.error("Error al eliminar."); }
  };

  if (isLoading) return <div>Cargando rutas...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Gestión de Mis Rutas Turísticas</h1>
      <button onClick={() => openModal()} className="bg-purple-600 text-white px-4 py-2 rounded mb-4">Crear Nueva Ruta</button>

      <div className="space-y-4">
        {rutas.map(ruta => (
          <div key={ruta.id} className="bg-white p-4 rounded-lg shadow-md flex justify-between items-center">
            <div>
              <p className="font-bold">{ruta.nombre}</p>
              <p className="text-sm text-gray-600">{ruta.descripcion}</p>
            </div>
            <div>
              <button onClick={() => openModal(ruta)} className="mr-2"><FiEdit /></button>
              <button onClick={() => handleDelete(ruta.id)}><FiTrash2 /></button>
            </div>
          </div>
        ))}
      </div>

      {modalOpen && (
        <Modal title={editingRuta ? 'Editar Ruta' : 'Nueva Ruta'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <input {...register('nombre', { required: true })} placeholder="Nombre de la ruta" />
            <textarea {...register('descripcion')} placeholder="Descripción" />
            <input type="checkbox" {...register('es_publicado')} /> Publicar
            <button type="submit">Guardar</button>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default RutasGuiasPage;