'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionMenuPage = () => {
    const { data: categorias, loading: loadingCategorias, createItem: createCategoria, updateItem: updateCategoria, deleteItem: deleteCategoria } = useApi('restaurantes/menu/categorias/');
    const { data: productos, loading: loadingProductos, createItem: createProducto, updateItem: updateProducto, deleteItem: deleteProducto } = useApi('restaurantes/menu/productos/');

    const [isCategoriaModalOpen, setIsCategoriaModalOpen] = useState(false);
    const [isProductoModalOpen, setIsProductoModalOpen] = useState(false);
    const [currentCategoria, setCurrentCategoria] = useState(null);
    const [currentProducto, setCurrentProducto] = useState(null);

    const handleSaveCategoria = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = { nombre: formData.get('nombre'), descripcion: formData.get('descripcion') };
        if (currentCategoria) {
            await updateCategoria(currentCategoria.id, data);
        } else {
            await createCategoria(data);
        }
        setIsCategoriaModalOpen(false);
    };

    const handleSaveProducto = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            nombre: formData.get('nombre'),
            descripcion: formData.get('descripcion'),
            precio: formData.get('precio'),
            categoria: formData.get('categoria'),
        };
        if (currentProducto) {
            await updateProducto(currentProducto.id, data);
        } else {
            await createProducto(data);
        }
        setIsProductoModalOpen(false);
    };

    if (loadingCategorias || loadingProductos) return <p>Cargando...</p>;

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Menú / Carta</h1>
            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-xl font-semibold">Mi Menú</h2>
                    <div>
                        <button onClick={() => setIsProductoModalOpen(true)} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 mr-2">Añadir Producto</button>
                        <button onClick={() => setIsCategoriaModalOpen(true)} className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700">Añadir Categoría</button>
                    </div>
                </div>
                {/* Renderizado de categorías y productos */}
            </div>

            {/* Modal para Categoría */}
            {isCategoriaModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form onSubmit={handleSaveCategoria}>
                            <h3 className="text-lg font-medium">Categoría</h3>
                            <input type="text" name="nombre" placeholder="Nombre" defaultValue={currentCategoria?.nombre} required className="w-full mt-2 p-2 border rounded"/>
                            <textarea name="descripcion" placeholder="Descripción" defaultValue={currentCategoria?.descripcion} className="w-full mt-2 p-2 border rounded"/>
                            <button type="submit" className="w-full mt-4 bg-blue-500 text-white p-2 rounded">Guardar</button>
                            <button type="button" onClick={() => setIsCategoriaModalOpen(false)} className="w-full mt-2 text-gray-500">Cancelar</button>
                        </form>
                    </div>
                </div>
            )}

            {/* Modal para Producto */}
            {isProductoModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form onSubmit={handleSaveProducto}>
                            <h3 className="text-lg font-medium">Producto</h3>
                            <input type="text" name="nombre" placeholder="Nombre" defaultValue={currentProducto?.nombre} required className="w-full mt-2 p-2 border rounded"/>
                            <textarea name="descripcion" placeholder="Descripción" defaultValue={currentProducto?.descripcion} className="w-full mt-2 p-2 border rounded"/>
                            <input type="number" name="precio" placeholder="Precio" defaultValue={currentProducto?.precio} required className="w-full mt-2 p-2 border rounded"/>
                            <select name="categoria" defaultValue={currentProducto?.categoria} required className="w-full mt-2 p-2 border rounded">
                                {categorias.map(c => <option key={c.id} value={c.id}>{c.nombre}</option>)}
                            </select>
                            <button type="submit" className="w-full mt-4 bg-blue-500 text-white p-2 rounded">Guardar</button>
                            <button type="button" onClick={() => setIsProductoModalOpen(false)} className="w-full mt-2 text-gray-500">Cancelar</button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default GestionMenuPage;
