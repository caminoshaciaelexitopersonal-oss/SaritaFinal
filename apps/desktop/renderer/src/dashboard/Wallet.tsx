import React from 'react';

export const WalletDashboard = () => (
  <div className="space-y-6">
    <div className="bg-white p-8 rounded-lg shadow-sm">
      <h2 className="text-xl font-bold text-primary mb-4">SARITA Wallet</h2>
      <div className="bg-primary text-white p-10 rounded-xl mb-10 flex justify-between items-center">
        <div>
          <p className="opacity-70 text-sm">Saldo en Cartera</p>
          <p className="text-4xl font-bold mt-2">$2,450.00 USD</p>
        </div>
        <button className="bg-secondary text-primary px-8 py-3 rounded-lg font-bold hover:bg-yellow-500 transition">
          Retirar Fondos
        </button>
      </div>

      <h3 className="font-bold mb-4">Transacciones Recientes</h3>
      <table className="w-full text-left">
        <thead>
          <tr className="text-gray-400 text-sm border-b">
            <th className="pb-4">Concepto</th>
            <th className="pb-4">Fecha</th>
            <th className="pb-4">Estado</th>
            <th className="pb-4 text-right">Monto</th>
          </tr>
        </thead>
        <tbody className="text-gray-600">
          <tr className="border-b">
            <td className="py-4">Venta Safari Río Meta</td>
            <td>07 Mar 2026</td>
            <td className="text-green-500 font-medium">Completado</td>
            <td className="text-right font-bold">$120.00</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
);
