'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockProductos = [
    {
        id: 1,
        nombre: 'Mochila Wayuu Tradicional',
        categoria: 'Tejidos',
        precio: '150,000',
        stock: 5,
    },
    {
        id: 2,
        nombre: 'Jarrón de Cerámica de Ráquira',
        categoria: 'Cerámica',
        precio: '80,000',
        stock: 12,
    },
    {
        id: 3,
        nombre: 'Collar de Filigrana de Mompox',
        categoria: 'Joyería',
        precio: '350,000',
        stock: 3,
    },
];

const GestionCatalogoPage = () => {
    const [productos, setProductos] = useState(mockProductos);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Catálogo de Productos</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mis Productos</h2>
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Producto
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {productos.map(producto => (
                        <div key={producto.id} className="border p-4 rounded-lg shadow-sm hover:shadow-lg transition-shadow flex flex-col">
                            {/* Idealmente aquí iría una <Image /> de Next.js */}
                            <div className="bg-gray-200 h-40 w-full rounded mb-3 flex items-center justify-center">
                                <span className="text-gray-500">Foto</span>
                            </div>
                            <h3 className="text-lg font-bold">{producto.nombre}</h3>
                            <p className="text-sm text-gray-500 mb-2">{producto.categoria}</p>
                            <div className="flex-grow"></div>
                            <div className="flex justify-between items-center mt-3">
                                <span className="text-lg font-bold text-green-700">${producto.precio}</span>
                                <span className="text-sm text-gray-600">Stock: {producto.stock}</span>
                            </div>
                            <div className="mt-4 pt-3 border-t flex justify-end space-x-2">
                                <button className="text-blue-600 hover:underline">Editar</button>
                                <button className="text-red-600 hover:underline">Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default GestionCatalogoPage;
