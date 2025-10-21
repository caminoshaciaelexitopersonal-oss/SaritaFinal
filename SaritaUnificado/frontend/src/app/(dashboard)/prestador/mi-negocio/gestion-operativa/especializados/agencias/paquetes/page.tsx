'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockPaquetes = [
    {
        id: 1,
        nombre: 'Fin de Semana Cafetero',
        descripcion: 'Vive la experiencia completa del café, desde la recolección hasta la taza. Incluye alojamiento en finca cafetera, tour guiado y cata profesional.',
        duracion: '3 días / 2 noches',
        precio: '750,000',
    },
    {
        id: 2,
        nombre: 'Aventura Extrema en el Río',
        descripcion: 'Un paquete lleno de adrenalina con rafting, canyoning y senderismo por la ribera del río. Incluye transporte, equipos y guía certificado.',
        duracion: '2 días / 1 noche',
        precio: '980,000',
    },
];

const GestionPaquetesPage = () => {
    const [paquetes, setPaquetes] = useState(mockPaquetes);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Paquetes Turísticos</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mis Paquetes</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Crear Nuevo Paquete
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {paquetes.map(paquete => (
                        <div key={paquete.id} className="border p-4 rounded-lg shadow-sm hover:shadow-lg transition-shadow">
                            <h3 className="text-lg font-bold mb-2">{paquete.nombre}</h3>
                            <p className="text-gray-600 text-sm mb-3">{paquete.descripcion}</p>
                            <div className="flex justify-between items-center text-sm text-gray-800">
                                <span>Duración: <strong>{paquete.duracion}</strong></span>
                                <span className="text-lg font-bold text-green-700">${paquete.precio} COP</span>
                            </div>
                            <div className="mt-4 pt-3 border-t flex justify-end space-x-2">
                                <button className="text-blue-600 hover:underline">Editar</button>
                                <button className="text-gray-500 hover:underline">Itinerario</button>
                                <button className="text-red-600 hover:underline">Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default GestionPaquetesPage;
