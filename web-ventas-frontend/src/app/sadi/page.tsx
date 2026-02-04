'use client';

import React, { useState, useEffect, useRef } from 'react';

// --- Helper Components ---
const Card = ({ children, className }: { children: React.ReactNode; className?: string }) => (
  <div className={`bg-gray-800 border border-gray-700 rounded-lg p-6 ${className}`}>
    {children}
  </div>
);

const Button = ({ children, onClick, disabled }: { children: React.ReactNode; onClick: () => void; disabled?: boolean }) => (
  <button
    onClick={onClick}
    disabled={disabled}
    className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-4 rounded-lg transition duration-300 disabled:bg-gray-500"
  >
    {children}
  </button>
);

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// --- Main SADI Agent UI Page ---
export default function SadiPage() {
  const [objective, setObjective] = useState('');
  const [executionId, setExecutionId] = useState<string | null>(null);
  const [status, setStatus] = useState('IDLE');
  const [logs, setLogs] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const pollIntervalRef = useRef<NodeJS.Timeout | null>(null);

  const clearPolling = () => {
    if (pollIntervalRef.current) {
      clearInterval(pollIntervalRef.current);
      pollIntervalRef.current = null;
    }
  };

  const pollExecutionStatus = async (id: string) => {
    try {
      // NOTE: Assuming token is stored in localStorage for this example.
      // In a real app, this should come from a secure auth context.
      const token = localStorage.getItem('authToken');
      if (!token) {
          throw new Error('Authentication token not found.');
      }

      const response = await fetch(`${API_BASE_URL}/api/sadi/v1/executions/${id}/`, {
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch execution status.');
      }

      const data = await response.json();
      setLogs(data.logs);
      setResult(data.final_result);
      setStatus(data.status);

      if (data.status === 'COMPLETED' || data.status === 'FAILED') {
        clearPolling();
      }
    } catch (err: any) {
      setError(`Polling error: ${err.message}`);
      setStatus('FAILED');
      clearPolling();
    }
  };

  useEffect(() => {
    if (executionId && (status === 'PENDING' || status === 'RUNNING')) {
      pollIntervalRef.current = setInterval(() => {
        pollExecutionStatus(executionId);
      }, 3000); // Poll every 3 seconds
    }

    // Cleanup on component unmount or when status changes to final state
    return () => clearPolling();
  }, [executionId, status]);


  const handleExecute = async () => {
    clearPolling();
    setLogs('');
    setResult('');
    setError('');
    setStatus('PENDING');

    try {
      const token = localStorage.getItem('authToken');
      if (!token) {
          throw new Error('Authentication token not found. Please log in.');
      }

      const response = await fetch(`${API_BASE_URL}/api/sadi/v1/executions/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ objective }),
      });

      if (response.status !== 202) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'The request was not accepted.');
      }

      const data = await response.json();
      setExecutionId(data.id);
      setStatus(data.status); // Should be PENDING
      setLogs('Agent execution initiated...');

    } catch (err: any) {
      setError(`Execution failed to start: ${err.message}`);
      setStatus('FAILED');
    }
  };

  const isLoading = status === 'PENDING' || status === 'RUNNING';

  const isModuleBlocked = true; // SADI Execution Engine no está expuesto en el routing real.

  return (
    <main className="bg-gray-900 text-white min-h-screen p-4 sm:p-6 lg:p-8">
      <div className="max-w-4xl mx-auto space-y-8">

        <div className="text-center">
          <h1 className="text-4xl font-bold text-indigo-400">S.A.D.I. Agent Interface</h1>
          <p className="text-gray-400 mt-2">Sistema Autónomo de Decisión e Inferencia</p>
        </div>

        <Card>
          <h2 className="text-2xl font-semibold mb-4">1. Define Your Objective</h2>
          {isModuleBlocked ? (
              <div className="p-8 bg-red-900/20 border border-red-500/50 rounded-xl text-center">
                  <p className="text-red-400 font-black uppercase tracking-widest text-sm mb-2">Motor Inactivo</p>
                  <p className="text-red-300/70 text-xs italic">
                      DOMINIO BLOQUEADO: El Sistema Autónomo de Decisión e Inferencia (SADI) no posee un endpoint de ejecución activo en el Kernel de Gobernanza.
                      Las misiones autónomas están suspendidas por política de seguridad institucional.
                  </p>
              </div>
          ) : (
            <>
                <textarea
                    value={objective}
                    onChange={(e) => setObjective(e.target.value)}
                    placeholder="e.g., Analyze the latest user feedback and generate a summary report."
                    className="w-full h-32 bg-gray-900 border border-gray-600 rounded-lg p-4 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                    disabled={isLoading}
                />
                <Button onClick={handleExecute} disabled={isLoading || !objective}>
                    {isLoading ? `Executing (Status: ${status})...` : 'Execute Agent'}
                </Button>
            </>
          )}
          {error && <p className="text-red-400 mt-4 text-center">{error}</p>}
        </Card>

        <div className="grid md:grid-cols-2 gap-8">
          <Card>
            <h2 className="text-2xl font-semibold mb-4">Agent Logs</h2>
            <pre className="bg-gray-900 border border-gray-700 rounded-lg p-4 h-80 overflow-y-auto text-sm text-gray-300 whitespace-pre-wrap">
              {logs || 'Agent logs will appear here...'}
            </pre>
          </Card>

          <Card>
            <h2 className="text-2xl font-semibold mb-4">Final Result</h2>
            <div className="bg-gray-900 border border-gray-700 rounded-lg p-4 h-80 overflow-y-auto text-gray-200">
              {result || 'The final result will be displayed here...'}
            </div>
          </Card>
        </div>

      </div>
    </main>
  );
}
