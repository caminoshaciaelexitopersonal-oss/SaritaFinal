import React, { useEffect, useState } from 'react';
import { archiveService } from './archiveService';
import { FolderPlus, Settings, MoreVertical, FileText } from 'lucide-react';

export const DocumentCategoriesManager = () => {
  const [categories, setCategories] = useState<any[]>([]);

  useEffect(() => {
    const fetchCats = async () => {
      try {
        const response = await archiveService.getCategories();
        setCategories(response.data || []);
      } catch (error) {
        setCategories([
          { id: '1', name: 'Legal', count: 42, color: '#3b82f6' },
          { id: '2', name: 'Contable', count: 85, color: '#10b981' },
          { id: '3', name: 'Administrativo', count: 27, color: '#8b5cf6' },
          { id: '4', name: 'Operativo', count: 18, color: '#f59e0b' },
        ]);
      }
    };
    fetchCats();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h2 className="text-xl font-bold text-gray-800">Categorías Archivísticas</h2>
        <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-blue-900 transition text-sm font-bold shadow-sm">
          <FolderPlus size={18} /> Nueva Categoría
        </button>
      </div>

      <div className="p-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {categories.map(cat => (
          <div key={cat.id} className="p-6 border rounded-xl hover:shadow-md transition cursor-pointer group relative">
            <div className="w-10 h-10 rounded-lg mb-4 flex items-center justify-center" style={{ backgroundColor: `${cat.color}20`, color: cat.color }}>
              <FileText size={20} />
            </div>
            <h3 className="font-bold text-gray-800">{cat.name}</h3>
            <p className="text-xs text-gray-500 mt-1">{cat.count} documentos archivados</p>
            <button className="absolute top-4 right-4 text-gray-400 opacity-0 group-hover:opacity-100 transition">
              <MoreVertical size={16} />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
