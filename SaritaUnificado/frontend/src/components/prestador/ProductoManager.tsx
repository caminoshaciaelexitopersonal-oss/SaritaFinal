'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/lib/api';
import FormField from '@/components/ui/FormField';
import { Button } from '@/components/ui/Button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { FiEdit, FiTrash2, FiPlus } from 'react-icons/fi';

interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
  activo: boolean;
}

type ProductoFormData = Omit<Producto, 'id'>;

const ProductoManager = () => {
  const [productos, setProductos] = useState<Producto[]>([]);
  const [editingProducto, setEditingProducto] = useState<Producto | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ProductoFormData>();

  const fetchProductos = useCallback(async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/prestador/productos/');
      setProductos(response.data.results || response.data);
    } catch (error) {
      toast.error('Error al cargar los productos.');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchProductos();
  }, [fetchProductos]);

  const onSubmit: SubmitHandler<ProductoFormData> = async (data) => {
    const apiCall = editingProducto
      ? api.put(`/prestador/productos/${editingProducto.id}/`, data)
      : api.post('/prestador/productos/', data);

    try {
      await apiCall;
      toast.success(`Producto ${editingProducto ? 'actualizado' : 'creado'} con éxito.`);
      reset();
      setEditingProducto(null);
      fetchProductos(); // Recargar la lista
    } catch (error) {
      toast.error('Ocurrió un error al guardar el producto.');
    }
  };

  const handleEdit = (producto: Producto) => {
    setEditingProducto(producto);
    setValue('nombre', producto.nombre);
    setValue('descripcion', producto.descripcion);
    setValue('precio', producto.precio);
    setValue('activo', producto.activo);
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este producto?')) {
      try {
        await api.delete(`/prestador/productos/${id}/`);
        toast.success('Producto eliminado con éxito.');
        fetchProductos();
      } catch (error) {
        toast.error('Error al eliminar el producto.');
      }
    }
  };

  const handleCancelEdit = () => {
    setEditingProducto(null);
    reset();
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Gestión de Productos</h1>

      <div className="bg-white p-6 rounded-lg shadow-md mb-8">
        <h2 className="text-xl font-semibold mb-4">{editingProducto ? 'Editar Producto' : 'Crear Nuevo Producto'}</h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            name="nombre"
            label="Nombre del Producto"
            register={register}
            errors={errors}
            required
          />
          <FormField
            name="descripcion"
            label="Descripción"
            type="textarea"
            register={register}
            errors={errors}
          />
          <FormField
            name="precio"
            label="Precio (COP)"
            type="number"
            register={register}
            errors={errors}
            required
            validation={{ valueAsNumber: true }}
          />
          <div className="flex items-center">
            <input
              id="activo"
              type="checkbox"
              {...register('activo')}
              className="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
            />
            <label htmlFor="activo" className="ml-2 block text-sm text-gray-900">
              Activo / Visible al público
            </label>
          </div>

          <div className="flex space-x-4">
            <Button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Guardando...' : (editingProducto ? 'Actualizar Producto' : 'Crear Producto')}
            </Button>
            {editingProducto && (
              <Button variant="outline" onClick={handleCancelEdit}>
                Cancelar Edición
              </Button>
            )}
          </div>
        </form>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">Listado de Productos</h2>
        {isLoading ? (
          <p>Cargando productos...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Nombre</TableHead>
                <TableHead>Precio</TableHead>
                <TableHead>Activo</TableHead>
                <TableHead>Acciones</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {productos.map((producto) => (
                <TableRow key={producto.id}>
                  <TableCell className="font-medium">{producto.nombre}</TableCell>
                  <TableCell>${parseFloat(producto.precio).toLocaleString('es-CO')}</TableCell>
                  <TableCell>{producto.activo ? 'Sí' : 'No'}</TableCell>
                  <TableCell>
                    <div className="flex space-x-2">
                      <Button variant="icon" onClick={() => handleEdit(producto)}>
                        <FiEdit className="h-4 w-4" />
                      </Button>
                      <Button variant="icon" color="danger" onClick={() => handleDelete(producto.id)}>
                        <FiTrash2 className="h-4 w-4" />
                      </Button>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </div>
    </div>
  );
};

export default ProductoManager;