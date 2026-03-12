import React from 'react';
import { Card, Text } from '@/components';
import { Archive, Folder, File, ChevronRight } from 'lucide-react';
import { spacing } from '@/tokens/spacing';

export const ArchiveExplorer = () => {
  const folders = [
    { name: 'Talento Humano', items: 12 },
    { name: 'Contratos Legales', items: 5 },
    { name: 'Contabilidad y Finanzas', items: 45 },
    { name: 'Certificaciones Municipales', items: 3 },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <Archive size={32} className="text-primary" />
        <Text variant="headingL">Acervo Archivístico</Text>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {folders.map(folder => (
          <Card key={folder.name} padding="md">
            <div className="flex justify-between items-center cursor-pointer hover:opacity-80">
              <div className="flex items-center gap-4">
                <Folder size={28} className="text-yellow-500 fill-yellow-100" />
                <div>
                  <Text variant="body">{folder.name}</Text>
                  <Text variant="small" color="textSecondary">{folder.items} elementos</Text>
                </div>
              </div>
              <ChevronRight size={20} className="text-gray-400" />
            </div>
          </Card>
        ))}
      </div>

      <div className="mt-10">
        <Text variant="headingM" className="mb-4">Actividad Reciente</Text>
        <Card>
          <div className="space-y-4">
            <div className="flex items-center gap-3 p-2">
              <File size={16} className="text-blue-500" />
              <Text variant="caption">Actualización de RNT - 2 horas atrás</Text>
            </div>
            <div className="flex items-center gap-3 p-2 border-t">
              <File size={16} className="text-green-500" />
              <Text variant="caption">Contrato firmado: Guía Nocturno - Ayer</Text>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
};
