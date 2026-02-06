'use client';

import React from 'react';
import { FiShield, FiAnchor, FiActivity, FiMap } from 'react-icons/fi';

export default function LegacyDashboardPage() {
  const principles = [
    { title: 'Subordinación Soberana', desc: 'Delegación algorítmica condicionada al mandato humano.' },
    { title: 'Imprivatizabilidad', desc: 'SARITA es un bien público civilizatorio inalienable.' },
    { title: 'Anti-Deriva Histórica', desc: 'Prohibición de expansión de mandato o auto-modificación.' },
    { title: 'Transmisión de Sabiduría', desc: 'Custodia del porqué técnico y ético del sistema.' },
  ];

  return (
    <div className="p-8 bg-black min-h-screen text-teal-500 font-mono">
      <div className="border-2 border-teal-900 p-6 rounded-lg bg-gray-900/50 backdrop-blur-md">
        <div className="flex items-center gap-4 mb-8 border-b border-teal-900 pb-4">
          <FiShield className="text-4xl text-teal-400 animate-pulse" />
          <div>
            <h1 className="text-3xl font-bold uppercase tracking-tighter text-teal-100">Custodia de Legado SARITA</h1>
            <p className="text-teal-600">Estado: <span className="text-green-400 underline italic">LEGADO_PROTEGIDO</span> | Ref: RC-S-CONSOLIDATED</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          {principles.map((p, i) => (
            <div key={i} className="border border-teal-900/50 p-4 rounded bg-black/40 hover:border-teal-500 transition-colors group">
              <div className="flex items-center gap-3 mb-2">
                <FiAnchor className="text-teal-400 group-hover:rotate-45 transition-transform" />
                <h3 className="text-teal-100 font-bold">{p.title}</h3>
              </div>
              <p className="text-sm text-teal-700 italic leading-snug">{p.desc}</p>
            </div>
          ))}
        </div>

        <div className="bg-teal-900/10 border border-teal-900 p-4 rounded-lg mb-8">
          <h2 className="text-lg font-bold text-teal-300 mb-4 flex items-center gap-2">
            <FiActivity className="text-teal-400" /> BITÁCORA DE TRANSMISIÓN GENERACIONAL
          </h2>
          <div className="space-y-3">
            {[
              { event: 'RATIFICACIÓN_CARTA_CUSTODIA', status: 'COMPLETADO', date: '2026-02-06' },
              { event: 'SELLADO_GUARDRAILS_LEGADO', status: 'ACTIVO', date: '2026-02-06' },
              { event: 'PAQUETE_EVIDENCIA_INMUTABLE', status: 'GENERADO', date: '2026-02-06' },
            ].map((e, i) => (
              <div key={i} className="flex justify-between text-xs border-l-2 border-teal-800 pl-4 py-1">
                <span className="text-teal-400">{e.event}</span>
                <span className="text-teal-600">{e.date}</span>
                <span className="text-green-900 font-bold px-2 bg-green-400/10 rounded">{e.status}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="border border-red-900/50 bg-red-950/10 p-4 rounded text-center">
          <p className="text-red-500 text-xs uppercase font-bold tracking-widest">
             Aviso de Seguridad Institucional: Cualquier intento de desvío del modelo original activará de-interoperabilidad inmediata.
          </p>
        </div>
      </div>
    </div>
  );
}
