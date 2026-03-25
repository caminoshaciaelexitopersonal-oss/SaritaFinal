import React, { useState } from 'react';
import { Button, Card, Text } from '@sarita/shared-ui';

import { ShoppingCart, Printer, Search, User } from 'lucide-react';

export default function POSModule() {
  const [cart, setCart] = useState<any[]>([]);
  const [search, setSearch] = useState('');

  const handlePrint = async () => {
    // @ts-ignore
    const res = await window.electron.invoke('print-thermal-receipt', {
        id: `TX-${Date.now()}`,
        items: cart,
        total: cart.reduce((a, b) => a + b.price, 0)
    });
    alert("Estado Impresión: " + res.status);
  };

  const handleScanID = async () => {
      // @ts-ignore
      const res = await window.electron.invoke('scan-identity-document');
      if (res.status === 'SUCCESS') {
          alert(`Cliente identificado: ${res.data.name}`);
      }
  };

  return (
    <div className="flex h-screen bg-slate-100 overflow-hidden">
        {/* Left: Product Selection */}
        <div className="flex-1 p-6 flex flex-col">
            <div className="flex justify-between items-center mb-8">
                <h1 className="text-3xl font-black text-slate-900 tracking-tighter uppercase">Terminal Soberana POS</h1>
                <div className="flex gap-2">
                    <button onClick={handleScanID} className="bg-white border p-3 rounded-xl shadow-sm hover:bg-slate-50 flex items-center gap-2 font-bold text-xs">
                        <User size={16} /> ESCANEAR CÉDULA
                    </button>
                </div>
            </div>

            <div className="relative mb-6">
                <Search className="absolute left-4 top-3.5 text-slate-400" size={20} />
                <input
                    className="w-full bg-white border-none shadow-sm rounded-2xl py-4 pl-12 pr-6 font-medium outline-none focus:ring-2 ring-indigo-500 transition-all"
                    placeholder="Buscar producto por nombre o código de barras..."
                    value={search}
                    onChange={e => setSearch(e.target.value)}
                />
            </div>

            <div className="grid grid-cols-3 gap-4 overflow-y-auto">
                {/* Mock products for POS layout maturity */}
                {[
                    {id: 1, name: 'Cena Llanera', price: 45000, cat: 'Gastronomía'},
                    {id: 2, name: 'Tour Río Meta', price: 120000, cat: 'Servicios'},
                    {id: 3, name: 'Artesanía Palma', price: 15000, cat: 'Productos'},
                ].map(p => (
                    <button key={p.id} onClick={() => setCart([...cart, p])} className="bg-white p-6 rounded-3xl shadow-sm hover:shadow-md border-2 border-transparent hover:border-indigo-500 transition-all text-left group">
                        <span className="text-[10px] font-black text-indigo-500 uppercase tracking-widest">{p.cat}</span>
                        <h4 className="font-bold text-slate-800 text-lg mt-1">{p.name}</h4>
                        <p className="text-xl font-black text-slate-900 mt-4">${p.price.toLocaleString()}</p>
                    </button>
                ))}
            </div>
        </div>

        {/* Right: Checkout Sidebar */}
        <div className="w-[400px] bg-white border-l shadow-2xl flex flex-col">
            <div className="p-8 border-b">
                <div className="flex items-center gap-3">
                    <ShoppingCart className="text-slate-900" />
                    <h2 className="text-xl font-black uppercase italic tracking-tight">Cuenta Actual</h2>
                </div>
            </div>

            <div className="flex-1 overflow-y-auto p-8 space-y-4">
                {cart.map((item, i) => (
                    <div key={i} className="flex justify-between items-center bg-slate-50 p-4 rounded-2xl">
                        <div>
                            <p className="font-bold text-sm text-slate-800">{item.name}</p>
                            <p className="text-[10px] text-slate-400 font-black uppercase">1 UNIDAD</p>
                        </div>
                        <p className="font-black text-slate-900">${item.price.toLocaleString()}</p>
                    </div>
                ))}
                {cart.length === 0 && (
                    <div className="h-full flex flex-col items-center justify-center text-slate-300 opacity-50">
                        <ShoppingCart size={64} className="mb-4" />
                        <p className="font-black uppercase tracking-widest text-xs">Carrito Vacío</p>
                    </div>
                )}
            </div>

            <div className="p-8 bg-slate-900 text-white rounded-t-[3rem] space-y-6">
                <div className="flex justify-between items-center">
                    <span className="text-slate-400 font-bold uppercase text-xs tracking-widest">Total a Pagar</span>
                    <span className="text-4xl font-black italic tracking-tighter">
                        ${cart.reduce((a, b) => a + b.price, 0).toLocaleString()}
                    </span>
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <button className="bg-white/10 hover:bg-white/20 py-4 rounded-2xl font-black uppercase tracking-widest text-[10px] transition-all">EFECTIVO</button>
                    <button className="bg-indigo-600 hover:bg-indigo-500 py-4 rounded-2xl font-black uppercase tracking-widest text-[10px] shadow-lg shadow-indigo-600/20 transition-all">TARJETA / WALLET</button>
                </div>

                <button
                    onClick={handlePrint}
                    disabled={cart.length === 0}
                    className="w-full bg-white text-slate-900 py-6 rounded-2xl font-black uppercase tracking-widest text-xs flex items-center justify-center gap-3 disabled:opacity-50"
                >
                    <Printer size={20} /> FINALIZAR E IMPRIMIR RECIBO
                </button>
            </div>
        </div>
    </div>
  );
}
