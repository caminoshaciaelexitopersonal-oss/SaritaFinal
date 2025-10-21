'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionEquipamientoPage = () => {
    const { data: equipamiento, loading, error, createItem, updateItem, deleteItem } = useApi('guias/equipamiento/');
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
            cantidad_total: formData.get('cantidad_total'),
            cantidad_disponible: formData.get('cantidad_disponible'),
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
            <h1 className="text-2xl font-bold mb-4">Gestión de Equipamiento y Materiales</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mi Inventario de Equipos</h2>
                    <button onClick={() => handleOpenModal()} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Equipo
                    </button>
                </div>

                <table className="min-w-full bg-white">
                    {/* ... (renderizado de la tabla) */}
                </table>
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

export default GestionEquipamientoPage;
