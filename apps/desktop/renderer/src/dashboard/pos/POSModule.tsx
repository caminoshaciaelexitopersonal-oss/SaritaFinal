import React, { useState } from 'react';
import { Button, Card, Text } from '@sarita/shared-ui';

export default function POSModule() {
  const [cart, setCart] = useState([]);

  const handlePrint = async () => {
    // @ts-ignore
    const res = await window.electron.invoke('print-thermal-receipt', { id: 'POS-001', items: cart });
    alert("Imprimiendo: " + res.status);
  };

  return (
    <div className="p-6 bg-slate-50 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Terminal Punto de Venta (POS)</h1>
      <Card className="mb-4 p-4">
        <Text>Bienvenido a la terminal soberana.</Text>
        <Button onClick={handlePrint} className="mt-4">Imprimir Recibo</Button>
      </Card>
    </div>
  );
}
