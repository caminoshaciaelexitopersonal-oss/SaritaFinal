import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Landmark, ArrowRightLeft, CheckCircle2, XCircle, RefreshCw } from 'lucide-react';

export const ReconciliationManager = () => {
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    setData([
      { id: '1', source: 'Wallet SARITA', amount: 120.00, journal_amount: 120.00, status: 'Matched' },
      { id: '2', source: 'Venta Directa #920', amount: 45.50, journal_amount: 41.00, status: 'Mismatch' },
    ]);
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Conciliación Contable</h2>
        <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-bold shadow-sm">
          <RefreshCw size={18} /> Ejecutar Conciliación
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {data.map(item => (
          <div key={item.id} className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
            <div className="flex justify-between items-start mb-4">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-blue-50 text-primary rounded-lg"><Landmark size={20} /></div>
                <h3 className="font-bold text-gray-800">{item.source}</h3>
              </div>
              {item.status === 'Matched' ? (
                <span className="text-green-600 flex items-center gap-1 text-[10px] font-bold"><CheckCircle2 size={14} /> CONCILIADO</span>
              ) : (
                <span className="text-red-500 flex items-center gap-1 text-[10px] font-bold"><XCircle size={14} /> DIFERENCIA</span>
              )}
            </div>

            <div className="flex justify-between items-center mt-6 py-4 border-t border-dashed">
              <div className="text-center flex-1">
                <p className="text-[10px] text-gray-400 font-bold uppercase">Monto Real</p>
                <p className="font-bold text-gray-800">${item.amount.toFixed(2)}</p>
              </div>
              <ArrowRightLeft className="text-gray-300" size={16} />
              <div className="text-center flex-1">
                <p className="text-[10px] text-gray-400 font-bold uppercase">Monto Contable</p>
                <p className="font-bold text-gray-800">${item.journal_amount.toFixed(2)}</p>
              </div>
            </div>

            {item.status === 'Mismatch' && (
              <div className="mt-4 p-3 bg-red-50 rounded text-[11px] text-red-700 font-medium italic">
                Faltan $4.50 USD en el registro contable. Posible comisión no registrada.
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};
