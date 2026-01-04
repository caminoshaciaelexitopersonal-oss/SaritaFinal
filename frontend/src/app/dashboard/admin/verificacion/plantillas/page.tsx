'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, useFieldArray, SubmitHandler } from 'react-hook-form';
import { FiClipboard, FiPlus, FiEdit, FiTrash2, FiPlusCircle } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface ItemVerificacion {
    id?: number;
    texto_requisito: string;
    puntaje: number;
    es_obligatorio: boolean;
}

interface Plantilla {
    id: number;
    nombre: string;
    descripcion: string;
    items: ItemVerificacion[];
}

type PlantillaFormData = Omit<Plantilla, 'id' | 'items'> & {
    items_attributes: ItemVerificacion[];
};

const PlantillasManager = () => {
    const [plantillas, setPlantillas] = useState<Plantilla[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [editingPlantilla, setEditingPlantilla] = useState<Plantilla | null>(null);

    const { register, control, handleSubmit, reset, setValue } = useForm<PlantillaFormData>();
    const { fields, append, remove } = useFieldArray({ control, name: "items_attributes" });

    const fetchPlantillas = async () => {
        setIsLoading(true);
        try {
            const response = await api.get('/api/plantillas-verificacion/');
            setPlantillas(response.data.results || response.data);
        } catch (error) {
            toast.error('No se pudieron cargar las plantillas.');
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => { fetchPlantillas() }, []);

    const openModalForCreate = () => {
        reset({ nombre: '', descripcion: '', items_attributes: [{ texto_requisito: '', puntaje: 1, es_obligatorio: true }] });
        setEditingPlantilla(null);
        setIsModalOpen(true);
    };

    const openModalForEdit = async (plantillaId: number) => {
        try {
            const data = await api.get(`/api/plantillas-verificacion/${plantillaId}/`);
            setEditingPlantilla(data);
            reset({ ...data, items_attributes: data.items });
            setIsModalOpen(true);
        } catch {
            toast.error("No se pudo cargar la plantilla para editar.");
        }
    };

    const onSubmit: SubmitHandler<PlantillaFormData> = async (data) => {
        const apiCall = editingPlantilla
            ? api.put(`/api/plantillas-verificacion/${editingPlantilla.id}/`, data)
            : api.post('/api/plantillas-verificacion/', data);
        try {
            await apiCall;
            toast.success(`Plantilla ${editingPlantilla ? 'actualizada' : 'creada'}.`);
            fetchPlantillas();
            setIsModalOpen(false);
        } catch (error) { toast.error('Error al guardar la plantilla.'); }
    };

    const handleDelete = async (id: number) => {
        if (window.confirm('¿Eliminar esta plantilla? No se podrá usar para nuevas verificaciones.')) {
            try {
                await api.delete(`/api/plantillas-verificacion/${id}/`);
                toast.success('Plantilla eliminada.');
                fetchPlantillas();
            } catch (error) { toast.error('No se pudo eliminar la plantilla.'); }
        }
    };

    if (isLoading) return <div>Cargando plantillas...</div>;

    return (
        <div className="p-6 bg-white rounded-lg shadow-md">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold text-gray-800">Plantillas de Verificación</h1>
                <button onClick={openModalForCreate} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
                    <FiPlus className="mr-2" />Crear Plantilla
                </button>
            </div>

            <div className="space-y-4">
                {plantillas.map(p => (
                    <div key={p.id} className="p-4 border rounded-lg flex justify-between items-center">
                        <div>
                            <h3 className="font-bold text-xl">{p.nombre}</h3>
                            <p className="text-sm text-gray-600">{p.descripcion}</p>
                        </div>
                        <div>
                            <button onClick={() => openModalForEdit(p.id)} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                            <button onClick={() => handleDelete(p.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                        </div>
                    </div>
                ))}
            </div>

            {isModalOpen && (
                <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingPlantilla ? 'Editar Plantilla' : 'Crear Plantilla'}>
                    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                        <input {...register('nombre', { required: true })} placeholder="Nombre de la Plantilla" className="w-full p-2 border rounded"/>
                        <textarea {...register('descripcion')} placeholder="Descripción" rows={3} className="w-full p-2 border rounded"/>
                        <h3 className="font-bold mt-4">Ítems de Verificación</h3>
                        <div className="space-y-2 max-h-60 overflow-y-auto">
                            {fields.map((field, index) => (
                                <div key={field.id} className="flex items-center gap-2 p-2 bg-gray-100 rounded">
                                    <input {...register(`items_attributes.${index}.texto_requisito`)} placeholder="Texto del requisito" className="flex-grow p-2 border rounded"/>
                                    <input type="number" {...register(`items_attributes.${index}.puntaje`, { valueAsNumber: true })} placeholder="Puntos" className="w-20 p-2 border rounded"/>
                                    <button type="button" onClick={() => remove(index)}><FiTrash2 className="text-red-500"/></button>
                                </div>
                            ))}
                        </div>
                        <button type="button" onClick={() => append({ texto_requisito: '', puntaje: 1, es_obligatorio: true })} className="text-sm text-blue-600 hover:underline">
                            <FiPlusCircle className="inline mr-1"/>Añadir Ítem
                        </button>
                        <button type="submit" className="w-full mt-4 px-4 py-2 bg-green-600 text-white rounded-md">Guardar Plantilla</button>
                    </form>
                </Modal>
            )}
        </div>
    );
};

const PlantillasPage = () => <AuthGuard allowedRoles={['ADMIN', 'FUNCIONARIO_DIRECTIVO']}><PlantillasManager /></AuthGuard>;
export default PlantillasPage;