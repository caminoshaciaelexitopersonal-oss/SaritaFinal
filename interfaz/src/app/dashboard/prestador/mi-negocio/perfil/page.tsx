'use client';

import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';

export default function PerfilPrestadorPage() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Perfil del Prestador</h1>
      <Card>
        <CardHeader><CardTitle>Datos de Empresa</CardTitle></CardHeader>
        <CardContent>
           <p className="text-slate-500 italic">Módulo de integración con /api/v1/turismo/business-profiles/</p>
        </CardContent>
      </Card>
    </div>
  );
}
