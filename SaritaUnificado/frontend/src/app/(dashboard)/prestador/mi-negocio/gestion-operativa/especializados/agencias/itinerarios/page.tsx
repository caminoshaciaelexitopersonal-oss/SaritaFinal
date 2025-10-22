'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';
import { useSearchParams } from 'next/navigation';

const GestionItinerarioPage = () => {
    const searchParams = useSearchParams();
    const paqueteId = searchParams.get('paqueteId');
    const { data: itinerarios, loading, error, createItem, updateItem, deleteItem } = useApi(`agencias/itinerarios/?paquete=${paqueteId}`);

    // ... (lógica de modales y guardado)

    if (loading) return <p>Cargando...</p>;
    if (error) return <p>Error al cargar los datos.</p>;
    if (!paqueteId) return <p>Por favor, seleccione un paquete primero.</p>;

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Itinerario</h1>

            {/* ... (renderizado de la página y modales) */}
        </div>
    );
};

export default GestionItinerarioPage;
