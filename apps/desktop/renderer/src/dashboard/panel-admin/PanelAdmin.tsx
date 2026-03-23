import React, { useEffect, useState } from 'react';
import { governanceService } from '../../services/governanceService';
import { Card } from '../../components/Card';

export const PanelAdmin = () => {
  const [officials, setOfficials] = useState([]);

  useEffect(() => {
    governanceService.getOfficials()
      .then(res => setOfficials(res.data.results || []))
      .catch(console.error);
  }, []);

  return (
    <div className="p-8 space-y-8 bg-slate-50 min-h-screen">
      <div className="flex justify-between items-center">
        <div>
           <h1 className="text-3xl font-black text-slate-900 uppercase tracking-tighter italic">Terminal de Control Regional</h1>
           <p className="text-slate-500 font-medium">Gobernanza Turística Certificada - SARITA Desktop</p>
        </div>
        <div className="flex gap-4">
           <div className="px-6 py-3 bg-brand-dark text-white rounded-lg font-black text-xs uppercase tracking-widest">Sincronizado</div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
         <Card className="p-6 border-l-4 border-l-indigo-500">
            <p className="text-xs font-bold text-slate-400 uppercase">Funcionarios</p>
            <p className="text-3xl font-black text-slate-800">{officials.length}</p>
         </Card>
         <Card className="p-6 border-l-4 border-l-emerald-500">
            <p className="text-xs font-bold text-slate-400 uppercase">Solicitudes</p>
            <p className="text-3xl font-black text-slate-800">0</p>
         </Card>
      </div>

      <div className="bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-200">
        <table className="w-full text-left">
          <thead className="bg-slate-900 text-white text-xs uppercase tracking-widest font-black">
            <tr>
              <th className="p-4">Funcionario</th>
              <th className="p-4">Cargo</th>
              <th className="p-4">Nivel</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 font-bold text-slate-700">
            {officials.map((off: any) => (
              <tr key={off.id} className="hover:bg-slate-50">
                <td className="p-4">{off.user_name}</td>
                <td className="p-4 text-xs">{off.cargo}</td>
                <td className="p-4">
                   <span className="bg-slate-200 px-2 py-1 rounded text-[10px] uppercase">{off.nivel}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {officials.length === 0 && (
           <div className="p-10 text-center text-slate-400 italic">No se detectan funcionarios en el nodo local.</div>
        )}
      </div>
    </div>
  );
}

// Keep export for compatibility if needed
export const PanelAdminStub = PanelAdmin;
