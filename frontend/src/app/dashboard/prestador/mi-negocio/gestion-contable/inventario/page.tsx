'use client';
import React from 'react';
import { useInventarioApi } from '../hooks/useInventarioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { PlusCircle, Package } from 'lucide-react';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';

const InventarioPage = () => {
    const {
        productos,
        productosLoading,
        movimientos,
        movimientosLoading,
    } = useInventarioApi();

    const getStockBadge = (stock: number, minStock: number) => {
        if (stock < minStock) return <Badge variant="destructive">Bajo Stock</Badge>;
        if (stock < minStock * 1.2) return <Badge variant="secondary">Nivel Óptimo</Badge>;
        return <Badge variant="default">En Stock</Badge>;
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4 flex items-center">
                <Package className="mr-2" /> Módulo de Inventario
            </h1>

            <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
                {/* Sección de Productos */}
                <Card className="xl:col-span-2">
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Productos en Inventario</CardTitle>
                        <Button size="sm">
                            <PlusCircle className="mr-2 h-4 w-4" /> Nuevo Producto
                        </Button>
                    </CardHeader>
                    <CardContent>
                        {productosLoading && <p>Cargando productos...</p>}
                        {!productosLoading && productos && (
                             <Table>
                                <TableHeader>
                                    <TableRow>
                                        <TableHead>SKU</TableHead>
                                        <TableHead>Producto</TableHead>
                                        <TableHead>Stock Actual</TableHead>
                                        <TableHead>Precio Venta</TableHead>
                                        <TableHead>Estado</TableHead>
                                    </TableRow>
                                </TableHeader>
                                <TableBody>
                                    {productos.results.map((producto: any) => (
                                        <TableRow key={producto.id}>
                                            <TableCell className="font-mono">{producto.sku}</TableCell>
                                            <TableCell>{producto.nombre}</TableCell>
                                            <TableCell>{producto.stock_actual}</TableCell>
                                            <TableCell>${producto.precio_venta}</TableCell>
                                            <TableCell>{getStockBadge(parseFloat(producto.stock_actual), parseFloat(producto.stock_minimo))}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        )}
                         {!productosLoading && (!productos || productos.results.length === 0) && (
                            <p className="text-center text-gray-500 py-8">No hay productos registrados.</p>
                        )}
                    </CardContent>
                </Card>

                {/* Sección de Últimos Movimientos */}
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Últimos Movimientos</CardTitle>
                         <Button size="sm">
                            <PlusCircle className="mr-2 h-4 w-4" /> Nuevo Movimiento
                        </Button>
                    </CardHeader>
                    <CardContent>
                        {movimientosLoading && <p>Cargando movimientos...</p>}
                        {!movimientosLoading && movimientos && (
                            <div className="space-y-4">
                                {movimientos.results.slice(0, 10).map((mov: any) => (
                                    <div key={mov.id} className="flex items-center">
                                        <div className="ml-4 space-y-1">
                                            <p className="text-sm font-medium leading-none">{mov.producto_nombre}</p>
                                            <p className="text-sm text-muted-foreground">{mov.descripcion || mov.tipo_movimiento}</p>
                                        </div>
                                        <div className={`ml-auto font-medium ${mov.tipo_movimiento.includes('ENTRADA') || mov.tipo_movimiento.includes('POSITIVO') ? 'text-green-600' : 'text-red-600'}`}>
                                            {mov.tipo_movimiento.includes('ENTRADA') || mov.tipo_movimiento.includes('POSITIVO') ? '+' : '-'}{mov.cantidad}
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                        {!movimientosLoading && (!movimientos || movimientos.results.length === 0) && (
                           <p className="text-center text-gray-500 py-8">No hay movimientos recientes.</p>
                        )}
                    </CardContent>
                </Card>
            </div>
        </div>
    );
};

export default InventarioPage;
