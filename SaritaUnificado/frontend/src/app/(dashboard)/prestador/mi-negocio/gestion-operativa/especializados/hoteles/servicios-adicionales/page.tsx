'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockServicios = [
    { id: 1, nombre: 'Desayuno Americano', precio: 35000 },
    { id: 2, nombre: 'Servicio de Lavandería', precio: 50000 },
    { id: 3, nombre: 'Acceso a Spa', precio: 80000 },
];

const GestionServiciosAdicionalesPage = () => {
    const [servicios, setServicios] = useState(mockServicios);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Servicios Adicionales</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mis Servicios</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
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
                                <td className="py-2 px-4 border-b text-center">${servicio.precio.toLocaleString()}</td>
                                <td className="py-2 px-4 border-b text-center">
                                    <button className="text-blue-600 hover:underline mr-4">Editar</button>
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

export default GestionServiciosAdicionalesPage;
