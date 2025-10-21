'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockRutas = [
    {
        id: 1,
        nombre: 'Ruta del Café y las Montañas',
        descripcion: 'Un recorrido escénico por las fincas cafeteras, con degustación y vistas panorámicas.',
        duracion: '4 horas',
        dificultad: 'Moderada',
    },
    {
        id: 2,
        nombre: 'Aventura a la Cascada Escondida',
        descripcion: 'Caminata ecológica a través de la selva para descubrir una cascada secreta.',
        duracion: '6 horas',
        dificultad: 'Difícil',
    },
    {
        id: 3,
        nombre: 'Paseo Histórico por el Centro',
        descripcion: 'Descubre la arquitectura colonial y las historias ocultas del centro histórico.',
        duracion: '2.5 horas',
        dificultad: 'Fácil',
    }
];

const GestionRutasPage = () => {
    const [rutas, setRutas] = useState(mockRutas);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Rutas y Tours</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mis Rutas</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Crear Nueva Ruta
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {rutas.map(ruta => (
                        <div key={ruta.id} className="border p-4 rounded-lg shadow-sm hover:shadow-lg transition-shadow">
                            <h3 className="text-lg font-bold mb-2">{ruta.nombre}</h3>
                            <p className="text-gray-600 text-sm mb-3">{ruta.descripcion}</p>
                            <div className="flex justify-between items-center text-sm text-gray-800">
                                <span>Duración: <strong>{ruta.duracion}</strong></span>
                                <span className={`px-2 py-1 rounded-full text-xs font-semibold ${
                                    ruta.dificultad === 'Fácil' ? 'bg-green-200 text-green-800' :
                                    ruta.dificultad === 'Moderada' ? 'bg-yellow-200 text-yellow-800' :
                                    'bg-red-200 text-red-800'
                                }`}>
                                    {ruta.dificultad}
                                </span>
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

export default GestionRutasPage;
