import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, Platform, StyleSheet } from 'react-native';

interface Reservation {
  id: string;
  client: string;
  service: string;
  startDate: string;
  endDate: string;
  status: 'PENDIENTE' | 'CONFIRMADA' | 'EN_CURSO' | 'FINALIZADA' | 'CANCELADA';
  price: string;
}

export const ReservationCard: React.FC<{ reservation: Reservation; onPress?: () => void }> = ({ reservation, onPress }) => {
  const getStatusColor = () => {
    switch (reservation.status) {
      case 'CONFIRMADA': return '#10b981';
      case 'EN_CURSO': return '#3b82f6';
      case 'PENDIENTE': return '#f59e0b';
      case 'CANCELADA': return '#ef4444';
      default: return '#6b7280';
    }
  };

  const isWeb = Platform.OS === 'web';

  const content = (
    <View style={isWeb ? { display: 'flex', justifyContent: 'space-between', alignItems: 'center' } : styles.nativeContent}>
      <View style={{ flex: 1 }}>
        <Text variant="headingS">{reservation.client}</Text>
        <Text variant="caption">{reservation.service}</Text>
        <Text variant="small" color="textSecondary">{reservation.startDate} - {reservation.endDate}</Text>
      </View>
      <View style={{ alignItems: 'flex-end', gap: 8 }}>
        <View style={{
          backgroundColor: getStatusColor() + '20',
          padding: '4px 10px',
          borderRadius: '9999px',
          border: isWeb ? `1px solid ${getStatusColor()}` : undefined
        }}>
          <Text variant="small" style={{ color: getStatusColor(), fontWeight: 'bold' }}>{reservation.status}</Text>
        </View>
        <Text variant="body" style={{ fontWeight: 'bold' }}>{reservation.price}</Text>
      </View>
    </View>
  );

  if (isWeb) {
    return (
      <Card style={{ cursor: 'pointer', marginBottom: '16px' }} onClick={onPress}>
        {content}
      </Card>
    );
  }

  return (
    <Card style={styles.nativeCard}>
      {content}
    </Card>
  );
};

const styles = StyleSheet.create({
  nativeCard: { marginBottom: 12 },
  nativeContent: { flexDirection: 'row', justifyContent: 'space-between' }
});
