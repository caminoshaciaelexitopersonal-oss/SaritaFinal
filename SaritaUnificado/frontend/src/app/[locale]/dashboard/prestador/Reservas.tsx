'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import Modal from '@/src/components/dashboard/Modal';
import CalendarioReservas from './CalendarioReservas'; // Importar el nuevo componente

// Tipos
type Cliente = { id: number; nombre: string; };
type Reserva = {
  id: number;
  cliente: number;
  cliente_info: Cliente;
  fecha_inicio_reserva: string;
  fecha_fin_reserva: string | null;
  numero_personas: number;
  estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
};
type ReservaFormInputs = {
    cliente: number;
    fecha_inicio_reserva: string;
    fecha_fin_reserva: string;
    numero_personas: number;
    estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
};

const estadoChoices = ['PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'COMPLETADA'];

const ReservasRAT = () => {
  const [reservas, setReservas] = useState<Reserva[]>([]);
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingReserva, setEditingReserva] = useState<Reserva | null>(null);
  const [slotInfo, setSlotInfo] = useState<{ start: Date; end: Date } | null>(null);

  const { register, handleSubmit, reset, formState: { isSubmitting } } = useForm<ReservaFormInputs>();

  // Cargar datos iniciales
  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const [reservasRes, clientesRes] = await Promise.all([
          api.get<Reserva[]>('/turismo/reservas/'),
          api.get<Cliente[]>('/empresa/gestion-clientes/')
        ]);
        setReservas(reservasRes.data);
        setClientes(clientesRes.data);
      } catch (err) { setError('No se pudieron cargar los datos.'); }
      finally { setIsLoading(false); }
    };
    fetchData();
  }, []);

  // Convertir reservas en eventos para el calendario
  const eventosCalendario = useMemo(() => reservas.map(r => ({
    id: r.id,
    title: `${r.cliente_info?.nombre || 'Cliente'} (${r.numero_personas}p)`,
    start: new Date(r.fecha_inicio_reserva),
    end: r.fecha_fin_reserva ? new Date(r.fecha_fin_reserva) : new Date(r.fecha_inicio_reserva),
    resource: r, // Guardar la reserva completa
  })), [reservas]);

  // Manejadores de eventos del calendario
  const handleSelectSlot = (slot: { start: Date; end: Date; }) => {
    if (clientes.length === 0) {
        toast.warn("Debe crear un cliente primero.");
        return;
    }
    setSlotInfo(slot);
    setEditingReserva(null);
    reset({
        cliente: clientes[0]?.id,
        fecha_inicio_reserva: moment(slot.start).format('YYYY-MM-DDTHH:mm'),
        fecha_fin_reserva: moment(slot.end).format('YYYY-MM-DDTHH:mm'),
        numero_personas: 1,
        estado: 'PENDIENTE',
    });
    setIsModalOpen(true);
  };

  const handleSelectEvent = (event: any) => {
    const reserva = event.resource as Reserva;
    setEditingReserva(reserva);
    reset({
        cliente: reserva.cliente,
        fecha_inicio_reserva: moment(reserva.fecha_inicio_reserva).format('YYYY-MM-DDTHH:mm'),
        fecha_fin_reserva: reserva.fecha_fin_reserva ? moment(reserva.fecha_fin_reserva).format('YYYY-MM-DDTHH:mm') : '',
        numero_personas: reserva.numero_personas,
        estado: reserva.estado,
    });
    setIsModalOpen(true);
  };

  const closeModal = () => setIsModalOpen(false);

  // Envío del formulario
  const onSubmit: SubmitHandler<ReservaFormInputs> = async (data) => {
    try {
      if (editingReserva) {
        await api.put(`/turismo/reservas/${editingReserva.id}/`, data);
        toast.success('Reserva actualizada');
      } else {
        await api.post('/turismo/reservas/', data);
        toast.success('Reserva creada');
      }
      const res = await api.get<Reserva[]>('/turismo/reservas/');
      setReservas(res.data);
      closeModal();
    } catch (err) { toast.error('Error al guardar la reserva.'); }
  };

  if (isLoading) return <div>Cargando calendario de reservas...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Calendario de Reservas (RAT)</h1>
      <p className="mb-4 text-gray-600">Haga clic en una fecha o arrastre sobre varias para crear una nueva reserva. Haga clic en una reserva existente para editarla.</p>

      <CalendarioReservas
        eventos={eventosCalendario}
        onSelectSlot={handleSelectSlot}
        onSelectEvent={handleSelectEvent}
      />

      {isModalOpen && (
        <Modal title={editingReserva ? 'Editar Reserva' : 'Nueva Reserva'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <select {...register('cliente', {valueAsNumber: true})}>
                {clientes.map(c => <option key={c.id} value={c.id}>{c.nombre}</option>)}
            </select>
            <input type="datetime-local" {...register('fecha_inicio_reserva')} />
            <input type="datetime-local" {...register('fecha_fin_reserva')} />
            <input type="number" {...register('numero_personas', {min: 1})} placeholder="Nº de personas"/>
            <select {...register('estado')}>
                {estadoChoices.map(e => <option key={e} value={e}>{e}</option>)}
            </select>
            <div className="flex justify-end space-x-2">
              <button type="button" onClick={closeModal}>Cancelar</button>
              <button type="submit" disabled={isSubmitting}>
                {isSubmitting ? 'Guardando...' : 'Guardar'}
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  );
};

import moment from 'moment';
export default ReservasRAT;