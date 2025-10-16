'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos
type Vehiculo = {
  id: number;
  placa: string;
  marca: string;
  modelo: string;
  tipo_vehiculo: 'BUS' | 'BUSETA' | 'VAN' | 'AUTOMOVIL' | 'CHIVA' | 'LANCHA';
  capacidad: number;
  documentacion_al_dia: boolean;
};
type VehiculoForm = Omit<Vehiculo, 'id'>;

const tipoVehiculoChoices = [
    { value: 'BUS', label: 'Autobús' },
    { value: 'BUSETA', label: 'Buseta' },
    { value: 'VAN', label: 'Van de Turismo' },
    { value: 'AUTOMOVIL', label: 'Automóvil Particular' },
    { value: 'CHIVA', label: 'Chiva Turística' },
    { value: 'LANCHA', label: 'Lancha Fluvial' },
];

const VehiculosPage = () => {
  const [vehiculos, setVehiculos] = useState<Vehiculo[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingVehiculo, setEditingVehiculo] = useState<Vehiculo | null>(null);

  const { register, handleSubmit, reset } = useForm<VehiculoForm>();

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/turismo/vehiculos/');
      setVehiculos(response.data.results || response.data);
    } catch (error) { toast.error("Error al cargar los vehículos."); }
    finally { setIsLoading(false); }
  };

  useEffect(() => { fetchData(); }, []);

  const openModal = (vehiculo: Vehiculo | null = null) => {
    setEditingVehiculo(vehiculo);
    reset(vehiculo || { documentacion_al_dia: true, tipo_vehiculo: 'AUTOMOVIL' });
    setModalOpen(true);
  };
  const closeModal = () => setModalOpen(false);

  const onSubmit: SubmitHandler<VehiculoForm> = async (data) => {
    const apiCall = editingVehiculo ? api.put(`/turismo/vehiculos/${editingVehiculo.id}/`, data) : api.post('/turismo/vehiculos/', data);
    try {
      await apiCall;
      toast.success(`Vehículo ${editingVehiculo ? 'actualizado' : 'creado'}.`);
      fetchData();
      closeModal();
    } catch (error) { toast.error("Error al guardar el vehículo."); }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Seguro que quieres eliminar este vehículo?")) return;
    try {
      await api.delete(`/turismo/vehiculos/${id}/`);
      toast.success("Vehículo eliminado.");
      fetchData();
    } catch (error) { toast.error("Error al eliminar."); }
  };

  if (isLoading) return <div>Cargando vehículos...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Gestión de Vehículos</h1>
      <button onClick={() => openModal()} className="bg-blue-600 text-white px-4 py-2 rounded mb-4">Añadir Vehículo</button>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {vehiculos.map(v => (
          <div key={v.id} className="bg-white p-4 rounded-lg shadow-md">
            <p className="font-bold text-xl">{v.marca} {v.modelo}</p>
            <p>Placa: {v.placa}</p>
            <p>Tipo: {v.tipo_vehiculo}</p>
            <p>Capacidad: {v.capacidad}</p>
            <p>Docs al día: {v.documentacion_al_dia ? 'Sí' : 'No'}</p>
            <div>
              <button onClick={() => openModal(v)} className="mr-2"><FiEdit /></button>
              <button onClick={() => handleDelete(v.id)}><FiTrash2 /></button>
            </div>
          </div>
        ))}
      </div>

      {modalOpen && (
        <Modal title={editingVehiculo ? 'Editar Vehículo' : 'Nuevo Vehículo'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <input {...register('placa', { required: true })} placeholder="Placa" />
            <input {...register('marca', { required: true })} placeholder="Marca" />
            <input {...register('modelo', { required: true })} placeholder="Modelo" />
            <select {...register('tipo_vehiculo')}>
              {tipoVehiculoChoices.map(c => <option key={c.value} value={c.value}>{c.label}</option>)}
            </select>
            <input type="number" {...register('capacidad', { required: true, valueAsNumber: true })} placeholder="Capacidad" />
            <input type="checkbox" {...register('documentacion_al_dia')} /> Documentación al día
            <button type="submit">Guardar</button>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default VehiculosPage;