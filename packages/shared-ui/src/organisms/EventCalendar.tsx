import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, Platform, StyleSheet } from 'react-native';

interface Event {
  id: string;
  title: string;
  date: string;
  location: string;
}

interface EventCalendarProps {
  events: Event[];
}

export const EventCalendar: React.FC<EventCalendarProps> = ({ events }) => {
  const isWeb = Platform.OS === 'web';

  return (
    <View style={isWeb ? undefined : styles.nativeContainer}>
      <Text variant="headingM" style={{ marginBottom: 16 }}>Agenda Cultural</Text>
      <View style={isWeb ? { display: 'flex', flexDirection: 'column', gap: '12px' } : { gap: 12 }}>
        {events.map(event => (
          <Card key={event.id} padding="sm">
            <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
               <View style={{ flex: 1 }}>
                 <Text variant="headingS">{event.title}</Text>
                 <Text variant="caption">{event.location}</Text>
               </View>
               <View style={{ alignItems: 'flex-end' }}>
                 <Text variant="small" color="primary" style={{ fontWeight: 'bold' }}>{event.date}</Text>
               </View>
            </View>
          </Card>
        ))}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  nativeContainer: { paddingVertical: 12 }
});
