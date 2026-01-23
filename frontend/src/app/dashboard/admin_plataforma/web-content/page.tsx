'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Button } from '@/components/ui/Button';
import { toast } from 'react-toastify';
import { FiEdit, FiTrash2, FiPlusCircle } from 'react-icons/fi';
import api from '@/services/api';

interface WebPage {
    id: number;
    title: string;
    slug: string;
    is_published: boolean;
}

export default function WebContentPage() {
    const [pages, setPages] = useState<WebPage[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const fetchPages = useCallback(async () => {
        try {
            setIsLoading(true);
            const response = await api.get('/web/admin/pages/');
            setPages(response.data.results || []);
        } catch (err) {
            setError('No se pudieron cargar las páginas.');
            toast.error('No se pudieron cargar las páginas.');
        } finally {
            setIsLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchPages();
    }, [fetchPages]);

    if (isLoading) {
        return <p>Cargando páginas...</p>;
    }

    if (error) {
        return <p className="text-red-500">{error}</p>;
    }

    return (
        <Card>
            <CardHeader className="flex flex-row items-center justify-between">
                <CardTitle>Gestión de Contenido Web</CardTitle>
                <Button>
                    <FiPlusCircle className="mr-2 h-4 w-4" />
                    Crear Nueva Página
                </Button>
            </CardHeader>
            <CardContent>
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Título</TableHead>
                            <TableHead>Slug (URL)</TableHead>
                            <TableHead>Estado</TableHead>
                            <TableHead>Acciones</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {pages.map((page) => (
                            <TableRow key={page.id}>
                                <TableCell className="font-medium">{page.title}</TableCell>
                                <TableCell>/_/{page.slug}</TableCell>
                                <TableCell>
                                    <span className={`px-2 py-1 text-xs font-semibold rounded-full ${page.is_published ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
                                        {page.is_published ? 'Publicada' : 'Borrador'}
                                    </span>
                                </TableCell>
                                <TableCell className="flex gap-2">
                                    <Button variant="outline" size="sm">
                                        <FiEdit className="h-4 w-4" />
                                    </Button>
                                    <Button variant="destructive" size="sm">
                                        <FiTrash2 className="h-4 w-4" />
                                    </Button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </CardContent>
        </Card>
    );
}
