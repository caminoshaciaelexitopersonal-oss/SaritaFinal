import React, { useEffect, useState } from 'react';
import { Landmark, RefreshCw } from 'lucide-react';
import { FinancialIndicators } from './FinancialIndicators';
import { FinancialRatiosDashboard } from './FinancialRatiosDashboard';
import { FinancialAlerts } from './FinancialAlerts';
import { financeService } from './financeService';
import { Button } from '../../components/Button';
import { Loader } from '../../../../mobile/src/components/Loader'; // Reutilizando componentes compartidos si es posible

export const FinanceDashboard = () => {
  const [data, setData] = useState<any>(null);
  const [cashflow, setCashflow] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  const loadData = async () => {
    setLoading(true);
    try {
      const [ratiosRes, cfRes] = await Promise.all([
        financeService.getRatios(),
        financeService.getCashFlow('2026-01-01', '2026-03-01')
      ]);
      setData(ratiosRes.data);
      setCashflow(cfRes.data.data);
    } catch (error) {
      console.error('Error loading finance data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  if (loading) return <Loader fullScreen message="Analizando Ratios Financieros..." />;

  return (
    <div className="p-8 space-y-8 animate-in fade-in duration-500">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
            <Landmark className="text-primary" size={32} /> Gestión Financiera
          </h1>
          <p className="text-gray-500 mt-2">Monitoreo de ratios, liquidez y rentabilidad en tiempo real.</p>
        </div>
        <Button onClick={loadData} variant="outline" className="gap-2">
          <RefreshCw size={16} /> Actualizar Datos
        </Button>
      </header>

      <FinancialAlerts ratios={data?.ratios} />

      <FinancialIndicators data={data} />

      <FinancialRatiosDashboard ratios={data?.ratios} cashflow={cashflow} />

      <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm mt-8">
        <h3 className="text-lg font-bold mb-4">Nota de Gestión</h3>
        <p className="text-sm text-gray-600 leading-relaxed">
          Este tablero consume indicadores calculados directamente por el <strong>SARITA LedgerEngine</strong> en el backend.
          Los valores de liquidez y rentabilidad se basan en el cierre del Libro Diario y los saldos de cuentas de Activos,
          Pasivos, Ingresos y Gastos debidamente certificados.
        </p>
      </div>
    </div>
  );
};
