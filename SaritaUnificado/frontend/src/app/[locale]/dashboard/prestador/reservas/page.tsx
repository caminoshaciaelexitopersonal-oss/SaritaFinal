'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import Modal from '@/src/components/dashboard/Modal';
import CalendarioReservas, { EventoCalendario } from './CalendarioReservas';
import moment from 'moment';

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
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingReserva, setEditingReserva] = useState<Reserva | null>(null);

  const { register, handleSubmit, reset, formState: { isSubmitting } } = useForm<ReservaFormInputs>();

  const fetchReservas = async () => {
    try {
      const response = await api.get<Reserva[]>('/turismo/reservas/');
      setReservas(response.data);
    } catch (err) { toast.error('Error al cargar reservas.'); }
  };

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      await Promise.all([fetchReservas(), api.get<Cliente[]>('/empresa/gestion-clientes/').then(res => setClientes(res.data))]);
      setIsLoading(false);
    };
    fetchData();
  }, []);

  const eventosCalendario = useMemo(() => reservas.map((r): EventoCalendario => ({
    id: r.id,
    title: `${r.cliente_info?.nombre || 'Cliente'} (${r.numero_personas}p)`,
    start: new Date(r.fecha_inicio_reserva),
    end: r.fecha_fin_reserva ? new Date(r.fecha_fin_reserva) : moment(r.fecha_inicio_reserva).add(1, 'hour').toDate(),
    resource: r,
    estado: r.estado,
  })), [reservas]);

  const handleEventDrop = async ({ event, start, end }: any) => {
    const reservaActualizada = {
        ...event.resource,
        fecha_inicio_reserva: start.toISOString(),
        fecha_fin_reserva: end.toISOString(),
    };
    try {
        await api.put(`/turismo/reservas/${event.id}/`, reservaActualizada);
        toast.success("Reserva reprogramada con éxito.");
        fetchReservas();
    } catch (error) {
        toast.error("No se pudo reprogramar la reserva.");
    }
  };

  // ... (resto de manejadores de modal y submit sin cambios) ...
  const handleSelectSlot = (slot: { start: Date; end: Date; }) => { /* ... */ };
  const handleSelectEvent = (event: any) => { /* ... */ };
  const closeModal = () => setIsModalOpen(false);
  const onSubmit: SubmitHandler<ReservaFormInputs> = async (data) => { /* ... */ };

  if (isLoading) return <div>Cargando calendario...</div>;

  return (
    <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-6">Calendario de Reservas (RAT)</h1>
        <CalendarioReservas
            eventos={eventosCalendario}
            onSelectSlot={handleSelectSlot}
            onSelectEvent={handleSelectEvent}
            onEventDrop={handleEventDrop}
        />
        {/* ... (Modal sin cambios) ... */}
    </div>
  );
};

export default ReservasRAT;