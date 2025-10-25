'use client';

import React, { useState, useEffect } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiUpload, FiTrash2 } from 'react-icons/fi';

// Tipos
type Imagen = {
  id: number;
  imagen: string;
  alt_text: string;
};

type FormInputs = {
  imagen: FileList;
  alt_text: string;
};

const Galeria = () => {
  const [imagenes, setImagenes] = useState<Imagen[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const { register, handleSubmit, reset } = useForm<FormInputs>();

  const fetchImagenes = async () => {
    try {
      setIsLoading(true);
      const response = await api.get<Imagen[]>('/galeria/prestador/');
      setImagenes(response.data);
    } catch (error) {
      toast.error("No se pudieron cargar las imágenes de la galería.");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchImagenes();
  }, []);

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    if (!data.imagen || data.imagen.length === 0) {
      toast.warn("Por favor, selecciona una imagen.");
      return;
    }
    const formData = new FormData();
    formData.append('imagen', data.imagen[0]);
    formData.append('alt_text', data.alt_text);

    try {
      await api.post('/galeria/prestador/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      toast.success("Imagen subida con éxito.");
      reset();
      fetchImagenes();
    } catch (error) {
      toast.error("Error al subir la imagen.");
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm("¿Estás seguro de que quieres eliminar esta imagen?")) {
      try {
        await api.delete(`/galeria/prestador/${id}/`);
        toast.success("Imagen eliminada.");
        setImagenes(imagenes.filter(img => img.id !== id));
      } catch (error) {
        toast.error("No se pudo eliminar la imagen.");
      }
    }
  };

  if (isLoading) return <div>Cargando galería...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Gestión de Galería Multimedia</h1>
      <div className="bg-white p-6 rounded-lg shadow-md mb-6">
        <h2 className="text-xl font-semibold mb-4">Subir Nueva Imagen</h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <input type="text" {...register('alt_text')} placeholder="Descripción de la imagen (opcional)" />
          <input type="file" {...register('imagen', { required: true })} accept="image/*" />
          <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 flex items-center">
            <FiUpload className="mr-2" /> Subir Imagen
          </button>
        </form>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {imagenes.map(img => (
          <div key={img.id} className="relative group">
            <img src={img.imagen} alt={img.alt_text} className="w-full h-48 object-cover rounded-lg" />
            <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
              <button onClick={() => handleDelete(img.id)} className="text-white text-2xl">
                <FiTrash2 />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Galeria;