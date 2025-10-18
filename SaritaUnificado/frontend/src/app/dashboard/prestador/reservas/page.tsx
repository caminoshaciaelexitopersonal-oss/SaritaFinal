'use client';

import React, { useState, useEffect, useMemo } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { FiCalendar, FiEye, FiCheckCircle, FiXCircle, FiClock } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Reserva {
  id: number;
  cliente_info: {
    nombre: string;
    email: string;
    telefono: string;
  };
  recurso_reservado_str: string; // Asumimos que el serializer del backend proveerá esto
  fecha_inicio_reserva: string;
  fecha_fin_reserva: string;
  numero_personas: number;
  estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
  monto_total: string;
  notas_reserva: string;
}

// --- Componente de Calendario Simple ---
// Nota: Un calendario real usaría una librería como react-big-calendar,
// pero para este propósito, una lista es suficiente para demostrar la funcionalidad.
const CalendarView = ({ reservas, onSelectReserva }: { reservas: Reserva[], onSelectReserva: (reserva: Reserva) => void }) => {
  const sortedReservas = useMemo(() =>
    [...reservas].sort((a, b) => new Date(b.fecha_inicio_reserva).getTime() - new Date(a.fecha_inicio_reserva).getTime()),
    [reservas]
  );

  const estadoEstilos: { [key: string]: string } = {
    PENDIENTE: 'bg-yellow-100 text-yellow-800 border-yellow-400',
    CONFIRMADA: 'bg-green-100 text-green-800 border-green-400',
    CANCELADA: 'bg-red-100 text-red-800 border-red-400',
    COMPLETADA: 'bg-blue-100 text-blue-800 border-blue-400',
  };

  const estadoIconos: { [key: string]: React.ElementType } = {
    PENDIENTE: FiClock,
    CONFIRMADA: FiCheckCircle,
    CANCELADA: FiXCircle,
    COMPLETADA: FiCheckCircle,
  };

  return (
    <div className="space-y-4">
      {sortedReservas.length > 0 ? sortedReservas.map(reserva => {
         const Icon = estadoIconos[reserva.estado];
         return (
            <div key={reserva.id} className={`p-4 rounded-lg border-l-4 shadow-sm ${estadoEstilos[reserva.estado]}`}>
                <div className="flex items-center justify-between">
                    <div>
                        <p className="font-bold text-lg">{reserva.cliente_info?.nombre || 'Cliente Anónimo'}</p>
                        <p className="text-sm">{new Date(reserva.fecha_inicio_reserva).toLocaleDateString()} - {new Date(reserva.fecha_fin_reserva).toLocaleDateString()}</p>
                        <p className="text-sm font-medium mt-1 inline-flex items-center">
                            <Icon className="mr-2"/>
                            {reserva.estado}
                        </p>
                    </div>
                    <button
                        onClick={() => onSelectReserva(reserva)}
                        className="p-2 bg-white rounded-full hover:bg-gray-100 transition"
                        aria-label="Ver detalles"
                    >
                        <FiEye className="h-5 w-5 text-gray-600"/>
                    </button>
                </div>
            </div>
         )
      }) : (
        <div className="text-center py-10 px-4 border-2 border-dashed rounded-lg">
            <FiCalendar className="mx-auto h-12 w-12 text-gray-400" />
            <p className="mt-2 text-sm font-medium text-gray-600">No tienes ninguna reserva registrada.</p>
        </div>
      )}
    </div>
  );
};


const ReservasManager = () => {
  const [reservas, setReservas] = useState<Reserva[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [selectedReserva, setSelectedReserva] = useState<Reserva | null>(null);

  const fetchReservas = async () => {
    setIsLoading(true);
    try {
      // El backend filtra automáticamente las reservas para el prestador autenticado
      const response = await api.get('/turismo/reservas/');
      setReservas(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar las reservas.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchReservas();
  }, []);

  const handleUpdateStatus = async (reservaId: number, nuevoEstado: Reserva['estado']) => {
    try {
        await api.patch(`/turismo/reservas/${reservaId}/`, { estado: nuevoEstado });
        toast.success(`Reserva actualizada a ${nuevoEstado}`);
        fetchReservas(); // Recargar
        setSelectedReserva(null); // Cerrar modal
    } catch (error) {
        toast.error('Error al actualizar el estado de la reserva.');
    }
  }

  if (isLoading) {
    return <div>Cargando reservas...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Gestionar Reservas</h1>
      <CalendarView reservas={reservas} onSelectReserva={setSelectedReserva} />

      {selectedReserva && (
        <Modal isOpen={!!selectedReserva} onClose={() => setSelectedReserva(null)} title={`Detalle de Reserva #${selectedReserva.id}`}>
            <div className="space-y-4">
                <p><strong>Cliente:</strong> {selectedReserva.cliente_info?.nombre}</p>
                <p><strong>Email:</strong> {selectedReserva.cliente_info?.email}</p>
                <p><strong>Teléfono:</strong> {selectedReserva.cliente_info?.telefono}</p>
                <p><strong>Fechas:</strong> {new Date(selectedReserva.fecha_inicio_reserva).toLocaleString()} - {new Date(selectedReserva.fecha_fin_reserva).toLocaleString()}</p>
                <p><strong>Personas:</strong> {selectedReserva.numero_personas}</p>
                <p><strong>Monto Total:</strong> ${selectedReserva.monto_total}</p>
                <p><strong>Estado Actual:</strong> {selectedReserva.estado}</p>
                <div className="border-t pt-4 mt-4">
                    <h3 className="font-semibold mb-2">Cambiar Estado</h3>
                    <div className="flex flex-wrap gap-2">
                        <button onClick={() => handleUpdateStatus(selectedReserva.id, 'CONFIRMADA')} className="px-3 py-1 text-sm bg-green-500 text-white rounded-md hover:bg-green-600">Confirmar</button>
                        <button onClick={() => handleUpdateStatus(selectedReserva.id, 'CANCELADA')} className="px-3 py-1 text-sm bg-red-500 text-white rounded-md hover:bg-red-600">Cancelar</button>
                        <button onClick={() => handleUpdateStatus(selectedReserva.id, 'COMPLETADA')} className="px-3 py-1 text-sm bg-blue-500 text-white rounded-md hover:bg-blue-600">Marcar como Completada</button>
                        <button onClick={() => handleUpdateStatus(selectedReserva.id, 'PENDIENTE')} className="px-3 py-1 text-sm bg-yellow-500 text-white rounded-md hover:bg-yellow-600">Volver a Pendiente</button>
                    </div>
                </div>
            </div>
        </Modal>
      )}
    </div>
  );
};


const ReservasPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <ReservasManager />
        </AuthGuard>
    )
}

export default ReservasPage;