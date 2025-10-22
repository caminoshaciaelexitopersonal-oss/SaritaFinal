'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionServiciosAdicionalesPage = () => {
    const { data: servicios, loading, error, createItem, updateItem, deleteItem } = useApi('hoteles/servicios-adicionales/');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentServicio, setCurrentServicio] = useState(null);

    const handleOpenModal = (servicio = null) => {
        setCurrentServicio(servicio);
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
        setCurrentServicio(null);
    };

    const handleSave = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            nombre: formData.get('nombre'),
            precio: formData.get('precio'),
        };

        if (currentServicio) {
            await updateItem(currentServicio.id, data);
        } else {
            await createItem(data);
        }
        handleCloseModal();
    };

    if (loading) return <p>Cargando...</p>;
    if (error) return <p>Error al cargar los datos.</p>;

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Servicios Adicionales</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mis Servicios</h2>
                    <button onClick={() => handleOpenModal()} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Servicio
                    </button>
                </div>

                <table className="min-w-full bg-white">
                    <thead className="bg-gray-100">
                        <tr>
                            <th className="py-2 px-4 border-b">Nombre del Servicio</th>
                            <th className="py-2 px-4 border-b">Precio</th>
                            <th className="py-2 px-4 border-b">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {servicios.map((servicio) => (
                            <tr key={servicio.id}>
                                <td className="py-2 px-4 border-b">{servicio.nombre}</td>
                                <td className="py-2 px-4 border-b text-center">${parseFloat(servicio.precio).toLocaleString()}</td>
                                <td className="py-2 px-4 border-b text-center">
                                    <button onClick={() => handleOpenModal(servicio)} className="text-blue-600 hover:underline mr-4">Editar</button>
                                    <button onClick={() => deleteItem(servicio.id)} className="text-red-600 hover:underline">Eliminar</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {isModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <div className="mt-3 text-center">
                            <h3 className="text-lg leading-6 font-medium text-gray-900">{currentServicio ? 'Editar' : 'Añadir'} Servicio</h3>
                            <form onSubmit={handleSave} className="mt-2 px-7 py-3 space-y-4">
                                <input
                                    type="text"
                                    name="nombre"
                                    defaultValue={currentServicio?.nombre}
                                    placeholder="Nombre del servicio"
                                    className="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none"
                                    required
                                />
                                <input
                                    type="number"
                                    name="precio"
                                    defaultValue={currentServicio?.precio}
                                    placeholder="Precio"
                                    className="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none"
                                    required
                                />
                                <div className="items-center px-4 py-3">
                                    <button
                                        type="submit"
                                        className="px-4 py-2 bg-blue-500 text-white text-base font-medium rounded-md w-full shadow-sm hover:bg-blue-700 focus:outline-none"
                                    >
                                        Guardar
                                    </button>
                                </div>
                            </form>
                            <button onClick={handleCloseModal} className="text-sm text-gray-500 mt-2">Cancelar</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default GestionServiciosAdicionalesPage;
