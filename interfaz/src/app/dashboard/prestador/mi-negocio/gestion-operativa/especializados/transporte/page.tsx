'use client';

import React, { useEffect, useState } from 'react';
import { useMiNegocioApi } from '@/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import {
  FiTruck,
  FiPlus,
  FiClock,
  FiCheckCircle,
  FiMapPin,
  FiActivity,
  FiShield
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';

import { toast } from 'react-toastify';
import Modal from '@/components/ui/Modal';
import { useForm } from 'react-hook-form';

export default function TransportePage() {
  const { getVehicles, createVehicle, deleteVehicle, isLoading } = useMiNegocioApi();
  const [vehicles, setVehicles] = useState<any[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const { register, handleSubmit, reset } = useForm();

  const loadData = async () => {
    const data = await getVehicles();
    if (data) setVehicles(data.results || []);
  };

  useEffect(() => {
    loadData();
  }, [getVehicles]);

  const onSubmit = async (data: any) => {
    const res = await createVehicle(data);
    if (res) {
        toast.success("Vehículo vinculado con éxito");
        loadData();
        setIsModalOpen(false);
        reset();
    }
  };

  return (
    <div className="space-y-10 animate-in fade-in duration-700">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight uppercase italic">Gestión de Flota y Logística</h1>
          <p className="text-slate-500 dark:text-slate-400 mt-2 text-lg">Control de vehículos, rutas de transporte y asignación de conductores.</p>
        </div>
        <Button
            onClick={() => setIsModalOpen(true)}
            className="bg-brand text-white font-black px-8 py-6 rounded-2xl shadow-xl shadow-brand/20"
        >
           <FiPlus className="mr-2" /> Vincular Vehículo
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8">
            <div className="flex justify-between items-start mb-6">
               <div className="p-4 bg-indigo-50 text-indigo-600 rounded-2xl">
                  <FiTruck size={28} />
               </div>
            </div>
            <p className="text-slate-400 font-bold uppercase tracking-widest text-xs mb-2">Flota Activa</p>
            <h3 className="text-4xl font-black text-slate-900 dark:text-white">05 Unidades</h3>
         </Card>

         <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8">
            <div className="flex justify-between items-start mb-6">
               <div className="p-4 bg-emerald-50 text-emerald-600 rounded-2xl">
                  <FiCheckCircle size={28} />
               </div>
            </div>
            <p className="text-slate-400 font-bold uppercase tracking-widest text-xs mb-2">Disponibilidad</p>
            <h3 className="text-4xl font-black text-slate-900 dark:text-white">80%</h3>
         </Card>

         <Card className="border-none shadow-xl bg-slate-900 text-white p-8 overflow-hidden relative group">
            <div className="absolute right-0 bottom-0 p-8 opacity-10 group-hover:scale-110 transition-transform duration-700">
               <FiShield size={120} />
            </div>
            <p className="text-brand-light font-black uppercase tracking-widest text-[10px] mb-4">Seguros y RTM</p>
            <h3 className="text-2xl font-black leading-tight italic">Toda la flota cuenta con pólizas vigentes.</h3>
         </Card>
      </div>

      <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/10 overflow-hidden">
         <CardHeader className="p-8 border-b border-slate-50 dark:border-white/5 flex flex-row items-center justify-between">
            <CardTitle className="text-xl font-bold flex items-center gap-3 italic text-brand">
               <FiActivity /> Monitor de Operaciones
            </CardTitle>
         </CardHeader>
         <CardContent className="p-0">
            <Table>
               <TableHeader className="bg-slate-50 dark:bg-black/40">
                  <TableRow>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest px-8">Placa / Modelo</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest">Capacidad</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest">Conductor</TableHead>
                     <TableHead className="font-bold text-[10px] uppercase tracking-widest text-center px-8">Estado</TableHead>
                  </TableRow>
               </TableHeader>
               <TableBody>
                  {vehicles.map((v, i) => (
                    <TableRow key={i} className="hover:bg-slate-50 dark:hover:bg-white/5 transition-colors border-slate-50 dark:border-white/5">
                       <TableCell className="px-8 py-6">
                          <div>
                             <p className="font-black text-slate-900 dark:text-white mb-1 uppercase tracking-tighter">{v.placa}</p>
                             <p className="text-[10px] text-slate-400 font-bold">{v.nombre} ({v.tipo_vehiculo})</p>
                          </div>
                       </TableCell>
                       <TableCell className="font-bold text-slate-500">{v.capacidad} PAX</TableCell>
                       <TableCell className="font-bold text-slate-700 dark:text-slate-200">Por Asignar</TableCell>
                       <TableCell className="text-center px-8">
                          <Badge className={v.status === 'AVAILABLE' ? 'bg-emerald-100 text-emerald-700' : 'bg-indigo-100 text-indigo-700'}>
                             {v.status === 'AVAILABLE' ? 'DISPONIBLE' : 'EN SERVICIO'}
                          </Badge>
                       </TableCell>
                       <TableCell className="text-right px-8">
                          <Button
                            variant="ghost"
                            size="sm"
                            className="text-red-500 font-bold"
                            onClick={async () => {
                                if(window.confirm("¿Desvincular vehículo?")) {
                                    await deleteVehicle(v.id);
                                    loadData();
                                }
                            }}
                          >
                              Eliminar
                          </Button>
                       </TableCell>
                    </TableRow>
                  ))}
                  {vehicles.length === 0 && !isLoading && (
                     <TableRow>
                        <TableCell colSpan={4} className="text-center py-20 text-slate-400 italic">
                           No hay vehículos vinculados a la flota.
                        </TableCell>
                     </TableRow>
                  )}
               </TableBody>
            </Table>
         </CardContent>
      </Card>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Vincular Nuevo Vehículo">
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            <div>
                <label className="text-xs font-black uppercase tracking-widest text-slate-400">Placa</label>
                <input {...register('placa', { required: true })} className="w-full p-4 border rounded-2xl dark:bg-brand-deep mt-2" placeholder="ABC-123" />
            </div>
            <div>
                <label className="text-xs font-black uppercase tracking-widest text-slate-400">Nombre / Modelo</label>
                <input {...register('nombre', { required: true })} className="w-full p-4 border rounded-2xl dark:bg-brand-deep mt-2" placeholder="Camioneta Ford" />
            </div>
            <div className="grid grid-cols-2 gap-4">
                <div>
                    <label className="text-xs font-black uppercase tracking-widest text-slate-400">Tipo</label>
                    <select {...register('tipo_vehiculo', { required: true })} className="w-full p-4 border rounded-2xl dark:bg-brand-deep mt-2">
                        <option value="VAN">Van</option>
                        <option value="BUS">Bus</option>
                        <option value="SUV">SUV</option>
                        <option value="OTRO">Otro</option>
                    </select>
                </div>
                <div>
                    <label className="text-xs font-black uppercase tracking-widest text-slate-400">Capacidad</label>
                    <input type="number" {...register('capacidad', { required: true })} className="w-full p-4 border rounded-2xl dark:bg-brand-deep mt-2" placeholder="12" />
                </div>
            </div>
            <Button type="submit" className="w-full bg-brand text-white font-black py-5 rounded-2xl shadow-xl">Vincular a Flota</Button>
        </form>
      </Modal>
    </div>
  );
}
