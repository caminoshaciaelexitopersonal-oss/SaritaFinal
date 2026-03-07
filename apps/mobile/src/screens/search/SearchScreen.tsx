import React, { useState } from 'react';
import { View, FlatList, Text, StyleSheet } from 'react-native';
import { SearchBar } from '../explore/SearchBar';
import { useTours } from '../../hooks/useTours';
import { TourCard } from '../../components/TourCard';
import { useNavigation } from '@react-navigation/native';

export const SearchScreen = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const navigation = useNavigation<any>();

  const handleSearch = async (text: string) => {
    setQuery(text);
    if (text.length > 2) {
      const response = await useTours({ search: text });
      setResults(response.data.results);
    }
  };

  return (
    <View style={styles.container}>
      <SearchBar value={query} onChangeText={handleSearch} />
      <FlatList
        data={results}
        keyExtractor={(item: any) => item.id}
        renderItem={({ item }) => (
          <TourCard
            tour={item}
            onPress={(t) => navigation.navigate('TourDetail', { id: t.id })}
          />
        )}
        contentContainerStyle={{ padding: 15 }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' }
});
