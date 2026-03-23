import React, { useEffect, useState } from 'react';
import { archiveService } from './archiveService';
import { FileText, Folder, HardDrive, Clock, Search } from 'lucide-react';

export const ArchiveDashboard = () => {
  const [metrics, setMetrics] = useState<any>({ total_docs: 0, storage_used: '0 GB' });

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await archiveService.getStorageMetrics();
        setMetrics(response.data);
      } catch (error) {
        setMetrics({ total_docs: 154, storage_used: '1.2 GB' });
      }
    };
    fetchMetrics();
  }, []);

  const integrationAlerts = [
    { title: 'Factura de Venta Archivada', desc: 'Se ha guardado automáticamente la factura de la Venta S-101.', type: 'Comercial', icon: '🛒' },
    { title: 'Contrato Laboral Actualizado', desc: 'Nueva versión 2.0 disponible para revisión.', type: 'Administrativo', icon: '📄' },
  ];

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Archivo Digital Empresarial</h2>
        <div className="relative w-64">
          <Search className="absolute left-3 top-2.5 text-gray-400" size={18} />
          <input type="text" placeholder="Buscar en documentos..." className="w-full pl-10 pr-4 py-2 border rounded-lg outline-none text-sm" />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
          <div className="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-primary">
            <FileText size={24} />
          </div>
          <div>
            <p className="text-gray-500 text-xs font-bold uppercase">Total Documentos</p>
            <p className="text-2xl font-bold">{metrics.total_docs}</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
          <div className="w-12 h-12 rounded-lg bg-green-100 flex items-center justify-center text-green-600">
            <HardDrive size={24} />
          </div>
          <div>
            <p className="text-gray-500 text-xs font-bold uppercase">Espacio Utilizado</p>
            <p className="text-2xl font-bold">{metrics.storage_used}</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
          <div className="w-12 h-12 rounded-lg bg-purple-100 flex items-center justify-center text-purple-600">
            <Folder size={24} />
          </div>
          <div>
            <p className="text-gray-500 text-xs font-bold uppercase">Categorías</p>
            <p className="text-2xl font-bold">6</p>
          </div>
        </div>
      </div>

      <div className="bg-primary/5 p-6 rounded-xl border border-primary/10">
        <h3 className="text-sm font-bold text-primary uppercase tracking-widest mb-4 px-2">Integración Sistémica SARITA</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {integrationAlerts.map(alert => (
            <div key={alert.title} className="flex items-center gap-4 bg-white p-4 rounded-lg shadow-sm border border-primary/5">
              <span className="text-2xl">{alert.icon}</span>
              <div>
                <p className="text-xs font-bold text-primary">{alert.type}</p>
                <p className="text-sm font-bold text-gray-800">{alert.title}</p>
                <p className="text-[10px] text-gray-500 mt-0.5">{alert.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6 flex items-center gap-2"><Clock size={20} /> Documentos Recientes</h3>
          <div className="space-y-4">
            {[
              { name: 'Factura_FE-2026-001.pdf', cat: 'Contable', date: 'Hace 10 min' },
              { name: 'Contrato_Guía_Llanero.docx', cat: 'Legal', date: 'Hace 2h' },
              { name: 'Reporte_Mensual_Marzo.xlsx', cat: 'Administrativo', date: 'Ayer' },
            ].map((doc, i) => (
              <div key={i} className="flex justify-between items-center p-3 hover:bg-gray-50 rounded-lg transition border border-transparent hover:border-gray-200">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-gray-100 rounded text-gray-500"><FileText size={16} /></div>
                  <div>
                    <p className="text-sm font-bold text-gray-800">{doc.name}</p>
                    <p className="text-[10px] text-primary uppercase font-bold">{doc.cat}</p>
                  </div>
                </div>
                <span className="text-[10px] text-gray-400 font-medium">{doc.date}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6 flex items-center gap-2"><Folder size={20} /> Distribución por Categoría</h3>
          <div className="space-y-4">
            {[
              { name: 'Legal', count: 42, color: 'bg-blue-500' },
              { name: 'Contable', count: 85, color: 'bg-green-500' },
              { name: 'Administrativo', count: 27, color: 'bg-purple-500' },
            ].map(cat => (
              <div key={cat.name}>
                <div className="flex justify-between text-sm mb-1 font-medium">
                  <span className="text-gray-600">{cat.name}</span>
                  <span className="text-gray-400">{cat.count} archivos</span>
                </div>
                <div className="h-2 w-full bg-gray-100 rounded-full overflow-hidden">
                  <div className={`h-full ${cat.color}`} style={{ width: `${(cat.count/154)*100}%` }} />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
