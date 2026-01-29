'use client';
import React from 'react';
import { FiShield } from 'react-icons/fi';

export default function GlobalAudit() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
        <FiShield className="mr-2" /> Auditoría de Sistema y Trazabilidad
      </h1>
      <div className="bg-white p-8 rounded-xl border border-gray-100 text-center">
        <p className="text-gray-500">Módulo de trazabilidad consolidada en preparación.</p>
        <p className="text-sm text-gray-400 mt-2">Próximamente: Detección de anomalías y alertas de riesgo.</p>
      </div>
    </div>
  );
}
