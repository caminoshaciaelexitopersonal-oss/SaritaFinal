import React, { useState, useEffect } from 'react';
import { AttractionCard, StatGrid, StatCard } from '@sarita/shared-ui';
import axios from 'axios';

export const DescubreTurismo = () => {
  const [atractivos, setAtractivos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/api/atractivos/')
      .then(res => setAtractivos(res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="space-y-8 p-8">
      <header>
        <h1 className="text-3xl font-bold text-blue-900">Descubre Puerto Gaitán</h1>
        <p className="text-gray-600">Explora atractivos, rutas e historia (Desktop Experience)</p>
      </header>

      <StatGrid columns={3}>
        <StatCard title="Atractivos Disponibles" value={atractivos.length} />
        <StatCard title="Rutas Activas" value="12" />
        <StatCard title="Eventos este mes" value="5" />
      </StatGrid>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {atractivos.map((a: any) => (
          <AttractionCard
            key={a.id}
            attraction={{
              id: a.id,
              name: a.nombre,
              description: a.descripcion,
              imageUrl: a.imagen_principal_url,
              category: a.categoria_color
            }}
          />
        ))}
      </div>
    </div>
  );
};
