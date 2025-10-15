'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';
import { FiPlus } from 'react-icons/fi';

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

type CategoriaFormInputs = { nombre: string };
type ProductoFormInputs = Omit<Producto, 'id'> & { categoria: number };

const Menu = () => {
  const [categorias, setCategorias] = useState<Categoria[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Estados para los modales
  const [isCategoriaModalOpen, setIsCategoriaModalOpen] = useState(false);
  const [isProductoModalOpen, setIsProductoModalOpen] = useState(false);
  const [editingCategoria, setEditingCategoria] = useState<Categoria | null>(null);
  const [editingProducto, setEditingProducto] = useState<Producto | null>(null);
  const [categoriaForNewProducto, setCategoriaForNewProducto] = useState<number | null>(null);

  const formCategoria = useForm<CategoriaFormInputs>();
  const formProducto = useForm<ProductoFormInputs>();

  const fetchMenu = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/restaurante/categorias-menu/');
      setCategorias(response.data.results || []);
    } catch (err: any) {
      setError('No se pudo cargar el menú. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchMenu();
  }, [fetchMenu]);

  // --- Lógica para Categorías ---
  const onCategoriaSubmit: SubmitHandler<CategoriaFormInputs> = async (data) => {
    try {
      if (editingCategoria) {
        await api.patch(`/restaurante/categorias-menu/${editingCategoria.id}/`, data);
        toast.success('Categoría actualizada');
      } else {
        await api.post('/restaurante/categorias-menu/', data);
        toast.success('Categoría creada');
      }
      setIsCategoriaModalOpen(false);
      fetchMenu();
    } catch (err: any) {
      toast.error('Error al guardar la categoría');
    }
  };

  // --- Lógica para Productos ---
  const onProductoSubmit: SubmitHandler<ProductoFormInputs> = async (data) => {
    try {
      if (editingProducto) {
        await api.patch(`/restaurante/productos-menu/${editingProducto.id}/`, data);
        toast.success('Producto actualizado');
      } else {
        await api.post('/restaurante/productos-menu/', data);
        toast.success('Producto creado');
      }
      setIsProductoModalOpen(false);
      fetchMenu();
    } catch (err: any) {
      toast.error('Error al guardar el producto');
    }
  };

  // --- Eliminación ---
  const handleCategoriaDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro? Esto eliminará la categoría y todos sus productos.')) {
      try {
        await api.delete(`/restaurante/categorias-menu/${id}/`);
        toast.success('Categoría eliminada');
        fetchMenu();
      } catch (err) {
        toast.error('Error al eliminar la categoría');
      }
    }
  };

  const handleProductoDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este producto?')) {
      try {
        await api.delete(`/restaurante/productos-menu/${id}/`);
        toast.success('Producto eliminado');
        fetchMenu();
      } catch (err) {
        toast.error('Error al eliminar el producto');
      }
    }
  };

  if (isLoading) return <div>Cargando menú...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      {/* Encabezado */}
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Menú</h1>
        <button
          onClick={() => setIsCategoriaModalOpen(true)}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Añadir Categoría
        </button>
      </div>

      {/* Modal para Categoría */}
      <Modal
        isOpen={isCategoriaModalOpen}
        onClose={() => setIsCategoriaModalOpen(false)}
        title="Nueva Categoría"
      >
        <form onSubmit={formCategoria.handleSubmit(onCategoriaSubmit)}>
          <input
            {...formCategoria.register('nombre', { required: true })}
            placeholder="Nombre de la categoría"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
          />
          <button type="submit" className="mt-4 px-4 py-2 bg-blue-600 text-white rounded">
            Guardar
          </button>
        </form>
      </Modal>

      {/* Modal para Producto */}
      <Modal
        isOpen={isProductoModalOpen}
        onClose={() => setIsProductoModalOpen(false)}
        title="Nuevo Producto"
      >
        <form onSubmit={formProducto.handleSubmit(onProductoSubmit)}>
          <input
            {...formProducto.register('nombre', { required: true })}
            placeholder="Nombre del producto"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
          />
          <textarea
            {...formProducto.register('descripcion')}
            placeholder="Descripción"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
          />
          <input
            type="number"
            step="0.01"
            {...formProducto.register('precio', { required: true })}
            placeholder="Precio"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
          />
          <input
            type="hidden"
            {...formProducto.register('categoria', { required: true })}
            value={categoriaForNewProducto || ''}
          />
          <button type="submit" className="mt-4 px-4 py-2 bg-blue-600 text-white rounded">
            Guardar
          </button>
        </form>
      </Modal>

      {/* Listado de Categorías y Productos */}
      <div className="space-y-6">
        {categorias.map((categoria) => (
          <div key={categoria.id}>
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold mb-2">{categoria.nombre}</h2>
              <div>
                <button
                  onClick={() => {
                    setCategoriaForNewProducto(categoria.id);
                    setIsProductoModalOpen(true);
                  }}
                  className="p-2 text-green-500 hover:text-green-700"
                >
                  <FiPlus />
                </button>
                <button
                  onClick={() => handleCategoriaDelete(categoria.id)}
                  className="p-2 text-red-500 hover:text-red-700"
                >
                  Eliminar Cat.
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {categoria.productos.map((producto) => (
                <div key={producto.id} className="bg-white p-4 rounded-lg shadow relative">
                  <h3 className="font-bold">{producto.nombre}</h3>
                  <p className="text-gray-600 text-sm">{producto.descripcion}</p>
                  <p className="text-lg font-semibold mt-2">${producto.precio}</p>
                  <button
                    onClick={() => handleProductoDelete(producto.id)}
                    className="absolute top-2 right-2 text-red-500 hover:text-red-700"
                  >
                    X
                  </button>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Menu;