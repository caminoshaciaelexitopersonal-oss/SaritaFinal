import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Calculator, Download, Table } from 'lucide-react';
import { Card } from '../../components/Card';

export const BalanceSheet = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Balance General</h2>
        <button className="flex items-center gap-2 px-3 py-1.5 border rounded-lg text-xs font-bold hover:bg-gray-50 transition">
          <Download size={14} /> Descargar PDF
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="space-y-4">
          <h3 className="font-bold text-sm uppercase text-gray-400 tracking-widest border-b pb-2">ACTIVOS</h3>
          {[
            { name: 'Disponible (Caja/Bancos)', amount: 2450.50 },
            { name: 'Cuentas por Cobrar', amount: 1200.00 },
            { name: 'Equipos y Maquinaria', amount: 8500.00 },
          ].map(a => (
            <div key={a.name} className="flex justify-between border-b border-gray-50 py-2">
              <span className="text-sm">{a.name}</span>
              <span className="font-bold font-mono">${a.amount.toFixed(2)}</span>
            </div>
          ))}
          <div className="flex justify-between bg-blue-50 p-4 rounded-lg">
            <span className="font-bold text-primary">TOTAL ACTIVOS</span>
            <span className="font-bold text-primary">$12,150.50</span>
          </div>
        </div>

        <div className="space-y-8">
          <div className="space-y-4">
            <h3 className="font-bold text-sm uppercase text-gray-400 tracking-widest border-b pb-2">PASIVOS</h3>
            {[
              { name: 'Cuentas por Pagar', amount: 450.00 },
              { name: 'Obligaciones Laborales', amount: 1500.00 },
            ].map(p => (
              <div key={p.name} className="flex justify-between border-b border-gray-50 py-2">
                <span className="text-sm">{p.name}</span>
                <span className="font-bold font-mono">${p.amount.toFixed(2)}</span>
              </div>
            ))}
            <div className="flex justify-between bg-red-50 p-4 rounded-lg">
              <span className="font-bold text-red-600">TOTAL PASIVOS</span>
              <span className="font-bold text-red-600">$1,950.00</span>
            </div>
          </div>

          <div className="space-y-4">
            <h3 className="font-bold text-sm uppercase text-gray-400 tracking-widest border-b pb-2">PATRIMONIO</h3>
            <div className="flex justify-between border-b border-gray-50 py-2">
              <span className="text-sm">Capital Social</span>
              <span className="font-bold font-mono">$10,200.50</span>
            </div>
            <div className="flex justify-between bg-green-50 p-4 rounded-lg">
              <span className="font-bold text-green-700">TOTAL PATRIMONIO</span>
              <span className="font-bold text-green-700">$10,200.50</span>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-gray-900 text-white p-6 rounded-xl flex justify-between items-center shadow-lg">
        <span className="font-bold uppercase tracking-widest text-xs opacity-60">Ecuación Contable: Activo = Pasivo + Patrimonio</span>
        <span className="text-xl font-bold text-secondary">$12,150.50 = $12,150.50 ✓</span>
      </div>
    </div>
  );
};

export const IncomeStatement = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Estado de Resultados (P&L)</h2>
        <span className="text-xs font-bold text-gray-400 uppercase">Periodo: Marzo 2026</span>
      </div>

      <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 max-w-2xl mx-auto space-y-6">
        <div className="space-y-2">
          <div className="flex justify-between text-lg font-bold"><span>INGRESOS OPERACIONALES</span><span>$24,500.00</span></div>
          <div className="flex justify-between text-sm text-gray-500 pl-4 italic"><span>Ventas de Servicios</span><span>$18,450.00</span></div>
          <div className="flex justify-between text-sm text-gray-500 pl-4 italic"><span>Delivery Ecosistema</span><span>$6,050.00</span></div>
        </div>

        <div className="space-y-2 border-t pt-4">
          <div className="flex justify-between text-lg font-bold text-red-600"><span>COSTOS Y GASTOS</span><span>($8,200.00)</span></div>
          <div className="flex justify-between text-sm text-gray-500 pl-4"><span>Gastos de Personal</span><span>($2,750.00)</span></div>
          <div className="flex justify-between text-sm text-gray-500 pl-4"><span>Comisiones SARITA</span><span>($2,450.00)</span></div>
          <div className="flex justify-between text-sm text-gray-500 pl-4"><span>Insumos y Operación</span><span>($3,000.00)</span></div>
        </div>

        <div className="border-t-2 border-primary pt-6 flex justify-between items-center">
          <span className="text-xl font-bold text-primary">UTILIDAD NETA DEL EJERCICIO</span>
          <span className="text-2xl font-bold text-green-600">$16,300.00 USD</span>
        </div>
      </div>
    </div>
  );
};
