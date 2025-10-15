'use client';

import React, { useState, useEffect, useCallback } from 'react';
import api from '@/lib/api';
import { useForm, SubmitHandler, useFieldArray } from 'react-hook-form';
import Modal from '@/components/shared/Modal';
import { toast } from 'react-toastify';

// --- Interfaces ---
interface ItemPedido {
  producto: { id: number; nombre: string };
  cantidad: number;
  precio_unitario: string;
}

interface Pedido {
  id: number;
  mesa: { id: number; numero_mesa: string };
  completado: boolean;
  total: string;
  items: ItemPedido[];
}

interface Mesa {
  id: number;
  numero_mesa: string;
}

interface ProductoMenu {
  id: number;
  nombre: string;
  precio: string;
}

type FormInputs = {
  mesa: number;
  items: { producto: number; cantidad: number }[];
};

// --- Componente Principal ---
const Pedidos = () => {
  const [pedidos, setPedidos] = useState<Pedido[]>([]);
  const [mesas, setMesas] = useState<Mesa[]>([]);
  const [productosMenu, setProductosMenu] = useState<ProductoMenu[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const { register, control, handleSubmit, reset } = useForm<FormInputs>({
    defaultValues: { items: [{ producto: 0, cantidad: 1 }] },
  });
  const { fields, append, remove } = useFieldArray({ control, name: 'items' });

  const fetchData = useCallback(async () => {
    try {
      setIsLoading(true);
      const [pedidosRes, mesasRes, productosRes] = await Promise.all([
        api.get('/restaurante/pedidos/'),
        api.get('/restaurante/mesas/'),
        api.get('/restaurante/productos-menu/'),
      ]);
      setPedidos(pedidosRes.data.results || []);
      setMesas(mesasRes.data.results || []);
      setProductosMenu(productosRes.data.results || []);
    } catch (err: any) {
      setError('No se pudieron cargar los datos. ' + (err.response?.data?.detail || err.message));
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const openModal = () => {
    reset({ items: [{ producto: 0, cantidad: 1 }] });
    setIsModalOpen(true);
  };

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    try {
      await api.post('/restaurante/pedidos/', data);
      toast.success('Pedido creado con éxito');
      setIsModalOpen(false);
      fetchData();
    } catch (err: any) {
      toast.error('Error al crear el pedido: ' + (err.response?.data?.detail || err.message));
    }
  };

  const handleComplete = async (id: number) => {
    if (window.confirm('¿Marcar este pedido como completado?')) {
      try {
        await api.patch(`/restaurante/pedidos/${id}/`, { completado: true });
        toast.success('Pedido completado');
        fetchData();
      } catch (err: any) {
        toast.error('Error al completar el pedido');
      }
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este pedido?')) {
      try {
        await api.delete(`/restaurante/pedidos/${id}/`);
        toast.success('Pedido eliminado con éxito');
        fetchData();
      } catch (err: any) {
        toast.error('Error al eliminar el pedido');
      }
    }
  };

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Pedidos (TPV)</h1>
        <button onClick={openModal} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Nuevo Pedido
        </button>
      </div>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Nuevo Pedido">
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label>Mesa</label>
            <select {...register('mesa', { valueAsNumber: true })} className="mt-1 block w-full">
              {mesas.map(m => <option key={m.id} value={m.id}>{m.numero_mesa}</option>)}
            </select>
          </div>
          <hr />
          <h3>Items del Pedido</h3>
          {fields.map((field, index) => (
            <div key={field.id} className="flex items-center space-x-2">
              <select {...register(`items.${index}.producto`, { valueAsNumber: true })} className="block w-full">
                {productosMenu.map(p => <option key={p.id} value={p.id}>{p.nombre} - ${p.precio}</option>)}
              </select>
              <input type="number" {...register(`items.${index}.cantidad`, { valueAsNumber: true, min: 1 })} defaultValue={1} className="w-20"/>
              <button type="button" onClick={() => remove(index)} className="text-red-500">X</button>
            </div>
          ))}
          <button type="button" onClick={() => append({ producto: 0, cantidad: 1 })}>Añadir Item</button>
          <div className="flex justify-end">
            <button type="submit">Crear Pedido</button>
          </div>
        </form>
      </Modal>

      {pedidos.length === 0 ? (
        <p>No hay pedidos registrados.</p>
      ) : (
        <div className="space-y-4">
          {pedidos.map((pedido) => (
            <div key={pedido.id} className="bg-white p-4 rounded-lg shadow">
              <div className="flex justify-between items-center">
                <h2 className="font-bold">Pedido #{pedido.id} - Mesa {pedido.mesa?.numero_mesa || 'N/A'}</h2>
                <span className={`px-2 py-1 text-xs rounded-full ${pedido.completado ? 'bg-green-200 text-green-800' : 'bg-yellow-200 text-yellow-800'}`}>
                  {pedido.completado ? 'Completado' : 'Pendiente'}
                </span>
              </div>
              <ul className="mt-2 list-disc list-inside">
                {pedido.items.map((item, index) => (
                  <li key={index}>{item.cantidad}x {item.producto.nombre}</li>
                ))}
              </ul>
              <p className="text-right font-bold mt-2">Total: ${pedido.total}</p>
              <div className="flex justify-end space-x-2 mt-2">
                {!pedido.completado && (
                  <button onClick={() => handleComplete(pedido.id)} className="text-xs px-2 py-1 bg-green-500 text-white rounded">Marcar como Completado</button>
                )}
                <button onClick={() => handleDelete(pedido.id)} className="text-xs px-2 py-1 bg-red-500 text-white rounded">Eliminar</button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Pedidos;