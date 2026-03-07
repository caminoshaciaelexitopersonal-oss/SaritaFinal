import React, { useState } from 'react';
import { View, FlatList, ActivityIndicator, Text, StyleSheet } from 'react-native';
import { usePagination } from '../../hooks/usePagination';
import { TourCard } from '../../components/TourCard';
import { SearchBar } from './SearchBar';
import { useNavigation } from '@react-navigation/native';

export const ExploreScreen = () => {
  const [search, setSearch] = useState('');
  const navigation = useNavigation<any>();
  const { data, loading, loadMore, hasMore } = usePagination(`/tours?search=${search}`);

  return (
    <View style={styles.container}>
      <SearchBar value={search} onChangeText={setSearch} />
      <FlatList
        data={data}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TourCard
            tour={item}
            onPress={(t) => navigation.navigate('TourDetail', { id: t.id })}
          />
        )}
        contentContainerStyle={styles.list}
        onEndReached={loadMore}
        onEndReachedThreshold={0.5}
        ListFooterComponent={loading ? <ActivityIndicator style={{ margin: 20 }} /> : null}
        ListEmptyComponent={!loading ? <Text style={styles.empty}>No hay tours disponibles</Text> : null}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb' },
  list: { padding: 15 },
  empty: { textAlign: 'center', marginTop: 50, color: '#6b7280' }
});
