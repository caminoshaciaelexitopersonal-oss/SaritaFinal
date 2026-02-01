'use client';

import React, { useState } from 'react';
import useSWR from 'swr';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import {
  FiBriefcase,
  FiPlus,
  FiHome,
  FiStar,
  FiUsers,
  FiActivity,
  FiSettings,
  FiGrid
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import api from '@/services/api';

interface Product { name: string; base_price: string; }
interface Amenity { id: number; nombre: string; }
interface RoomType { id: number; product: Product; capacidad: number; amenities: Amenity[]; }

const fetcher = (url: string) => api.get(url).then(res => res.data.results || []);

export default function HotelManagementPage() {
    const { data: roomTypes, error, isLoading } = useSWR<RoomType[]>('/v1/mi-negocio/operativa/modulos-especializados/hoteles/room-types/', fetcher);
    const [selectedRoomTypeId, setSelectedRoomTypeId] = useState<number | null>(null);

    return (
        <div className="space-y-10 animate-in fade-in duration-700">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div>
                    <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight uppercase italic">Operación Hotelera</h1>
                    <p className="text-slate-500 dark:text-slate-400 mt-1 text-lg">Control de inventario de habitaciones, amenidades y servicios de alojamiento.</p>
                </div>
                <Button className="bg-brand text-white font-black px-8 py-6 rounded-2xl shadow-xl shadow-brand/20 transition-all">
                    <FiPlus className="mr-2" /> Definir Tipo de Habitación
                </Button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
               <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8">
                  <div className="flex justify-between items-start mb-6">
                     <div className="p-4 bg-indigo-50 text-indigo-600 rounded-2xl">
                        <FiHome size={28} />
                     </div>
                  </div>
                  <p className="text-slate-400 font-bold uppercase tracking-widest text-[10px] mb-2">Unidades Totales</p>
                  <h3 className="text-4xl font-black text-slate-900 dark:text-white">12</h3>
               </Card>

               <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/20 p-8">
                  <div className="flex justify-between items-start mb-6">
                     <div className="p-4 bg-emerald-50 text-emerald-600 rounded-2xl">
                        <FiUsers size={28} />
                     </div>
                  </div>
                  <p className="text-slate-400 font-bold uppercase tracking-widest text-[10px] mb-2">Capacidad Máxima</p>
                  <h3 className="text-4xl font-black text-slate-900 dark:text-white">42</h3>
               </Card>

               <Card className="border-none shadow-xl bg-slate-900 text-white p-8 overflow-hidden relative group">
                  <div className="absolute right-0 bottom-0 p-8 opacity-10 group-hover:scale-110 transition-transform duration-700">
                     <FiActivity size={120} />
                  </div>
                  <p className="text-brand-light font-black uppercase tracking-widest text-[10px] mb-4">Estatus IA</p>
                  <h3 className="text-2xl font-black leading-tight italic">Optimización de precios por temporada activa.</h3>
               </Card>
            </div>

            <Card className="border-none shadow-sm bg-white dark:bg-brand-deep/10 overflow-hidden rounded-[2rem]">
                <CardHeader className="p-8 border-b border-slate-50 dark:border-white/5 flex flex-row items-center justify-between bg-white dark:bg-black/40">
                   <CardTitle className="text-xl font-bold flex items-center gap-3 italic text-brand">
                      <FiGrid /> Tipos de Inventario
                   </CardTitle>
                   <Button variant="ghost" className="text-brand font-black text-xs uppercase tracking-widest">Ver Mapa de Habitaciones</Button>
                </CardHeader>
                <CardContent className="p-0">
                    <div className="divide-y divide-slate-50 dark:divide-white/5">
                        {roomTypes?.map(rt => (
                            <div key={rt.id} className="p-8 hover:bg-slate-50 dark:hover:bg-white/5 transition-all">
                                <div className="flex flex-col md:flex-row md:items-center justify-between gap-8">
                                    <div className="flex items-center gap-6">
                                       <div className="w-16 h-16 bg-slate-100 dark:bg-black/20 rounded-2xl flex items-center justify-center text-slate-400">
                                          <FiHome size={24} />
                                       </div>
                                       <div>
                                          <h3 className="text-xl font-black text-slate-900 dark:text-white uppercase tracking-tighter italic">{rt.product.name}</h3>
                                          <p className="text-sm text-slate-500 font-medium">Capacidad: {rt.capacidad} personas | Precio Base: ${rt.product.base_price}</p>
                                       </div>
                                    </div>
                                    <div className="flex gap-2">
                                       <Button variant="outline" className="border-slate-200 dark:border-white/10 font-bold h-12 px-6"><FiSettings className="mr-2" /> Configurar</Button>
                                       <Button className="bg-brand text-white font-black h-12 px-8">Audit</Button>
                                    </div>
                                </div>
                            </div>
                        ))}
                        {roomTypes?.length === 0 && !isLoading && (
                            <div className="p-32 text-center">
                                <FiHome size={64} className="mx-auto text-slate-200 mb-6" />
                                <h3 className="text-xl font-black text-slate-400 uppercase tracking-widest">Sin Configuración de Inventario</h3>
                                <p className="text-slate-500 mt-2">Define los tipos de habitación para habilitar la venta en la Triple Vía.</p>
                            </div>
                        )}
                        {isLoading && (
                           <div className="p-20 space-y-6">
                              {[...Array(2)].map((_, i) => <div key={i} className="h-20 bg-slate-50 dark:bg-white/5 rounded-2xl animate-pulse" />)}
                           </div>
                        )}
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}
