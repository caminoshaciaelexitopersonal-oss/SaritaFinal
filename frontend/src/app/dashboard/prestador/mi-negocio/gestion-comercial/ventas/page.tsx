'use client';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useMiNegocioApi, FacturaVenta } from '../../../hooks/useMiNegocioApi';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { PlusCircle } from 'lucide-react';
import { format } from 'date-fns';

export default function VentasPage() {
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
        <CardTitle>Facturación de Ventas</CardTitle>
        <Link href="/dashboard/prestador/mi-negocio/gestion-comercial/ventas/nueva" passHref>
          <Button>
            <PlusCircle className="mr-2 h-4 w-4" />
            Nueva Factura
          </Button>
        </Link>
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <p>Cargando facturas...</p>
        ) : (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead># Factura</TableHead>
                <TableHead>Cliente</TableHead>
                <TableHead>Fecha Emisión</TableHead>
                <TableHead>Total</TableHead>
                <TableHead>Estado</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {facturas.map((factura) => (
                <TableRow key={factura.id}>
                  <TableCell>#{factura.id}</TableCell>
                  <TableCell>{factura.cliente_nombre}</TableCell>
                  <TableCell>{format(new Date(factura.fecha_emision), 'dd/MM/yyyy')}</TableCell>
                  <TableCell>${factura.total}</TableCell>
                  <TableCell>
                    <Badge>{factura.estado}</Badge>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}
