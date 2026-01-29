'use client';

import React, { useEffect, useState } from 'react';
import {
  getStrategyProposals,
  approveStrategyProposal,
  executeStrategyProposal,
  rejectStrategyProposal,
  StrategyProposal
} from '@/services/intelligence';
import { toast } from 'react-hot-toast';

export default function InteligenciaPage() {
  const [proposals, setProposals] = useState<StrategyProposal[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchProposals = async () => {
    try {
      const data = await getStrategyProposals();
      setProposals(data);
    } catch (error) {
      toast.error("Error al cargar propuestas de inteligencia.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProposals();
  }, []);

  const handleApprove = async (id: string) => {
    try {
      await approveStrategyProposal(id);
      toast.success("Propuesta aprobada.");
      fetchProposals();
    } catch (error) {
      toast.error("Error al aprobar.");
    }
  };

  const handleExecute = async (id: string) => {
    try {
      await executeStrategyProposal(id);
      toast.success("Acción ejecutada correctamente.");
      fetchProposals();
    } catch (error) {
      toast.error("Error en la ejecución.");
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Núcleo de Inteligencia Estratégica</h1>

      {loading ? (
        <p>Cargando recomendaciones de los agentes...</p>
      ) : (
        <div className="grid gap-6">
          {proposals.map((proposal) => (
            <div key={proposal.id} className="bg-white p-6 rounded-lg shadow-md border-l-4 border-blue-500">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <span className="text-xs font-bold uppercase px-2 py-1 bg-blue-100 text-blue-700 rounded">
                    {proposal.domain}
                  </span>
                  <h2 className="text-xl font-semibold mt-2">{proposal.status}</h2>
                </div>
                <div className="text-right">
                  <p className="text-sm font-medium text-gray-500">Nivel de Decisión</p>
                  <p className="font-bold">{proposal.decision_level === 1 ? 'Automática' : proposal.decision_level === 2 ? 'Supervisada' : 'Estratégica'}</p>
                </div>
              </div>

              <div className="grid md:grid-cols-2 gap-4 mb-6">
                <div>
                  <h3 className="font-bold text-gray-700">Contexto Detectado</h3>
                  <p className="text-gray-600">{proposal.contexto_detectado}</p>
                </div>
                <div>
                  <h3 className="font-bold text-gray-700">Riesgo Actual</h3>
                  <p className="text-gray-600">{proposal.riesgo_actual}</p>
                </div>
              </div>

              <div className="bg-gray-50 p-4 rounded mb-6">
                <h3 className="font-bold text-gray-700 mb-2">Acción Sugerida: {proposal.accion_sugerida.intention}</h3>
                <pre className="text-xs text-gray-500 overflow-auto">
                  {JSON.stringify(proposal.accion_sugerida.parameters, null, 2)}
                </pre>
              </div>

              <div className="flex gap-4">
                {proposal.status === 'PENDING' && (
                  <>
                    <button
                      onClick={() => handleApprove(proposal.id)}
                      className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
                    >
                      Aprobar
                    </button>
                    <button
                      onClick={() => rejectStrategyProposal(proposal.id).then(() => fetchProposals())}
                      className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition"
                    >
                      Rechazar
                    </button>
                  </>
                )}
                {proposal.status === 'APPROVED' && (
                  <button
                    onClick={() => handleExecute(proposal.id)}
                    className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
                  >
                    Ejecutar Ahora
                  </button>
                )}
              </div>
            </div>
          ))}
          {proposals.length === 0 && (
            <div className="text-center py-20 bg-gray-50 rounded">
              <p className="text-gray-500">No hay propuestas estratégicas pendientes. El sistema está operando en niveles nominales.</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
