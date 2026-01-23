
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Button } from '@/components/ui/Button';
import { toast } from 'react-toastify';
import { FiEdit, FiTrash2, FiPlusCircle } from 'react-icons/fi';
import api from '@/services/api';
import PlanFormModal from './PlanFormModal';

interface Plan {
    id: number;
    nombre: string;
    descripcion: string;
    precio: string;
    frecuencia: string;
    tipo_usuario_objetivo: string;
    is_active: boolean;
}

export default function PlanesPage() {
    const [planes, setPlanes] = useState<Plan[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [planToEdit, setPlanToEdit] = useState<Plan | null>(null);

    const fetchPlanes = useCallback(async () => {
        try {
            setIsLoading(true);
            const response = await api.get('/admin/plataforma/planes/');
            setPlanes(response.data.results || []);
        } catch (err) {
            setError('No se pudieron cargar los planes.');
            console.error(err);
            toast.error('No se pudieron cargar los planes.');
        } finally {
            setIsLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchPlanes();
    }, [fetchPlanes]);

    const handleOpenModal = (plan: Plan | null = null) => {
        setPlanToEdit(plan);
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
        setPlanToEdit(null);
    };

    const handleSavePlan = (savedPlan: Plan) => {
        if (planToEdit) {
            setPlanes(planes.map(p => p.id === savedPlan.id ? savedPlan : p));
        } else {
            setPlanes([...planes, savedPlan]);
        }
        // Opcional: podrías volver a llamar a fetchPlanes() para asegurar la consistencia.
    };

    const handleDeletePlan = async (planId: number) => {
        if (!window.confirm('¿Estás seguro de que quieres eliminar este plan?')) {
            return;
        }
        try {
            await api.delete(`/admin/plataforma/planes/${planId}/`);
            setPlanes(planes.filter(p => p.id !== planId));
            toast.success('Plan eliminado con éxito.');
        } catch (error) {
            toast.error('Error al eliminar el plan.');
            console.error(error);
        }
    };

    if (isLoading) {
        return <p>Cargando planes...</p>;
    }

    if (error) {
        return <p className="text-red-500">{error}</p>;
    }

    return (
        <>
            <Card>
                <CardHeader className="flex flex-row items-center justify-between">
                    <CardTitle>Gestión de Planes</CardTitle>
                    <Button onClick={() => handleOpenModal()}>
                        <FiPlusCircle className="mr-2 h-4 w-4" />
                        Crear Nuevo Plan
                    </Button>
                </CardHeader>
                <CardContent>
                    <Table>
                        <TableHeader>
                            <TableRow>
                                <TableHead>Nombre</TableHead>
                                <TableHead>Público</TableHead>
                                <TableHead>Frecuencia</TableHead>
                                <TableHead>Precio</TableHead>
                                <TableHead>Estado</TableHead>
                                <TableHead>Acciones</TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {planes.map((plan) => (
                                <TableRow key={plan.id}>
                                    <TableCell className="font-medium">{plan.nombre}</TableCell>
                                    <TableCell>{plan.tipo_usuario_objetivo}</TableCell>
                                    <TableCell>{plan.frecuencia}</TableCell>
                                    <TableCell>${plan.precio}</TableCell>
                                    <TableCell>
                                        <span className={`px-2 py-1 text-xs font-semibold rounded-full ${plan.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                                            {plan.is_active ? 'Activo' : 'Inactivo'}
                                        </span>
                                    </TableCell>
                                    <TableCell className="flex gap-2">
                                        <Button variant="outline" size="sm" onClick={() => handleOpenModal(plan)}>
                                            <FiEdit className="h-4 w-4" />
                                        </Button>
                                        <Button variant="destructive" size="sm" onClick={() => handleDeletePlan(plan.id)}>
                                            <FiTrash2 className="h-4 w-4" />
                                        </Button>
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </CardContent>
            </Card>

            <PlanFormModal
                isOpen={isModalOpen}
                onClose={handleCloseModal}
                onSave={handleSavePlan}
                planToEdit={planToEdit}
            />
        </>
    );
}
