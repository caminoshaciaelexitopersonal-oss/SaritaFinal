'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionPaquetesPage = () => {
    const { data: paquetes, loading, error, createItem, updateItem, deleteItem } = useApi('agencias/paquetes/');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentItem, setCurrentItem] = useState(null);

    const handleOpenModal = (item = null) => {
        setCurrentItem(item);
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
        setCurrentItem(null);
    };

    const handleSave = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            nombre: formData.get('nombre'),
            descripcion: formData.get('descripcion'),
            duracion_dias: formData.get('duracion_dias'),
            precio_base: formData.get('precio_base'),
        };

        if (currentItem) {
            await updateItem(currentItem.id, data);
        } else {
            await createItem(data);
        }
        handleCloseModal();
    };

    if (loading) return <p>Cargando...</p>;
    if (error) return <p>Error al cargar los datos.</p>;

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Paquetes Turísticos</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mis Paquetes</h2>
                    <button onClick={() => handleOpenModal()} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Crear Nuevo Paquete
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {paquetes.map(paquete => (
                        <div key={paquete.id} className="border p-4 rounded-lg shadow-sm hover:shadow-lg transition-shadow">
                           {/* ... (renderizado de la tarjeta del paquete) */}
                            <div className="mt-4 pt-3 border-t flex justify-end space-x-2">
                                <button onClick={() => handleOpenModal(paquete)} className="text-blue-600 hover:underline">Editar</button>
                                <button className="text-gray-500 hover:underline">Itinerario</button>
                                <button onClick={() => deleteItem(paquete.id)} className="text-red-600 hover:underline">Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {isModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form onSubmit={handleSave}>
                            {/* Campos del formulario */}
                            <button type="submit">Guardar</button>
                            <button type="button" onClick={handleCloseModal}>Cancelar</button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default GestionPaquetesPage;
