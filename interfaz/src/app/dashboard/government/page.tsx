"use client";

import React, { useState, useEffect } from 'react';
import { governmentService } from '@/services/tripleViaService';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';

export default function GovernmentDashboard() {
  const [officials, setOfficials] = useState([]);

  useEffect(() => {
    governmentService.getOfficials().then(res => setOfficials(res.data.results || []));
  }, []);

  return (
    <div className="p-8 space-y-6">
      <h1 className="text-3xl font-black">Panel de Gobernanza Turística</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {officials.map((off: any) => (
          <Card key={off.id}>
            <CardHeader><CardTitle>{off.user_name}</CardTitle></CardHeader>
            <CardContent>
              <p className="text-sm text-slate-500">{off.cargo} - {off.nivel}</p>
            </CardContent>
          </Card>
        ))}
      </div>
      <Button className="bg-brand text-white font-black px-8 py-4 rounded-xl">Crear Nuevo Funcionario</Button>
    </div>
  );
}
