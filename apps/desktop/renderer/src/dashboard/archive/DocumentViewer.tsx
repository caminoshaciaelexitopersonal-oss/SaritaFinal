import React, { useState } from 'react';
import { X, Download, Share2, Printer, ZoomIn, ZoomOut, RotateCw } from 'lucide-react';

export const DocumentViewer = ({ onClose, docName }: any) => {
  const [zoom, setZoom] = useState(100);
  const [rotation, setRotation] = useState(0);

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center z-50 p-10">
      <div className="bg-white rounded-2xl w-full max-w-6xl h-full flex flex-col shadow-2xl overflow-hidden">
        <header className="p-4 bg-gray-900 text-white flex justify-between items-center px-8">
          <div className="flex items-center gap-3">
            <h3 className="font-bold text-lg">{docName || 'Visualizador de Documentos'}</h3>
            <span className="text-[10px] bg-primary px-2 py-0.5 rounded font-bold">PDF SECURE</span>
          </div>

          <div className="flex items-center gap-2 bg-gray-800 rounded-lg p-1 px-4">
            <button onClick={() => setZoom(z => Math.max(50, z - 10))} className="p-2 hover:text-primary transition"><ZoomOut size={18} /></button>
            <span className="text-xs font-mono w-12 text-center">{zoom}%</span>
            <button onClick={() => setZoom(z => Math.min(200, z + 10))} className="p-2 hover:text-primary transition"><ZoomIn size={18} /></button>
            <div className="w-px h-4 bg-gray-700 mx-2" />
            <button onClick={() => setRotation(r => (r + 90) % 360)} className="p-2 hover:text-primary transition"><RotateCw size={18} /></button>
          </div>

          <div className="flex items-center gap-4">
            <button className="p-2 hover:bg-gray-800 rounded-lg transition"><Download size={20} /></button>
            <button className="p-2 hover:bg-gray-800 rounded-lg transition"><Printer size={20} /></button>
            <div className="w-px h-6 bg-gray-700 mx-2" />
            <button onClick={onClose} className="p-2 hover:bg-red-500 rounded-lg transition"><X size={20} /></button>
          </div>
        </header>

        <div className="flex-1 bg-gray-100 flex items-center justify-center p-10 overflow-auto scrollbar-hide">
          <div
            className="bg-white shadow-2xl transition-all duration-300 transform origin-center"
            style={{
              width: `${zoom * 8}px`,
              height: `${zoom * 11}px`,
              transform: `rotate(${rotation}deg)`,
              padding: '60px'
            }}
          >
            {/* Simulación de Contenido del Documento */}
            <div className="flex justify-between items-start mb-20">
              <div className="w-32 h-12 bg-gray-100 rounded" />
              <div className="text-right">
                <p className="text-xs font-bold text-gray-400 uppercase">Documento Oficial</p>
                <p className="text-sm font-bold text-gray-800">SARITA-2026-ARCHIVE</p>
              </div>
            </div>

            <div className="space-y-6">
              <div className="h-6 bg-gray-50 rounded w-full" />
              <div className="h-6 bg-gray-50 rounded w-full" />
              <div className="h-6 bg-gray-50 rounded w-3/4" />
            </div>

            <div className="mt-40 grid grid-cols-2 gap-20">
              <div className="space-y-4">
                <div className="h-40 bg-gray-50 rounded-lg border border-dashed border-gray-200" />
                <p className="text-center text-[10px] text-gray-300 font-bold uppercase">Sello Digital RS256</p>
              </div>
              <div className="space-y-4">
                <div className="h-40 bg-gray-50 rounded-lg border border-dashed border-gray-200" />
                <p className="text-center text-[10px] text-gray-300 font-bold uppercase">Firma del Prestador</p>
              </div>
            </div>

            <div className="mt-auto pt-20 border-t border-gray-100 flex justify-center italic text-gray-300 text-[10px]">
              Este documento ha sido generado y custodiado por el Sistema de Gestión Archivística de SARITA.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
