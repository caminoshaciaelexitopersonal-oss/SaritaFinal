import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { ShieldAlert, User, History, Check } from 'lucide-react';

export const AccountingAuditLog = () => {
  const [logs, setLogs] = useState<any[]>([]);

  useEffect(() => {
    setLogs([
      { id: '1', user: 'Contador Pro', action: 'Creación Asiento Manual', ref: 'J-1202', date: '07 Mar 2026 15:45' },
      { id: '2', user: 'Sistema SARITA', action: 'Posteo Automático Venta', ref: 'S-101', date: '07 Mar 2026 14:30' },
      { id: '3', user: 'Admin SARITA', action: 'Cierre de Periodo Fiscal', ref: 'Feb-2026', date: '01 Mar 2026 09:00' },
    ]);
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 bg-gray-900 text-white flex items-center gap-3">
        <ShieldAlert className="text-secondary" size={24} />
        <div>
          <h2 className="text-lg font-bold">Registro de Auditoría Contable</h2>
          <p className="text-[10px] text-gray-400 font-medium">Trazabilidad total de cada movimiento financiero.</p>
        </div>
      </div>

      <div className="divide-y divide-gray-100">
        {logs.map(log => (
          <div key={log.id} className="p-6 flex items-center justify-between hover:bg-gray-50 transition">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 border border-gray-200">
                <User size={20} />
              </div>
              <div>
                <p className="text-sm font-medium text-gray-800">
                  <span className="font-bold text-primary">{log.user}</span> ejecutó: <span className="font-bold">{log.action}</span>
                </p>
                <div className="flex items-center gap-4 mt-1">
                  <span className="text-[10px] text-gray-400 font-bold uppercase"><History size={10} className="inline mr-1" /> {log.date}</span>
                  <span className="text-[10px] text-primary font-bold"><Check size={10} className="inline mr-1" /> REF: {log.ref}</span>
                </div>
              </div>
            </div>
            <div className="text-right">
              <span className="text-[9px] font-bold bg-green-50 text-green-600 px-2 py-1 rounded border border-green-100 uppercase">Integridad Verificada</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
