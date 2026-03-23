import React, { useState } from 'react';
import { commercialService } from './commercialService';

const POSInterface = () => {
  const [total, setTotal] = useState(0);
  const [clienteId, setClienteId] = useState('');

const handleVenta = async () => {
    const res = await commercialService.posVentaRapida({ total, cliente_id: clienteId });
    const facturaRes = await commercialService.triggerDian(res.id);  // New method
    alert(`Factura CUFE: ${facturaRes.cufe} - Enviada DIAN/Email`);
    setTotal(0);
  };

  return (
    <div className="p-6 border rounded">
      <h2>POS Rápido</h2>
      <input value={clienteId} onChange={(e) => setClienteId(e.target.value)} placeholder="Cliente ID" />
      <input value={total} type="number" onChange={(e) => setTotal(Number(e.target.value))} />
      <button onClick={handleVenta}>Generar Factura</button>
    </div>
  );
};

export default POSInterface;

