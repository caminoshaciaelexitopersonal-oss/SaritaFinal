'use client';
import React, { useState } from 'react';
import { useApi } from '@/hooks/useApi';

const GestionRutasPage = () => {
    const { data: rutas, loading: loadingRutas, createItem: createRuta, updateItem: updateRuta, deleteItem: deleteRuta } = useApi('guias/rutas/');
    const { data: hitos, loading: loadingHitos, createItem: createHito, updateItem: updateHito, deleteItem: deleteHito } = useApi('guias/rutas-hitos/');

    const [isRutaModalOpen, setIsRutaModalOpen] = useState(false);
    const [isHitoModalOpen, setIsHitoModalOpen] = useState(false);
    const [currentRuta, setCurrentRuta] = useState(null);
    const [currentHito, setCurrentHito] = useState(null);

    const handleSaveRuta = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {
            nombre: formData.get('nombre'),
            descripcion_corta: formData.get('descripcion_corta'),
            duracion_horas: formData.get('duracion_horas'),
            dificultad: formData.get('dificultad'),
        };
        if (currentRuta) {
            await updateRuta(currentRuta.id, data);
        } else {
            await createRuta(data);
        }
        setIsRutaModalOpen(false);
    };

    // Funciones para guardar hitos...

    if (loadingRutas || loadingHitos) return <p>Cargando...</p>;

    return (
        <div className="container mx-auto p-4">
            {/* ... (renderizado de la página) */}

            {/* Modal para Ruta */}
            {isRutaModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form onSubmit={handleSaveRuta}>
                            {/* Campos del formulario para Ruta */}
                            <button type="submit">Guardar</button>
                            <button type="button" onClick={() => setIsRutaModalOpen(false)}>Cancelar</button>
                        </form>
                    </div>
                </div>
            )}

            {/* Modal para Hito */}
            {isHitoModalOpen && (
                <div className="fixed inset-0 bg-gray-600 bg-opacity-50 h-full w-full">
                    <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                        <form>
                            {/* Campos del formulario para Hito */}
                            <button type="submit">Guardar</button>
                            <button type="button" onClick={() => setIsHitoModalOpen(false)}>Cancelar</button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default GestionRutasPage;
