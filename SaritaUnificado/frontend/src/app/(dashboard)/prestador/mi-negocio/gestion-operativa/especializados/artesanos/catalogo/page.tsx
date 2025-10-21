'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionCatalogoPage = () => {
    const { data: productos, loading, error, createItem, updateItem, deleteItem } = useApi('artesanos/productos/');
    const { data: categorias } = useApi('artesanos/categorias/');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentItem, setCurrentItem] = useState(null);

    // ... (lógica de modales y guardado)

    if (loading) return <p>Cargando...</p>;
    if (error) return <p>Error al cargar los datos.</a`

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Catálogo de Productos</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mis Productos</h2>
                    <button onClick={() => setIsModalOpen(true)} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Añadir Producto
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {productos.map(producto => (
                        <div key={producto.id} className="border p-4 rounded-lg shadow-sm hover:shadow-lg flex flex-col">
                           {/* ... (renderizado de la tarjeta del producto) */}
                            <div className="mt-4 pt-3 border-t flex justify-end space-x-2">
                                <button onClick={() => { setCurrentItem(producto); setIsModalOpen(true); }} className="text-blue-600 hover:underline">Editar</button>
                                <button onClick={() => deleteItem(producto.id)} className="text-red-600 hover:underline">Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {isModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form>
                            {/* Campos del formulario */}
                            <select name="categoria">
                                {categorias.map(c => <option key={c.id} value={c.id}>{c.nombre}</option>)}
                            </select>
                            <button type="submit">Guardar</button>
                            <button type="button" onClick={() => setIsModalOpen(false)}>Cancelar</button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default GestionCatalogoPage;
