'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos
type Categoria = {
  id: number;
  nombre: string;
  productos: Producto[];
};
type Producto = {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
  disponible: boolean;
};
type CategoriaForm = { nombre: string; };
type ProductoForm = Omit<Producto, 'id'> & { categoria: number; };

const MenuPage = () => {
  const [categorias, setCategorias] = useState<Categoria[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modal, setModal] = useState<'categoria' | 'producto' | null>(null);
  const [editingItem, setEditingItem] = useState<Categoria | Producto | null>(null);
  const [categoriaParaProducto, setCategoriaParaProducto] = useState<number | null>(null);

  const { register, handleSubmit, reset } = useForm();

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await api.get('/restaurante/categorias-con-productos/');
      setCategorias(response.data.results || response.data);
    } catch (error) { toast.error("Error al cargar el menú."); }
    finally { setIsLoading(false); }
  };

  useEffect(() => { fetchData(); }, []);

  // --- Manejadores de Modales ---
  const openModal = (type: 'categoria' | 'producto', item: Categoria | Producto | null = null, catId: number | null = null) => {
    setModal(type);
    setEditingItem(item);
    setCategoriaParaProducto(catId);
    reset(item || {});
  };
  const closeModal = () => setModal(null);

  // --- Handlers de Submit ---
  const onCategoriaSubmit: SubmitHandler<CategoriaForm> = async (data) => {
    const apiCall = editingItem ? api.put(`/restaurante/categorias-menu/${(editingItem as Categoria).id}/`, data) : api.post('/restaurante/categorias-menu/', data);
    try {
      await apiCall;
      toast.success(`Categoría ${editingItem ? 'actualizada' : 'creada'}.`);
      fetchData();
      closeModal();
    } catch (error) { toast.error("Error al guardar la categoría."); }
  };

  const onProductoSubmit: SubmitHandler<ProductoForm> = async (data) => {
      const payload = {...data, categoria: categoriaParaProducto};
      const apiCall = editingItem ? api.put(`/restaurante/productos-menu/${(editingItem as Producto).id}/`, payload) : api.post('/restaurante/productos-menu/', payload);
      try {
          await apiCall;
          toast.success(`Producto ${editingItem ? 'actualizado' : 'creado'}.`);
          fetchData();
          closeModal();
      } catch (error) { toast.error("Error al guardar el producto."); }
  };

  // --- Handlers de Delete ---
  const handleDelete = async (type: 'categoria' | 'producto', id: number) => {
      if (!window.confirm("¿Seguro que quieres eliminar este ítem?")) return;
      const endpoint = type === 'categoria' ? 'categorias-menu' : 'productos-menu';
      try {
          await api.delete(`/restaurante/${endpoint}/${id}/`);
          toast.success("Ítem eliminado.");
          fetchData();
      } catch (error) { toast.error("Error al eliminar."); }
  };

  if (isLoading) return <div>Cargando menú...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Gestión de Menú / Carta</h1>
      <button onClick={() => openModal('categoria')} className="bg-blue-600 text-white px-4 py-2 rounded mb-4">Añadir Categoría</button>

      <div className="space-y-6">
        {categorias.map(cat => (
          <div key={cat.id} className="bg-white p-4 rounded-lg shadow-md">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-semibold">{cat.nombre}</h2>
              <div>
                <button onClick={() => openModal('categoria', cat)} className="mr-2"><FiEdit /></button>
                <button onClick={() => handleDelete('categoria', cat.id)}><FiTrash2 /></button>
              </div>
            </div>
            <button onClick={() => openModal('producto', null, cat.id)} className="text-sm text-green-600 mt-2">Añadir Producto a esta Categoría</button>
            <div className="mt-4 space-y-2">
              {cat.productos.map(prod => (
                <div key={prod.id} className="flex justify-between items-center border-t pt-2">
                  <div>{prod.nombre} - ${prod.precio}</div>
                  <div>
                    <button onClick={() => openModal('producto', prod, cat.id)} className="mr-2"><FiEdit /></button>
                    <button onClick={() => handleDelete('producto', prod.id)}><FiTrash2 /></button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Modales */}
      {modal === 'categoria' && (
        <Modal title={editingItem ? 'Editar Categoría' : 'Nueva Categoría'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onCategoriaSubmit)}>
            <input {...register('nombre', { required: true })} placeholder="Nombre de la categoría" />
            <button type="submit">Guardar</button>
          </form>
        </Modal>
      )}
      {modal === 'producto' && (
        <Modal title={editingItem ? 'Editar Producto' : 'Nuevo Producto'} onClose={closeModal}>
          <form onSubmit={handleSubmit(onProductoSubmit)}>
            <input {...register('nombre', { required: true })} placeholder="Nombre del producto" />
            <textarea {...register('descripcion')} placeholder="Descripción" />
            <input type="number" step="0.01" {...register('precio', { required: true })} placeholder="Precio" />
            <input type="checkbox" {...register('disponible')} defaultChecked /> Disponible
            <button type="submit">Guardar</button>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default MenuPage;