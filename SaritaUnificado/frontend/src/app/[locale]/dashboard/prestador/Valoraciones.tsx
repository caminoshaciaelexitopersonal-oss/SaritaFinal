'use client';

import React, { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiStar, FiMessageSquare } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';
import { useForm, SubmitHandler } from 'react-hook-form';

// Tipos
type Valoracion = {
  id: number;
  usuario_nombre: string;
  calificacion: number;
  comentario: string;
  fecha_creacion: string;
  respuesta_prestador: string | null;
};
type RespuestaForm = {
    respuesta_prestador: string;
}

const StarRating = ({ rating }: { rating: number }) => { /* ... (sin cambios) ... */ };

const Valoraciones = () => {
  const [valoraciones, setValoraciones] = useState<Valoracion[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingValoracion, setEditingValoracion] = useState<Valoracion | null>(null);
  const { register, handleSubmit, reset } = useForm<RespuestaForm>();

  const fetchValoraciones = async () => {
    try {
      setIsLoading(true);
      const response = await api.get<Valoracion[]>('/profile/prestador/valoraciones/');
      setValoraciones(response.data);
    } catch (error) { toast.error("Error al cargar valoraciones."); }
    finally { setIsLoading(false); }
  };

  useEffect(() => { fetchValoraciones(); }, []);

  const openResponseModal = (valoracion: Valoracion) => {
      setEditingValoracion(valoracion);
      reset({ respuesta_prestador: valoracion.respuesta_prestador || '' });
      setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<RespuestaForm> = async (data) => {
      if (!editingValoracion) return;
      try {
          await api.patch(`/profile/prestador/valoraciones/${editingValoracion.id}/`, data);
          toast.success("Respuesta guardada con éxito.");
          fetchValoraciones();
          setIsModalOpen(false);
      } catch (error) {
          toast.error("No se pudo guardar la respuesta.");
      }
  };

  if (isLoading) return <div>Cargando...</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Valoraciones y Comentarios</h1>
      {valoraciones.length === 0 ? (
        <p>Aún no has recibido ninguna valoración.</p>
      ) : (
        <div className="space-y-6">
          {valoraciones.map((v) => (
            <div key={v.id} className="bg-white p-4 rounded-lg shadow-md border">
              {/* ... (código para mostrar la valoración) ... */}
              <p className="mt-2 text-gray-700">{v.comentario}</p>

              {v.respuesta_prestador && (
                  <div className="mt-4 p-3 bg-gray-100 rounded-md border-l-4 border-gray-300">
                      <p className="font-semibold">Nuestra Respuesta:</p>
                      <p className="text-gray-600">{v.respuesta_prestador}</p>
                  </div>
              )}

              <div className="text-right mt-2">
                <button onClick={() => openResponseModal(v)} className="text-sm text-blue-600 hover:underline flex items-center">
                    <FiMessageSquare className="mr-1"/> {v.respuesta_prestador ? 'Editar Respuesta' : 'Responder'}
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {isModalOpen && editingValoracion && (
          <Modal title={`Respondiendo a ${editingValoracion.usuario_nombre}`} onClose={() => setIsModalOpen(false)}>
              <form onSubmit={handleSubmit(onSubmit)}>
                  <textarea {...register('respuesta_prestador')} rows={4} className="w-full p-2 border rounded"/>
                  <button type="submit">Guardar Respuesta</button>
              </form>
          </Modal>
      )}
    </div>
  );
};

export default Valoraciones;