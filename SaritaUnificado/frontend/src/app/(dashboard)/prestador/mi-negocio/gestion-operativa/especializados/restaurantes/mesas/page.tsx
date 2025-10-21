'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockMesas = [
    { id: 1, numero: '1', capacidad: 4, ubicacion: 'Salón Principal', disponible: true },
    { id: 2, numero: '2', capacidad: 2, ubicacion: 'Ventanal', disponible: false },
    { id: 3, numero: 'T1', capacidad: 6, ubicacion: 'Terraza', disponible: true },
    { id: 4, numero: 'Barra 1', capacidad: 1, ubicacion: 'Barra', disponible: true },
];

const mockReservas = [
    { id: 1, mesa: '2', cliente: 'Carlos Mendoza', fecha: '2023-10-27 20:00', personas: 2 },
    { id: 2, mesa: 'T1', cliente: 'Ana Sofía Rojas', fecha: '2023-10-27 21:00', personas: 5 },
];

const GestionMesasPage = () => {
    const [mesas, setMesas] = useState(mockMesas);
    const [reservas, setReservas] = useState(mockReservas);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Mesas y Reservaciones</h1>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {/* Sección de Gestión de Mesas */}
                <div className="bg-white p-6 rounded-lg shadow-md">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-xl font-semibold">Mis Mesas</h2>
                        <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                            Añadir Mesa
                        </button>
                    </div>
                    <table className="min-w-full bg-white">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="py-2 px-4 border-b">Número</th>
                                <th className="py-2 px-4 border-b">Capacidad</th>
                                <th className="py-2 px-4 border-b">Ubicación</th>
                                <th className="py-2 px-4 border-b">Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {mesas.map((mesa) => (
                                <tr key={mesa.id}>
                                    <td className="py-2 px-4 border-b text-center">{mesa.numero}</td>
                                    <td className="py-2 px-4 border-b text-center">{mesa.capacidad}</td>
                                    <td className="py-2 px-4 border-b">{mesa.ubicacion}</td>
                                    <td className="py-2 px-4 border-b text-center">
                                        <button className="text-blue-600 hover:underline mr-2">Editar</button>
                                        <button className="text-red-600 hover:underline">Eliminar</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                {/* Sección de Próximas Reservas */}
                <div className="bg-white p-6 rounded-lg shadow-md">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-xl font-semibold">Próximas Reservas</h2>
                        <button className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700">
                            Nueva Reserva
                        </button>
                    </div>
                    <ul className="space-y-3">
                        {reservas.map(reserva => (
                             <li key={reserva.id} className="p-3 bg-gray-50 rounded-md shadow-sm">
                                <p><strong>Cliente:</strong> {reserva.cliente}</p>
                                <p><strong>Mesa:</strong> {reserva.mesa} - <strong>Personas:</strong> {reserva.personas}</p>
                                <p><strong>Fecha:</strong> {reserva.fecha}</p>
                             </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default GestionMesasPage;
