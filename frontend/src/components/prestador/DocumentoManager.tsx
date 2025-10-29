'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import useMiNegocioApi from '../../../app/dashboard/prestador/mi-negocio/ganchos/useMiNegocioApi';
import { Button } from '@/components/ui/Button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { FiUpload, FiPaperclip, FiCheck, FiX, FiClock } from 'react-icons/fi';

// --- Tipos ---
interface TipoDocumento {
  id: number;
  nombre: string;
  descripcion: string;
}

interface DocumentoSubido {
  id: number;
  tipo_documento_nombre: string;
  archivo_url: string;
  estado: 'PENDIENTE' | 'APROBADO' | 'RECHAZADO';
  observaciones: string;
  fecha_subida: string;
}

interface UploadFormData {
  tipo_documento: number;
  archivo: FileList;
}

const DocumentoManager = () => {
  const [tipos, setTipos] = useState<TipoDocumento[]>([]);
  const [documentos, setDocumentos] = useState<DocumentoSubido[]>([]);
  const { request, loading: apiLoading } = useMiNegocioApi();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<UploadFormData>();

  const fetchData = useCallback(async () => {
    try {
      const [tiposRes, docsRes] = await Promise.all([
        request('/documentos/tipos/'), // Suponiendo que hay un endpoint para esto
        request('/documentos/'),
      ]);
      setTipos(tiposRes.results || tiposRes);
      setDocumentos(docsRes.results || docsRes);
    } catch (error) {
      toast.error('Error al cargar los datos de documentos.');
    }
  }, [request]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const onSubmit: SubmitHandler<UploadFormData> = async (data) => {
    if (!data.archivo || data.archivo.length === 0) {
      toast.error('Por favor, selecciona un archivo.');
      return;
    }

    const formData = new FormData();
    formData.append('tipo_documento', data.tipo_documento.toString());
    formData.append('archivo', data.archivo[0]);

    try {
      await request('/documentos/', {
        method: 'POST',
        body: formData,
        headers: {
          // Dejar que el navegador establezca el Content-Type para FormData
          'Content-Type': undefined,
        },
      });
      toast.success('Documento subido con éxito.');
      reset();
      fetchData();
    } catch (error) {
      toast.error('Error al subir el documento.');
    }
  };

  const estadoIcono = (estado: DocumentoSubido['estado']) => {
    switch (estado) {
      case 'APROBADO': return <FiCheck className="text-green-500" />;
      case 'RECHAZADO': return <FiX className="text-red-500" />;
      default: return <FiClock className="text-yellow-500" />;
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Gestión de Documentos de Verificación</h1>

      <div className="bg-white p-6 rounded-lg shadow-md mb-8">
        <h2 className="text-xl font-semibold mb-4">Subir Nuevo Documento</h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label htmlFor="tipo_documento" className="block text-sm font-medium text-gray-700">Tipo de Documento</label>
            <select
              id="tipo_documento"
              {...register('tipo_documento', { required: 'Debe seleccionar un tipo.' })}
              className="w-full px-3 py-2 mt-1 border rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">Seleccione...</option>
              {tipos.map(t => <option key={t.id} value={t.id}>{t.nombre}</option>)}
            </select>
            {errors.tipo_documento && <p className="mt-1 text-xs text-red-600">{errors.tipo_documento.message}</p>}
          </div>
          <div>
            <label htmlFor="archivo" className="block text-sm font-medium text-gray-700">Archivo</label>
            <input
              id="archivo"
              type="file"
              {...register('archivo', { required: 'Debe seleccionar un archivo.' })}
              className="w-full px-3 py-2 mt-1 text-sm text-gray-900 border border-gray-300 rounded-md cursor-pointer bg-gray-50 focus:outline-none"
            />
            {errors.archivo && <p className="mt-1 text-xs text-red-600">{errors.archivo.message}</p>}
          </div>
          <Button type="submit" disabled={isSubmitting}>
            <FiUpload className="mr-2" />
            {isSubmitting ? 'Subiendo...' : 'Subir Documento'}
          </Button>
        </form>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">Documentos Subidos</h2>
        {apiLoading ? (
          <p>Cargando documentos...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Tipo de Documento</TableHead>
                <TableHead>Estado</TableHead>
                <TableHead>Fecha de Subida</TableHead>
                <TableHead>Acciones</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {documentos.map((doc) => (
                <TableRow key={doc.id}>
                  <TableCell className="font-medium">{doc.tipo_documento_nombre}</TableCell>
                  <TableCell>
                    <div className="flex items-center space-x-2">
                      {estadoIcono(doc.estado)}
                      <span>{doc.estado}</span>
                    </div>
                  </TableCell>
                  <TableCell>{new Date(doc.fecha_subida).toLocaleDateString()}</TableCell>
                  <TableCell>
                    <a href={doc.archivo_url} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                      <FiPaperclip className="inline mr-1" />
                      Ver
                    </a>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </div>
    </div>
  );
};

export default DocumentoManager;
