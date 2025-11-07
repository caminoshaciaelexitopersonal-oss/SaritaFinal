"use client";

import { ColumnDef } from "@tanstack/react-table";
import Link from "next/link";

// --- Importaciones de Componentes de UI Reales (con mayúsculas corregidas) ---
import { Button } from "@/components/ui/Button";
import { Badge } from "@/components/ui/Badge";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { MoreHorizontal } from "lucide-react";

// Tipo de Dato para cada fila
export type DocumentData = {
    id: string;
    document_code: string;
    latest_version: {
        title: string;
        version_number: number;
        status: 'PENDING_UPLOAD' | 'PENDING_CONFIRMATION' | 'VERIFIED' | 'COMPROMISED';
        uploaded_at: string;
    } | null;
    process: {
        name: string;
    };
}

// Definición del Array de Columnas
export const columns: ColumnDef<DocumentData>[] = [
    {
        accessorKey: "document_code",
        header: "Código",
        cell: ({ row }) => (
            <Link href={`/dashboard/prestador/mi-negocio/gestion-archivistica/${row.original.id}`} passHref>
                <span className="font-medium text-primary hover:underline cursor-pointer">
                    {row.getValue("document_code")}
                </span>
            </Link>
        ),
    },
    {
        id: "title",
        header: "Título",
        accessorFn: (row) => row.latest_version?.title,
        cell: ({ row }) => row.original.latest_version?.title || "Sin Versiones",
    },
    {
        accessorFn: (row) => row.process.name,
        header: "Proceso",
    },
    {
        id: 'status',
        header: "Estado",
        accessorFn: (row) => row.latest_version?.status,
        cell: ({ row }) => {
            const status = row.original.latest_version?.status;
            if (!status) return null;

            const variant = {
                "VERIFIED": "default",
                "PENDING_CONFIRMATION": "secondary",
                "COMPROMISED": "destructive",
                "PENDING_UPLOAD": "outline"
            }[status] || "outline";

            const text = {
                "VERIFIED": "Verificado",
                "PENDING_CONFIRMATION": "Pendiente Verif.",
                "PENDING_UPLOAD": "Procesando",
                "COMPROMISED": "Comprometido"
            }[status] || "Desconocido";

            return <Badge variant={variant as any}>{text}</Badge>;
        }
    },
    {
        id: "uploaded_at",
        header: "Actualizado",
        accessorFn: (row) => row.latest_version?.uploaded_at,
        cell: ({ getValue }) => {
            const date = getValue<string | null>();
            return date ? new Date(date).toLocaleDateString("es-ES", { day: '2-digit', month: 'short', year: 'numeric'}) : "-";
        },
    },
    {
        id: "actions",
        cell: ({ row }) => (
            <div className="text-right">
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <Button variant="ghost" className="h-8 w-8 p-0">
                            <span className="sr-only">Abrir menú</span>
                            <MoreHorizontal className="h-4 w-4" />
                        </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                        <DropdownMenuItem>Ver Detalles</DropdownMenuItem>
                        <DropdownMenuItem>Descargar</DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            </div>
        ),
    },
];
