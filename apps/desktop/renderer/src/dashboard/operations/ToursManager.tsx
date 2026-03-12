import React, { useEffect, useState } from 'react';
import { operationalService } from './operationalService';
import { Plus, Edit2, Trash2, MapPin, Clock, Users, Star } from 'lucide-react';
import { Card } from '../../components/Card';

export const ToursManager = () => {
  const [tours, setTours] = useState<any[]>([]);

  useEffect(() => {
    const fetchTours = async () => {
      try {
        const response = await operationalService.getTours();
        setTours(response.data || []);
      } catch (error) {
        setTours([
          { id: '1', name: 'Safari Río Meta', price: 120, duration: '4h', capacity: 10, status: 'Active', rating: 4.9 },
          { id: '2', name: 'Atardecer en Altillanura', price: 80, duration: '2h', capacity: 15, status: 'Active', rating: 4.8 },
        ]);
      }
    };
    fetchTours();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Catálogo de Experiencias</h2>
        <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 font-bold text-sm hover:bg-blue-900 transition shadow-sm">
          <Plus size={18} /> Crear Nuevo Tour
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {tours.map(tour => (
          <Card key={tour.id} className="p-0 overflow-hidden hover:shadow-md transition group">
            <div className="h-40 bg-gray-200 flex items-center justify-center text-gray-400 font-bold uppercase tracking-widest text-xs relative">
              Placeholder Imagen
              <div className="absolute top-3 right-3 bg-white/90 backdrop-blur px-2 py-1 rounded text-primary text-[10px] font-bold shadow-sm flex items-center gap-1">
                <Star size={10} className="fill-primary" /> {tour.rating}
              </div>
            </div>
            <div className="p-5">
              <h3 className="font-bold text-lg text-gray-800 group-hover:text-primary transition">{tour.name}</h3>
              <div className="flex items-center gap-4 mt-3 text-gray-500 text-xs font-medium">
                <div className="flex items-center gap-1"><Clock size={14} /> {tour.duration}</div>
                <div className="flex items-center gap-1"><Users size={14} /> máx {tour.capacity}</div>
              </div>
              <div className="mt-4 pt-4 border-t flex justify-between items-center">
                <p className="font-bold text-primary">${tour.price} USD</p>
                <div className="flex gap-2">
                  <button className="p-2 text-gray-400 hover:text-primary hover:bg-blue-50 rounded-lg transition"><Edit2 size={16} /></button>
                  <button className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition"><Trash2 size={16} /></button>
                </div>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
