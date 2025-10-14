'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import api from '@/lib/api';
import FormField from '@/components/ui/FormField';
import { Button } from '@/components/ui/Button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';

interface ClienteFormData {
  pais_origen: string;
  cantidad: number;
  fecha_registro: string;
}

interface ClienteResumen {
    pais_origen: string;
    total_clientes: number;
}

const paises = [
    "Colombia", "Estados Unidos", "España", "México", "Argentina", "Chile",
    "Perú", "Ecuador", "Venezuela", "Brasil", "Canadá", "Francia", "Alemania",
    "Italia", "Reino Unido", "Otro"
];

const ClienteManager = () => {
  const [resumen, setResumen] = useState<ClienteResumen[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ClienteFormData>({
      defaultValues: {
          cantidad: 1,
          fecha_registro: new Date().toISOString().split('T')[0], // Hoy por defecto
      }
  });

  const fetchResumen = useCallback(async () => {
    setIsLoading(true);
    try {
      // Asumimos que el endpoint de registros_clientes puede devolver un resumen.
      // Si no, esto necesitaría un endpoint dedicado /prestador/clientes/resumen/
      const response = await api.get('/prestador/clientes/');
      // Aquí se necesitaría procesar los datos para agruparlos si la API no lo hace.
      // Por ahora, simularemos que la API devuelve el resumen.
      const groupedData = response.data.results.reduce((acc: any, curr: any) => {
          acc[curr.pais_origen] = (acc[curr.pais_origen] || 0) + curr.cantidad;
          return acc;
      }, {});
      const resumenData = Object.keys(groupedData).map(key => ({ pais_origen: key, total_clientes: groupedData[key] }));
      setResumen(resumenData);
    } catch (error) {
      toast.error('Error al cargar el resumen de clientes.');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchResumen();
  }, [fetchResumen]);

  const onSubmit: SubmitHandler<ClienteFormData> = async (data) => {
    try {
      await api.post('/prestador/clientes/', data);
      toast.success('Clientes registrados con éxito.');
      reset();
      fetchResumen();
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Ocurrió un error al registrar los clientes.');
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Registro de Clientes por Nacionalidad</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-1">
          <form onSubmit={handleSubmit(onSubmit)} className="bg-white p-6 rounded-lg shadow-md space-y-4">
            <h2 className="text-xl font-semibold mb-4">Registrar Nuevos Clientes</h2>
            <div>
              <label htmlFor="pais_origen" className="block text-sm font-medium text-gray-700">País de Origen</label>
              <select
                id="pais_origen"
                {...register('pais_origen', { required: 'Este campo es obligatorio.' })}
                className="w-full px-3 py-2 mt-1 border rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="">Seleccione un país</option>
                {paises.map(p => <option key={p} value={p}>{p}</option>)}
              </select>
              {errors.pais_origen && <p className="mt-1 text-xs text-red-600">{errors.pais_origen.message}</p>}
            </div>
            <FormField
              name="cantidad"
              label="Cantidad de Clientes"
              type="number"
              register={register}
              errors={errors}
              required
            />
            <FormField
              name="fecha_registro"
              label="Fecha del Registro"
              type="date"
              register={register}
              errors={errors}
              required
            />
            <Button type="submit" disabled={isSubmitting} className="w-full">
              {isSubmitting ? 'Registrando...' : 'Registrar'}
            </Button>
          </form>
        </div>

        <div className="md:col-span-2">
            <div className="bg-white p-6 rounded-lg shadow-md">
                <h2 className="text-xl font-semibold mb-4">Resumen de Clientes</h2>
                {isLoading ? (
                <p>Cargando resumen...</p>
                ) : (
                <Table>
                    <TableHeader>
                    <TableRow>
                        <TableHead>País de Origen</TableHead>
                        <TableHead className="text-right">Total Clientes</TableHead>
                    </TableRow>
                    </TableHeader>
                    <TableBody>
                    {resumen.map((item) => (
                        <TableRow key={item.pais_origen}>
                        <TableCell className="font-medium">{item.pais_origen}</TableCell>
                        <TableCell className="text-right">{item.total_clientes}</TableCell>
                        </TableRow>
                    ))}
                    </TableBody>
                </Table>
                )}
            </div>
        </div>
      </div>
    </div>
  );
};

export default ClienteManager;