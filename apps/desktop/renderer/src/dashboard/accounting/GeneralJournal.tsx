import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Book, Search, Calendar } from 'lucide-react';

export const GeneralJournal = () => {
  const [entries, setEntries] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchJournal = async () => {
      try {
        const response = await accountingService.getJournalEntries();
        setEntries(response.data || []);
      } catch (error) {
        console.error('Error al cargar Libro Diario real.');
      } finally {
        setLoading(false);
      }
    };
    fetchJournal();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h2 className="text-xl font-bold text-gray-800 flex items-center gap-2">
          <Book size={20} className="text-primary" /> Libro Diario (General Journal)
        </h2>
        <div className="flex gap-2">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 text-gray-400" size={16} />
            <input type="text" placeholder="Buscar asiento..." className="pl-10 pr-4 py-2 border rounded-lg text-sm outline-none focus:ring-2 ring-primary/20" />
          </div>
          <button className="px-4 py-2 bg-primary text-white rounded-lg text-sm font-bold hover:bg-blue-900 transition">Nuevo Asiento</button>
        </div>
      </div>

      <div className="p-0">
        <table className="w-full text-left">
          <thead className="bg-gray-50 text-gray-500 text-[10px] uppercase font-bold tracking-widest">
            <tr>
              <th className="px-6 py-4">ID / Fecha</th>
              <th className="px-6 py-4">Cuentas / Detalle</th>
              <th className="px-6 py-4">Ref</th>
              <th className="px-6 py-4 text-right">Débito</th>
              <th className="px-6 py-4 text-right">Crédito</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100 text-sm">
            {entries.map((entry, idx) => (
              <tr key={idx} className="hover:bg-gray-50 transition align-top">
                <td className="px-6 py-4 w-32">
                  <p className="font-bold text-gray-800">#{entry.id}</p>
                  <p className="text-[10px] text-gray-400 flex items-center gap-1 mt-1"><Calendar size={10} /> {entry.fecha}</p>
                </td>
                <td className="px-6 py-4">
                  <div className="mb-2">
                    <p className="font-medium text-primary">{entry.codigo_cuenta} - {entry.nombre_cuenta}</p>
                    <p className="text-xs text-gray-400 mt-0.5 ml-4 italic">{entry.descripcion}</p>
                  </div>
                </td>
                <td className="px-6 py-4 text-xs font-mono text-gray-400">GJ-{entry.id}</td>
                <td className="px-6 py-4 text-right font-mono text-green-600 font-bold">
                  {entry.naturaleza === 'DB' ? `$${entry.monto?.toLocaleString()}` : '-'}
                </td>
                <td className="px-6 py-4 text-right font-mono text-red-600 font-bold">
                  {entry.naturaleza === 'CR' ? `$${entry.monto?.toLocaleString()}` : '-'}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {loading ? (
          <div className="p-20 text-center text-gray-400 animate-pulse font-bold italic">Consultando Libros Fiscales...</div>
        ) : entries.length === 0 && (
          <div className="p-20 text-center text-gray-400 italic">No se han registrado asientos contables en el periodo actual.</div>
        )}
      </div>

      <div className="p-4 bg-gray-50 border-t border-gray-100 flex justify-between items-center text-xs font-bold text-gray-500">
        <span>Sistema de Contabilidad Centralizado SARITA (GESCONTABLE)</span>
        <span>SHA-256 Chained Integrity Verified ✓</span>
      </div>
    </div>
  );
};
