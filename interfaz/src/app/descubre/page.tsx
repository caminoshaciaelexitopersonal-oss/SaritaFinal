'use client';

import React from 'react';
import { AttractionCard, EventCalendar, InteractiveRouteMap } from '@sarita/shared-ui';

const TOURIST_MOCK = {
  attractions: [
    { id: '1', name: 'Río Manacacías', category: 'Naturaleza', description: 'Avistamiento de delfines rosados y atardeceres únicos.', imageUrl: 'https://images.unsplash.com/photo-1501785888041-af3ef285b470' },
    { id: '2', name: 'Arco de la Maloca', category: 'Cultura', description: 'Monumento emblemático de la cultura llanera.', imageUrl: 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b' }
  ],
  events: [
    { id: '1', title: 'Festival del Retorno', date: 'Octubre 2026', location: 'Plaza Principal' },
    { id: '2', title: 'Muestra Gastronómica', date: 'Abril 12', location: 'Puerto Malecón' }
  ],
  route: {
    name: 'Ruta del Amanecer Llanero',
    points: [
      { label: 'Puerto Gaitán', type: 'Punto de Inicio' },
      { label: 'Mirador del Manacacías', type: 'Atractivo Natural' },
      { label: 'Finca La Esperanza', type: 'Agroturismo' }
    ]
  }
};

export default function DescubrePage() {
  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f9fafb', padding: '40px' }}>
      <h1 style={{ fontSize: '32px', fontWeight: 'bold', color: '#1e40af', marginBottom: '40px' }}>Descubre el Paraíso</h1>

      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '32px' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '32px' }}>
          <section>
            <h2 style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '16px' }}>Atractivos Destacados</h2>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
              {TOURIST_MOCK.attractions.map(attr => (
                <AttractionCard key={attr.id} attraction={attr} />
              ))}
            </div>
          </section>

          <InteractiveRouteMap routeName={TOURIST_MOCK.route.name} points={TOURIST_MOCK.route.points} />
        </div>

        <aside>
          <EventCalendar events={TOURIST_MOCK.events} />
        </aside>
      </div>
    </div>
  );
}
