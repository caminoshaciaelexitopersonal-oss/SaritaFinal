'use client';

import React, { useEffect, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/src/lib/api';
import { FiUpload, FiCheckCircle, FiXCircle, FiClock, FiDownload } from 'react-icons/fi';
import Modal from '@/src/components/dashboard/Modal';

// Tipos de datos del backend
type TipoDocumento = {
  id: string;
  nombre: string;
  requerido: boolean;
};

type Documento = {
  id: string;
  tipo_documento_nombre: string;
  archivo_url: string;
  estado: 'PENDIENTE' | 'APROBADO' | 'RECHAZADO';
  observaciones: string;
  fecha_subida: string;
};

type FormInputs = {
  tipo_documento: string;
  archivo: FileList;
};

const EstadoIcon = ({ estado }: { estado: Documento['estado'] }) => {
    switch (estado) {
        case 'APROBADO':
            return <FiCheckCircle className="text-green-500" title="Aprobado" />;
        case 'RECHAZADO':
            return <FiXCircle className="text-red-500" title="Rechazado" />;
        case 'PENDIENTE':
        default:
            return <FiClock className="text-yellow-500" title="Pendiente" />;
    }
}

const Certificaciones = () => {
  const [documentos, setDocumentos] = useState<Documento[]>([]);
  const [tipos, setTipos] = useState<TipoDocumento[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const { register, handleSubmit, reset, formState: { isSubmitting } } = useForm<FormInputs>();

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const [docsRes, tiposRes] = await Promise.all([
        api.get<Documento[]>('/documentos-verificacion/'),
        api.get<TipoDocumento[]>('/documentos-verificacion/tipos/')
      ]);
      setDocumentos(docsRes.data);
      setTipos(tiposRes.data);
      setError(null);
    } catch (err) {
      setError('No se pudieron cargar los datos.');
      toast.error('Error al cargar datos.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const onSubmit: SubmitHandler<FormInputs> = async (data) => {
    if (!data.archivo || data.archivo.length === 0) {
      toast.warn('Por favor, selecciona un archivo para subir.');
      return;
    }

    const formData = new FormData();
    formData.append('tipo_documento', data.tipo_documento);
    formData.append('archivo', data.archivo[0]);

    try {
      await api.post('/documentos-verificacion/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      toast.success('¡Documento subido con éxito! Pendiente de verificación.');
      fetchData();
      setIsModalOpen(false);
      reset();
    } catch (err) {
      toast.error('Ocurrió un error al subir el documento.');
    }
  };

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Documentos y Certificaciones</h1>
        <button onClick={() => setIsModalOpen(true)} className="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded-full flex items-center">
          <FiUpload className="mr-2" /> Subir Documento
        </button>
      </div>

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left">Tipo de Documento</th>
              <th className="px-6 py-3 text-left">Fecha de Subida</th>
              <th className="px-6 py-3 text-left">Estado</th>
              <th className="px-6 py-3 text-left">Observaciones</th>
              <th className="px-6 py-3 text-right">Acciones</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {documentos.map((doc) => (
              <tr key={doc.id}>
                <td className="px-6 py-4">{doc.tipo_documento_nombre}</td>
                <td className="px-6 py-4">{new Date(doc.fecha_subida).toLocaleDateString()}</td>
                <td className="px-6 py-4"><EstadoIcon estado={doc.estado} /></td>
                <td className="px-6 py-4 text-sm text-gray-500">{doc.observaciones || 'N/A'}</td>
                <td className="px-6 py-4 text-right">
                  <a href={doc.archivo_url} target="_blank" rel="noopener noreferrer" className="text-indigo-600 hover:text-indigo-900 inline-flex items-center">
                    <FiDownload className="mr-1"/> Ver
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {isModalOpen && (
        <Modal title="Subir Nuevo Documento" onClose={() => setIsModalOpen(false)}>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label htmlFor="tipo_documento">Tipo de Documento</label>
              <select id="tipo_documento" {...register('tipo_documento', { required: true })}>
                {tipos.map(t => <option key={t.id} value={t.id}>{t.nombre}</option>)}
              </select>
            </div>
            <div>
              <label htmlFor="archivo">Archivo</label>
              <input id="archivo" type="file" {...register('archivo', { required: true })} />
            </div>
            <div className="flex justify-end space-x-2">
              <button type="button" onClick={() => setIsModalOpen(false)} className="bg-gray-200 rounded px-4 py-2">Cancelar</button>
              <button type="submit" disabled={isSubmitting} className="bg-indigo-600 text-white rounded px-4 py-2">
                {isSubmitting ? 'Subiendo...' : 'Subir'}
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  );
};

export default Certificaciones;