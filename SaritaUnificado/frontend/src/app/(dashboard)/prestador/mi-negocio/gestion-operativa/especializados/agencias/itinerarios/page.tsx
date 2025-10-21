'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockItinerario = {
    paqueteNombre: 'Fin de Semana Cafetero',
    dias: [
        {
            dia: 1,
            titulo: 'Llegada y Bienvenida',
            descripcion: 'Registro en la finca cafetera. Por la tarde, recorrido guiado por los cafetales aprendiendo sobre el proceso de siembra y recolección. Cena tradicional.'
        },
        {
            dia: 2,
            titulo: 'Del Grano a la Taza',
            descripcion: 'Taller de tostado y molienda. Cata de diferentes perfiles de café con un barista experto. Tarde libre para disfrutar del paisaje.'
        },
        {
            dia: 3,
            titulo: 'Despedida',
            descripcion: 'Desayuno de despedida. Tiempo para comprar café de origen y artesanías locales antes del regreso.'
        },
    ]
};

const GestionItinerarioPage = () => {
    const [itinerario, setItinerario] = useState(mockItinerario);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-1">Gestión de Itinerario</h1>
            <h2 className="text-xl text-gray-600 mb-4">Paquete: {itinerario.paqueteNombre}</h2>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Cronograma de Actividades</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Actividad
                    </button>
                </div>

                <div className="space-y-6">
                    {itinerario.dias.map(item => (
                        <div key={item.dia} className="border-l-4 border-blue-600 pl-4 py-2">
                            <h3 className="text-lg font-bold">Día {item.dia}: {item.titulo}</h3>
                            <p className="text-gray-700 mt-1">{item.descripcion}</p>
                            <div className="mt-2 text-right">
                                <button className="text-sm text-blue-600 hover:underline mr-3">Editar</button>
                                <button className="text-sm text-red-600 hover:underline">Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default GestionItinerarioPage;
