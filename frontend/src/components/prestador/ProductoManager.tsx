'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import useMiNegocioApi from '../../app/dashboard/prestador/mi-negocio/ganchos/useMiNegocioApi';
import FormField from '@/components/ui/FormField';
import { Button } from '@/components/ui/Button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { FiEdit, FiTrash2, FiPlus } from 'react-icons/fi';

interface ProductoServicio {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
  tipo: 'PRODUCTO' | 'SERVICIO';
  cantidad_disponible: number;
  unidad_medida: string;
  activo: boolean;
}

type ProductoFormData = Omit<ProductoServicio, 'id'>;

const ProductoManager = () => {
  const [productos, setProductos] = useState<ProductoServicio[]>([]);
  const [editingProducto, setEditingProducto] = useState<ProductoServicio | null>(null);
  const { request, loading: apiLoading } = useMiNegocioApi();

  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ProductoFormData>();

  const fetchProductos = useCallback(async () => {
    try {
      const response = await request('/productos-servicios/');
      setProductos(response.results || response);
    } catch (error) {
      toast.error('Error al cargar los productos.');
    }
  }, [request]);

  useEffect(() => {
    fetchProductos();
  }, [fetchProductos]);

  const onSubmit: SubmitHandler<ProductoFormData> = async (data) => {
    try {
      if (editingProducto) {
        await request(`/productos-servicios/${editingProducto.id}/`, {
          method: 'PUT',
          body: JSON.stringify(data),
        });
        toast.success('Producto actualizado con éxito.');
      } else {
        await request('/productos-servicios/', {
          method: 'POST',
          body: JSON.stringify(data),
        });
        toast.success('Producto creado con éxito.');
      }
      reset();
      setEditingProducto(null);
      fetchProductos();
    } catch (error) {
      toast.error('Ocurrió un error al guardar el producto.');
    }
  };

  const handleEdit = (producto: ProductoServicio) => {
    setEditingProducto(producto);
    Object.keys(producto).forEach((key) => {
      setValue(key as keyof ProductoFormData, producto[key as keyof ProductoServicio]);
    });
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este producto?')) {
      try {
        await request(`/productos-servicios/${id}/`, { method: 'DELETE' });
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
          <FormField
            name="tipo"
            label="Tipo"
            as="select"
            register={register}
            errors={errors}
            required
          >
            <option value="PRODUCTO">Producto</option>
            <option value="SERVICIO">Servicio</option>
          </FormField>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <FormField
              name="cantidad_disponible"
              label="Cantidad Disponible"
              type="number"
              register={register}
              errors={errors}
              required
              defaultValue={1}
            />
            <FormField
              name="unidad_medida"
              label="Unidad de Medida"
              register={register}
              errors={errors}
              placeholder="Ej: unidad, kg, hora"
            />
          </div>
          <div className="flex items-center">
            <input
              id="activo"
              type="checkbox"
              {...register('activo')}
              defaultChecked={true}
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
        <h2 className="text-xl font-semibold mb-4">Listado de Productos y Servicios</h2>
        {apiLoading ? (
          <p>Cargando...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Nombre</TableHead>
                <TableHead>Tipo</TableHead>
                <TableHead>Precio</TableHead>
                <TableHead>Disponible</TableHead>
                <TableHead>Activo</TableHead>
                <TableHead>Acciones</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {productos.map((producto) => (
                <TableRow key={producto.id}>
                  <TableCell className="font-medium">{producto.nombre}</TableCell>
                  <TableCell>{producto.tipo}</TableCell>
                  <TableCell>${parseFloat(producto.precio).toLocaleString('es-CO')}</TableCell>
                  <TableCell>{producto.cantidad_disponible} {producto.unidad_medida}</TableCell>
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