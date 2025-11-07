"use client";

import React from 'react';

// --- Componentes Reales (con mayúsculas corregidas) ---
import { columns } from "./components/columns";
import { DataTable } from "./components/data-table";
import { DataTableSkeleton } from "./components/data-table-skeleton";
import { UploadDialog } from "./components/upload-dialog";
import { PageHeader } from "@/components/shared/page-header";
import { Button } from "@/components/ui/Button";

// Simulación de datos de la API
const mockDocuments = [
    {
        id: "doc-uuid-1",
        document_code: "OP-CAL-MAN-01",
        process: { name: "Gestión de Calidad" },
        latest_version: {
            title: "Manual de Procedimientos v2",
            version_number: 2,
            status: "VERIFIED",
            uploaded_at: new Date().toISOString(),
        },
    },
    {
        id: "doc-uuid-2",
        document_code: "RH-CON-FOR-03",
        process: { name: "Recursos Humanos" },
        latest_version: {
            title: "Formato de Contratación",
            version_number: 1,
            status: "PENDING_CONFIRMATION",
            uploaded_at: new Date().toISOString(),
        },
    },
];

export default function GestionArchivisticaPage() {
    const { data: documents, isLoading, isError } = {
        data: mockDocuments,
        isLoading: false,
        isError: false,
    };

    if (isError) {
        return <div>Error al cargar los documentos.</div>;
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
                        data={documents}
                        searchColumnId="title"
                        searchPlaceholder="Filtrar por título..."
                    />
                )}
            </div>
        </div>
    );
}
