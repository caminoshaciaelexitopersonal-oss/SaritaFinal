// /app/dashboard/prestador/mi-negocio/gestion-contable/asientos/page.tsx
'use client';

import { useEffect, useState, useCallback } from 'react';
import { useMiNegocioApi, JournalEntry, ChartOfAccount } from '../../../hooks/useMiNegocioApi';
import JournalEntryForm from '../components/JournalEntryForm';
import Modal from '@/components/ui/Modal';
import { FiPlus } from 'react-icons/fi';

export default function AsientosContablesPage() {
  const {
    getJournalEntries,
    createJournalEntry,
    getChartOfAccounts,
    isLoading,
    error
  } = useMiNegocioApi();

  const [asientos, setAsientos] = useState<JournalEntry[]>([]);
  const [accounts, setAccounts] = useState<ChartOfAccount[]>([]);
  const [selectedAsiento, setSelectedAsiento] = useState<JournalEntry | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchAsientos = useCallback(async () => {
    const data = await getJournalEntries();
    if (data) {
      setAsientos(data);
    }
  }, [getJournalEntries]);

  useEffect(() => {
    fetchAsientos();
    // También cargamos las cuentas para el formulario
    const fetchAccounts = async () => {
        const data = await getChartOfAccounts();
        if(data) setAccounts(data);
    }
    fetchAccounts();
  }, [fetchAsientos, getChartOfAccounts]);

  const handleFormSubmit = async (data: any) => {
    const success = await createJournalEntry(data);
    if (success) {
      fetchAsientos();
      setIsModalOpen(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Asientos Contables</h1>
        <button onClick={() => setIsModalOpen(true)} className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg flex items-center">
          <FiPlus className="mr-2" />
          Nuevo Asiento
        </button>
      </div>

       {/* ... (código de la vista de lista/detalle igual que antes) ... */}
       <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-1 bg-white shadow-md rounded-lg p-4 overflow-y-auto h-[70vh]">
          <h2 className="text-lg font-semibold mb-4">Comprobantes</h2>
          {isLoading && asientos.length === 0 ? (
            <p>Cargando...</p>
          ) : error ? (
            <p className="text-red-500">{error}</p>
          ) : (
            <ul className="space-y-2">
              {asientos.map(asiento => (
                <li key={asiento.id} onClick={() => setSelectedAsiento(asiento)} className={`p-3 rounded-lg cursor-pointer hover:bg-gray-100 ${selectedAsiento?.id === asiento.id ? 'bg-blue-100' : ''}`}>
                  <p className="font-semibold text-gray-800">JE-{asiento.id}</p>
                  <p className="text-sm text-gray-600">{asiento.date}</p>
                  <p className="text-sm text-gray-500 truncate">{asiento.description}</p>
                </li>
              ))}
            </ul>
          )}
        </div>
        <div className="md:col-span-2 bg-white shadow-md rounded-lg p-6">
          {selectedAsiento ? (
            <div>
              <h2 className="text-xl font-bold mb-2">Detalle del Asiento JE-{selectedAsiento.id}</h2>
              {/* ... (resto del detalle) ... */}
            </div>
          ) : (
            <div className="flex items-center justify-center h-full">
              <p className="text-gray-500">Seleccione un asiento para ver su detalle o cree uno nuevo.</p>
            </div>
          )}
        </div>
      </div>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Crear Nuevo Asiento Contable">
        <JournalEntryForm
          onSubmit={handleFormSubmit}
          isLoading={isLoading}
          accounts={accounts}
        />
      </Modal>
    </div>
  );
}
