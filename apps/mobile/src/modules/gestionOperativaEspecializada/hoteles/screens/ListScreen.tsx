import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import { specializedService } from '../../specializedService';

export const HotelListScreen = () => {
  const [rooms, setRooms] = useState([]);

  useEffect(() => {
    specializedService.getHotels().then(res => setRooms(res.data.results || []));
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Habitaciones de Hotel</Text>
      <FlatList
        data={rooms}
        keyExtractor={(item: any) => item.id}
        renderItem={({ item }: any) => (
          <View style={styles.item}>
            <Text style={styles.itemTitle}>{item.room_number} - {item.room_type_name}</Text>
            <Text style={styles.itemStatus}>{item.status}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  item: { padding: 15, borderBottomWidth: 1, borderBottomColor: '#eee' },
  itemTitle: { fontWeight: 'bold' },
  itemStatus: { color: '#10b981', fontSize: 12 }
});
