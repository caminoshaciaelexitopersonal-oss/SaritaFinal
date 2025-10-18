'use client';

import React, { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiEye, FiCheck, FiX } from 'react-icons/fi';

// Tipos de datos
type Reserva = {
  id: number;
  fecha_inicio: string;
  fecha_fin: string;
  cantidad_personas: number;
  estado: 'PENDIENTE' | 'CONFIRMADA' | 'CANCELADA' | 'COMPLETADA';
  cliente: {
    username: string;
    email: string;
  };
  recurso: {
    nombre: string;
  };
};

const ReservasPage = () => {
  const [reservas, setReservas] = useState<Reserva[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchReservas = async () => {
    setIsLoading(true);
    try {
      const response = await api.get<Reserva[]>('/turismo/reservas/');
      setReservas(response.data);
    } catch (error) {
      toast.error("Error al cargar las reservas.");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchReservas();
  }, []);

  const handleUpdateEstado = async (id: number, estado: Reserva['estado']) => {
    try {
      await api.patch(`/turismo/reservas/${id}/`, { estado });
      toast.success(`Reserva ${estado.toLowerCase()}.`);
      fetchReservas();
    } catch (error) {
      toast.error("No se pudo actualizar el estado de la reserva.");
    }
  };

  if (isLoading) return <div>Cargando reservas...</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Gestión de Reservas</h1>
      {reservas.length === 0 ? (
        <p>No tienes ninguna reserva.</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th>Cliente</th>
                <th>Recurso</th>
                <th>Fechas</th>
                <th>Personas</th>
                <th>Estado</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {reservas.map((reserva) => (
                <tr key={reserva.id}>
                  <td>{reserva.cliente.username}</td>
                  <td>{reserva.recurso.nombre}</td>
                  <td>{new Date(reserva.fecha_inicio).toLocaleDateString()} - {new Date(reserva.fecha_fin).toLocaleDateString()}</td>
                  <td>{reserva.cantidad_personas}</td>
                  <td>{reserva.estado}</td>
                  <td className="flex space-x-2">
                    <button onClick={() => handleUpdateEstado(reserva.id, 'CONFIRMADA')} title="Confirmar"><FiCheck className="text-green-500" /></button>
                    <button onClick={() => handleUpdateEstado(reserva.id, 'CANCELADA')} title="Cancelar"><FiX className="text-red-500" /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default ReservasPage;