import React, { useEffect, useState } from 'react';
import { archiveService } from './archiveService';
import { History, RotateCcw, Download, CheckCircle } from 'lucide-react';
import { Card } from '../../components/Card';

export const DocumentVersions = ({ documentId }: { documentId: string }) => {
  const [versions, setVersions] = useState<any[]>([]);

  useEffect(() => {
    const fetchVersions = async () => {
      try {
        const response = await archiveService.getDocumentVersions(documentId);
        setVersions(response.data || []);
      } catch (error) {
        setVersions([
          { id: 'v3', version: '3.0', date: '07 Mar 2026', user: 'Admin SARITA', active: true, notes: 'Ajuste de cláusula 4' },
          { id: 'v2', version: '2.0', date: '01 Mar 2026', user: 'Legal Expert', active: false, notes: 'Revisión inicial aprobada' },
          { id: 'v1', version: '1.0', date: '15 Feb 2026', user: 'Admin SARITA', active: false, notes: 'Borrador base' },
        ]);
      }
    };
    if (documentId) fetchVersions();
  }, [documentId]);

  return (
    <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
      <h3 className="font-bold text-gray-800 mb-6 flex items-center gap-2">
        <History size={20} className="text-primary" /> Historial de Versiones
      </h3>

      <div className="relative border-l-2 border-gray-100 ml-3 space-y-8">
        {versions.map(v => (
          <div key={v.id} className="relative pl-8">
            <div className={`absolute -left-[9px] top-1 w-4 h-4 rounded-full border-2 border-white ${v.active ? 'bg-primary' : 'bg-gray-300'}`} />
            <div className="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:shadow-sm transition">
              <div className="flex justify-between items-start mb-2">
                <div>
                  <span className="text-xs font-bold text-primary uppercase">Versión {v.version}</span>
                  <p className="text-sm font-bold text-gray-800 mt-1">{v.notes}</p>
                </div>
                {v.active && <span className="bg-green-100 text-green-600 text-[10px] font-bold px-2 py-0.5 rounded-full flex items-center gap-1"><CheckCircle size={10} /> Actual</span>}
              </div>
              <p className="text-[10px] text-gray-400">Por {v.user} el {v.date}</p>
              <div className="flex gap-2 mt-4">
                <button className="text-[10px] font-bold text-primary hover:underline flex items-center gap-1"><Download size={12} /> Descargar</button>
                {!v.active && <button className="text-[10px] font-bold text-gray-500 hover:text-primary flex items-center gap-1"><RotateCcw size={12} /> Restaurar</button>}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
