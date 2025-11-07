"use client";

import React from 'react';

// --- Componentes de UI Simulados ---
const Card = ({ children }) => <div className="border rounded-lg shadow-sm">{children}</div>;
const CardHeader = ({ children }) => <div className="p-4 border-b">{children}</div>;
const CardTitle = ({ children }) => <h3 className="text-lg font-semibold">{children}</h3>;
const CardDescription = ({ children }) => <p className="text-sm text-muted-foreground">{children}</p>;
const CardContent = ({ children }) => <div className="p-4 space-y-4">{children}</div>;
const Badge = ({ children, ...props }) => <span className="px-2 py-1 text-xs font-semibold rounded-full" {...props}>{children}</span>;
const Button = ({ children, ...props }) => <button {...props}>{children}</button>;
const Skeleton = ({ className }) => <div className={`animate-pulse bg-muted rounded-md ${className}`} />;

const InfoRow = ({ label, value }) => (
    <div>
        <span className="text-sm font-medium text-muted-foreground">{label}</span>
        <p className="text-sm font-mono break-all">{value}</p>
    </div>
);

const StatusBadge = ({ status }) => {
    const styles = {
        VERIFIED: "bg-green-100 text-green-800",
        PENDING_CONFIRMATION: "bg-yellow-100 text-yellow-800",
        COMPROMISED: "bg-red-100 text-red-800",
        DEFAULT: "bg-gray-100 text-gray-800",
    };
    const text = {
        VERIFIED: "Verificado",
        PENDING_CONFIRMATION: "Pendiente Notarización",
        COMPROMISED: "Comprometido",
        DEFAULT: "Procesando"
    };
    const style = styles[status] || styles.DEFAULT;
    const label = text[status] || text.DEFAULT;
    return <Badge className={style}>{label}</Badge>;
};

export function IntegrityCertificate({ version }) {
    if (!version) {
        return <Skeleton className="h-96 w-full" />;
    }

    const isVerified = version.status === 'VERIFIED';

    return (
        <Card>
            <CardHeader>
                <CardTitle>Certificado de Integridad</CardTitle>
                <CardDescription>Prueba criptográfica de la existencia e integridad del documento.</CardDescription>
            </CardHeader>
            <CardContent>
                <div>
                    <span className="text-sm font-medium text-muted-foreground">Estado</span>
                    <StatusBadge status={version.status} />
                </div>

                {version.file_hash_sha256 && (
                    <InfoRow label="Huella Digital (SHA-256)" value={version.file_hash_sha256} />
                )}

                {isVerified && version.blockchain_timestamp && (
                    <InfoRow label="Fecha de Verificación (UTC)" value={new Date(version.blockchain_timestamp).toLocaleString()} />
                )}

                {isVerified && version.blockchain_transaction && (
                    <div>
                        <span className="text-sm font-medium text-muted-foreground">Prueba en Blockchain</span>
                        <a href={`https://polygonscan.com/tx/${version.blockchain_transaction}`} target="_blank" rel="noopener noreferrer" className="text-sm text-primary hover:underline font-mono break-all block">
                            {version.blockchain_transaction}
                        </a>
                    </div>
                )}

                <div className="border-t pt-4">
                    <Button className="w-full" disabled={!isVerified}>
                        Verificar Integridad Ahora
                    </Button>
                </div>
            </CardContent>
        </Card>
    );
}
