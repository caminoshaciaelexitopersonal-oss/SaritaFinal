'use client';

import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { Button } from '@/components/ui/Button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import {
  FiCpu, FiZap, FiAlertOctagon, FiActivity, FiShield, FiFileText, FiClock, FiSearch, FiPower
} from 'react-icons/fi';
import { autonomyService, AutonomousAction, AutonomousExecutionLog, AutonomyControl } from '@/services/autonomyService';
import { useAuth } from '@/contexts/AuthContext';

export default function AutonomyControlCenter() {
  const [actions, setActions] = useState<AutonomousAction[]>([]);
  const [logs, setLogs] = useState<AutonomousExecutionLog[]>([]);
  const [controls, setControls] = useState<AutonomyControl[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const { user } = useAuth();

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 10000); // Refresh cada 10s
    return () => clearInterval(interval);
  }, []);

  const fetchData = async () => {
    try {
      const [actionsRes, logsRes, controlsRes] = await Promise.all([
        autonomyService.getActions(),
        autonomyService.getLogs(),
        autonomyService.getControls()
      ]);
      setActions(actionsRes);
      setLogs(logsRes);
      setControls(controlsRes);
    } catch (error) {
      console.error("Error fetching autonomy data:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const globalControl = controls.find(c => c.domain === null) || { is_enabled: true, reason: "" };

  const handleKillSwitch = async () => {
    const nextState = !globalControl.is_enabled;
    const reason = window.prompt("Motivo de la intervención soberana:");
    if (reason !== null) {
      try {
        await autonomyService.toggleGlobalKillSwitch(nextState, reason);
        fetchData();
      } catch (error) {
        alert("Error al activar Kill Switch");
      }
    }
  };

  const getLevelBadge = (level: number) => {
    switch(level) {
        case 0: return <Badge variant="outline">N0: Manual</Badge>;
        case 1: return <Badge className="bg-blue-100 text-blue-700">N1: Asistida</Badge>;
        case 2: return <Badge className="bg-emerald-100 text-emerald-700">N2: Autónoma</Badge>;
        case 3: return <Badge className="bg-red-100 text-red-700">N3: Bloqueado</Badge>;
        default: return null;
    }
  }

  return (
    <div className="space-y-8 animate-in fade-in duration-700">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 border-b border-gray-100 pb-8">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="bg-emerald-900 text-white p-2 rounded-lg">
              <FiCpu size={24} />
            </div>
            <h1 className="text-4xl font-black text-slate-900 tracking-tighter uppercase">Centro de Autonomía de IA (Fase F-F)</h1>
          </div>
          <p className="text-slate-500 text-lg">Control soberano y supervisión de agentes inteligentes autónomos.</p>
        </div>

        <Button
          onClick={handleKillSwitch}
          className={`px-8 py-6 rounded-2xl flex items-center gap-3 transition-all font-black uppercase tracking-widest text-sm shadow-2xl ${
            globalControl.is_enabled
            ? 'bg-slate-900 text-white hover:bg-red-600'
            : 'bg-red-600 text-white animate-pulse'
          }`}
        >
          <FiPower size={20} />
          {globalControl.is_enabled ? 'Activar Kill Switch Global' : 'Kill Switch Activado (Bloqueo)'}
        </Button>
      </div>

      {/* KPI Section */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
         <Card className="border-none shadow-sm bg-white overflow-hidden">
            <CardContent className="p-8">
               <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">Acciones Tipificadas</p>
               <h3 className="text-4xl font-black text-slate-900">{actions.length}</h3>
               <p className="text-xs text-slate-500 mt-2">Solo estas acciones pueden ser autónomas.</p>
            </CardContent>
         </Card>
         <Card className="border-none shadow-sm bg-white">
            <CardContent className="p-8">
               <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">Estado de Autonomía</p>
               <div className="flex items-center gap-2 mt-1">
                 <div className={`w-3 h-3 rounded-full ${globalControl.is_enabled ? 'bg-emerald-500 animate-pulse' : 'bg-red-500'}`} />
                 <h3 className="text-2xl font-black uppercase italic">
                    {globalControl.is_enabled ? 'Operativo (Nivel 2)' : 'Bloqueado (Soberano)'}
                 </h3>
               </div>
               {!globalControl.is_enabled && (
                 <p className="text-xs text-red-500 font-bold mt-2 uppercase">Razón: {globalControl.reason}</p>
               )}
            </CardContent>
         </Card>
         <Card className="border-none shadow-sm bg-white">
            <CardContent className="p-8">
               <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">Ejecuciones (Hoy)</p>
               <h3 className="text-4xl font-black text-indigo-600">
                 {logs.filter(l => new Date(l.timestamp).toDateString() === new Date().toDateString()).length}
               </h3>
               <p className="text-xs text-slate-500 mt-2">Todas bajo límites regulatorios.</p>
            </CardContent>
         </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Actions Table */}
        <Card className="border-none shadow-sm overflow-hidden">
          <CardHeader className="bg-slate-50 border-b border-slate-100">
             <CardTitle className="text-xs font-black uppercase tracking-widest flex items-center gap-2">
                <FiZap className="text-amber-500" /> Acciones Autónomas Permitidas
             </CardTitle>
          </CardHeader>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="font-black uppercase text-[10px] px-6">Acción / Dominio</TableHead>
                  <TableHead className="font-black uppercase text-[10px]">Nivel</TableHead>
                  <TableHead className="font-black uppercase text-[10px]">Límites</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {actions.length === 0 ? (
                    <TableRow><TableCell colSpan={3} className="p-10 text-center text-slate-400 uppercase italic">No hay acciones autónomas registradas.</TableCell></TableRow>
                ) : actions.map((action) => (
                  <TableRow key={action.id}>
                    <TableCell className="px-6">
                       <p className="font-bold text-slate-800">{action.name}</p>
                       <p className="text-[9px] text-slate-400 uppercase tracking-widest">{action.domain}</p>
                    </TableCell>
                    <TableCell>{getLevelBadge(action.autonomy_level)}</TableCell>
                    <TableCell>
                       <div className="text-[9px] font-bold text-slate-500">
                          <p>MAX/DÍA: {action.max_daily_executions}</p>
                          <p>IMPACTO: ${action.max_financial_impact}</p>
                       </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>

        {/* Live Audit Log with XAI */}
        <Card className="border-none shadow-sm overflow-hidden bg-slate-900 text-slate-300">
           <CardHeader className="border-b border-white/5 p-6 flex flex-row items-center justify-between">
              <CardTitle className="text-white font-black uppercase text-xs tracking-widest flex items-center gap-2">
                 <FiActivity className="text-emerald-400" /> Registro Autónomo Sistémico
              </CardTitle>
              <Badge className="bg-emerald-500">Live XAI Trace</Badge>
           </CardHeader>
           <CardContent className="p-0">
              <div className="max-h-[600px] overflow-y-auto divide-y divide-white/5">
                 {logs.length === 0 ? (
                   <div className="p-20 text-center text-slate-500 uppercase italic tracking-widest">Esperando ejecuciones autónomas...</div>
                 ) : (
                   logs.map((log) => (
                     <div key={log.id} className="p-6 hover:bg-white/5 transition-colors space-y-3">
                        <div className="flex justify-between items-start">
                           <div>
                              <span className="text-[9px] font-bold text-slate-500 uppercase">{new Date(log.timestamp).toLocaleString()}</span>
                              <h4 className="text-emerald-400 font-black uppercase italic tracking-tight">{log.action_name}</h4>
                           </div>
                           <Badge className={
                                log.result_status === 'SUCCESS' ? 'bg-emerald-100/10 text-emerald-400 border-emerald-500/20' :
                                'bg-red-100/10 text-red-400 border-red-500/20'
                           }>
                             {log.result_status}
                           </Badge>
                        </div>

                        <div className="bg-black/40 p-4 rounded-xl border border-white/5">
                           <p className="text-xs leading-relaxed text-slate-200">
                             <FiFileText className="inline mr-2 text-slate-500" />
                             {log.explanation}
                           </p>
                        </div>

                        <div className="flex items-center justify-between text-[9px] font-black uppercase tracking-widest text-slate-500">
                           <span className="flex items-center gap-1"><FiShield /> Política: {log.policy_applied}</span>
                           {log.was_interrupted && <span className="text-red-400 flex items-center gap-1"><FiAlertOctagon /> Interrumpido</span>}
                        </div>
                     </div>
                   ))
                 )}
              </div>
           </CardContent>
        </Card>
      </div>
    </div>
  );
}
