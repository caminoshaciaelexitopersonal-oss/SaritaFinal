import React from 'react';
import { View, FlatList, Text, StyleSheet } from 'react-native';
import { usePagination } from '../../hooks/usePagination';
import { TourCard } from '../../components/TourCard';
import { useNavigation } from '@react-navigation/native';

export const FavoritesScreen = () => {
  const { data, loading } = usePagination('/favorites');
  const navigation = useNavigation<any>();

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TourCard
            tour={item}
            onPress={(t) => navigation.navigate('TourDetail', { id: t.id })}
          />
        )}
        contentContainerStyle={{ padding: 15 }}
        ListEmptyComponent={!loading ? <Text style={styles.empty}>No tienes favoritos aún.</Text> : null}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  empty: { textAlign: 'center', marginTop: 50, color: '#6b7280' }
});
