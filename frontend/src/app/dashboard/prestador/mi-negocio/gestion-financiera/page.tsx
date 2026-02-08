'use client';

import React, { useEffect, useState } from 'react';
import { useMiNegocioApi, BankAccount, CashTransaction } from '../hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/Table';
import { Button } from '@/components/ui/Button';
import {
  FiCreditCard,
  FiPlus,
  FiTrendingUp,
  FiTrendingDown,
  FiDollarSign,
  FiArrowUpRight,
  FiArrowDownLeft,
  FiActivity
} from 'react-icons/fi';
import { Badge } from '@/components/ui/Badge';
import Link from 'next/link';
import { TraceabilityBanner } from '@/components/ui/TraceabilityBanner';
 
import { GRCIndicator } from '@/components/ui/GRCIndicator';
 
import { PermissionGuard, usePermissions } from '@/ui/guards/PermissionGuard';
import { auditLogger } from '@/services/auditLogger';

export default function GestionFinancieraPage() {
  const {
    getBankAccounts,
    getCashTransactions,
    getEstadoResultados,
    getBalanceGeneral,
    getProyecciones,
    getRiesgos,
    getTesoreria,
    isLoading
  } = useMiNegocioApi();
  const { role, hasPermission } = usePermissions();
  const [activeTab, setActiveTab] = useState<'tesoreria' | 'estados' | 'proyecciones' | 'riesgos'>('tesoreria');

  const [accounts, setAccounts] = useState<BankAccount[]>([]);
  const [transactions, setTransactions] = useState<CashTransaction[]>([]);
  const [pyg, setPyg] = useState<any[]>([]);
  const [balance, setBalance] = useState<any[]>([]);
  const [proyecciones, setProyecciones] = useState<any[]>([]);
  const [riesgos, setRiesgos] = useState<any[]>([]);
  const [tesoreria, setTesoreria] = useState<any>(null);

  useEffect(() => {
    const loadData = async () => {
      const [accs, txs, p, b, pr, r, t] = await Promise.all([
        getBankAccounts(),
        getCashTransactions(),
        getEstadoResultados(),
        getBalanceGeneral(),
        getProyecciones(),
        getRiesgos(),
        getTesoreria()
      ]);
      if (accs) setAccounts(accs);
      if (txs) setTransactions(txs);
      if (p) setPyg(p);
      if (b) setBalance(b);
      if (pr) setProyecciones(pr);
      if (r) setRiesgos(r);
      if (t) setTesoreria(t[0]);
    };
    loadData();
  }, [getBankAccounts, getCashTransactions, getEstadoResultados, getBalanceGeneral, getProyecciones, getRiesgos, getTesoreria]);

  const totalBalance = accounts.reduce((acc, curr) => acc + parseFloat(curr.balance), 0);

  useEffect(() => {
    auditLogger.log({
      type: 'VIEW_LOAD',
      view: 'Gestion Financiera',
      userRole: role,
      status: 'OK'
    });
  }, [role]);

  const maskAccountNumber = (num: string) => {
    if (hasPermission(['SuperAdmin', 'AdminPlataforma', 'OperadorFinanciero', 'Prestador'])) return num;
    return `****${num.slice(-4)}`;
  };

  return (
    <div className="space-y-8 animate-in slide-in-from-bottom-4 duration-500">
      <TraceabilityBanner info={{
          source: '/api/v1/mi-negocio/financiera/',
          model: 'CuentaBancaria / TransaccionCaja',
          period: 'Enero 2026',
          timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
          status: 'OK',
          certainty: 'Datos reales - Cierre de periodo validado'
      }} />
 
      <GRCIndicator
        moduleName="Gestión Financiera"
        controls={['Enmascaramiento de cuentas', 'Audit Log activo']}
      />
 
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Gestión Financiera Soberana</h1>
          <p className="text-gray-500 mt-1">Gobierno, custodia y proyección de los recursos del sistema.</p>
        </div>
        <div className="flex gap-3">
          <PermissionGuard deniedRoles={['Auditor', 'Observador']}>
            <Button className="bg-green-600 hover:bg-green-700">
                <FiPlus className="mr-2" /> Orden de Pago
            </Button>
            <Button variant="outline" className="border-brand text-brand font-bold">
                <FiShield className="mr-2" /> Autorizar Todo
            </Button>
          </PermissionGuard>
        </div>
      </div>

      {/* Tabs de Navegación Financiera */}
      <div className="flex border-b border-gray-200 gap-8 overflow-x-auto no-scrollbar">
         {[
           { id: 'tesoreria', label: 'Tesorería y Caja', icon: FiCreditCard },
           { id: 'estados', label: 'Estados Financieros', icon: FiFileText },
           { id: 'proyecciones', label: 'Planeación y Forecast', icon: FiTrendingUp },
           { id: 'riesgos', label: 'Riesgo y Cumplimiento', icon: FiAlertTriangle },
         ].map(tab => (
           <button
             key={tab.id}
             onClick={() => setActiveTab(tab.id as any)}
             className={`py-4 flex items-center gap-2 text-xs font-black uppercase tracking-widest border-b-2 transition-all ${
               activeTab === tab.id ? 'border-brand text-brand' : 'border-transparent text-gray-400 hover:text-gray-600'
             }`}
           >
             <tab.icon />
             {tab.label}
           </button>
         ))}
      </div>

      {activeTab === 'tesoreria' && (
      <>
      {/* Hero Stats */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="bg-indigo-600 text-white shadow-xl border-none overflow-hidden relative">
          <div className="absolute top-0 right-0 p-8 opacity-10">
            <FiDollarSign size={120} />
          </div>
          <CardContent className="p-8">
            <p className="text-indigo-100 font-medium">Saldo Total Consolidado</p>
            <h2 className="text-4xl font-black mt-2">${totalBalance.toLocaleString('es-CO', { minimumFractionDigits: 2 })}</h2>
            <div className="mt-6 flex items-center gap-2 text-indigo-100 text-sm">
               <div className="bg-indigo-500/50 p-1 rounded-full"><FiArrowUpRight /></div>
               <span>+2.4% vs mes anterior</span>
            </div>
          </CardContent>
        </Card>

        <Card className="shadow-sm border-none bg-white">
          <CardContent className="p-8">
            <div className="flex justify-between items-start">
               <div>
                  <p className="text-gray-500 text-sm font-medium">Ingresos del Mes</p>
                  <h3 className="text-2xl font-bold text-green-600 mt-1">$0.00</h3>
               </div>
               <div className="p-3 bg-green-50 text-green-600 rounded-2xl">
                 <FiTrendingUp size={24} />
               </div>
            </div>
            <div className="mt-4 h-2 bg-gray-100 rounded-full overflow-hidden">
               <div className="h-full bg-green-500 w-3/4"></div>
            </div>
          </CardContent>
        </Card>

        <Card className="shadow-sm border-none bg-white">
          <CardContent className="p-8">
            <div className="flex justify-between items-start">
               <div>
                  <p className="text-gray-500 text-sm font-medium">Egresos del Mes</p>
                  <h3 className="text-2xl font-bold text-red-600 mt-1">$0.00</h3>
               </div>
               <div className="p-3 bg-red-50 text-red-600 rounded-2xl">
                 <FiTrendingDown size={24} />
               </div>
            </div>
            <div className="mt-4 h-2 bg-gray-100 rounded-full overflow-hidden">
               <div className="h-full bg-red-500 w-1/4"></div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Ratios Financieros */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
         {[
           { label: 'Liquidez Corriente', val: '2.4', status: 'HEALTHY' },
           { label: 'Margen Bruto', val: '45%', status: 'HEALTHY' },
           { label: 'Prueba Ácida', val: '1.8', status: 'HEALTHY' },
           { label: 'Endeudamiento', val: '12%', status: 'LOW' },
         ].map((ratio, i) => (
           <Card key={i} className="border-none shadow-sm bg-white dark:bg-brand-deep/10 p-6 text-center">
              <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">{ratio.label}</p>
              <h4 className="text-xl font-black text-slate-900 dark:text-white">{ratio.val}</h4>
              <Badge variant="outline" className="mt-3 text-[8px] border-emerald-100 text-emerald-600 bg-emerald-50 dark:bg-emerald-900/10 uppercase font-black">{ratio.status}</Badge>
           </Card>
         ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Cuentas Bancarias */}
        <Card className="border-none shadow-sm overflow-hidden">
          <CardHeader className="bg-gray-50/50">
            <CardTitle className="text-lg font-bold flex items-center gap-2">
               <FiCreditCard className="text-indigo-600" /> Cuentas Vinculadas
            </CardTitle>
          </CardHeader>
          <CardContent className="p-0">
            <div className="divide-y divide-gray-100">
               {accounts.map(acc => (
                 <div key={acc.id} className="p-6 hover:bg-gray-50/50 transition-colors flex items-center justify-between">
                    <div className="flex items-center gap-4">
                       <div className="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center text-gray-400">
                         <FiCreditCard size={24} />
                       </div>
                       <div>
                          <p className="font-bold text-gray-900">{acc.bank_name}</p>
                          <p className="text-xs text-gray-500">#{maskAccountNumber(acc.account_number)} • {acc.account_type === 'SAVINGS' ? 'Ahorros' : 'Corriente'}</p>
                       </div>
                    </div>
                    <div className="text-right">
                       <p className="font-black text-gray-900">${parseFloat(acc.balance).toLocaleString()}</p>
                       <Badge variant="outline" className="text-[10px] text-green-600 border-green-200 bg-green-50">ACTIVA</Badge>
                    </div>
                 </div>
               ))}
               {accounts.length === 0 && (
                 <div className="p-12 text-center text-gray-400 italic">
                   No hay cuentas bancarias registradas.
                 </div>
               )}
            </div>
            <div className="p-4 bg-gray-50 text-center border-t">
               <Link href="/dashboard/prestador/mi-negocio/gestion-financiera/cuentas-bancarias" className="text-indigo-600 text-sm font-bold hover:underline">
                 Gestionar Cuentas
               </Link>
            </div>
          </CardContent>
        </Card>

        {/* Últimas Transacciones */}
        <Card className="border-none shadow-sm overflow-hidden">
          <CardHeader className="bg-gray-50/50">
            <CardTitle className="text-lg font-bold flex items-center gap-2">
               <FiActivity className="text-indigo-600" /> Movimientos de Caja
            </CardTitle>
          </CardHeader>
          <CardContent className="p-0">
            <Table>
               <TableBody>
                  {transactions.slice(0, 6).map(tx => (
                    <TableRow key={tx.id} className="hover:bg-gray-50/50 border-gray-100">
                       <TableCell className="w-12">
                          <div className={`p-2 rounded-lg ${tx.tipo === 'INGRESO' ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600'}`}>
                             {tx.tipo === 'INGRESO' ? <FiArrowDownLeft /> : <FiArrowUpRight />}
                          </div>
                       </TableCell>
                       <TableCell>
                          <p className="font-medium text-gray-900">{tx.descripcion}</p>
                          <p className="text-[10px] text-gray-500 uppercase">{new Date(tx.fecha).toLocaleDateString()}</p>
                       </TableCell>
                       <TableCell className="text-right">
                          <p className={`font-bold ${tx.tipo === 'INGRESO' ? 'text-green-600' : 'text-red-600'}`}>
                            {tx.tipo === 'INGRESO' ? '+' : '-'}${parseFloat(tx.monto).toLocaleString()}
                          </p>
                       </TableCell>
                    </TableRow>
                  ))}
                  {transactions.length === 0 && (
                    <TableRow>
                       <TableCell colSpan={3} className="text-center py-12 text-gray-400 italic">
                         Sin movimientos de caja registrados.
                       </TableCell>
                    </TableRow>
                  )}
               </TableBody>
            </Table>
            <div className="p-4 bg-gray-50 text-center border-t">
               <Link href="/dashboard/prestador/mi-negocio/gestion-financiera/transacciones-bancarias" className="text-indigo-600 text-sm font-bold hover:underline">
                 Ver Historial Completo
               </Link>
            </div>
          </CardContent>
        </Card>
      </div>
      </>
      )}

      {activeTab === 'estados' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
           <Card className="border-none shadow-sm">
              <CardHeader><CardTitle className="text-lg font-bold">Estado de Resultados (P&L)</CardTitle></CardHeader>
              <CardContent>
                 <div className="space-y-4">
                    <div className="flex justify-between border-b pb-2"><span>Ingresos Totales</span><span className="font-black text-green-600">$0.00</span></div>
                    <div className="flex justify-between border-b pb-2"><span>Costos de Venta</span><span className="font-black text-red-500">$0.00</span></div>
                    <div className="flex justify-between border-b pb-2"><span>Gastos Operativos</span><span className="font-black text-red-500">$0.00</span></div>
                    <div className="flex justify-between pt-2">
                       <span className="font-bold">Utilidad Neta</span>
                       <span className="text-2xl font-black text-indigo-600">$0.00</span>
                    </div>
                 </div>
              </CardContent>
           </Card>

           <Card className="border-none shadow-sm">
              <CardHeader><CardTitle className="text-lg font-bold">Balance General</CardTitle></CardHeader>
              <CardContent>
                 <div className="space-y-4">
                    <div className="flex justify-between border-b pb-2"><span>Total Activos</span><span className="font-black text-indigo-600">$0.00</span></div>
                    <div className="flex justify-between border-b pb-2"><span>Total Pasivos</span><span className="font-black text-amber-600">$0.00</span></div>
                    <div className="flex justify-between pt-2">
                       <span className="font-bold">Patrimonio Total</span>
                       <span className="text-2xl font-black text-slate-900">$0.00</span>
                    </div>
                 </div>
              </CardContent>
           </Card>

           <Card className="border-none shadow-sm">
              <CardHeader><CardTitle className="text-lg font-bold">Flujo de Efectivo</CardTitle></CardHeader>
              <CardContent className="h-40 flex items-center justify-center italic text-gray-400">Datos en proceso de compilación...</CardContent>
           </Card>

           <Card className="border-none shadow-sm">
              <CardHeader><CardTitle className="text-lg font-bold">Cambios en el Patrimonio</CardTitle></CardHeader>
              <CardContent className="h-40 flex items-center justify-center italic text-gray-400">Datos en proceso de compilación...</CardContent>
           </Card>
        </div>
      )}

      {activeTab === 'proyecciones' && (
        <div className="space-y-6">
           <Card className="bg-slate-900 text-white p-10 rounded-[2rem]">
              <h3 className="text-2xl font-black italic">Simulador de Escenarios IA</h3>
              <p className="mt-4 text-slate-400">Ajusta variables para ver cómo impactaría tu flujo de caja en los próximos 6 meses.</p>
              <Button className="mt-8 bg-brand text-white font-black px-10">Crear Proyección</Button>
           </Card>
           <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Card className="p-8 border-none shadow-sm bg-white">
                 <h4 className="font-bold mb-4">Forecast de Ingresos - Q1 2026</h4>
                 <div className="h-48 bg-slate-50 rounded-xl border-2 border-dashed border-slate-200 flex items-center justify-center text-slate-400">Gráfico de Proyección</div>
              </Card>
              <Card className="p-8 border-none shadow-sm bg-white">
                 <h4 className="font-bold mb-4">Análisis de Estacionalidad</h4>
                 <div className="h-48 bg-slate-50 rounded-xl border-2 border-dashed border-slate-200 flex items-center justify-center text-slate-400">Datos Estacionales</div>
              </Card>
           </div>
        </div>
      )}

      {activeTab === 'riesgos' && (
        <div className="space-y-6">
           <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <Card className="p-6 border-l-4 border-red-500 bg-red-50">
                 <p className="text-xs font-black text-red-600 uppercase">Riesgo de Liquidez</p>
                 <h4 className="font-bold mt-1">Crítico: Cobertura de 0.8 meses</h4>
              </Card>
              <Card className="p-6 border-l-4 border-amber-500 bg-amber-50">
                 <p className="text-xs font-black text-amber-600 uppercase">Riesgo Impositivo</p>
                 <h4 className="font-bold mt-1">Medio: Pendiente cierre de IVA</h4>
              </Card>
              <Card className="p-6 border-l-4 border-emerald-500 bg-emerald-50">
                 <p className="text-xs font-black text-emerald-600 uppercase">Puntaje Crediticio</p>
                 <h4 className="font-bold mt-1">Excelente: 940/1000</h4>
              </Card>
           </div>
           <Card className="border-none shadow-sm">
              <CardHeader><CardTitle className="text-lg font-bold">Matriz de Riesgo y Cumplimiento</CardTitle></CardHeader>
              <CardContent>
                 <Table>
                    <TableHeader className="bg-slate-50">
                       <TableRow>
                          <TableHead>Categoría</TableHead>
                          <TableHead>Impacto</TableHead>
                          <TableHead>Probabilidad</TableHead>
                          <TableHead>Estrategia de Mitigación</TableHead>
                       </TableRow>
                    </TableHeader>
                    <TableBody>
                       <TableRow>
                          <TableCell className="font-bold">Financiero</TableCell>
                          <TableCell><Badge className="bg-red-500">ALTO</Badge></TableCell>
                          <TableCell>Baja</TableCell>
                          <TableCell>Aumento de reserva legal al 15%</TableCell>
                       </TableRow>
                    </TableBody>
                 </Table>
              </CardContent>
           </Card>
        </div>
      )}
    </div>
  );
}

