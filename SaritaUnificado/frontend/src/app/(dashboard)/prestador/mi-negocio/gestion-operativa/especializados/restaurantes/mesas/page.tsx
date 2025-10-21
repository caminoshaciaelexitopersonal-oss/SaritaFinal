'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionMesasPage = () => {
    const { data: mesas, loading: loadingMesas, createItem: createMesa, updateItem: updateMesa, deleteItem: deleteMesa } = useApi('restaurantes/mesas/');
    const { data: reservas, loading: loadingReservas, createItem: createReserva, updateItem: updateReserva, deleteItem: deleteReserva } = useApi('restaurantes/reservas-mesas/');

    const [isMesaModalOpen, setIsMesaModalOpen] = useState(false);
    const [isReservaModalOpen, setIsReservaModalOpen] = useState(false);
    const [currentMesa, setCurrentMesa] = useState(null);
    const [currentReserva, setCurrentReserva] = useState(null);

    const handleSaveMesa = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            numero: formData.get('numero'),
            capacidad: formData.get('capacidad'),
            ubicacion: formData.get('ubicacion'),
        };
        if (currentMesa) {
            await updateMesa(currentMesa.id, data);
        } else {
            await createMesa(data);
        }
        setIsMesaModalOpen(false);
    };

    const handleSaveReserva = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            mesa: formData.get('mesa'),
            nombre_cliente: formData.get('nombre_cliente'),
            fecha_hora: formData.get('fecha_hora'),
            numero_personas: formData.get('numero_personas'),
        };
        if (currentReserva) {
            await updateReserva(currentReserva.id, data);
        } else {
            await createReserva(data);
        }
        setIsReservaModalOpen(false);
    };

    if (loadingMesas || loadingReservas) return <p>Cargando...</p>;

    return (
        <div className="container mx-auto p-4">
            {/* ... (renderizado de la página) */}

            {/* Modal para Mesa */}
            {isMesaModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form onSubmit={handleSaveMesa}>
                            {/* Campos del formulario para Mesa */}
                            <button type="submit">Guardar</button>
                            <button type="button" onClick={() => setIsMesaModalOpen(false)}>Cancelar</button>
                        </form>
                    </div>
                </div>
            )}

            {/* Modal para Reserva */}
            {isReservaModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form onSubmit={handleSaveReserva}>
                            {/* Campos del formulario para Reserva */}
                            <button type="submit">Guardar</button>
                            <button type="button" onClick={() => setIsReservaModalOpen(false)}>Cancelar</button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default GestionMesasPage;
