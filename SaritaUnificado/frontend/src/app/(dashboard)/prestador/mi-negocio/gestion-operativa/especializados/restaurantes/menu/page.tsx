'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockCategorias = [
    {
        id: 1,
        nombre: 'Entradas',
        productos: [
            { id: 101, nombre: 'Empanadas de Cambray', precio: 12000 },
            { id: 102, nombre: 'Patacones con Hogao', precio: 15000 },
        ]
    },
    {
        id: 2,
        nombre: 'Platos Fuertes',
        productos: [
            { id: 201, nombre: 'Bandeja Paisa', precio: 35000 },
            { id: 202, nombre: 'Sancocho de Gallina', precio: 32000 },
            { id: 203, nombre: 'Mojarra Frita', precio: 40000 },
        ]
    },
    {
        id: 3,
        nombre: 'Bebidas',
        productos: [
            { id: 301, nombre: 'Jugo de Lulo', precio: 8000 },
            { id: 302, nombre: 'Gaseosa', precio: 5000 },
        ]
    }
];

const GestionMenuPage = () => {
    const [categorias, setCategorias] = useState(mockCategorias);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Menú / Carta</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mi Menú</h2>
                    <div>
                        <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 mr-2">
                            Añadir Producto
                        </button>
                        <button className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700">
                            Añadir Categoría
                        </button>
                    </div>
                </div>

                <div className="space-y-6">
                    {categorias.map(categoria => (
                        <div key={categoria.id}>
                            <h3 className="text-lg font-semibold border-b pb-2 mb-3">{categoria.nombre}</h3>
                            <table className="min-w-full bg-white">
                                <thead className="bg-gray-50">
                                    <tr>
                                        <th className="py-2 px-4 text-left">Producto</th>
                                        <th className="py-2 px-4 text-right">Precio</th>
                                        <th className="py-2 px-4 text-center">Acciones</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {categoria.productos.map(producto => (
                                        <tr key={producto.id}>
                                            <td className="py-2 px-4 border-b">{producto.nombre}</td>
                                            <td className="py-2 px-4 border-b text-right">${producto.precio.toLocaleString()}</td>
                                            <td className="py-2 px-4 border-b text-center">
                                                <button className="text-blue-600 hover:underline mr-4">Editar</button>
                                                <button className="text-red-600 hover:underline">Eliminar</button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default GestionMenuPage;
