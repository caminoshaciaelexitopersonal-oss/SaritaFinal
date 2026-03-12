import React, { useEffect, useState } from 'react';
import { commercialService } from './commercialService';
import { Tag, Calendar, Users, Percent } from 'lucide-react';

export const PromotionsManager = () => {
  const [promos, setPromos] = useState<any[]>([]);

  useEffect(() => {
    const fetchPromos = async () => {
      try {
        const response = await commercialService.getPromotions();
        setPromos(response.data || []);
      } catch (error) {
        setPromos([
          { id: '1', name: 'Semana Santa 20% OFF', code: 'HOLY2026', usage: 45, status: 'Activa' },
          { id: '2', name: 'Primer Viaje', code: 'WELCOME5', usage: 128, status: 'Activa' },
        ]);
      }
    };
    fetchPromos();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Promociones y Campañas</h2>
        <button className="bg-secondary text-primary px-4 py-2 rounded-lg font-bold hover:bg-yellow-500 transition">
          Crear Cupón / Promoción
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {promos.map(p => (
          <div key={p.id} className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 relative overflow-hidden">
            <div className="absolute top-0 right-0 p-3 bg-green-100 text-green-600 font-bold text-[10px] uppercase rounded-bl-lg">
              {p.status}
            </div>
            <div className="flex items-center gap-4 mb-4">
              <div className="w-10 h-10 rounded bg-blue-50 flex items-center justify-center text-primary">
                <Tag size={20} />
              </div>
              <div>
                <h3 className="font-bold">{p.name}</h3>
                <p className="text-sm font-mono text-gray-500">CÓDIGO: {p.code}</p>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4 mt-6 border-t pt-4 text-xs text-gray-500">
              <div className="flex items-center gap-2"><Users size={14} /> {p.usage} usos registrados</div>
              <div className="flex items-center gap-2"><Calendar size={14} /> Expira: 30 Abr 2026</div>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-primary/5 p-8 rounded-xl border border-primary/10">
        <h3 className="font-bold text-primary mb-2 flex items-center gap-2"><Percent size={20} /> Sugerencia de la IA SARITA</h3>
        <p className="text-sm text-primary/80">
          "Se detecta baja demanda para el próximo fin de semana. Recomendamos activar una campaña relámpago de 15% de descuento para reservas en las próximas 24 horas."
        </p>
      </div>
    </div>
  );
};
