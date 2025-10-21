'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockHabitaciones = [
    { id: 1, nombre: '101', tipo: 'Sencilla', capacidad: 1, precio: 150000 },
    { id: 2, nombre: '102', tipo: 'Doble', capacidad: 2, precio: 250000 },
    { id: 3, nombre: '201', tipo: 'Suite', capacidad: 2, precio: 400000 },
];

const GestionHabitacionesPage = () => {
    const [habitaciones, setHabitaciones] = useState(mockHabitaciones);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Habitaciones</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mis Habitaciones</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Habitación
                    </button>
                </div>

                <table className="min-w-full bg-white">
                    <thead className="bg-gray-100">
                        <tr>
                            <th className="py-2 px-4 border-b">Nombre/Número</th>
                            <th className="py-2 px-4 border-b">Tipo</th>
                            <th className="py-2 px-4 border-b">Capacidad</th>
                            <th className="py-2 px-4 border-b">Precio Base</th>
                            <th className="py-2 px-4 border-b">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {habitaciones.map((hab) => (
                            <tr key={hab.id}>
                                <td className="py-2 px-4 border-b text-center">{hab.nombre}</td>
                                <td className="py-2 px-4 border-b text-center">{hab.tipo}</td>
                                <td className="py-2 px-4 border-b text-center">{hab.capacidad}</td>
                                <td className="py-2 px-4 border-b text-center">${hab.precio.toLocaleString()}</td>
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

export default GestionHabitacionesPage;
