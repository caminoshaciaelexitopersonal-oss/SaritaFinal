import React, { useEffect, useState } from 'react';
import { operationalService } from './operationalService';
import { UserCheck, Shield, Phone, Star, MoreVertical } from 'lucide-react';
import { Card } from '../../components/Card';

export const StaffManager = () => {
  const [staff, setStaff] = useState<any[]>([]);

  useEffect(() => {
    const fetchStaff = async () => {
      try {
        const response = await operationalService.getStaff();
        setStaff(response.data || []);
      } catch (error) {
        console.error('Error loading staff:', error);
        setStaff([]);
      }
    };
    fetchStaff();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <div className="flex items-center gap-3">
          <Shield className="text-primary" size={24} />
          <h2 className="text-xl font-bold text-gray-800">Gestión de Personal</h2>
        </div>
        <button className="bg-primary text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-blue-900 transition">
          Agregar Personal
        </button>
      </div>

      <div className="divide-y divide-gray-100">
        {staff.map(member => (
          <div key={member.id} className="p-6 flex items-center justify-between hover:bg-gray-50 transition group">
            <div className="flex items-center gap-4">
              <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-primary font-bold">
                {member.name.charAt(0)}
              </div>
              <div>
                <p className="font-bold text-gray-800">{member.name}</p>
                <p className="text-xs text-gray-500 font-medium">{member.role}</p>
              </div>
            </div>

            <div className="flex items-center gap-8">
              <div className="text-center">
                <p className="text-[10px] text-gray-400 font-bold uppercase mb-1">Estatus</p>
                <span className={`px-3 py-1 rounded-full text-[10px] font-bold ${member.status === 'Disponible' ? 'bg-green-100 text-green-600' : 'bg-blue-100 text-blue-600'}`}>
                  {member.status}
                </span>
              </div>
              <div className="text-center">
                <p className="text-[10px] text-gray-400 font-bold uppercase mb-1">Rating</p>
                <div className="flex items-center gap-1 text-xs font-bold text-gray-700">
                  <Star size={12} className="fill-yellow-400 text-yellow-400" /> {member.rating}
                </div>
              </div>
              <button className="p-2 text-gray-300 hover:text-gray-600 transition"><MoreVertical size={20} /></button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
