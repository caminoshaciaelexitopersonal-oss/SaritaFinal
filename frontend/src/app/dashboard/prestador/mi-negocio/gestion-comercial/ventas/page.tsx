"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { useMiNegocioApi, FacturaVenta } from "../../../../(authenticated)/prestador/mi-negocio/hooks/useMiNegocioApi";
import { PlusCircle } from "lucide-react";

export default function FacturasVentaPage() {
  const { getFacturasVenta } = useMiNegocioApi();
  const [facturas, setFacturas] = useState<FacturaVenta[]>([]);

  useEffect(() => {
    const fetchFacturas = async () => {
      const data = await getFacturasVenta();
      if (data) setFacturas(data);
    };
    fetchFacturas();
  }, [getFacturasVenta]);

  return (
    <div className="p-4 md:p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Facturas de Venta</h1>
        <Button asChild>
          <Link href="/dashboard/prestador/mi-negocio/gestion-comercial/ventas/nueva">
            <PlusCircle className="mr-2 h-4 w-4" />
            Nueva Factura
          </Link>
        </Button>
      </div>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead># Factura</TableHead>
            <TableHead>Cliente</TableHead>
            <TableHead>Fecha Emisión</TableHead>
            <TableHead>Estado</TableHead>
            <TableHead className="text-right">Total</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {facturas.map((factura) => (
            <TableRow key={factura.id}>
              <TableCell className="font-medium">#{factura.id}</TableCell>
              <TableCell>{factura.cliente_nombre}</TableCell>
              <TableCell>{factura.fecha_emision}</TableCell>
              <TableCell>{factura.estado_display}</TableCell>
              <TableCell className="text-right">
                {new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(parseFloat(factura.total))}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
