'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, SubmitHandler } from 'react-hook-form';
import { FiBookOpen, FiPlus, FiEdit, FiTrash2, FiPackage, FiTag } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Producto {
    id: number;
    nombre: string;
    descripcion: string;
    precio: string;
    disponible: boolean;
}

interface Categoria {
    id: number;
    nombre: string;
    productos: Producto[];
}

type CategoriaFormData = { nombre: string };
type ProductoFormData = Omit<Producto, 'id'> & { categoria: number };

const MenuManager = () => {
    const [categorias, setCategorias] = useState<Categoria[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isCategoriaModalOpen, setIsCategoriaModalOpen] = useState(false);
    const [isProductoModalOpen, setIsProductoModalOpen] = useState(false);
    const [editingCategoria, setEditingCategoria] = useState<Categoria | null>(null);
    const [editingProducto, setEditingProducto] = useState<Producto | null>(null);
    const [categoriaForNewProducto, setCategoriaForNewProducto] = useState<number | null>(null);

    const { register: registerCategoria, handleSubmit: handleCategoriaSubmit, reset: resetCategoria } = useForm<CategoriaFormData>();
    const { register: registerProducto, handleSubmit: handleProductoSubmit, reset: resetProducto, setValue: setProductoValue } = useForm<ProductoFormData>();

    const fetchMenu = async () => {
        setIsLoading(true);
        try {
            const response = await api.get('/restaurante/categorias-con-productos/');
            setCategorias(response.data.results || response.data);
        } catch (error) {
            toast.error('No se pudo cargar el menú.');
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => { fetchMenu() }, []);

    // --- Lógica para Categorías ---
    const onCategoriaSubmit: SubmitHandler<CategoriaFormData> = async (data) => {
        const apiCall = editingCategoria
            ? api.patch(`/restaurante/categorias/${editingCategoria.id}/`, data)
            : api.post('/restaurante/categorias/', data);
        try {
            await apiCall;
            toast.success(`Categoría ${editingCategoria ? 'actualizada' : 'creada'}.`);
            fetchMenu();
            setIsCategoriaModalOpen(false);
        } catch (error) { toast.error('Error al guardar la categoría.'); }
    };

    const handleDeleteCategoria = async (id: number) => {
        if (window.confirm('¿Eliminar esta categoría? Todos sus productos también serán eliminados.')) {
            try {
                await api.delete(`/restaurante/categorias/${id}/`);
                toast.success('Categoría eliminada.');
                fetchMenu();
            } catch (error) { toast.error('No se pudo eliminar la categoría.'); }
        }
    };

    // --- Lógica para Productos ---
    const onProductoSubmit: SubmitHandler<ProductoFormData> = async (data) => {
        const apiCall = editingProducto
            ? api.patch(`/restaurante/productos/${editingProducto.id}/`, data)
            : api.post('/restaurante/productos/', { ...data, categoria: categoriaForNewProducto });
        try {
            await apiCall;
            toast.success(`Producto ${editingProducto ? 'actualizado' : 'creado'}.`);
            fetchMenu();
            setIsProductoModalOpen(false);
        } catch (error) { toast.error('Error al guardar el producto.'); }
    };

    const handleDeleteProducto = async (id: number) => {
        if (window.confirm('¿Eliminar este producto?')) {
            try {
                await api.delete(`/restaurante/productos/${id}/`);
                toast.success('Producto eliminado.');
                fetchMenu();
            } catch (error) { toast.error('No se pudo eliminar el producto.'); }
        }
    };

    if (isLoading) return <div>Cargando menú...</div>;

    return (
        <div className="p-6 bg-white rounded-lg shadow-md">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold text-gray-800">Gestionar Menú / Carta</h1>
                <button onClick={() => { setEditingCategoria(null); resetCategoria(); setIsCategoriaModalOpen(true); }} className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
                    <FiPlus className="mr-2" /> Añadir Categoría
                </button>
            </div>

            <div className="space-y-6">
                {categorias.length > 0 ? categorias.map(cat => (
                    <div key={cat.id} className="p-4 border rounded-lg">
                        <div className="flex justify-between items-center mb-3">
                            <h2 className="text-2xl font-semibold text-gray-700 flex items-center"><FiTag className="mr-3"/>{cat.nombre}</h2>
                            <div>
                                <button onClick={() => { setEditingCategoria(cat); resetCategoria({ nombre: cat.nombre }); setIsCategoriaModalOpen(true); }} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                                <button onClick={() => handleDeleteCategoria(cat.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                                <button onClick={() => { setCategoriaForNewProducto(cat.id); setEditingProducto(null); resetProducto(); setIsProductoModalOpen(true); }} className="ml-4 inline-flex items-center px-3 py-1 bg-green-500 text-white text-sm rounded hover:bg-green-600"><FiPlus className="mr-1"/>Añadir Producto</button>
                            </div>
                        </div>
                        <div className="space-y-2 pl-4">
                            {cat.productos.map(prod => (
                                <div key={prod.id} className="flex justify-between items-center p-2 border-b">
                                    <div>
                                        <p className="font-semibold">{prod.nombre}</p>
                                        <p className="text-sm text-gray-500">{prod.descripcion}</p>
                                    </div>
                                    <div className="flex items-center">
                                        <p className="mr-4 font-bold text-gray-800">${prod.precio}</p>
                                        <button onClick={() => { setEditingProducto(prod); setProductoValue('nombre', prod.nombre); setProductoValue('descripcion', prod.descripcion); setProductoValue('precio', prod.precio); setProductoValue('disponible', prod.disponible); setProductoValue('categoria', cat.id); setIsProductoModalOpen(true); }} className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
                                        <button onClick={() => handleDeleteProducto(prod.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                )) : <p>No hay categorías en el menú. ¡Añade una para empezar!</p>}
            </div>

            {/* Modales */}
            {isCategoriaModalOpen && (
                <Modal isOpen={isCategoriaModalOpen} onClose={() => setIsCategoriaModalOpen(false)} title={editingCategoria ? "Editar Categoría" : "Crear Categoría"}>
                    <form onSubmit={handleCategoriaSubmit(onCategoriaSubmit)} className="space-y-4">
                        <input {...registerCategoria('nombre', { required: true })} placeholder="Nombre de la categoría" className="w-full mt-1 p-2 border rounded" />
                        <button type="submit" className="w-full px-4 py-2 bg-blue-600 text-white rounded-md">Guardar</button>
                    </form>
                </Modal>
            )}
            {isProductoModalOpen && (
                 <Modal isOpen={isProductoModalOpen} onClose={() => setIsProductoModalOpen(false)} title={editingProducto ? "Editar Producto" : "Crear Producto"}>
                    <form onSubmit={handleProductoSubmit(onProductoSubmit)} className="space-y-4">
                        <input {...registerProducto('nombre', { required: true })} placeholder="Nombre del producto" className="w-full mt-1 p-2 border rounded" />
                        <textarea {...registerProducto('descripcion')} placeholder="Descripción" className="w-full mt-1 p-2 border rounded" />
                        <input type="text" {...registerProducto('precio', { required: true })} placeholder="Precio" className="w-full mt-1 p-2 border rounded" />
                        <div className="flex items-center"><input type="checkbox" {...registerProducto('disponible')} defaultChecked={true} /> <label className="ml-2">Disponible</label></div>
                        <button type="submit" className="w-full px-4 py-2 bg-blue-600 text-white rounded-md">Guardar</button>
                    </form>
                </Modal>
            )}
        </div>
    );
};

const MenuPage = () => <AuthGuard allowedRoles={['PRESTADOR']}><MenuManager /></AuthGuard>;
export default MenuPage;