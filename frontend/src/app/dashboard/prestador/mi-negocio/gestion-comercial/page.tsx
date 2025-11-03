'use client';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useMiNegocioApi, FacturaVenta } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Button } from '@/components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { PlusCircle } from 'lucide-react';

export default function GestionComercialPage() {
  const { getFacturasVenta, isLoading } = useMiNegocioApi();
  const [facturas, setFacturas] = useState<FacturaVenta[]>([]);

  useEffect(() => {
    const fetchFacturas = async () => {
      const data = await getFacturasVenta();
      if (data) {
        setFacturas(data);
      }
    };
    fetchFacturas();
  }, [getFacturasVenta]);

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
                  <TableCell>{factura.id}</TableCell>
                  <TableCell>{factura.cliente_nombre || factura.cliente}</TableCell>
                  <TableCell>{new Date(factura.fecha_emision).toLocaleDateString()}</TableCell>
                  <TableCell>${factura.total}</TableCell>
                  <TableCell>{factura.estado}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
