import React from 'react';
import { AlertCircle, ShieldAlert, CheckCircle } from 'lucide-react';

export const FinancialAlerts = ({ ratios }: { ratios: any }) => {
  const alerts = [];

  if (ratios?.liquidez?.value < 1.2) {
    alerts.push({
      type: 'critical',
      title: 'Riesgo de Liquidez',
      message: 'El ratio de liquidez está por debajo del nivel óptimo. Considere revisar las cuentas por pagar.',
      icon: ShieldAlert
    });
  }

  if (ratios?.rentabilidad?.value < 0.1) {
    alerts.push({
      type: 'warning',
      title: 'Rentabilidad Ajustada',
      message: 'El margen neto del periodo es menor al 10%. Revise los costos operativos.',
      icon: AlertCircle
    });
  }

  if (alerts.length === 0) {
    return (
      <div className="bg-green-50 border border-green-200 p-4 rounded-lg flex items-center gap-3 text-green-700">
        <CheckCircle size={20} />
        <span className="text-sm font-bold uppercase tracking-wider">Estado Financiero: Saludable</span>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {alerts.map((alert, idx) => (
        <div
          key={idx}
          className={`p-4 rounded-lg border flex gap-4 ${
            alert.type === 'critical' ? 'bg-red-50 border-red-200 text-red-700' : 'bg-yellow-50 border-yellow-200 text-yellow-700'
          }`}
        >
          <div className="mt-1">
            <alert.icon size={20} />
          </div>
          <div>
            <h4 className="font-bold">{alert.title}</h4>
            <p className="text-sm opacity-90">{alert.message}</p>
          </div>
        </div>
      ))}
    </div>
  );
};
