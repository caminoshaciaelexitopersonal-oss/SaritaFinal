'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiClipboard, FiUser, FiFile } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import { useRouter } from 'next/navigation';

// --- Tipos ---
interface Prestador {
  id: number;
  nombre_negocio: string;
}

interface Plantilla {
  id: number;
  nombre: string;
}

interface IniciarVerificacionData {
  prestador_id: number;
  plantilla_id: number;
}

const IniciarVerificacion = () => {
    const [prestadores, setPrestadores] = useState<Prestador[]>([]);
    const [plantillas, setPlantillas] = useState<Plantilla[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const router = useRouter();
    const { register, handleSubmit } = useForm<IniciarVerificacionData>();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [prestadoresRes, plantillasRes] = await Promise.all([
                    api.get('/api/admin/prestadores/'),
                    api.get('/api/plantillas-verificacion/')
                ]);
                setPrestadores(prestadoresRes.data.results || prestadoresRes.data);
                setPlantillas(plantillasRes.data.results || plantillasRes.data);
            } catch (error) {
                toast.error("No se pudo cargar la información necesaria.");
            } finally {
                setIsLoading(false);
            }
        };
        fetchData();
    }, []);

    const onSubmit: SubmitHandler<IniciarVerificacionData> = async (data) => {
        try {
            const response = await api.post('/api/verificaciones/iniciar/', data);
            const newVerificationId = response.data.id;
            toast.success("Verificación iniciada. Redirigiendo al checklist...");
            // Esta parte necesitaría una página de detalle de verificación que no está en el alcance actual
            // router.push(`/dashboard/admin/verificacion/${newVerificationId}`);
        } catch (error) {
            toast.error("No se pudo iniciar la verificación.");
        }
    };

    if (isLoading) return <div>Cargando...</div>

    return (
        <div className="p-6 bg-white rounded-lg shadow-md max-w-2xl mx-auto">
            <h1 className="text-3xl font-bold text-gray-800 mb-6">Iniciar Nueva Verificación</h1>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                <div>
                    <label htmlFor="prestador_id" className="block text-sm font-medium text-gray-700 mb-1">
                        <FiUser className="inline mr-2"/>Seleccionar Prestador de Servicio
                    </label>
                    <select id="prestador_id" {...register('prestador_id', { required: true, valueAsNumber: true })} className="w-full p-2 border rounded">
                        <option value="">-- Elige un prestador --</option>
                        {prestadores.map(p => <option key={p.id} value={p.id}>{p.nombre_negocio}</option>)}
                    </select>
                </div>
                <div>
                    <label htmlFor="plantilla_id" className="block text-sm font-medium text-gray-700 mb-1">
                        <FiFile className="inline mr-2"/>Seleccionar Plantilla de Verificación
                    </label>
                    <select id="plantilla_id" {...register('plantilla_id', { required: true, valueAsNumber: true })} className="w-full p-2 border rounded">
                        <option value="">-- Elige una plantilla --</option>
                        {plantillas.map(p => <option key={p.id} value={p.id}>{p.nombre}</option>)}
                    </select>
                </div>
                <button type="submit" className="w-full mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
                    Comenzar Verificación
                </button>
            </form>
        </div>
    );
};

const VerificacionPage = () => {
    return (
        <AuthGuard allowedRoles={['ADMIN', 'FUNCIONARIO_DIRECTIVO']}>
            <IniciarVerificacion />
        </AuthGuard>
    );
};

export default VerificacionPage;