'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { FiGrid, FiShoppingCart, FiPlus, FiX } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Modal from '@/components/ui/Modal';

// --- Tipos ---
interface Mesa {
    id: number;
    numero_mesa: string;
    estado: string;
}
interface Producto {
    id: number;
    nombre: string;
    precio: string;
}
interface Categoria {
    id: number;
    nombre: string;
    productos: Producto[];
}
interface Pedido {
    id: number;
    mesa: number;
    total: string;
    items: { producto: number; cantidad: number }[];
}

const PedidosManager = () => {
    const [mesas, setMesas] = useState<Mesa[]>([]);
    const [menu, setMenu] = useState<Categoria[]>([]);
    const [selectedMesa, setSelectedMesa] = useState<Mesa | null>(null);
    const [currentOrder, setCurrentOrder] = useState<{ [productId: number]: number }>({});
    const [isLoading, setIsLoading] = useState(true);

    const fetchData = async () => {
        setIsLoading(true);
        try {
            const [mesasRes, menuRes] = await Promise.all([
                api.get('/restaurante/mesas/'),
                api.get('/restaurante/categorias-con-productos/')
            ]);
            setMesas(mesasRes.data.results || mesasRes.data);
            setMenu(menuRes.data.results || menuRes.data);
        } catch (error) {
            toast.error('No se pudo cargar la información para tomar pedidos.');
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => { fetchData() }, []);

    const addToOrder = (productId: number) => {
        setCurrentOrder(prev => ({ ...prev, [productId]: (prev[productId] || 0) + 1 }));
    };

    const removeFromOrder = (productId: number) => {
        setCurrentOrder(prev => {
            const newOrder = { ...prev };
            if (newOrder[productId] > 1) {
                newOrder[productId]--;
            } else {
                delete newOrder[productId];
            }
            return newOrder;
        });
    };

    const calculateTotal = () => {
        return Object.entries(currentOrder).reduce((total, [productId, quantity]) => {
            const product = menu.flatMap(c => c.productos).find(p => p.id === Number(productId));
            return total + (product ? parseFloat(product.precio) * quantity : 0);
        }, 0).toFixed(2);
    };

    const handleCreatePedido = async () => {
        if (!selectedMesa || Object.keys(currentOrder).length === 0) {
            toast.warn('Selecciona una mesa y añade productos al pedido.');
            return;
        }
        const payload = {
            mesa: selectedMesa.id,
            items: Object.entries(currentOrder).map(([producto, cantidad]) => ({ producto: Number(producto), cantidad })),
        };
        try {
            await api.post('/restaurante/pedidos/', payload);
            toast.success(`Pedido creado para la mesa ${selectedMesa.numero_mesa}`);
            setSelectedMesa(null);
            setCurrentOrder({});
            fetchData(); // Recargar estado de mesas
        } catch (error) {
            toast.error('Error al crear el pedido.');
        }
    };

    if (isLoading) return <div>Cargando TPV...</div>

    return (
        <div className="p-6 bg-white rounded-lg shadow-md">
            <h1 className="text-3xl font-bold text-gray-800 mb-6">Terminal Punto de Venta (TPV)</h1>
            <div className="grid grid-cols-3 md:grid-cols-5 lg:grid-cols-8 gap-4">
                {mesas.map(mesa => (
                    <button
                        key={mesa.id}
                        onClick={() => setSelectedMesa(mesa)}
                        className={`p-4 rounded-lg text-center font-bold text-lg shadow-md transition
                            ${mesa.estado === 'OCUPADA' ? 'bg-red-500 text-white' : 'bg-green-500 text-white hover:bg-green-600'}`}
                        disabled={mesa.estado === 'OCUPADA'}
                    >
                        {mesa.numero_mesa}
                    </button>
                ))}
            </div>

            {selectedMesa && (
                <Modal isOpen={!!selectedMesa} onClose={() => {setSelectedMesa(null); setCurrentOrder({});}} title={`Nuevo Pedido para Mesa: ${selectedMesa.numero_mesa}`}>
                    <div className="grid grid-cols-2 gap-6">
                        {/* Columna de Menú */}
                        <div className="space-y-4 h-96 overflow-y-auto pr-2">
                            {menu.map(cat => (
                                <div key={cat.id}>
                                    <h3 className="font-bold text-lg text-gray-700">{cat.nombre}</h3>
                                    {cat.productos.map(prod => (
                                        <div key={prod.id} className="flex justify-between items-center p-2 border-b">
                                            <span>{prod.nombre}</span>
                                            <button onClick={() => addToOrder(prod.id)} className="px-2 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"><FiPlus/></button>
                                        </div>
                                    ))}
                                </div>
                            ))}
                        </div>

                        {/* Columna de Pedido Actual */}
                        <div className="p-4 bg-gray-50 rounded-lg">
                            <h3 className="font-bold text-xl mb-4">Pedido Actual</h3>
                            <div className="space-y-2 h-72 overflow-y-auto">
                                {Object.keys(currentOrder).length > 0 ? Object.entries(currentOrder).map(([productId, quantity]) => {
                                    const product = menu.flatMap(c => c.productos).find(p => p.id === Number(productId));
                                    if (!product) return null;
                                    return (
                                        <div key={productId} className="flex justify-between items-center">
                                            <span>{product.nombre}</span>
                                            <div className="flex items-center gap-2">
                                                <button onClick={() => removeFromOrder(Number(productId))} className="px-2 py-1 text-xs bg-red-200 rounded">-</button>
                                                <span>{quantity}</span>
                                                <button onClick={() => addToOrder(Number(productId))} className="px-2 py-1 text-xs bg-green-200 rounded">+</button>
                                            </div>
                                        </div>
                                    )
                                }) : <p className="text-gray-500">Añade productos desde el menú.</p>}
                            </div>
                            <div className="border-t mt-4 pt-4">
                                <p className="text-xl font-bold">Total: ${calculateTotal()}</p>
                                <button onClick={handleCreatePedido} className="w-full mt-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700">Crear Pedido</button>
                            </div>
                        </div>
                    </div>
                </Modal>
            )}
        </div>
    );
};

const PedidosPage = () => <AuthGuard allowedRoles={['PRESTADOR']}><PedidosManager /></AuthGuard>;
export default PedidosPage;