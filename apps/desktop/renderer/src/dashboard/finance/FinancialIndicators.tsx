import React from 'react';
import { TrendingUp, TrendingDown, DollarSign, Activity } from 'lucide-react';
import { Card } from '../../components/Card';

interface RatioCardProps {
  title: string;
  value: number;
  status: 'HEALTHY' | 'WARNING' | 'CRITICAL' | 'STABLE';
  icon: any;
  suffix?: string;
}

const RatioCard: React.FC<RatioCardProps> = ({ title, value, status, icon: Icon, suffix = '' }) => {
  const statusColors = {
    HEALTHY: 'text-green-600 bg-green-50 border-green-200',
    STABLE: 'text-blue-600 bg-blue-50 border-blue-200',
    WARNING: 'text-yellow-600 bg-yellow-50 border-yellow-200',
    CRITICAL: 'text-red-600 bg-red-50 border-red-200',
  };

  return (
    <Card className={`border ${statusColors[status]}`}>
      <div className="flex justify-between items-start">
        <div>
          <p className="text-sm font-medium opacity-80 mb-1">{title}</p>
          <h3 className="text-2xl font-bold">{value.toLocaleString()}{suffix}</h3>
        </div>
        <div className="p-2 bg-white/50 rounded-lg">
          <Icon size={20} />
        </div>
      </div>
      <div className="mt-4 text-xs font-bold uppercase">
        Estado: {status}
      </div>
    </Card>
  );
};

export const FinancialIndicators = ({ data }: { data: any }) => {
  if (!data) return null;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <RatioCard
        title="Ratio de Liquidez"
        value={data.ratios.liquidez.value}
        status={data.ratios.liquidez.status}
        icon={DollarSign}
        suffix="x"
      />
      <RatioCard
        title="Rentabilidad Neta"
        value={data.ratios.rentabilidad.value * 100}
        status={data.ratios.rentabilidad.status}
        icon={TrendingUp}
        suffix="%"
      />
      <RatioCard
        title="Margen de Ganancia"
        value={data.ratios.margen_ganancia.value * 100}
        status={data.ratios.margen_ganancia.status}
        icon={Activity}
        suffix="%"
      />
      <RatioCard
        title="Utilidad Neta (Mes)"
        value={data.summary.net_income_month}
        status={data.summary.net_income_month > 0 ? 'HEALTHY' : 'CRITICAL'}
        icon={data.summary.net_income_month > 0 ? TrendingUp : TrendingDown}
      />
    </div>
  );
};
