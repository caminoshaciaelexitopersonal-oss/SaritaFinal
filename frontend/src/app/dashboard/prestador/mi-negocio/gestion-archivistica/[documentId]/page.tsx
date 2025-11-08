// frontend/src/app/dashboard/prestador/mi-negocio/gestion-archivistica/[documentId]/page.tsx
"use client";

import React from 'react';
import { useQuery } from "@tanstack/react-query";
import { useParams } from 'next/navigation';
import apiClient from "@/services/api";
// import { PageHeader } from "@/components/shared/page-header"; // Eliminado
import { Button } from "@/components/ui/Button";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { AlertTriangle, Download, ChevronsRight, Hash, ShieldCheck } from 'lucide-react';
// import { Badge } from "@/components/ui/badge"; // Usaremos un span simple
import Link from 'next/link';

// --- Tipos de Datos (deben coincidir con el DocumentDetailSerializer) ---
interface VersionData {
    id: number;
    version_number: number;
    title: string;
    status: "PENDING_UPLOAD" | "PENDING_CONFIRMATION" | "VERIFIED" | "COMPROMISED";
    uploaded_at: string;
    original_filename: string;
    file_hash_sha256: string | null;
    merkle_root: string | null;
    blockchain_transaction: string | null;
    blockchain_timestamp: string | null;
}

interface DocumentDetailData {
    id: string;
    document_code: string;
    title: string; // Título de la primera versión
    versions: VersionData[];
}

const fetchDocumentDetail = async (id: string): Promise<DocumentDetailData> => {
    const response = await apiClient.get(`/mi-negocio/archivistica/documents/${id}/`);
    return response.data;
};

// --- Componentes de UI de la página ---
const CryptoProof = ({ version }: { version: VersionData }) => {
    if (version.status !== 'VERIFIED') return null;
    return (
        <div className="bg-gray-50 p-4 rounded-lg mt-4 border">
            <h4 className="font-semibold text-md mb-2 flex items-center"><ShieldCheck className="mr-2 h-5 w-5 text-green-600"/> Prueba Criptográfica</h4>
            <div className="text-sm space-y-2">
                <div className="flex justify-between">
                    <span className="font-medium text-gray-600">Hash (SHA-256):</span>
                    <code className="text-xs truncate">{version.file_hash_sha256}</code>
                </div>
                <div className="flex justify-between">
                    <span className="font-medium text-gray-600">Raíz de Merkle:</span>
                    <code className="text-xs truncate">{version.merkle_root}</code>
                </div>
                <div className="flex justify-between items-center">
                    <span className="font-medium text-gray-600">Transacción Blockchain:</span>
                    <Link href={`https://polygonscan.com/tx/${version.blockchain_transaction}`} target="_blank" className="text-blue-600 hover:underline">
                        <code className="text-xs truncate">{version.blockchain_transaction}</code>
                    </Link>
                </div>
            </div>
        </div>
    );
};

const statusVariant = {
    PENDING_UPLOAD: "secondary",
    PENDING_CONFIRMATION: "warning",
    VERIFIED: "success",
    COMPROMISED: "destructive",
};


// --- Componente Principal de la Página ---
export default function DocumentDetailPage() {
    const params = useParams();
    const documentId = params.documentId as string;

    const { data: document, isLoading, isError, error } = useQuery<DocumentDetailData, Error>({
        queryKey: ['archivisticaDocumentDetail', documentId],
        queryFn: () => fetchDocumentDetail(documentId),
        enabled: !!documentId, // Solo ejecutar si el ID está presente
    });

    if (isLoading) return <div>Cargando detalle del documento...</div>;
    if (isError) return (
        <Alert variant="destructive">
            <AlertTriangle className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{error.message}</AlertDescription>
        </Alert>
    );

    return (
        <div className="flex flex-col gap-8">
            <div>
                <h1 className="text-2xl font-bold">Documento: {document?.document_code}</h1>
                <p className="text-gray-500">Historial de versiones y pruebas de integridad para "{document?.title}".</p>
            </div>

            <div className="space-y-6">
                {document?.versions.map(version => (
                    <div key={version.id} className="border p-4 rounded-lg">
                        <div className="flex justify-between items-start">
                            <div>
                                <h3 className="font-bold text-lg">{version.title} (v{version.version_number})</h3>
                                <p className="text-sm text-gray-500">Subido el {new Date(version.uploaded_at).toLocaleString()}</p>
                            </div>
                            <div className="flex items-center gap-4">
                                <span className="p-2 bg-gray-200 rounded">{version.status.replace(/_/g, ' ')}</span>
                                <Button size="sm" variant="outline" disabled={version.status !== 'VERIFIED'}>
                                    <Download className="mr-2 h-4 w-4"/>
                                    Descargar
                                </Button>
                            </div>
                        </div>
                        <CryptoProof version={version} />
                    </div>
                ))}
            </div>
        </div>
    );
}
