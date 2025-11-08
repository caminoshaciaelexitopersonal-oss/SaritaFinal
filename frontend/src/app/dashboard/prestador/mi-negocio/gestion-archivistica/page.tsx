"use client";

import React from 'react';
import { useQuery } from "@tanstack/react-query";
import apiClient from "@/services/api"; // Usaremos el cliente de API real

// --- Componentes Reales ---
import { columns, DocumentData } from "./components/columns";
import { DataTable } from "./components/data-table";
import { DataTableSkeleton } from "./components/data-table-skeleton";
import { UploadDialog } from "./components/upload-dialog";
import { PageHeader } from "@/components/shared/page-header";
import { Button } from "@/components/ui/Button";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { AlertTriangle } from 'lucide-react';

// Función para obtener los datos desde el backend
const fetchDocuments = async (): Promise<DocumentData[]> => {
    const response = await apiClient.get('/mi-negocio/archivistica/documents/');
    // La API de DRF devuelve los datos paginados en un objeto `results`
    return response.data.results || response.data;
};

export default function GestionArchivisticaPage() {
    const { data: documents, isLoading, isError, error } = useQuery<DocumentData[], Error>({
        queryKey: ['archivisticaDocuments'],
        queryFn: fetchDocuments,
    });

    if (isError) {
        return (
            <Alert variant="destructive">
                <AlertTriangle className="h-4 w-4" />
                <AlertTitle>Error al Cargar Documentos</AlertTitle>
                <AlertDescription>
                    No se pudo obtener la lista de documentos. Por favor, intente de nuevo más tarde.
                    <p className="text-xs mt-2">({error.message})</p>
                </AlertDescription>
            </Alert>
        );
    }

    return (
        <div className="flex flex-col gap-8">
            <PageHeader
                title="Gestión Archivística"
                description="Centralice, asegure y gestione todos los documentos de su empresa."
            >
                <UploadDialog>
                    <Button>Subir Nuevo Documento</Button>
                </UploadDialog>
            </PageHeader>

            <div>
                {isLoading ? (
                    <DataTableSkeleton columnCount={6} rowCount={5} />
                ) : (
                    <DataTable
                        columns={columns}
                        data={documents || []}
                        searchColumnId="title"
                        searchPlaceholder="Filtrar por título..."
                    />
                )}
            </div>
        </div>
    );
}
