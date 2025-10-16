'use client';

import React, { useState, useEffect, Suspense, useMemo } from 'react';
import { useParams, useRouter } from 'next/navigation';
import {
    getPrestadorById, getPublicDisponibilidad, getPublicHabitaciones,
    PrestadorPublicoDetalle, Disponibilidad, Habitacion
} from '@/services/api';
import { useAuth } from '@/contexts/AuthContext';
import Link from 'next/link';
import Image from 'next/image';
import CalendarioReservas from '@/app/[locale]/dashboard/prestador/CalendarioReservas';
import Modal from '@/src/components/dashboard/Modal';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';

// --- Esqueleto y componente principal ... (sin cambios) ---
function DetailPageSkeleton() { /* ... */ }

function PrestadorDetailPageContent() {
  const params = useParams();
  const router = useRouter();
  const { user, isAuthenticated } = useAuth();
  const id = params && params.id ? parseInt(params.id as string, 10) : null;

  const [prestador, setPrestador] = useState<PrestadorPublicoDetalle | null>(null);
  const [recursos, setRecursos] = useState<Habitacion[]>([]); // Usamos Habitacion como recurso base
  const [selectedRecurso, setSelectedRecurso] = useState<Habitacion | null>(null);
  const [disponibilidad, setDisponibilidad] = useState<Disponibilidad[]>([]);
  const [loading, setLoading] = useState(true);
  const [isReservaModalOpen, setIsReservaModalOpen] = useState(false);
  const [selectedSlot, setSelectedSlot] = useState<{ start: Date, end: Date } | null>(null);

  // Cargar datos del prestador y sus recursos (habitaciones)
  useEffect(() => {
    if (id === null) return;
    const loadPrestadorYRecursos = async () => {
      try {
        setLoading(true);
        const prestadorData = await getPrestadorById(id);
        setPrestador(prestadorData);
        // Si es un hotel, cargar sus habitaciones
        if (prestadorData.categoria.nombre.toLowerCase().includes('hotel')) {
            const habitacionesData = await getPublicHabitaciones(prestadorData.id);
            setRecursos(habitacionesData);
            if (habitacionesData.length > 0) {
                setSelectedRecurso(habitacionesData[0]); // Seleccionar el primero por defecto
            }
        }
      } catch (err) {
        toast.error('No se pudo cargar la información del prestador.');
      } finally {
        setLoading(false);
      }
    };
    loadPrestadorYRecursos();
  }, [id]);

  // Cargar disponibilidad cuando cambia el recurso seleccionado
  useEffect(() => {
    if (!selectedRecurso) return;
    const loadDisponibilidad = async () => {
        try {
            const data = await getPublicDisponibilidad('turismo', 'habitacion', selectedRecurso.id);
            setDisponibilidad(data);
        } catch (error) {
            toast.error("No se pudo cargar la disponibilidad para este recurso.");
        }
    };
    loadDisponibilidad();
  }, [selectedRecurso]);

  // ... (resto de la lógica de modal y reserva sin cambios) ...

  const eventosDisponibilidad = useMemo(() => { /* ... */ });
  const handleSelectSlot = (slot: { start: Date; end: Date; }) => { /* ... */ };
  const handleConfirmReserva = async (numeroPersonas: number) => { /* ... */ };

  if (loading) return <DetailPageSkeleton />;
  if (!prestador) return <div>Prestador no encontrado.</div>;

  return (
    <div className="container mx-auto px-4 py-8">
      {/* ... (encabezado, galería, etc.) ... */}

      <div className="mt-12">
        <h2 className="text-3xl font-semibold text-center mb-6">Disponibilidad y Reservas</h2>
        {/* Selector de Recurso (si hay más de uno) */}
        {recursos.length > 1 && (
            <select onChange={(e) => setSelectedRecurso(recursos.find(r => r.id === parseInt(e.target.value)) || null)}>
                {recursos.map(r => <option key={r.id} value={r.id}>{r.nombre_o_numero}</option>)}
            </select>
        )}
        <div className="max-w-4xl mx-auto bg-white p-4 rounded-lg shadow-lg">
          <CalendarioReservas eventos={eventosDisponibilidad} onSelectSlot={handleSelectSlot} onSelectEvent={() => {}} />
        </div>
      </div>

      {/* ... (Modal de reserva y link de volver) ... */}
    </div>
  );
}

export default function PrestadorDetailPage() {
    return (
        <Suspense fallback={<DetailPageSkeleton />}>
            <PrestadorDetailPageContent />
        </Suspense>
    )
}