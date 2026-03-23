import React, { useState } from 'react';
import { Card, Button, Text, Input } from '@/components';
import { FileStack, Search, Plus } from 'lucide-react';

export const DocumentLibrary = () => {
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <Text variant="headingL">Biblioteca Documental</Text>
        <Button label="Subir Documento" />
      </div>

      <div className="relative">
        <div className="absolute inset-y-0 left-3 flex items-center pointer-events-none">
          <Search size={18} className="text-gray-400" />
        </div>
        <input
          type="text"
          className="w-full pl-10 pr-4 py-3 bg-white border rounded-xl"
          placeholder="Buscar facturas, resoluciones, certificados..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <div className="flex items-start gap-4">
            <div className="p-3 bg-blue-50 text-blue-600 rounded-lg">
              <FileStack size={24} />
            </div>
            <div>
              <Text variant="headingM">RNT Vigente</Text>
              <Text variant="small" color="textSecondary">Expira: 31 Dic 2026</Text>
              <div className="mt-4 flex gap-2">
                <Button label="Ver" variant="ghost" />
                <Button label="Actualizar" variant="ghost" />
              </div>
            </div>
          </div>
        </Card>

        {/* Placeholder for more docs */}
      </div>
    </div>
  );
};
