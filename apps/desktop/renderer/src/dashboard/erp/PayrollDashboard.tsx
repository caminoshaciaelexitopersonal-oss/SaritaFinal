import React, { useState, useEffect } from 'react';
import { Card, Button, Text, StatCard } from '@/components';
import { erpService } from '@/services/erpService';

export const PayrollDashboard = () => {
  const [runs, setRuns] = useState<any[]>([]);

  useEffect(() => {
    erpService.getPayrollRuns().then(res => setRuns(res.data));
  }, []);

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <Text variant="headingL">Nómina y Compensación</Text>
        <Button label="Liquidar Periodo" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <StatCard title="Total Pagado (Mes)" value="$12,450,000" trend="+2%" trendDirection="up" />
        <StatCard title="Empleados en Nómina" value="8" />
        <StatCard title="Próximo Vencimiento" value="30 Mar 2026" />
      </div>

      <Card>
        <Text variant="headingM" className="mb-4">Historial de Pagos</Text>
        <div className="space-y-3">
          {runs.map(run => (
            <div key={run.id} className="flex justify-between items-center p-4 border rounded-lg">
              <div>
                <p className="font-bold">Periodo: {run.period_name}</p>
                <p className="text-sm text-gray-500">Fecha: {run.execution_date}</p>
              </div>
              <div className="text-right">
                <p className="font-bold text-primary">${run.total_amount}</p>
                <Button label="Descargar PDF" variant="ghost" />
              </div>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};
