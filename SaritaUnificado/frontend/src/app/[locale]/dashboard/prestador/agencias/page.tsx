'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos
type Paquete = {
  id: number;
  nombre: string;
  descripcion: string;
  servicios_incluidos: string;
  precio_por_persona: string;
  duracion_dias: number;
  es_publico: boolean;
};
type PaqueteForm = Omit<Paquete, 'id'>;

const PaquetesPage = () => {
  const [paquetes, setPaquetes] = useState<Paquete[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingPaquete, setEditingPaquete] = useState<Paquete | null>(null);

  const { register, handleSubmit, reset } = useForm<PaqueteForm>();

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/turismo/paquetes/');
      setPaquetes(response.data.results || response.data);
    } catch (error) { toast.error("Error al cargar los paquetes."); }
    finally { setIsLoading(false); }
  };

  useEffect(() => { fetchData(); }, []);

  const openModal = (paquete: Paquete | null = null) => {
    setEditingPaquete(paquete);
    reset(paquete || { es_publico: false, duracion_dias: 1 });
    setModalOpen(true);
  };
  const closeModal = () => setModalOpen(false);

  const onSubmit: SubmitHandler<PaqueteForm> = async (data) => {
    const apiCall = editingPaquete ? api.put(`/turismo/paquetes/${editingPaquete.id}/`, data) : api.post('/turismo/paquetes/', data);
    try {
      await apiCall;
      toast.success(`Paquete ${editingPaquete ? 'actualizado' : 'creado'}.`);
      fetchData();
      closeModal();
    } catch (error) { toast.error("Error al guardar el paquete."); }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Seguro que quieres eliminar este paquete?")) return;
    try {
      await api.delete(`/turismo/paquetes/${id}/`);
      toast.success("Paquete eliminado.");
      fetchData();
    } catch (error) { toast.error("Error al eliminar."); }
  };

  if (isLoading) return <div>Cargando paquetes...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Gestión de Paquetes Turísticos</h1>
      <button onClick={() => openModal()} className="bg-purple-600 text-white px-4 py-2 rounded mb-4">Crear Paquete</button>

      <div className="space-y-4">
        {paquetes.map(p => (
          <div key={p.id} className="bg-white p-4 rounded-lg shadow-md">
            <div className="flex justify-between items-center">
              <p className="font-bold">{p.nombre}</p>
              <div>
                <button onClick={() => openModal(p)} className="mr-2"><FiEdit /></button>
                <button onClick={() => handleDelete(p.id)}><FiTrash2 /></button>
              </div>
            </div>
            <p>Duración: {p.duracion_dias} días</p>
            <p>Precio p/p: ${p.precio_por_persona}</p>
            <p>Estado: {p.es_publico ? 'Público' : 'Borrador'}</p>
          </div>
        ))}
      </div>

      {modalOpen && (
        <Modal title={editingPaquete ? 'Editar Paquete' : 'Nuevo Paquete'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <input {...register('nombre', { required: true })} placeholder="Nombre del paquete" />
            <textarea {...register('descripcion')} placeholder="Descripción" />
            <textarea {...register('servicios_incluidos')} placeholder="Servicios Incluidos" />
            <input type="number" step="0.01" {...register('precio_por_persona', { required: true })} placeholder="Precio por persona" />
            <input type="number" {...register('duracion_dias', { required: true, valueAsNumber: true })} placeholder="Duración (días)" />
            <input type="checkbox" {...register('es_publico')} /> Publicar
            <button type="submit">Guardar</button>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default PaquetesPage;