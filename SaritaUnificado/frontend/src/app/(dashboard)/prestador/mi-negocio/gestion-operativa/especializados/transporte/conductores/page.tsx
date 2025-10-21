'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockConductores = [
    { id: 1, nombre: 'Juan', apellido: 'Pérez', cedula: '12345678', licencia: 'C1', vencimiento: '2024-12-31' },
    { id: 2, nombre: 'Ana', apellido: 'García', cedula: '87654321', licencia: 'C2', vencimiento: '2025-06-15' },
    { id: 3, nombre: 'Luis', apellido: 'Martínez', cedula: '11223344', licencia: 'C1', vencimiento: '2024-11-20' },
];

const GestionConductoresPage = () => {
    const [conductores, setConductores] = useState(mockConductores);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Conductores</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mi Equipo de Conductores</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Conductor
                    </button>
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full bg-white">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="py-2 px-4 border-b">Nombre Completo</th>
                                <th className="py-2 px-4 border-b">Cédula</th>
                                <th className="py-2 px-4 border-b">Licencia</th>
                                <th className="py-2 px-4 border-b">Vencimiento</th>
                                <th className="py-2 px-4 border-b">Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {conductores.map((conductor) => (
                                <tr key={conductor.id}>
                                    <td className="py-2 px-4 border-b">{conductor.nombre} {conductor.apellido}</td>
                                    <td className="py-2 px-4 border-b">{conductor.cedula}</td>
                                    <td className="py-2 px-4 border-b text-center">{conductor.licencia}</td>
                                    <td className="py-2 px-4 border-b text-center">{conductor.vencimiento}</td>
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
        </div>
    );
};

export default GestionConductoresPage;
