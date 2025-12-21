"use client";

import { useState } from 'react';
import useSWR, { useSWRConfig } from 'swr';
import toast from 'react-hot-toast';
import { PageHeader } from '@/components/shared/page-header';
import { Button } from '@/components/ui/Button';
import { Spinner } from '@/components/common/Spinner'; // Asumo que existe
import { Alert } from '@/components/common/Alert'; // Asumo que existe

// Simulación de tipos, deben coincidir con la API
interface Product { name: string; base_price: string; }
interface Amenity { id: number; nombre: string; }
interface RoomType { id: number; product: Product; capacidad: number; amenities: Amenity[]; }

const fetcher = (url: string) => apiClient.get(url).then(res => res.data.results);

// --- Componentes Anidados (Simplificados por ahora) ---

const RoomList = ({ roomTypeId }: { roomTypeId: number }) => {
    // Lógica para listar y añadir habitaciones físicas (Rooms)
    return <div className="p-4 bg-gray-100 rounded mt-4">Gestión de Habitaciones Físicas (Próximamente)</div>;
};

const AmenitySelector = ({ roomTypeId, initialAmenityIds }: { roomTypeId: number; initialAmenityIds: number[] }) => {
    // Lógica para asignar amenities a un RoomType
    return <div className="p-4 bg-gray-100 rounded mt-4">Gestor de Amenidades (Próximamente)</div>;
};

// --- Componente Principal ---

export default function HotelManagementPage() {
    const { data: roomTypes, error, isLoading } = useSWR<RoomType[]>('/api/v1/mi-negocio/gestion-operativa/hotel/room-types/', fetcher);
    const [selectedRoomTypeId, setSelectedRoomTypeId] = useState<number | null>(null);

    if (isLoading) return <Spinner text="Cargando configuración del hotel..." />;
    if (error) return <Alert type="error" title="Error">No se pudo cargar la configuración del hotel.</Alert>;

    return (
        <div className="flex flex-col gap-8">
            <PageHeader
                title="Gestión de Hotel"
                description="Configure los tipos de habitación, el inventario físico y los servicios de su hotel."
            >
                <Button>+ Nuevo Tipo de Habitación</Button>
            </PageHeader>

            <div className="space-y-4">
                {roomTypes?.map(rt => (
                    <div key={rt.id} className="border p-4 rounded-lg shadow-sm">
                        <button
                            className="w-full text-left"
                            onClick={() => setSelectedRoomTypeId(selectedRoomTypeId === rt.id ? null : rt.id)}
                        >
                            <h3 className="font-bold text-lg">{rt.product.name}</h3>
                            <p className="text-sm text-gray-600">
                                Capacidad: {rt.capacidad} personas | Precio Base: ${rt.product.base_price}
                            </p>
                        </button>

                        {selectedRoomTypeId === rt.id && (
                            <div className="pl-4 mt-4 border-l-2">
                                <AmenitySelector roomTypeId={rt.id} initialAmenityIds={rt.amenities.map(a => a.id)} />
                                <RoomList roomTypeId={rt.id} />
                            </div>
                        )}
                    </li>
                ))}
                {roomTypes?.length === 0 && (
                    <Alert type="info" title="Sin Configuración">
                        Aún no has creado ningún tipo de habitación. Haz clic en "+ Nuevo Tipo de Habitación" para empezar.
                    </Alert>
                )}
            </div>
        </div>
    );
}

// Asumo que existe un cliente de API en @/services/api
import axios from 'axios';
const apiClient = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000',
    // Aquí iría la lógica para añadir el token de autenticación
});
