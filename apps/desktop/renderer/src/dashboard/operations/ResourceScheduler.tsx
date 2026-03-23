import React, { useEffect, useState } from 'react';
import { operationalService } from './operationalService';
import { Truck, Anchor, CheckCircle, AlertTriangle } from 'lucide-react';
import { Card } from '../../components/Card';

export const ResourceScheduler = () => {
  const [resources, setResources] = useState<any[]>([]);

  useEffect(() => {
    const fetchResources = async () => {
      try {
        const response = await operationalService.getResources();
        setResources(response.data || []);
      } catch (error) {
        setResources([
          { id: '1', name: 'Lancha El Pescador', type: 'Fluvial', cap: 12, status: 'Active' },
          { id: '2', name: '4x4 Safari Master', type: 'Terrestre', cap: 6, status: 'Maintenance' },
        ]);
      }
    };
    fetchResources();
  }, []);

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-bold text-gray-800">Programador de Recursos Físicos</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {resources.map(res => (
          <Card key={res.id} className="p-6 border-l-4" style={{ borderLeftColor: res.status === 'Active' ? '#10b981' : '#ef4444' }}>
            <div className="flex justify-between items-start">
              <div className="flex items-center gap-4">
                <div className={`p-3 rounded-lg ${res.type === 'Fluvial' ? 'bg-blue-100 text-blue-600' : 'bg-orange-100 text-orange-600'}`}>
                  {res.type === 'Fluvial' ? <Anchor size={20} /> : <Truck size={20} />}
                </div>
                <div>
                  <h3 className="font-bold text-gray-800">{res.name}</h3>
                  <p className="text-xs text-gray-400 font-medium">Capacidad: {res.cap} personas</p>
                </div>
              </div>
              <div className="text-right">
                {res.status === 'Active' ? (
                  <span className="text-green-600 flex items-center gap-1 text-xs font-bold uppercase tracking-tight"><CheckCircle size={14} /> Operativo</span>
                ) : (
                  <span className="text-red-500 flex items-center gap-1 text-xs font-bold uppercase tracking-tight"><AlertTriangle size={14} /> En Taller</span>
                )}
              </div>
            </div>

            <div className="mt-6 flex justify-between items-center text-sm border-t pt-4">
              <span className="text-gray-500 font-medium">Próximo Uso: Mañana 08:00 AM</span>
              <button className="text-primary font-bold hover:underline">Ver Agenda</button>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
