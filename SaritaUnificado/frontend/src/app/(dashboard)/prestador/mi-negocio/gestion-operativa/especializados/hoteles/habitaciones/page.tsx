'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionHabitacionesPage = () => {
    const { data: habitaciones, loading, error, createItem, updateItem, deleteItem } = useApi('hoteles/habitaciones/');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentHabitacion, setCurrentHabitacion] = useState(null);

    const handleOpenModal = (habitacion = null) => {
        setCurrentHabitacion(habitacion);
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
        setCurrentHabitacion(null);
    };

    const handleSave = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            nombre: formData.get('nombre'),
        };

        if (currentHabitacion) {
            await updateItem(currentHabitacion.id, data);
        } else {
            await createItem(data);
        }
        handleCloseModal();
    };

    if (loading) return <p>Cargando...</p>;
    if (error) return <p>Error al cargar los datos.</p>;

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Habitaciones</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mis Habitaciones</h2>
                    <button onClick={() => handleOpenModal()} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Habitación
                    </button>
                </div>

                <table className="min-w-full bg-white">
                    <thead className="bg-gray-100">
                        <tr>
                            <th className="py-2 px-4 border-b">Nombre</th>
                            <th className="py-2 px-4 border-b">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {habitaciones.map((habitacion) => (
                            <tr key={habitacion.id}>
                                <td className="py-2 px-4 border-b">{habitacion.nombre}</td>
                                <td className="py-2 px-4 border-b text-center">
                                    <button onClick={() => handleOpenModal(habitacion)} className="text-blue-600 hover:underline mr-4">Editar</button>
                                    <button onClick={() => deleteItem(habitacion.id)} className="text-red-600 hover:underline">Eliminar</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {isModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" id="my-modal">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <div className="mt-3 text-center">
                            <h3 className="text-lg leading-6 font-medium text-gray-900">{currentHabitacion ? 'Editar' : 'Añadir'} Habitación</h3>
                            <form onSubmit={handleSave} className="mt-2 px-7 py-3">
                                <input
                                    type="text"
                                    name="nombre"
                                    defaultValue={currentHabitacion?.nombre}
                                    placeholder="Nombre de la habitación"
                                    className="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none"
                                />
                                <div className="items-center px-4 py-3">
                                    <button
                                        type="submit"
                                        className="px-4 py-2 bg-blue-500 text-white text-base font-medium rounded-md w-full shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300"
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

export default GestionHabitacionesPage;
