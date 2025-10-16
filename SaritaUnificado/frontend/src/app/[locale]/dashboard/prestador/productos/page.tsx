'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal'; // Asumo que existe un componente Modal reutilizable

// Tipado para un producto, basado en ProductoSerializer
type Producto = {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string; // El serializer lo devuelve como string
  activo: boolean;
};

// Tipado para el formulario (sin el id)
type ProductoFormInputs = Omit<Producto, 'id'>;

const Productos = () => {
  const [productos, setProductos] = useState<Producto[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Estado para el modal
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingProducto, setEditingProducto] = useState<Producto | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { isSubmitting, errors },
  } = useForm<ProductoFormInputs>();

  const fetchProductos = async () => {
    try {
      setIsLoading(true);
      // El endpoint viene de empresa/urls.py
      const response = await api.get<Producto[]>('/empresa/productos/');
      setProductos(response.data);
      setError(null);
    } catch (err) {
      setError('No se pudieron cargar los productos.');
      toast.error('Error al cargar productos.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchProductos();
  }, []);

  const openCreateModal = () => {
    setEditingProducto(null);
    reset({ nombre: '', descripcion: '', precio: '0.00', activo: true });
    setIsModalOpen(true);
  };

  const openEditModal = (producto: Producto) => {
    setEditingProducto(producto);
    reset({
        nombre: producto.nombre,
        descripcion: producto.descripcion,
        precio: producto.precio,
        activo: producto.activo
    });
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingProducto(null);
  };

  const onSubmit: SubmitHandler<ProductoFormInputs> = async (data) => {
    try {
      if (editingProducto) {
        // Actualizando
        await api.put(`/empresa/productos/${editingProducto.id}/`, data);
        toast.success('¡Producto actualizado con éxito!');
      } else {
        // Creando
        await api.post('/empresa/productos/', data);
        toast.success('¡Producto creado con éxito!');
      }
      fetchProductos(); // Recargar la lista
      closeModal();
    } catch (err) {
      toast.error('Ocurrió un error al guardar el producto.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este producto?')) {
      try {
        await api.delete(`/empresa/productos/${id}/`);
        toast.success('Producto eliminado con éxito.');
        fetchProductos(); // Recargar la lista
      } catch (err) {
        toast.error('No se pudo eliminar el producto.');
      }
    }
  };

  if (isLoading) {
    return <div>Cargando productos...</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Gestión de Productos y Servicios</h1>
        <button
          onClick={openCreateModal}
          className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full flex items-center"
        >
          <FiPlus className="mr-2" /> Añadir Producto
        </button>
      </div>

      {productos.length === 0 ? (
        <p>No tienes productos registrados. ¡Añade el primero!</p>
      ) : (
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Precio</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Estado</th>
                <th scope="col" className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {productos.map((producto) => (
                <tr key={producto.id}>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="text-sm font-medium text-gray-900">{producto.nombre}</div>
                    <div className="text-sm text-gray-500 truncate max-w-xs">{producto.descripcion}</div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${parseFloat(producto.precio).toFixed(2)}</td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${producto.activo ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                      {producto.activo ? 'Activo' : 'Inactivo'}
                    </span>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <button onClick={() => openEditModal(producto)} className="text-indigo-600 hover:text-indigo-900 mr-4"><FiEdit /></button>
                    <button onClick={() => handleDelete(producto.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal title={editingProducto ? 'Editar Producto' : 'Crear Producto'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label htmlFor="nombre" className="block text-sm font-medium text-gray-700">Nombre del Producto</label>
              <input
                id="nombre"
                type="text"
                {...register('nombre', { required: 'El nombre es obligatorio' })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
              />
              {errors.nombre && <p className="text-red-500 text-xs mt-1">{errors.nombre.message}</p>}
            </div>
            <div>
              <label htmlFor="descripcion" className="block text-sm font-medium text-gray-700">Descripción</label>
              <textarea
                id="descripcion"
                rows={3}
                {...register('descripcion')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
              />
            </div>
            <div>
              <label htmlFor="precio" className="block text-sm font-medium text-gray-700">Precio</label>
              <input
                id="precio"
                type="number"
                step="0.01"
                {...register('precio', { required: 'El precio es obligatorio', valueAsNumber: true })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
              />
               {errors.precio && <p className="text-red-500 text-xs mt-1">{errors.precio.message}</p>}
            </div>
            <div className="flex items-center">
              <input
                id="activo"
                type="checkbox"
                {...register('activo')}
                className="h-4 w-4 text-indigo-600 border-gray-300 rounded"
              />
              <label htmlFor="activo" className="ml-2 block text-sm text-gray-900">Producto Activo</label>
            </div>
            <div className="flex justify-end space-x-2">
              <button type="button" onClick={closeModal} className="bg-gray-200 text-gray-800 font-bold py-2 px-4 rounded">Cancelar</button>
              <button type="submit" disabled={isSubmitting} className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded disabled:opacity-50">
                {isSubmitting ? 'Guardando...' : 'Guardar'}
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default Productos;