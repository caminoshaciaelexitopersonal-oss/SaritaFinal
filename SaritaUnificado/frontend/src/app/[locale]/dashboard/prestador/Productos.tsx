 'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';

interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
  activo: boolean;
}

type FormInputs = Omit<Producto, 'id'>;

const Productos = () => {
  const [productos, setProductos] = useState<Producto[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingProducto, setEditingProducto] = useState<Producto | null>(null);

  const { register, handleSubmit, reset, setValue } = useForm<FormInputs>();

  const fetchProductos = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/empresa/productos/');
      setProductos(response.data.results || []);
    } catch (err: any) {
      setError('No se pudieron cargar los productos. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchProductos();
  }, [fetchProductos]);

  const openModalForCreate = () => {
    reset({ nombre: '', descripcion: '', precio: '0.00', activo: true });
    setEditingProducto(null);
    setIsModalOpen(true);
  };

  const openModalForEdit = (producto: Producto) => {
    setEditingProducto(producto);
    setValue('nombre', producto.nombre);
    setValue('descripcion', producto.descripcion);
    setValue('precio', producto.precio);
    setValue('activo', producto.activo);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setEditingProducto(null);
    reset();
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      if (editingProducto) {
        await api.patch(`/empresa/productos/${editingProducto.id}/`, data);
        toast.success('Producto actualizado con éxito');
      } else {
        await api.post('/empresa/productos/', data);
        toast.success('Producto creado con éxito');
      }
      closeModal();
      fetchProductos();
    } catch (err: any) {
      toast.error('Error al guardar el producto: ' + (err.response?.data?.detail || err.message));
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este producto?')) {
      try {
        await api.delete(`/empresa/productos/${id}/`);
        toast.success('Producto eliminado con éxito');
        fetchProductos();
      } catch (err: any) {
        toast.error('Error al eliminar el producto: ' + (err.response?.data?.detail || err.message));
      }
    }
  };

  if (isLoading) return <div>Cargando productos...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Productos y Servicios</h1>
        <button
          onClick={openModalForCreate}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Añadir Producto
        </button>
      </div>

      <Modal
        isOpen={isModalOpen}
        onClose={closeModal}
        title={editingProducto ? 'Editar Producto' : 'Nuevo Producto'}
      >
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label htmlFor="nombre" className="block text-sm font-medium text-gray-700">
              Nombre
            </label>
            <input
              id="nombre"
              {...register('nombre', { required: true })}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
            />
          </div>
          <div>
            <label htmlFor="descripcion" className="block text-sm font-medium text-gray-700">
              Descripción
            </label>
            <textarea
              id="descripcion"
              {...register('descripcion')}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
            />
          </div>
          <div>
            <label htmlFor="precio" className="block text-sm font-medium text-gray-700">
              Precio
            </label>
            <input
              id="precio"
              type="number"
              step="0.01"
              {...register('precio', { required: true, valueAsNumber: true })}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
            />
          </div>
          <div className="flex items-center">
            <input
              id="activo"
              type="checkbox"
              {...register('activo')}
              className="h-4 w-4 text-blue-600 border-gray-300 rounded"
            />
            <label htmlFor="activo" className="ml-2 block text-sm text-gray-900">
              Activo
            </label>
          </div>
          <div className="flex justify-end space-x-2">
            <button type="button" onClick={closeModal} className="px-4 py-2 bg-gray-200 rounded">
              Cancelar
            </button>
            <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded">
              Guardar
            </button>
          </div>
        </form>
      </Modal>

      {productos.length === 0 ? (
        <p>No tienes productos registrados.</p>
      ) : (
        <table className="min-w-full bg-white border">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b text-left">Nombre</th>
              <th className="py-2 px-4 border-b text-left">Precio</th>
              <th className="py-2 px-4 border-b text-left">Activo</th>
              <th className="py-2 px-4 border-b text-left">Acciones</th>
            </tr>
          </thead>
          <tbody>
            {productos.map((producto) => (
              <tr key={producto.id}>
                <td className="py-2 px-4 border-b">{producto.nombre}</td>
                <td className="py-2 px-4 border-b">${producto.precio}</td>
                <td className="py-2 px-4 border-b">{producto.activo ? 'Sí' : 'No'}</td>
                <td className="py-2 px-4 border-b">
                  <button
                    onClick={() => openModalForEdit(producto)}
                    className="text-blue-500 hover:underline mr-2"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(producto.id)}
                    className="text-red-500 hover:underline"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Productos;