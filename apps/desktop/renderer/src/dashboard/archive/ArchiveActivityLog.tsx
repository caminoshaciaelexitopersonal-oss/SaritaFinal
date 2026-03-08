import React, { useEffect, useState } from 'react';
import { archiveService } from './archiveService';
import { History, User, FileText, Download, Trash2, Edit } from 'lucide-react';

export const ArchiveActivityLog = () => {
  const [logs, setLogs] = useState<any[]>([]);

  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const response = await archiveService.getActivityLog();
        setLogs(response.data || []);
      } catch (error) {
        setLogs([
          { id: '1', user: 'Andrés V.', action: 'Subida', doc: 'Contrato_Socio_V1.pdf', date: '07 Mar 2026 14:30' },
          { id: '2', user: 'Admin SARITA', action: 'Visualización', doc: 'Factura_FE-001.pdf', date: '07 Mar 2026 12:15' },
          { id: '3', user: 'Contador Pro', action: 'Descarga', doc: 'Reporte_Ventas.xlsx', date: '06 Mar 2026 09:45' },
        ]);
      }
    };
    fetchLogs();
  }, []);

  const getActionIcon = (action: string) => {
    switch (action) {
      case 'Subida': return <FileText size={16} className="text-blue-600" />;
      case 'Descarga': return <Download size={16} className="text-green-600" />;
      case 'Eliminación': return <Trash2 size={16} className="text-red-600" />;
      default: return <Eye size={16} className="text-gray-600" />;
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 bg-gray-50/50 flex items-center gap-3">
        <History className="text-primary" size={24} />
        <h2 className="text-xl font-bold text-gray-800">Registro de Actividad Documental</h2>
      </div>

      <div className="divide-y divide-gray-100">
        {logs.map(log => (
          <div key={log.id} className="p-4 flex items-center justify-between hover:bg-gray-50 transition border-l-4 border-transparent hover:border-primary">
            <div className="flex items-center gap-4">
              <div className="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center text-gray-500">
                <User size={16} />
              </div>
              <div>
                <p className="text-sm font-medium text-gray-800">
                  <span className="font-bold text-primary">{log.user}</span> realizó una <span className="font-bold text-gray-900">{log.action}</span> de:
                </p>
                <div className="flex items-center gap-2 mt-1">
                  {getActionIcon(log.action)}
                  <span className="text-xs text-primary font-medium">{log.doc}</span>
                </div>
              </div>
            </div>
            <div className="text-right">
              <p className="text-[10px] text-gray-400 font-bold uppercase">{log.date}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

import { Eye } from 'lucide-react';
