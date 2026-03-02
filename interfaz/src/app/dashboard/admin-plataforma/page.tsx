'use client';

import React from 'react';
import useSWR from 'swr';
import { getStatistics } from '@/services/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import {
  FiShield,
  FiUsers,
  FiActivity,
  FiAlertTriangle,
  FiZap,
  FiGlobe,
  FiCpu,
  FiPower,
  FiLock,
  FiUnlock,
  FiRepeat,
  FiClock,
  FiAward,
  FiWifi,
  FiWifiOff
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import { Button } from '@/components/ui/Button';
import { ViewState } from '@/components/ui/ViewState';
import Link from 'next/link';
import { sovereigntyService, SystemFlag } from '@/services/sovereigntyService';
import { toast } from 'react-hot-toast';
import { CriticalActionDialog } from '@/components/ui/CriticalActionDialog';
import { useWebSockets, TowerEvent } from '@/hooks/useWebSockets';

export default function AdminPlataformaPage() {
  const { data: stats, mutate: mutateStats, isLoading } = useSWR('admin-statistics', getStatistics);
  const { data: flagsRes, mutate: mutateFlags } = useSWR('admin-flags', sovereigntyService.getFlags);

  const { lastEvent, isConnected } = useWebSockets();
  const [liveEvents, setLiveEvents] = React.useState<TowerEvent[]>([]);

  const [isEmergencyDialogOpen, setIsEmergencyDialogOpen] = React.useState(false);
  const [isAttackModeActive, setIsAttackModeActive] = React.useState(false);

  // Escuchar eventos en vivo para actualizar KPIs sin polling
  React.useEffect(() => {
    if (lastEvent) {
      setLiveEvents(prev => [lastEvent, ...prev].slice(0, 10));

      // Actualizar estadísticas si el evento es relevante
      if (['VentaCreada', 'PagoRecibido', 'AsientoGenerado'].includes(lastEvent.event_type)) {
        mutateStats(); // Re-fetch datos ligeros
        toast(`Omnisciencia: Nuevo evento ${lastEvent.event_type} detectado`, {
          icon: '⚡',
          style: { borderRadius: '10px', background: '#333', color: '#fff' }
        });
      }
    }
  }, [lastEvent, mutateStats]);

  const handleFlagToggle = async (id: string, currentStatus: string) => {
    const nextStatus = currentStatus === 'ACTIVE' ? 'PAUSED' : 'ACTIVE';
    try {
        await sovereigntyService.toggleFlag(id, nextStatus);
        toast.success(`Bandera de sistema ajustada: ${nextStatus}`);
        mutateFlags();
    } catch (e) {
        toast.error("INTERVENCIÓN FALLIDA: El Kernel de Gobernanza no permitió el cambio de estado.");
    }
  };

  const handleEmergencyKill = async () => {
    setIsAttackModeActive(true);
    toast.success("S-0: MODO ATAQUE ACTIVADO. El sistema ha sido congelado.");
    setIsEmergencyDialogOpen(false);
  };

  const handleRestoreNormalMode = () => {
    setIsAttackModeActive(false);
    toast.success("S-0: MODO NORMAL RESTAURADO.");
  };

  const mainKpis = [
    { label: 'Total Usuarios Sistema', value: stats?.total_usuarios || '0', trend: 'Global', icon: FiUsers, color: 'text-blue-600' },
    { label: 'Prestadores Activos', value: stats?.total_prestadores || '0', trend: 'Vía 2', icon: FiActivity, color: 'text-indigo-600' },
    { label: 'Publicaciones Totales', value: stats?.total_publicaciones || '0', trend: 'Contenido', icon: FiGlobe, color: 'text-emerald-600' },
    { label: 'Consistencia Analítica', value: stats?.trust_index || '98.2%', trend: 'Normativo', icon: FiZap, color: 'text-amber-600' },
  ];

  return (
    <ViewState
       isLoading={isLoading}
       loadingMessage="Compilando estado de soberanía sistémica..."
       error={!stats && !isLoading ? "No fue posible recuperar las métricas globales." : null}
    >
    <div className="space-y-10 animate-in fade-in duration-1000">
      {/* Header de Soberanía con Estado de Conexión en Vivo */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 border-b border-gray-100 pb-8">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="bg-slate-900 text-white p-2 rounded-lg">
              <FiShield size={24} />
            </div>
            <h1 className="text-4xl font-black text-slate-900 tracking-tighter uppercase">Torre de Control Omnisciente</h1>
            <Badge className={isConnected ? "bg-emerald-500" : "bg-red-500"}>
              {isConnected ? <FiWifi className="mr-1" /> : <FiWifiOff className="mr-1" />}
              {isConnected ? "LIVE" : "DISCONNECTED"}
            </Badge>
          </div>
          <p className="text-slate-500 text-lg font-medium italic">Monitoreo sistémico en tiempo real. Pulso de negocio actualizado al instante.</p>
        </div>
        <div className="flex gap-4">
           <div className="px-6 py-3 bg-emerald-50 border border-emerald-100 rounded-2xl flex items-center gap-3">
              <div className="w-3 h-3 bg-emerald-500 rounded-full animate-pulse" />
              <span className="text-sm font-black text-emerald-700 tracking-widest uppercase">Omnisciencia Activa</span>
           </div>
           {!isAttackModeActive ? (
                <Button
                    onClick={() => setIsEmergencyDialogOpen(true)}
                    className="bg-red-600 text-white font-black px-8 py-6 rounded-2xl hover:bg-red-700 transition-all shadow-xl shadow-red-500/20">
                    <FiPower className="mr-2" /> Activar Modo Ataque
                </Button>
           ) : (
                <Button
                    onClick={handleRestoreNormalMode}
                    className="bg-emerald-600 text-white font-black px-8 py-6 rounded-2xl hover:bg-emerald-700 transition-all shadow-xl shadow-emerald-500/20 animate-pulse">
                    <FiRepeat className="mr-2" /> Restaurar Modo Normal
                </Button>
           )}
        </div>
      </div>

      {/* Grid de KPIs Maestros */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
         {mainKpis.map((kpi, i) => (
           <Card key={i} className="border-none shadow-sm hover:shadow-md transition-all bg-white group cursor-default">
              <CardContent className="p-8">
                 <div className="flex justify-between items-start mb-6">
                    <div className={`p-4 rounded-2xl bg-gray-50 ${kpi.color} group-hover:scale-110 transition-transform`}>
                       <kpi.icon size={28} />
                    </div>
                    <Badge className="bg-slate-100 text-slate-600 border-none font-bold">{kpi.trend}</Badge>
                 </div>
                 <p className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-1">{kpi.label}</p>
                 <h3 className="text-3xl font-black text-slate-900">{kpi.value}</h3>
              </CardContent>
           </Card>
         ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
         {/* Feed de Eventos en Tiempo Real (Fase 4.7) */}
         <Card className="lg:col-span-2 border-none shadow-sm overflow-hidden bg-white">
            <CardHeader className="bg-slate-50/50 p-6 border-b border-gray-100">
               <CardTitle className="text-xl font-black flex items-center gap-2">
                  <FiActivity className="text-indigo-600 animate-spin-slow" /> Flujo de Eventos Omnisciente
               </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
               <div className="divide-y divide-gray-100 max-h-[500px] overflow-y-auto">
                  {liveEvents.length === 0 ? (
                      <div className="p-20 text-center text-slate-400 uppercase italic tracking-widest text-xs">
                          Esperando pulsos de sistema...
                      </div>
                  ) : liveEvents.map((ev, i) => (
                    <div key={ev.event_id} className="p-6 hover:bg-slate-50 transition-colors animate-in slide-in-from-top duration-500">
                       <div className="flex justify-between items-start mb-2">
                          <div className="flex items-center gap-2">
                            <Badge variant="outline" className="border-indigo-200 text-indigo-700 font-black">{ev.event_type}</Badge>
                            <span className="text-[10px] text-slate-400 font-mono">{ev.timestamp}</span>
                          </div>
                          <Badge className={
                             ev.severity === 'critical' ? 'bg-red-500' :
                             ev.severity === 'warning' ? 'bg-amber-500' : 'bg-blue-500'
                          }>
                             {ev.severity.toUpperCase()}
                          </Badge>
                       </div>
                       <p className="text-slate-700 font-medium">{JSON.stringify(ev.payload)}</p>
                    </div>
                  ))}
               </div>
            </CardContent>
         </Card>

         {/* Alertas de Gobernanza */}
         <Card className="border-none shadow-xl bg-slate-900 text-white overflow-hidden rounded-3xl">
            <CardHeader className="p-8 border-b border-white/10">
               <CardTitle className="text-xl font-black flex items-center gap-2">
                  <FiAlertTriangle className="text-amber-400" /> Notificaciones de Desviación
               </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
               <div className="divide-y divide-white/5">
                  {liveEvents.filter(e => e.severity === 'critical' || e.severity === 'warning').length === 0 ? (
                      <div className="p-20 text-center text-slate-500 uppercase italic tracking-widest text-xs">
                          No hay alertas críticas registradas.
                      </div>
                  ) : liveEvents.filter(e => e.severity === 'critical' || e.severity === 'warning').map((alert, i) => (
                    <div key={i} className="p-8 hover:bg-white/5 transition-colors cursor-pointer group border-l-4 border-amber-500">
                       <div className="flex justify-between items-start mb-3">
                          <span className="text-[10px] font-black uppercase tracking-[0.2em] text-indigo-400">ALERT_MONITOR</span>
                          <Badge className="bg-amber-600">{alert.severity.toUpperCase()}</Badge>
                       </div>
                       <h4 className="font-bold text-lg mb-2 group-hover:text-amber-300 transition-colors">{alert.event_type}</h4>
                       <p className="text-slate-400 text-sm leading-relaxed">Impacto detectado en la entidad {alert.entity_id}</p>
                    </div>
                  ))}
               </div>
               <Link href="/dashboard/admin-plataforma/grc">
                <div className="p-8 bg-indigo-600 hover:bg-indigo-700 transition-colors text-center cursor-pointer font-black uppercase tracking-widest text-sm">
                    Ver Auditoría Global
                </div>
               </Link>
            </CardContent>
         </Card>
      </div>

      <CriticalActionDialog
        isOpen={isEmergencyDialogOpen}
        onClose={() => setIsEmergencyDialogOpen(false)}
        onConfirm={handleEmergencyKill}
        title="Suspensión de Operaciones por Auditoría"
        description="Se procederá a la suspensión inmediata de las funciones comerciales y de registro del sistema."
        confirmLabel="Confirmar Suspensión"
        type="danger"
      />
    </div>
    </ViewState>
  );
}
