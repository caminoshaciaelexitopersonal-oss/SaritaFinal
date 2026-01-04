'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiAward } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';

// --- Tipos ---
interface ScoringRules {
  id: number;
  puntos_asistencia_capacitacion: number;
  puntos_por_estrella_reseña: number;
  puntos_completar_formulario: number;
}

const ScoringManager = () => {
  const [isLoading, setIsLoading] = useState(true);
  const { register, handleSubmit, reset } = useForm<ScoringRules>();

  useEffect(() => {
    const fetchRules = async () => {
      try {
        const response = await api.get('/api/admin/scoring-rules/');
        const rules = response.data.results ? response.data.results[0] : response.data[0];
        if (rules) {
          reset(rules);
        }
      } catch (error) {
        toast.error('No se pudieron cargar las reglas de puntuación.');
      } finally {
        setIsLoading(false);
      }
    };
    fetchRules();
  }, [reset]);

  const onSubmit: SubmitHandler<ScoringRules> = async (data) => {
    try {
      await api.put(`/api/admin/scoring-rules/1/`, data);
      toast.success('Reglas de puntuación actualizadas con éxito.');
    } catch (error) {
      toast.error('Error al guardar las reglas.');
    }
  };

  if (isLoading) return <div>Cargando configuración de puntuación...</div>;

  return (
    <div className="p-6 bg-white rounded-lg shadow-md max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Configurar Sistema de Puntuación</h1>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div>
          <label htmlFor="puntos_asistencia_capacitacion" className="block text-sm font-medium text-gray-700">
            Puntos por Asistencia a Capacitación
          </label>
          <input
            id="puntos_asistencia_capacitacion"
            type="number"
            {...register('puntos_asistencia_capacitacion', { valueAsNumber: true })}
            className="w-full mt-1 p-2 border rounded"
          />
        </div>
        <div>
          <label htmlFor="puntos_por_estrella_reseña" className="block text-sm font-medium text-gray-700">
            Puntos por cada Estrella en Reseñas
          </label>
          <input
            id="puntos_por_estrella_reseña"
            type="number"
            {...register('puntos_por_estrella_reseña', { valueAsNumber: true })}
            className="w-full mt-1 p-2 border rounded"
          />
        </div>
        <div>
          <label htmlFor="puntos_completar_formulario" className="block text-sm font-medium text-gray-700">
            Puntos por Completar un Formulario
          </label>
          <input
            id="puntos_completar_formulario"
            type="number"
            {...register('puntos_completar_formulario', { valueAsNumber: true })}
            className="w-full mt-1 p-2 border rounded"
          />
        </div>
        <button type="submit" className="w-full mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          Guardar Reglas
        </button>
      </form>
    </div>
  );
};

const ScoringPage = () => {
    return (
        <AuthGuard allowedRoles={['ADMIN']}>
            <ScoringManager />
        </AuthGuard>
    );
};

export default ScoringPage;