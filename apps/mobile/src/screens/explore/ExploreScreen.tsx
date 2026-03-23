import React, { useEffect, useMemo, useState } from 'react';
import { View, ScrollView, StyleSheet, ActivityIndicator, Text } from 'react-native';
import { AttractionCard, EventCalendar, InteractiveRouteMap } from '@sarita/shared-ui';
import { api } from '../../services/api';

type AttractionItem = {
  id: string | number;
  name: string;
  category?: string;
  description?: string;
  imageUrl?: string;
};

type EventItem = {
  id: string | number;
  title: string;
  date?: string;
  location?: string;
};

type RoutePoint = {
  label: string;
  type?: string;
};

export const ExploreScreen = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [attractions, setAttractions] = useState<AttractionItem[]>([]);
  const [events, setEvents] = useState<EventItem[]>([]);
  const [routePoints, setRoutePoints] = useState<RoutePoint[]>([]);

  useEffect(() => {
    let isMounted = true;

    const loadTouristData = async () => {
      try {
        setLoading(true);
        setError(null);

const [attractionsResponse, eventsResponse] = await Promise.all([
          api.get('/v1/turismo/providers/'),
          api.get('/publicaciones/', { params: { tipo: 'evento' } })
        ]);

        if (!isMounted) return;

        const attractionsData = Array.isArray(attractionsResponse?.data?.results)
          ? attractionsResponse.data.results
          : Array.isArray(attractionsResponse?.data)
            ? attractionsResponse.data
            : [];

        const eventsData = Array.isArray(eventsResponse?.data?.results)
          ? eventsResponse.data.results
          : Array.isArray(eventsResponse?.data)
            ? eventsResponse.data
            : [];

        setAttractions(
          attractionsData.slice(0, 10).map((item: any, index: number) => ({
            id: item.id ?? `attr-${index}`,
            name: item.nombre || item.name || 'Atractivo turístico',
            category: item.categoria || item.category || 'Turismo',
            description: item.descripcion || item.description || '',
            imageUrl: item.imagen || item.image || item.imageUrl || undefined
          }))
        );

        setEvents(
          eventsData.slice(0, 10).map((item: any, index: number) => ({
            id: item.id ?? `event-${index}`,
            title: item.titulo || item.title || 'Evento turístico',
            date: item.fecha || item.date || '',
            location: item.ubicacion || item.location || ''
          }))
        );

        setRoutePoints(
          attractionsData.slice(0, 5).map((item: any) => ({
            label: item.nombre || item.name || 'Punto turístico',
            type: item.categoria || item.category || 'Atractivo'
          }))
        );
      } catch (e) {
        if (isMounted) {
          setError('No fue posible cargar la información turística en este momento.');
        }
      } finally {
        if (isMounted) setLoading(false);
      }
    };

    loadTouristData();
    return () => {
      isMounted = false;
    };
  }, []);

  const routeName = useMemo(() => 'Ruta Turística Sugerida', []);

  if (loading) {
    return (
      <View style={styles.centerState}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.centerState}>
        <Text style={styles.errorText}>{error}</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={{ marginBottom: 30 }}>
        <InteractiveRouteMap routeName={routeName} points={routePoints} />
      </View>

      <EventCalendar events={events} />

      <View style={{ marginTop: 30 }}>
        {attractions.map((attr: AttractionItem) => (
          <AttractionCard key={attr.id} attraction={attr} />
        ))}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  content: { padding: 16 },
  centerState: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 24 },
  errorText: { color: '#b91c1c', textAlign: 'center' }
});
