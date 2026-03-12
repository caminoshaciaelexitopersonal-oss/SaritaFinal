import React from 'react';

interface KpiCardProps {
  title: string;
  value: string | number;
  icon?: React.ReactNode;
  trend?: string;
}

export function KpiCard({ title, value, icon, trend }: KpiCardProps) {
  return (
    <div className="p-4 bg-white rounded-xl shadow-sm border border-slate-100">
      <div className="flex justify-between items-center mb-2">
        <span className="text-sm text-slate-500 font-medium">{title}</span>
        {icon}
      </div>
      <div className="flex items-baseline gap-2">
        <span className="text-2xl font-bold text-slate-900">{value}</span>
        {trend && <span className="text-xs text-green-500">{trend}</span>}
      </div>
    </div>
  );
}
