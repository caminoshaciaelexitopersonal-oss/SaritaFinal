import React from 'react';
import { View, ScrollView, StyleSheet } from 'react-native';
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

export const ExploreScreen = () => {
  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={{ marginBottom: 30 }}>
         <InteractiveRouteMap routeName={TOURIST_MOCK.route.name} points={TOURIST_MOCK.route.points} />
      </View>

      <EventCalendar events={TOURIST_MOCK.events} />

      <View style={{ marginTop: 30 }}>
        {TOURIST_MOCK.attractions.map(attr => (
          <AttractionCard key={attr.id} attraction={attr} />
        ))}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  content: { padding: 16 }
});
