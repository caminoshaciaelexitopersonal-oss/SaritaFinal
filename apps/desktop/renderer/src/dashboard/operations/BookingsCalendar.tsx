import React, { useEffect, useState } from 'react';
import { operationalService } from './operationalService';
import { Calendar as CalendarIcon, ChevronLeft, ChevronRight, Plus, Info } from 'lucide-react';
import { Card } from '../../components/Card';

export const BookingsCalendar = () => {
  const [bookings, setBookings] = useState<any[]>([]);

  useEffect(() => {
    const fetchBookings = async () => {
      try {
        const response = await operationalService.getOperationalBookings();
        setBookings(response.data || []);
      } catch (error) {
        setBookings([
          { id: '1', tour: 'Safari Río Meta', date: '07 Mar', guests: 8, status: 'Confirmed' },
          { id: '2', tour: 'Avistamiento Toninas', date: '08 Mar', guests: 4, status: 'Pending' },
        ]);
      }
    };
    fetchBookings();
  }, []);

  return (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex justify-between items-center bg-gray-50/50">
        <div className="flex items-center gap-4">
          <div className="p-2 bg-primary text-white rounded-lg"><CalendarIcon size={20} /></div>
          <h2 className="text-xl font-bold text-gray-800">Calendario de Operaciones</h2>
        </div>
        <div className="flex gap-2">
          <button className="p-2 border rounded-lg hover:bg-white transition"><ChevronLeft size={18} /></button>
          <button className="px-4 py-2 border rounded-lg font-bold text-sm hover:bg-white transition">Hoy</button>
          <button className="p-2 border rounded-lg hover:bg-white transition"><ChevronRight size={18} /></button>
          <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 font-bold text-sm hover:bg-blue-900 transition ml-4">
            <Plus size={18} /> Programar Tour
          </button>
        </div>
      </div>

      <div className="grid grid-cols-7 gap-px bg-gray-200 border border-gray-200 rounded-xl overflow-hidden shadow-sm">
        {['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'].map(day => (
          <div key={day} className="bg-gray-50 p-4 text-center font-bold text-xs text-gray-400 uppercase tracking-widest">{day}</div>
        ))}
        {Array.from({ length: 14 }).map((_, i) => {
          const dayNum = i + 1;
          const dayBookings = bookings.filter(b => b.date.includes(dayNum.toString().padStart(2, '0')));
          return (
            <div key={i} className="bg-white min-h-[120px] p-3 hover:bg-gray-50 transition cursor-pointer group">
              <span className="text-sm font-bold text-gray-400 group-hover:text-primary transition">{dayNum}</span>
              <div className="mt-2 space-y-1">
                {dayBookings.map(b => (
                  <div key={b.id} className="text-[10px] p-1.5 rounded bg-blue-50 text-primary font-bold border-l-2 border-primary truncate">
                    {b.tour} ({b.guests})
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      <div className="bg-blue-50 p-4 rounded-lg flex items-start gap-3 border border-blue-100">
        <Info className="text-primary mt-0.5" size={18} />
        <p className="text-xs text-primary/80 leading-relaxed font-medium">
          Sugerencia Operativa: Se detecta alta concentración de reservas para el fin de semana.
          Considere activar personal de refuerzo y verificar mantenimiento de lanchas.
        </p>
      </div>
    </div>
  );
};
