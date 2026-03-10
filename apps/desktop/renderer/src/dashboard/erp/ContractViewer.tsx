import React from 'react';
import { Card, Button, Text } from '@/components';
import { Signature } from 'lucide-react';

export const ContractViewer = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <Text variant="headingL">Gestión de Contratos</Text>
        <Button label="Nuevo Contrato" />
      </div>

      <div className="space-y-4">
        {[1, 2, 3].map(i => (
          <Card key={i} padding="md">
            <div className="flex justify-between items-center">
              <div className="flex items-center gap-4">
                <Signature size={24} className="text-gray-400" />
                <div>
                  <Text variant="body">Contrato Laboral - Juan Pérez</Text>
                  <Text variant="small" color="textSecondary">Firmado el 15 Ene 2026</Text>
                </div>
              </div>
              <div className="flex gap-2">
                <Button label="Descargar" variant="ghost" />
                <Button label="Historial" variant="ghost" />
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
