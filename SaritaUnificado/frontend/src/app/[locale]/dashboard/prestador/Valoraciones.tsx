'use client';

import React, { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiStar } from 'react-icons/fi';

// Tipado para una reseña/valoración
type Valoracion = {
  id: number;
  usuario_nombre: string;
  calificacion: number;
  comentario: string;
  fecha_creacion: string;
};

const StarRating = ({ rating }: { rating: number }) => {
  return (
    <div className="flex items-center">
      {[...Array(5)].map((_, index) => (
        <FiStar
          key={index}
          className={`h-5 w-5 ${index < rating ? 'text-yellow-400' : 'text-gray-300'}`}
          fill={index < rating ? 'currentColor' : 'none'}
        />
      ))}
    </div>
  );
};

const Valoraciones = () => {
  const [valoraciones, setValoraciones] = useState<Valoracion[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchValoraciones = async () => {
      try {
        setIsLoading(true);
        // Usamos el nuevo endpoint para las valoraciones del prestador
        const response = await api.get<Valoracion[]>('/profile/prestador/valoraciones/');
        setValoraciones(response.data);
        setError(null);
      } catch (err) {
        setError('No se pudieron cargar las valoraciones.');
        toast.error('Error al cargar valoraciones.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchValoraciones();
  }, []);

  if (isLoading) return <div>Cargando valoraciones...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Valoraciones y Comentarios</h1>

      {valoraciones.length === 0 ? (
        <p>Aún no has recibido ninguna valoración de tus clientes.</p>
      ) : (
        <div className="space-y-4">
          {valoraciones.map((valoracion) => (
            <div key={valoracion.id} className="bg-white p-4 rounded-lg shadow-md border">
              <div className="flex justify-between items-start">
                <div>
                  <p className="font-semibold text-lg">{valoracion.usuario_nombre}</p>
                  <p className="text-sm text-gray-500">{new Date(valoracion.fecha_creacion).toLocaleDateString()}</p>
                </div>
                <StarRating rating={valoracion.calificacion} />
              </div>
              <p className="mt-2 text-gray-700">{valoracion.comentario}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Valoraciones;