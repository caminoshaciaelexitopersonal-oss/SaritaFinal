'use client';

import React, { useEffect, useState } from 'react';
import {
  getOptimizationProposals,
  approveAndExecuteOptimization,
  rollbackOptimization,
  OptimizationProposal
} from '@/services/optimization';
import { toast } from 'react-hot-toast';
import { FiRefreshCw, FiCheckCircle, FiAlertCircle, FiSettings } from 'react-icons/fi';

export default function OptimizacionPage() {
  const [proposals, setProposals] = useState<OptimizationProposal[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchProposals = async () => {
    try {
      const data = await getOptimizationProposals();
      setProposals(data);
    } catch (error) {
      toast.error("Error al cargar optimizaciones.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProposals();
  }, []);

  const handleApply = async (id: string) => {
    try {
      await approveAndExecuteOptimization(id);
      toast.success("Optimización aplicada correctamente.");
      fetchProposals();
    } catch (error) {
      toast.error("Error al aplicar la optimización.");
    }
  };

  const handleRollback = async (id: string) => {
    try {
      await rollbackOptimization(id);
      toast.success("Cambio revertido.");
      fetchProposals();
    } catch (error) {
      toast.error("Error en el rollback.");
    }
  };

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-2xl font-bold flex items-center gap-2">
            <FiSettings className="text-blue-600" />
            Optimización del Ecosistema SARITA
          </h1>
          <p className="text-gray-500">Ajuste dinámico y evolución proactiva del sistema.</p>
        </div>
        <div className="bg-blue-50 p-4 rounded-lg border border-blue-100">
          <p className="text-sm font-bold text-blue-800">Aprendizaje Dirigido: Activo</p>
          <p className="text-xs text-blue-600">Nivel Maestro de Integración SADI</p>
        </div>
      </div>

      {loading ? (
        <p>Analizando patrones del ecosistema...</p>
      ) : (
        <div className="grid gap-6">
          {proposals.map((proposal) => (
            <div key={proposal.id} className={`bg-white p-6 rounded-lg shadow-md border-t-4 ${
              proposal.status === 'EXECUTED' ? 'border-green-500' : 'border-yellow-500'
            }`}>
              <div className="flex justify-between items-start mb-4">
                <div className="flex items-center gap-3">
                  <div className={`p-2 rounded-full ${
                    proposal.status === 'EXECUTED' ? 'bg-green-100 text-green-600' : 'bg-yellow-100 text-yellow-600'
                  }`}>
                    {proposal.status === 'EXECUTED' ? <FiCheckCircle size={24} /> : <FiRefreshCw size={24} className="animate-spin-slow" />}
                  </div>
                  <div>
                    <h2 className="text-lg font-bold">{proposal.domain} - {proposal.status}</h2>
                    <p className="text-xs text-gray-400">{new Date(proposal.created_at).toLocaleString()}</p>
                  </div>
                </div>
                <div className="text-right">
                  <span className="text-xs font-mono bg-gray-100 p-1 rounded">ID: {proposal.id.slice(0,8)}</span>
                </div>
              </div>

              <div className="space-y-4 mb-6">
                <div className="bg-blue-50 p-3 rounded border-l-4 border-blue-400">
                  <h3 className="text-sm font-bold text-blue-800 mb-1">Hallazgo del Sistema</h3>
                  <p className="text-sm text-blue-900 italic">"{proposal.hallazgo}"</p>
                </div>

                <div>
                  <h3 className="font-bold text-gray-700">Propuesta de Ajuste</h3>
                  <p className="text-gray-600">{proposal.propuesta_ajuste}</p>
                </div>

                <div className="grid md:grid-cols-2 gap-4">
                  <div className="p-3 bg-gray-50 rounded">
                    <h3 className="text-xs font-bold text-gray-500 uppercase">Impacto Esperado</h3>
                    <p className="text-sm font-medium">{proposal.impacto_esperado}</p>
                  </div>
                  <div className="p-3 bg-gray-50 rounded">
                    <h3 className="text-xs font-bold text-gray-500 uppercase">Parámetros Técnicos</h3>
                    <pre className="text-xs text-gray-400 mt-1">{JSON.stringify(proposal.parametros_cambio, null, 2)}</pre>
                  </div>
                </div>
              </div>

              <div className="flex gap-4 border-t pt-4">
                {proposal.status === 'PROPOSED' && (
                  <button
                    onClick={() => handleApply(proposal.id)}
                    className="flex items-center gap-2 bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition font-bold"
                  >
                    Aprobar y Ejecutar Ajuste
                  </button>
                )}
                {proposal.status === 'EXECUTED' && (
                  <button
                    onClick={() => handleRollback(proposal.id)}
                    className="flex items-center gap-2 bg-red-100 text-red-600 px-6 py-2 rounded-lg hover:bg-red-200 transition font-bold"
                  >
                    <FiRefreshCw />
                    Rollback (Revertir)
                  </button>
                )}
              </div>
            </div>
          ))}
          {proposals.length === 0 && (
            <div className="text-center py-20 bg-gray-50 border-2 border-dashed border-gray-200 rounded-xl">
              <FiCheckCircle className="mx-auto text-green-400 mb-4" size={48} />
              <p className="text-gray-500 font-bold">El ecosistema SARITA se encuentra en equilibrio dinámico.</p>
              <p className="text-sm text-gray-400">No se requieren optimizaciones estructurales por el momento.</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
