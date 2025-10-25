"use client";

import React, { useState, useEffect } from 'react';
import Modal from '../../../components/Modal';
import ProductServiceForm from '../../../components/ProductServiceForm';
import { useMiNegocioApi } from '../../../hooks/useMiNegocioApi';

// Tipado para los datos del producto/servicio
interface ProductService {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
  tipo: 'PRODUCTO' | 'SERVICIO';
  activo: boolean;
}

export default function ProductosServiciosPage() {
  const { data: products, isLoading, error, fetchData, createData, updateData, deleteData } = useMiNegocioApi<ProductService[]>();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingProduct, setEditingProduct] = useState<ProductService | undefined>(undefined);

  // Cargar datos cuando el componente se monta
  useEffect(() => {
    fetchData('operativa/productos/');
  }, [fetchData]);

  const handleOpenCreateModal = () => {
    setEditingProduct(undefined);
    setIsModalOpen(true);
  };

  const handleOpenEditModal = (product: ProductService) => {
    setEditingProduct(product);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setEditingProduct(undefined);
  };

  const handleFormSubmit = async (formData: any) => {
    if (editingProduct) {
      await updateData(`operativa/productos/${editingProduct.id}/`, formData);
    } else {
      await createData('operativa/productos/', formData);
    }
    fetchData('operativa/productos/'); // Recargar la lista
    handleCloseModal();
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este ítem?')) {
      await deleteData(`operativa/productos/${id}/`);
      fetchData('operativa/productos/'); // Recargar la lista
    }
  };


  return (
    <div className="p-4 sm:p-6 lg:p-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Mis Productos y Servicios</h1>
        <button
          onClick={handleOpenCreateModal}
          className="bg-blue-600 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        >
          Añadir Nuevo
        </button>
      </div>

      {isLoading && <p>Cargando...</p>}
      {error && <p className="text-red-600">Error: {error}</p>}

      {!isLoading && !error && (
        <div className="bg-white p-6 rounded-lg shadow-md">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Tipo</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Precio</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Estado</th>
                <th scope="col" className="relative px-6 py-3"><span className="sr-only">Acciones</span></th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {(products && products.length > 0) ? products.map((product) => (
                <tr key={product.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{product.nombre}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{product.tipo}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${product.precio}</td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                      product.activo ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                    }`}>
                      {product.activo ? 'Activo' : 'Inactivo'}
                    </span>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium space-x-4">
                    <button onClick={() => handleOpenEditModal(product)} className="text-blue-600 hover:text-blue-900">
                      Editar
                    </button>
                    <button onClick={() => handleDelete(product.id)} className="text-red-600 hover:text-red-900">
                      Eliminar
                    </button>
                  </td>
                </tr>
              )) : (
                <tr>
                  <td colSpan={5} className="px-6 py-4 text-center text-sm text-gray-500">
                    No has añadido ningún producto o servicio todavía.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={handleCloseModal} title={editingProduct ? "Editar Producto/Servicio" : "Añadir Nuevo Producto/Servicio"}>
          <ProductServiceForm
            initialData={editingProduct}
            onSubmit={handleFormSubmit}
            onCancel={handleCloseModal}
            isSaving={isLoading}
          />
        </Modal>
      )}
    </div>
  );
}
