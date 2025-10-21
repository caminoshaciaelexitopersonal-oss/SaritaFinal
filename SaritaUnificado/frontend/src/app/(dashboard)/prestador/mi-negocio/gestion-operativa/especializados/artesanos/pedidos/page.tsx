'use client';
import React, { useState } from 'react';

// Mock data - Reemplazar con llamadas a la API
const mockPedidos = [
    { id: 101, cliente: 'Ana María Suárez', fecha: '2023-10-26', total: '230,000', estado: 'En Preparación' },
    { id: 102, cliente: 'Carlos Jiménez', fecha: '2023-10-25', total: '80,000', estado: 'Enviado' },
    { id: 103, cliente: 'Sofía Castro', fecha: '2023-10-22', total: '350,000', estado: 'Entregado' },
    { id: 104, cliente: 'Luis Fernando Ríos', fecha: '2023-10-26', total: '150,000', estado: 'Pagado' },
];

const getStatusColor = (estado) => {
    switch (estado) {
        case 'Entregado': return 'bg-green-200 text-green-800';
        case 'Enviado': return 'bg-blue-200 text-blue-800';
        case 'En Preparación': return 'bg-yellow-200 text-yellow-800';
        case 'Pagado': return 'bg-indigo-200 text-indigo-800';
        default: return 'bg-gray-200 text-gray-800';
    }
};

const GestionPedidosPage = () => {
    const [pedidos, setPedidos] = useState(mockPedidos);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Gestión de Pedidos y Ventas</h1>

            <div className="bg-white p-6 rounded-lg shadow-md">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-semibold">Mis Pedidos</h2>
                    {/* <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">
                        Crear Pedido Manual
                    </button> */}
                </div>

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
                                    <td className="py-2 px-4 border-b">{pedido.cliente}</td>
                                    <td className="py-2 px-4 border-b">{pedido.fecha}</td>
                                    <td className="py-2 px-4 border-b text-right">${pedido.total}</td>
                                    <td className="py-2 px-4 border-b text-center">
                                        <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getStatusColor(pedido.estado)}`}>
                                            {pedido.estado}
                                        </span>
                                    </td>
                                    <td className="py-2 px-4 border-b text-center">
                                        <button className="text-blue-600 hover:underline">Ver Detalles</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default GestionPedidosPage;
