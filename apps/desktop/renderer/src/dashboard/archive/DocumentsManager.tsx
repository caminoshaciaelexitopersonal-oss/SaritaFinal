import React, { useEffect, useState } from 'react';
import { archiveService } from './archiveService';
import { Upload, Download, Trash2, Eye, MoreVertical, Filter, FileText } from 'lucide-react';

export const DocumentsManager = () => {
  const [documents, setDocuments] = useState<any[]>([]);
  const [search, setSearch] = useState('');
  const [selectedCat, setSelectedCat] = useState('Todas');

  useEffect(() => {
    const fetchDocs = async () => {
      try {
        const response = await archiveService.getDocuments();
        setDocuments(response.data || []);
      } catch (error) {
        setDocuments([
          { id: '1', name: 'Contrato_Socio_V1.pdf', cat: 'Legal', size: '2.4 MB', owner: 'Admin SARITA', date: '2026-03-07' },
          { id: '2', name: 'Factura_Amazon_AWS.pdf', cat: 'Contable', size: '450 KB', owner: 'Contador Pro', date: '2026-03-05' },
          { id: '3', name: 'Manual_Operativo.docx', cat: 'Operativo', size: '1.8 MB', owner: 'Gerente Ops', date: '2026-03-01' },
        ]);
      }
    };
    fetchDocs();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h2 className="text-xl font-bold text-gray-800">Explorador de Archivos</h2>
        <div className="flex gap-4">
          <div className="relative w-64">
            <Search className="absolute left-3 top-2.5 text-gray-400" size={18} />
            <input
              type="text"
              placeholder="Buscar por nombre..."
              className="w-full pl-10 pr-4 py-2 border rounded-lg outline-none text-sm"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>
          <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-blue-900 transition text-sm font-bold shadow-sm">
            <Upload size={18} /> Subir Documento
          </button>
        </div>
      </div>

      <table className="w-full text-left">
        <thead className="bg-gray-50 text-gray-500 text-xs uppercase font-bold">
          <tr>
            <th className="px-6 py-4">Nombre del Archivo</th>
            <th className="px-6 py-4">Categoría</th>
            <th className="px-6 py-4">Tamaño</th>
            <th className="px-6 py-4">Subido por</th>
            <th className="px-6 py-4 text-right">Acciones</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100 text-sm">
          {documents.map(doc => (
            <tr key={doc.id} className="hover:bg-gray-50/80 transition group">
              <td className="px-6 py-4 flex items-center gap-3">
                <div className="p-2 bg-blue-50 text-primary rounded"><FileText size={18} /></div>
                <div>
                  <p className="font-bold text-gray-800 group-hover:text-primary transition cursor-pointer">{doc.name}</p>
                  <p className="text-[10px] text-gray-400">Fecha: {doc.date}</p>
                </div>
              </td>
              <td className="px-6 py-4">
                <span className="px-2 py-1 bg-gray-100 rounded text-gray-600 text-xs font-medium">{doc.cat}</span>
              </td>
              <td className="px-6 py-4 text-gray-500">{doc.size}</td>
              <td className="px-6 py-4 text-gray-500">{doc.owner}</td>
              <td className="px-6 py-4 text-right">
                <div className="flex justify-end gap-1 opacity-0 group-hover:opacity-100 transition">
                  <button className="p-2 text-gray-400 hover:text-primary rounded-lg hover:bg-white border border-transparent hover:border-gray-200"><Eye size={16} /></button>
                  <button className="p-2 text-gray-400 hover:text-primary rounded-lg hover:bg-white border border-transparent hover:border-gray-200"><Download size={16} /></button>
                  <button className="p-2 text-gray-400 hover:text-red-600 rounded-lg hover:bg-white border border-transparent hover:border-gray-200"><Trash2 size={16} /></button>
                  <button className="p-2 text-gray-400 hover:text-gray-600 rounded-lg hover:bg-white border border-transparent hover:border-gray-200"><MoreVertical size={16} /></button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
