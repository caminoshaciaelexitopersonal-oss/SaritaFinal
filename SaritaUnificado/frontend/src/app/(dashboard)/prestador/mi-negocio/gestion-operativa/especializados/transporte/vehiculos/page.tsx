'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockVehiculos = [
    { id: 1, placa: 'XYZ-123', marca: 'Toyota', modelo: 'Prado', año: 2022, capacidad: 7 },
    { id: 2, placa: 'ABC-456', marca: 'Mercedes-Benz', modelo: 'Sprinter', año: 2021, capacidad: 16 },
    { id: 3, placa: 'DEF-789', marca: 'Renault', modelo: 'Duster', año: 2023, capacidad: 5 },
];

const GestionVehiculosPage = () => {
    const [vehiculos, setVehiculos] = useState(mockVehiculos);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Vehículos</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mi Flota de Vehículos</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Vehículo
                    </button>
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full bg-white">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="py-2 px-4 border-b">Placa</th>
                                <th className="py-2 px-4 border-b">Marca y Modelo</th>
                                <th className="py-2 px-4 border-b">Año</th>
                                <th className="py-2 px-4 border-b">Capacidad</th>
                                <th className="py-2 px-4 border-b">Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {vehiculos.map((vehiculo) => (
                                <tr key={vehiculo.id}>
                                    <td className="py-2 px-4 border-b font-mono bg-gray-50">{vehiculo.placa}</td>
                                    <td className="py-2 px-4 border-b">{vehiculo.marca} {vehiculo.modelo}</td>
                                    <td className="py-2 px-4 border-b text-center">{vehiculo.año}</td>
                                    <td className="py-2 px-4 border-b text-center">{vehiculo.capacidad} pasajeros</td>
                                    <td className="py-2 px-4 border-b text-center">
                                        <button className="text-blue-600 hover:underline mr-4">Editar</button>
                                        <button className="text-gray-600 hover:underline mr-4">Documentos</button>
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

export default GestionVehiculosPage;
