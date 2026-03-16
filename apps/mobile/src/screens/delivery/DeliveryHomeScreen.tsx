import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, Image, TouchableOpacity } from 'react-native';
import { Card } from '../../components/Card';
import { deliveryService } from '../../services/deliveryService';

export const DeliveryHomeScreen = () => {
  const [activeDeliveries, setActiveDeliveries] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDeliveries = async () => {
      try {
        const response = await deliveryService.getActiveOrders();
        setActiveDeliveries(response.data.results || []);
      } catch (error) {
        console.error("Delivery Load Error:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchDeliveries();
  }, []);

  const handleComplete = async (id: string) => {
     try {
       await deliveryService.completeDelivery(id, {
         status: 'ENTREGADO',
         firma: 'MOBILE_APP_SIGNATURE',
         latitud: 0,
         longitud: 0
       });
       // Refresh
       const response = await deliveryService.getActiveOrders();
       setActiveDeliveries(response.data.results || []);
     } catch (e) {
       console.error("Complete error", e);
     }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Panel de Reparto</Text>
      <Text style={styles.subtitle}>Gestión operativa de entregas en tiempo real.</Text>

      <FlatList
        data={activeDeliveries}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Card style={styles.resCard}>
            <View style={styles.header}>
              <Text style={styles.resName}>Pedido #{item.id.substring(0, 8)}</Text>
              <Text style={styles.resRating}>{item.status}</Text>
            </View>
            <Text style={styles.resCat}>De: {item.origin_address}</Text>
            <Text style={styles.resCat}>A: {item.destination_address}</Text>
            {item.status !== 'ENTREGADO' && (
               <TouchableOpacity
                  onPress={() => handleComplete(item.id)}
                  style={{ backgroundColor: '#4f46e5', padding: 10, borderRadius: 8, marginTop: 10 }}>
                  <Text style={{ color: 'white', textAlign: 'center', fontWeight: 'bold' }}>Marcar como Entregado</Text>
               </TouchableOpacity>
            )}
          </Card>
        )}
        contentContainerStyle={{ padding: 20 }}
      />
      {activeDeliveries.length === 0 && !loading && (
          <Text style={{ textAlign: 'center', color: '#9ca3af', marginTop: 40 }}>No hay servicios asignados.</Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginHorizontal: 20, marginTop: 30 },
  subtitle: { color: '#6b7280', marginHorizontal: 20, marginBottom: 20 },
  resCard: { marginBottom: 15, padding: 15 },
  header: { flexDirection: 'row', justifyContent: 'space-between' },
  resName: { fontSize: 18, fontWeight: 'bold' },
  resRating: { color: '#f59e0b', fontWeight: 'bold' },
  resCat: { color: '#4b5563', marginVertical: 5 },
  deliveryInfo: { fontSize: 12, color: '#10b981', fontWeight: 'bold' }
});
