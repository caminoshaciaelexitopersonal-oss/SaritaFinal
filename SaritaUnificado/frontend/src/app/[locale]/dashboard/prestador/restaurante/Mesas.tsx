'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';
import { FiUsers } from 'react-icons/fi';

interface Mesa {
  id: number;
  numero_mesa: string;
  capacidad: number;
  estado: 'DISPONIBLE' | 'OCUPADA' | 'RESERVADA';
}

type FormInputs = Omit<Mesa, 'id'>;

const MesaCard = ({ mesa, onEdit }: { mesa: Mesa, onEdit: (mesa: Mesa) => void }) => {
  const estadoColor = {
    DISPONIBLE: 'bg-green-100 border-green-400',
    OCUPADA: 'bg-red-100 border-red-400',
    RESERVADA: 'bg-yellow-100 border-yellow-400',
  };

  return (
    <div className={`p-4 rounded-lg border-2 ${estadoColor[mesa.estado]} cursor-pointer`} onClick={() => onEdit(mesa)}>
      <h3 className="text-lg font-bold">Mesa {mesa.numero_mesa}</h3>
      <div className="flex items-center text-gray-600 mt-2">
        <FiUsers className="mr-2" />
        <span>Capacidad: {mesa.capacidad}</span>
      </div>
      <p className="mt-2 font-semibold">{mesa.estado}</p>
    </div>
  );
};

const Mesas = () => {
  const [mesas, setMesas] = useState<Mesa[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingMesa, setEditingMesa] = useState<Mesa | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormInputs>();

  const fetchMesas = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/restaurante/mesas/');
      setMesas(response.data.results || []);
    } catch (err: any) {
      setError('No se pudieron cargar las mesas. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchMesas();
  }, [fetchMesas]);

  const openModalForCreate = () => {
    reset({ numero_mesa: '', capacidad: 4, estado: 'DISPONIBLE' });
    setEditingMesa(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (mesa: Mesa) => {
    setEditingMesa(mesa);
    setValue('numero_mesa', mesa.numero_mesa);
    setValue('capacidad', mesa.capacidad);
    setValue('estado', mesa.estado);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingMesa(null);
    reset();
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      if (editingMesa) {
        await api.patch(`/restaurante/mesas/${editingMesa.id}/`, data);
        toast.success('Mesa actualizada con éxito');
      } else {
        await api.post('/restaurante/mesas/', data);
        toast.success('Mesa creada con éxito');
      }
      closeModal();
      fetchMesas();
    } catch (err: any) {
      toast.error('Error al guardar la mesa: ' + (err.response?.data?.detail || err.message));
    }
  };

  if (isLoading) return <div>Cargando mesas...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Mesas</h1>
        <button onClick={openModalForCreate} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Añadir Mesa
        </button>
      </div>

      <Modal isOpen={isModalOpen} onClose={closeModal} title={editingMesa ? 'Editar Mesa' : 'Nueva Mesa'}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label htmlFor="numero_mesa">Número o Nombre de Mesa</label>
            <input id="numero_mesa" {...register('numero_mesa', { required: true })} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm" />
          </div>
          <div>
            <label htmlFor="capacidad">Capacidad</label>
            <input id="capacidad" type="number" {...register('capacidad', { required: true, min: 1 })} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm" />
          </div>
          <div>
            <label htmlFor="estado">Estado</label>
            <select id="estado" {...register('estado')} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm">
              <option value="DISPONIBLE">Disponible</option>
              <option value="OCUPADA">Ocupada</option>
              <option value="RESERVADA">Reservada</option>
            </select>
          </div>
          <div className="flex justify-end space-x-2">
            <button type="button" onClick={closeModal}>Cancelar</button>
            <button type="submit">Guardar</button>
          </div>
        </form>
      </Modal>

      {mesas.length === 0 ? (
        <p>No tienes mesas registradas.</p>
      ) : (
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {mesas.map((mesa) => (
            <MesaCard key={mesa.id} mesa={mesa} onEdit={openModalForEdit} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Mesas;