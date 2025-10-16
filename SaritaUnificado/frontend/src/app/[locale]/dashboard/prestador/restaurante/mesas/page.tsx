'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos
type Mesa = {
  id: number;
  numero_mesa: string;
  capacidad: number;
  estado: 'DISPONIBLE' | 'OCUPADA' | 'RESERVADA';
};
type MesaForm = Omit<Mesa, 'id'>;

const estadoChoices = ['DISPONIBLE', 'OCUPADA', 'RESERVADA'];

const MesasPage = () => {
  const [mesas, setMesas] = useState<Mesa[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingMesa, setEditingMesa] = useState<Mesa | null>(null);

  const { register, handleSubmit, reset } = useForm<MesaForm>();

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/restaurante/mesas/');
      setMesas(response.data.results || response.data);
    } catch (error) { toast.error("Error al cargar las mesas."); }
    finally { setIsLoading(false); }
  };

  useEffect(() => { fetchData(); }, []);

  const openModal = (mesa: Mesa | null = null) => {
    setEditingMesa(mesa);
    reset(mesa || { estado: 'DISPONIBLE', capacidad: 4 });
    setModalOpen(true);
  };
  const closeModal = () => setModalOpen(false);

  const onSubmit: SubmitHandler<MesaForm> = async (data) => {
    const apiCall = editingMesa ? api.put(`/restaurante/mesas/${editingMesa.id}/`, data) : api.post('/restaurante/mesas/', data);
    try {
      await apiCall;
      toast.success(`Mesa ${editingMesa ? 'actualizada' : 'creada'}.`);
      fetchData();
      closeModal();
    } catch (error) { toast.error("Error al guardar la mesa."); }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Seguro que quieres eliminar esta mesa?")) return;
    try {
      await api.delete(`/restaurante/mesas/${id}/`);
      toast.success("Mesa eliminada.");
      fetchData();
    } catch (error) { toast.error("Error al eliminar."); }
  };

  if (isLoading) return <div>Cargando mesas...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Gestión de Mesas</h1>
      <button onClick={() => openModal()} className="bg-green-600 text-white px-4 py-2 rounded mb-4">Añadir Mesa</button>

      <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
        {mesas.map(mesa => (
          <div key={mesa.id} className="p-4 rounded-lg shadow-md text-center bg-white">
            <p className="font-bold text-xl">{mesa.numero_mesa}</p>
            <p>Capacidad: {mesa.capacidad}</p>
            <p>Estado: {mesa.estado}</p>
            <div>
              <button onClick={() => openModal(mesa)} className="mr-2"><FiEdit /></button>
              <button onClick={() => handleDelete(mesa.id)}><FiTrash2 /></button>
            </div>
          </div>
        ))}
      </div>

      {modalOpen && (
        <Modal title={editingMesa ? 'Editar Mesa' : 'Nueva Mesa'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <input {...register('numero_mesa', { required: true })} placeholder="Número o Nombre de Mesa" />
            <input type="number" {...register('capacidad', { required: true, valueAsNumber: true })} placeholder="Capacidad" />
            <select {...register('estado')}>
              {estadoChoices.map(e => <option key={e} value={e}>{e}</option>)}
            </select>
            <button type="submit">Guardar</button>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default MesasPage;