
'use client';

import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import api from '@/services/api';

interface Plan {
    id: number;
    nombre: string;
    precio: string;
    frecuencia: string;
    tipo_usuario_objetivo: string;
    is_active: boolean;
}

export default function PlanesPage() {
    const [planes, setPlanes] = useState<Plan[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchPlanes = async () => {
            try {
                const response = await api.get('/admin/plataforma/planes/');
                setPlanes(response.data.results);
            } catch (err) {
                setError('No se pudieron cargar los planes.');
                console.error(err);
            } finally {
                setIsLoading(false);
            }
        };

        fetchPlanes();
    }, []);

    if (isLoading) {
        return <p>Cargando planes...</p>;
    }

    if (error) {
        return <p className="text-red-500">{error}</p>;
    }

    return (
        <Card>
            <CardHeader>
                <CardTitle>Gestión de Planes</CardTitle>
            </CardHeader>
            <CardContent>
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Nombre</TableHead>
                            <TableHead>Precio</TableHead>
                            <TableHead>Frecuencia</TableHead>
                            <TableHead>Estado</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {planes.map((plan) => (
                            <TableRow key={plan.id}>
                                <TableCell>{plan.nombre}</TableCell>
                                <TableCell>${plan.precio}</TableCell>
                                <TableCell>{plan.frecuencia}</TableCell>
                                <TableCell>{plan.is_active ? 'Activo' : 'Inactivo'}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </CardContent>
        </Card>
    );
}
