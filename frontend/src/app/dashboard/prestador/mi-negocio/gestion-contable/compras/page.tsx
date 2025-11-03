'use client';
import React, { useState } from 'react';
import { useComprasApi } from '../hooks/useComprasApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { PlusCircle, Download } from 'lucide-react';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Checkbox } from '@/components/ui/checkbox';
import { format } from 'date-fns';

const ComprasPage = () => {
    const {
        proveedores,
        proveedoresLoading,
        facturasCompra,
        facturasCompraLoading,
        generarPagoMasivo
    } = useComprasApi();
    const [selectedFacturas, setSelectedFacturas] = useState<number[]>([]);

    const handleSelectFactura = (id: number, checked: boolean | 'indeterminate') => {
        if (checked) {
            setSelectedFacturas(prev => [...prev, id]);
        } else {
            setSelectedFacturas(prev => prev.filter(facturaId => facturaId !== id));
        }
    };

    const handleGenerarPago = async () => {
        if (selectedFacturas.length === 0) return;
        try {
            await generarPagoMasivo(selectedFacturas);
            setSelectedFacturas([]);
        } catch (error) {
            console.error("Error al generar el archivo de pago masivo", error);
            // Aquí se podría mostrar una notificación de error al usuario
        }
    };

    const facturasPorPagar = facturasCompra?.results.filter((f: any) => f.estado === 'POR_PAGAR');

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Módulo de Compras y Proveedores</h1>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* Sección de Proveedores */}
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Proveedores</CardTitle>
                        <Button size="sm">
                            <PlusCircle className="mr-2 h-4 w-4" /> Nuevo Proveedor
                        </Button>
                    </CardHeader>
                    <CardContent>
                        {proveedoresLoading && <p>Cargando proveedores...</p>}
                        {!proveedoresLoading && proveedores && (
                             <Table>
                                <TableHeader>
                                    <TableRow>
                                        <TableHead>Nombre</TableHead>
                                        <TableHead>Teléfono</TableHead>
                                    </TableRow>
                                </TableHeader>
                                <TableBody>
                                    {proveedores.results.map((proveedor: any) => (
                                        <TableRow key={proveedor.id}>
                                            <TableCell>{proveedor.nombre}</TableCell>
                                            <TableCell>{proveedor.telefono || 'N/A'}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        )}
                        {!proveedoresLoading && (!proveedores || proveedores.results.length === 0) && (
                            <p className="text-center text-gray-500">No hay proveedores registrados.</p>
                        )}
                    </CardContent>
                </Card>

                {/* Sección de Facturas de Compra */}
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Facturas por Pagar</CardTitle>
                        <div>
                            <Button size="sm" onClick={handleGenerarPago} disabled={selectedFacturas.length === 0}>
                                <Download className="mr-2 h-4 w-4" /> Generar Pago ({selectedFacturas.length})
                            </Button>
                            <Button size="sm" className="ml-2">
                                <PlusCircle className="mr-2 h-4 w-4" /> Nueva Factura
                            </Button>
                        </div>
                    </CardHeader>
                    <CardContent>
                        {facturasCompraLoading && <p>Cargando facturas...</p>}
                        {!facturasCompraLoading && facturasPorPagar && (
                             <Table>
                                <TableHeader>
                                    <TableRow>
                                        <TableHead className="w-[50px]"></TableHead>
                                        <TableHead># Factura</TableHead>
                                        <TableHead>Proveedor</TableHead>
                                        <TableHead>Total</TableHead>
                                    </TableRow>
                                </TableHeader>
                                <TableBody>
                                    {facturasPorPagar.map((factura: any) => (
                                        <TableRow key={factura.id}>
                                            <TableCell>
                                                <Checkbox
                                                    checked={selectedFacturas.includes(factura.id)}
                                                    onCheckedChange={(checked) => handleSelectFactura(factura.id, checked)}
                                                />
                                            </TableCell>
                                            <TableCell>{factura.numero_factura}</TableCell>
                                            <TableCell>{factura.proveedor_nombre}</TableCell>
                                            <TableCell>${factura.total}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        )}
                        {!facturasCompraLoading && (!facturasPorPagar || facturasPorPagar.length === 0) && (
                            <p className="text-center text-gray-500">No hay facturas por pagar.</p>
                        )}
                    </CardContent>
                </Card>
            </div>
        </div>
    );
};

export default ComprasPage;
