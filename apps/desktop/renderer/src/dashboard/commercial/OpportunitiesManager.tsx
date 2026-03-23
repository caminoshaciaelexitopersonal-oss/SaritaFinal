import React, { useEffect, useState } from 'react';
import { commercialService } from './commercialService';
import { Plus, Target, Clock, CheckCircle } from 'lucide-react';

export const OpportunitiesManager = () => {
  const [opps, setOpps] = useState<any[]>([]);

  useEffect(() => {
    const fetchOpps = async () => {
      try {
        const response = await commercialService.getOpportunities();
        setOpps(response.data || []);
      } catch (error) {
        setOpps([
          { id: '1', customer: 'Andrés V.', service: 'Safari Río Yucao', status: 'En Negociación', value: 450, prob: 70 },
          { id: '2', customer: 'Familia Perez', service: 'Cena Lanchas', status: 'Propuesta Enviada', value: 200, prob: 40 },
        ]);
      }
    };
    fetchOpps();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Embudo de Oportunidades</h2>
        <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 font-bold hover:bg-blue-900 transition">
          <Plus size={18} /> Nueva Oportunidad
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {['Nuevo Contacto', 'En Negociación', 'Cerrado'].map(col => (
          <div key={col} className="bg-gray-50 p-4 rounded-xl border-t-4 border-primary">
            <h3 className="font-bold text-gray-700 mb-4 flex items-center justify-between">
              {col}
              <span className="bg-gray-200 text-gray-600 px-2 py-1 rounded text-xs">
                {opps.filter(o => o.status === col || (col === 'Cerrado' && o.status === 'Propuesta Enviada')).length}
              </span>
            </h3>
            <div className="space-y-4">
              {opps.map(o => (o.status === col || (col === 'Cerrado' && o.status === 'Propuesta Enviada')) && (
                <div key={o.id} className="bg-white p-4 rounded-lg shadow-sm border border-gray-100">
                  <div className="flex justify-between items-start mb-2">
                    <p className="font-bold text-sm">{o.customer}</p>
                    <span className="text-xs text-green-600 font-bold">${o.value} USD</span>
                  </div>
                  <p className="text-xs text-gray-500 mb-3">{o.service}</p>
                  <div className="w-full bg-gray-100 h-1.5 rounded-full">
                    <div className="bg-secondary h-full rounded-full" style={{ width: `${o.prob}%` }} />
                  </div>
                  <p className="text-[10px] text-gray-400 mt-2 text-right">Probabilidad: {o.prob}%</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
