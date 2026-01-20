
'use client';

import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export default function AdminGestionComercialPage() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Gestión Comercial de la Plataforma</CardTitle>
      </CardHeader>
      <CardContent>
        <p>
          Este es el módulo de Gestión Comercial para la plataforma Sarita.
        </p>
        <ul className="list-disc pl-5 mt-4 space-y-2 text-sm text-gray-700">
          <li>Gestión de Planes y Suscripciones</li>
          <li>Facturación a Clientes (Entes y Prestadores)</li>
          <li>Campañas de Marketing</li>
          <li>Gestión de Contratos</li>
        </ul>
      </CardContent>
    </Card>
  );
}
