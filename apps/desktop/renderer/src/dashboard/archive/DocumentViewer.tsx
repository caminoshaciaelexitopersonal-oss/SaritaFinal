import React from 'react';
import { X, Download, Share2, Printer } from 'lucide-react';

export const DocumentViewer = ({ onClose, docName }: any) => {
  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-10">
      <div className="bg-white rounded-2xl w-full max-w-5xl h-full flex flex-col shadow-2xl overflow-hidden">
        <header className="p-4 bg-gray-900 text-white flex justify-between items-center">
          <div className="flex items-center gap-3">
            <h3 className="font-bold">{docName || 'Visualizador de Documentos'}</h3>
            <span className="text-xs bg-primary px-2 py-0.5 rounded">PDF</span>
          </div>
          <div className="flex items-center gap-4">
            <button className="p-2 hover:bg-gray-800 rounded-lg transition"><Download size={20} /></button>
            <button className="p-2 hover:bg-gray-800 rounded-lg transition"><Printer size={20} /></button>
            <button className="p-2 hover:bg-gray-800 rounded-lg transition"><Share2 size={20} /></button>
            <div className="w-px h-6 bg-gray-700 mx-2" />
            <button onClick={onClose} className="p-2 hover:bg-red-500 rounded-lg transition"><X size={20} /></button>
          </div>
        </header>

        <div className="flex-1 bg-gray-200 flex items-center justify-center p-10 overflow-auto">
          <div className="bg-white w-full max-w-[800px] h-[1100px] shadow-lg p-12 flex flex-col gap-10">
            <div className="h-20 bg-gray-100 rounded-lg w-1/3" />
            <div className="space-y-4">
              <div className="h-4 bg-gray-100 rounded w-full" />
              <div className="h-4 bg-gray-100 rounded w-full" />
              <div className="h-4 bg-gray-100 rounded w-4/5" />
            </div>
            <div className="grid grid-cols-2 gap-8 mt-20">
              <div className="h-32 bg-gray-50 rounded-lg" />
              <div className="h-32 bg-gray-50 rounded-lg" />
            </div>
            <div className="mt-auto flex justify-center text-gray-300 text-xs uppercase tracking-widest font-bold">
              SARITA ARCHIVE SYSTEM - PREVIEW MODE
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
