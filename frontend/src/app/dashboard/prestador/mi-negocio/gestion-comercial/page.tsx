'use client';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useComercialApi } from './hooks/useComercialApi';
import { Button } from '@/components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { PlusCircle } from 'lucide-react';

export default function GestionComercialPage() {
  const { facturas, isLoading, isError } = useComercialApi();

  if (isError) {
    return (
        <Card>
            <CardHeader>
                <CardTitle>Error</CardTitle>
            </CardHeader>
            <CardContent>
                <p>No se pudieron cargar las facturas. Por favor, intente de nuevo más tarde.</p>
            </CardContent>
        </Card>
    );
  }

  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle>Gestión Comercial - Facturas de Venta</CardTitle>
        <Link href="/dashboard/prestador/mi-negocio/gestion-comercial/ventas/nueva" passHref>
          <Button>
            <PlusCircle className="mr-2 h-4 w-4" />
            Nueva Factura
          </Button>
        </Link>
      </CardHeader>
      <CardContent>
        {isLoading && facturas.length === 0 ? (
          <p>Cargando facturas...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>Cliente</TableHead>
                <TableHead>Fecha Emisión</TableHead>
                <TableHead>Total</TableHead>
                <TableHead>Estado</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {facturas.map((factura) => (
                <TableRow key={factura.id}>
                  <TableCell>{factura.numero_factura}</TableCell>
                  <TableCell>{factura.cliente_nombre}</TableCell>
                  <TableCell>{new Date(factura.fecha_emision).toLocaleDateString()}</TableCell>
                  <TableCell>${factura.total}</TableCell>
                  <TableCell>{factura.estado_display}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
