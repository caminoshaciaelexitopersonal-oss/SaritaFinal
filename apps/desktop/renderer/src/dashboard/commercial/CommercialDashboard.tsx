import React, { useEffect, useState } from 'react';
import { commercialService } from './commercialService';

const CommercialDashboard = () => {
  const [stats, setStats] = useState({ totalVentas: 0, opsMes: 0, clientesActivos: 0 });

  useEffect(() => {
    commercialService.getStats().then(setStats);
  }, []);

  return (
    <div className="grid grid-cols-3 gap-4">
      <div className="bg-blue-500 text-white p-4 rounded">
        <h3>Ventas Total</h3>
        <p>${stats.totalVentas}</p>
      </div>
      <div className="bg-green-500 text-white p-4 rounded">
        <h3>Ops Mes</h3>
        <p>{stats.opsMes}</p>
      </div>
      <div className="bg-purple-500 text-white p-4 rounded">
        <h3>Clientes</h3>
        <p>{stats.clientesActivos}</p>
      </div>
    </div>
  );
};

export default CommercialDashboard;

