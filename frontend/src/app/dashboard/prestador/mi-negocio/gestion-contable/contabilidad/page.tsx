'use client';
import React, { useState } from 'react';
import { useContabilidadApi, JournalEntry } from '@/app/dashboard/prestador/mi-negocio/hooks/useContabilidadApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { PlusCircle, Eye } from 'lucide-react';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Modal } from '@/components/ui/Modal';
import { format } from 'date-fns';

// TODO: Crear un componente de formulario separado para JournalEntry
const JournalEntryForm = ({ onSubmit, onCancel }) => {
    // ... implementación del formulario ...
    return <div>Formulario de Asiento Contable (Pendiente)</div>
}

const ContabilidadPage = () => {
    const {
        costCenters, costCentersLoading,
        journalEntries, journalEntriesLoading,
        createJournalEntry
    } = useContabilidadApi();

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedEntry, setSelectedEntry] = useState<JournalEntry | null>(null);

    const handleCreateEntry = async (formData) => {
        try {
            await createJournalEntry(formData);
            setIsModalOpen(false);
        } catch (error) {
            console.error("Error al crear el asiento", error);
        }
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Módulo de Contabilidad</h1>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Centros de Costo</CardTitle>
                        <Button size="sm"><PlusCircle className="mr-2 h-4 w-4" /> Nuevo</Button>
                    </CardHeader>
                    <CardContent>
                        {costCentersLoading && <p>Cargando...</p>}
                        {costCenters && (
                             <Table>
                                <TableHeader><TableRow><TableHead>Código</TableHead><TableHead>Nombre</TableHead></TableRow></TableHeader>
                                <TableBody>
                                    {costCenters.map((center: any) => (
                                        <TableRow key={center.id}>
                                            <TableCell>{center.code}</TableCell>
                                            <TableCell>{center.name}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        )}
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Asientos Contables</CardTitle>
                         <Button size="sm" onClick={() => setIsModalOpen(true)}>
                            <PlusCircle className="mr-2 h-4 w-4" /> Nuevo Asiento
                        </Button>
                    </CardHeader>
                    <CardContent>
                        {journalEntriesLoading && <p>Cargando...</p>}
                        {journalEntries && (
                             <Table>
                                <TableHeader><TableRow><TableHead>Fecha</TableHead><TableHead>Descripción</TableHead><TableHead>Acciones</TableHead></TableRow></TableHeader>
                                <TableBody>
                                    {journalEntries.map((entry) => (
                                        <TableRow key={entry.id}>
                                            <TableCell>{format(new Date(entry.entry_date), 'dd/MM/yyyy')}</TableCell>
                                            <TableCell>{entry.description}</TableCell>
                                            <TableCell>
                                                <Button variant="outline" size="sm" onClick={() => setSelectedEntry(entry)}>
                                                    <Eye className="h-4 w-4" />
                                                </Button>
                                            </TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        )}
                    </CardContent>
                </Card>
            </div>

            {/* Modal para ver detalles del Asiento */}
            {selectedEntry && (
                <Modal isOpen={!!selectedEntry} onClose={() => setSelectedEntry(null)} title={`Detalle Asiento #${selectedEntry.id}`}>
                    <div className="p-4">
                        <p><strong>Fecha:</strong> {format(new Date(selectedEntry.entry_date), 'dd/MM/yyyy')}</p>
                        <p><strong>Descripción:</strong> {selectedEntry.description}</p>
                        <Table className="mt-4">
                            <TableHeader><TableRow><TableHead>Cuenta</TableHead><TableHead className="text-right">Débito</TableHead><TableHead className="text-right">Crédito</TableHead></TableRow></TableHeader>
                            <TableBody>
                                {selectedEntry.transactions.map(tx => (
                                    <TableRow key={tx.account.code}>
                                        <TableCell>{tx.account.code} - {tx.account.name}</TableCell>
                                        <TableCell className="text-right">{tx.debit}</TableCell>
                                        <TableCell className="text-right">{tx.credit}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </div>
                </Modal>
            )}

            {/* Modal para crear Asiento */}
            {isModalOpen && (
                <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Nuevo Asiento Contable">
                    <JournalEntryForm onSubmit={handleCreateEntry} onCancel={() => setIsModalOpen(false)} />
                </Modal>
            )}
        </div>
    );
};

export default ContabilidadPage;
