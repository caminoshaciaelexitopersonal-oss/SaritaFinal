
'use client';

import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export default function AdminPlataformaPage() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Panel de Administración de la Plataforma</CardTitle>
      </CardHeader>
      <CardContent>
        <p>
          Bienvenido al nuevo panel de administración. Este es el punto de partida
          para la gestión centralizada del sistema Sarita.
        </p>
        <p className="mt-4 text-sm text-gray-600">
          Las funcionalidades futuras, como la gestión de planes, la supervisión
          financiera y la configuración del sitio, se construirán aquí.
        </p>
      </CardContent>
    </Card>
  );
}
