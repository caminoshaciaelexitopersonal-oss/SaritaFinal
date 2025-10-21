'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockEquipamiento = [
    { id: 1, nombre: 'Cascos de Seguridad', total: 20, disponible: 15 },
    { id: 2, nombre: 'Chalecos Salvavidas', total: 15, disponible: 15 },
    { id: 3, nombre: 'Radios de Comunicación', total: 10, disponible: 8 },
    { id: 4, nombre: 'Binoculares', total: 5, disponible: 2 },
];

const GestionEquipamientoPage = () => {
    const [equipamiento, setEquipamiento] = useState(mockEquipamiento);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Equipamiento y Materiales</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mi Inventario de Equipos</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Equipo
                    </button>
                </div>

                <table className="min-w-full bg-white">
                    <thead className="bg-gray-100">
                        <tr>
                            <th className="py-2 px-4 border-b">Nombre del Equipo</th>
                            <th className="py-2 px-4 border-b">Disponibles</th>
                            <th className="py-2 px-4 border-b">Total</th>
                            <th className="py-2 px-4 border-b">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {equipamiento.map((item) => (
                            <tr key={item.id}>
                                <td className="py-2 px-4 border-b">{item.nombre}</td>
                                <td className="py-2 px-4 border-b text-center">
                                    <span className="font-bold text-lg">{item.disponible}</span>
                                </td>
                                <td className="py-2 px-4 border-b text-center">{item.total}</td>
                                <td className="py-2 px-4 border-b text-center">
                                    <button className="text-blue-600 hover:underline mr-4">Editar</button>
                                    <button className="text-gray-600 hover:underline mr-4">Registrar Uso</button>
                                    <button className="text-red-600 hover:underline">Eliminar</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default GestionEquipamientoPage;
