'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { FiStar, FiMessageSquare, FiSend } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';

// --- Tipos ---
interface Resena {
  id: number;
  usuario_nombre: string;
  calificacion: number;
  comentario: string;
  fecha_creacion: string;
  respuesta_prestador: string | null;
}

const StarRating = ({ rating }: { rating: number }) => (
  <div className="flex items-center">
    {[...Array(5)].map((_, i) => (
      <FiStar
        key={i}
        className={`h-5 w-5 ${i < rating ? 'text-yellow-400' : 'text-gray-300'}`}
        fill={i < rating ? 'currentColor' : 'none'}
      />
    ))}
  </div>
);

const ValoracionesManager = () => {
  const [resenas, setResenas] = useState<Resena[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [respuesta, setRespuesta] = useState<{ [key: number]: string }>({});

  const fetchResenas = async () => {
    setIsLoading(true);
    try {
      // El backend filtra automáticamente las reseñas para el prestador autenticado
      const response = await api.get('/profile/resenas/');
      setResenas(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar las valoraciones.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchResenas();
  }, []);

  const handleRespuestaChange = (id: number, text: string) => {
    setRespuesta(prev => ({ ...prev, [id]: text }));
  };

  const handleEnviarRespuesta = async (id: number) => {
    const textoRespuesta = respuesta[id];
    if (!textoRespuesta) {
        toast.warn('La respuesta no puede estar vacía.');
        return;
    }
    try {
        await api.patch(`/profile/resenas/${id}/`, { respuesta_prestador: textoRespuesta });
        toast.success('Respuesta enviada con éxito.');
        fetchResenas(); // Recargar para mostrar la respuesta guardada
    } catch (error) {
        toast.error('No se pudo enviar la respuesta.');
    }
  };

  if (isLoading) {
    return <div>Cargando valoraciones...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Valoraciones y Reseñas de Clientes</h1>

      <div className="space-y-6">
        {resenas.length > 0 ? resenas.map(resena => (
          <div key={resena.id} className="p-4 border rounded-lg">
            <div className="flex justify-between items-start">
                <div>
                    <p className="font-bold text-lg">{resena.usuario_nombre}</p>
                    <p className="text-sm text-gray-500 mb-2">{new Date(resena.fecha_creacion).toLocaleDateString()}</p>
                </div>
                <StarRating rating={resena.calificacion} />
            </div>
            <p className="text-gray-700 mt-2 mb-4 italic">"{resena.comentario}"</p>

            {resena.respuesta_prestador ? (
                <div className="p-3 bg-blue-50 border-l-4 border-blue-400 rounded-r-lg">
                    <p className="font-semibold text-blue-800">Tu respuesta:</p>
                    <p className="text-gray-600 italic">{resena.respuesta_prestador}</p>
                </div>
            ) : (
                <div className="mt-4">
                    <label htmlFor={`respuesta-${resena.id}`} className="block text-sm font-medium text-gray-700">Escribe una respuesta:</label>
                    <div className="mt-1 flex rounded-md shadow-sm">
                        <textarea
                            id={`respuesta-${resena.id}`}
                            rows={2}
                            value={respuesta[resena.id] || ''}
                            onChange={(e) => handleRespuestaChange(resena.id, e.target.value)}
                            className="flex-1 block w-full rounded-none rounded-l-md sm:text-sm border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                            placeholder="Agradece el comentario o aclara la situación..."
                        />
                        <button
                            onClick={() => handleEnviarRespuesta(resena.id)}
                            className="inline-flex items-center px-3 py-2 border border-l-0 border-blue-600 bg-blue-600 text-white rounded-r-md hover:bg-blue-700"
                        >
                            <FiSend className="h-5 w-5" />
                        </button>
                    </div>
                </div>
            )}
          </div>
        )) : (
          <div className="text-center py-10 px-4 border-2 border-dashed rounded-lg">
            <FiMessageSquare className="mx-auto h-12 w-12 text-gray-400" />
            <p className="mt-2 text-sm font-medium text-gray-600">Aún no has recibido ninguna valoración.</p>
          </div>
        )}
      </div>
    </div>
  );
};


const ValoracionesPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <ValoracionesManager />
        </AuthGuard>
    )
}

export default ValoracionesPage;