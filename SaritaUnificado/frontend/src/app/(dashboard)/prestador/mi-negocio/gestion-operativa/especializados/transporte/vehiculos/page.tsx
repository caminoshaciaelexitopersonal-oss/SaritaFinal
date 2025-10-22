'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionVehiculosPage = () => {
    const { data: vehiculos, loading, error, createItem, updateItem, deleteItem } = useApi('transporte/vehiculos/');
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
            placa: formData.get('placa'),
            marca: formData.get('marca'),
            modelo: formData.get('modelo'),
            año: formData.get('año'),
            capacidad_pasajeros: formData.get('capacidad_pasajeros'),
            tipo_vehiculo: formData.get('tipo_vehiculo'),
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
            <h1 className="text-2xl font-bold mb-4">Gestión de Vehículos</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mi Flota de Vehículos</h2>
                    <button onClick={() => handleOpenModal()} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Vehículo
                    </button>
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full bg-white">
                        {/* ... (renderizado de la tabla) */}
                    </table>
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

export default GestionVehiculosPage;
