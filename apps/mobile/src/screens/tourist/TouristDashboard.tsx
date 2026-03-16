import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView } from 'react-native';
import { MobileLayout, KpiCard } from '@sarita/shared-ui';
import { bookingService } from '../../services/bookingService';
import { walletService } from '../../services/walletService';

export const TouristDashboard = () => {
  const [reservations, setReservations] = useState([]);
  const [balance, setBalance] = useState('0');

  useEffect(() => {
    bookingService.getReservations().then(res => setReservations(res.data.results || []));
    walletService.getBalance().then(res => setBalance(res.data.balance || '0'));
  }, []);

  return (
    <MobileLayout title="Mi Viaje (Mobile)">
      <ScrollView className="p-4">
        <View className="flex-row justify-between mb-6">
          <KpiCard title="Reservas Activas" value={reservations.length.toString()} unit="Próximas" />
          <KpiCard title="Saldo Wallet" value={balance} unit="COP" />
        </View>

        <Text className="text-xl font-bold mb-4">Mis Reservas Recientes</Text>
        {reservations.map((res: any) => (
          <View key={res.id} className="bg-white p-4 rounded-xl mb-3 shadow-sm">
             <Text className="font-bold">{res.service_name}</Text>
             <Text className="text-slate-500 text-sm">{res.start_date}</Text>
             <Text className="text-indigo-600 font-bold mt-2">{res.status}</Text>
          </View>
        ))}
      </ScrollView>
    </MobileLayout>
  );
};
