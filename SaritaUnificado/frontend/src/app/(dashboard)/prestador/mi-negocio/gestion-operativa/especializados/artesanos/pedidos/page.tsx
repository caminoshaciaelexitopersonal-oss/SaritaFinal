'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const getStatusColor = (estado) => {
    switch (estado) {
        case 'entregado': return 'bg-green-200 text-green-800';
        case 'enviado': return 'bg-blue-200 text-blue-800';
        case 'en_preparacion': return 'bg-yellow-200 text-yellow-800';
        case 'pagado': return 'bg-indigo-200 text-indigo-800';
        default: return 'bg-gray-200 text-gray-800';
    }
};

const GestionPedidosPage = () => {
    const { data: pedidos, loading, error, updateItem } = useApi('artesanos/pedidos/');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedPedido, setSelectedPedido] = useState(null);

    const handleOpenModal = (pedido) => {
        setSelectedPedido(pedido);
        setIsModalOpen(true);
    };

    const handleStatusChange = async (newStatus) => {
        if (selectedPedido) {
            await updateItem(selectedPedido.id, { ...selectedPedido, estado: newStatus });
            setIsModalOpen(false);
        }
    };

    if (loading) return <p>Cargando...</p>;
    if (error) return <p>Error al cargar los datos.</p>;

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Pedidos y Ventas</h1>
            <div className="bg-white p-6 rounded-lg shadow-md">
                <h2 className="text-xl font-semibold mb-4">Mis Pedidos</h2>
                <div className="overflow-x-auto">
                    <table className="min-w-full bg-white">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="py-2 px-4 border-b"># Pedido</th>
                                <th className="py-2 px-4 border-b">Cliente</th>
                                <th className="py-2 px-4 border-b">Fecha</th>
                                <th className="py-2 px-4 border-b">Total</th>
                                <th className="py-2 px-4 border-b">Estado</th>
                                <th className="py-2 px-4 border-b">Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {pedidos.map((pedido) => (
                                <tr key={pedido.id}>
                                    <td className="py-2 px-4 border-b font-semibold">#{pedido.id}</td>
                                    <td className="py-2 px-4 border-b">{pedido.nombre_cliente}</td>
                                    <td className="py-2 px-4 border-b">{new Date(pedido.fecha_pedido).toLocaleDateString()}</td>
                                    <td className="py-2 px-4 border-b text-right">${parseFloat(pedido.total).toLocaleString()}</td>
                                    <td className="py-2 px-4 border-b text-center">
                                        <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getStatusColor(pedido.estado)}`}>
                                            {pedido.estado.replace('_', ' ')}
                                        </span>
                                    </td>
                                    <td className="py-2 px-4 border-b text-center">
                                        <button onClick={() => handleOpenModal(pedido)} className="text-blue-600 hover:underline">Ver Detalles</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>

            {isModalOpen && selectedPedido && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    {/* Modal Content Here */}
                </div>
            )}
        </div>
    );
};

export default GestionPedidosPage;
