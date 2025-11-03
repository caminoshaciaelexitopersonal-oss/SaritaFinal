'use client';
import React, { useEffect, useState } from 'react';
import { useMiNegocioApi } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export default function NominaPage() {
  const { getNominaPlaceholder, isLoading } = useMiNegocioApi();
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      // La respuesta de los placeholders que creamos es una lista
      const response = await getNominaPlaceholder();
      if (response && Array.isArray(response) && response.length > 0) {
        setMessage(response[0].message);
      } else {
        setMessage('El módulo se encuentra actualmente en desarrollo.');
      }
    };
    fetchData();
  }, [getNominaPlaceholder]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Gestión de Nómina</CardTitle>
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <p>Cargando...</p>
        ) : (
          <p className="text-gray-600">{message}</p>
        )}
      </CardContent>
    </Card>
  );
}
