import React, { useState } from 'react';
import { View, FlatList, StyleSheet, Dimensions, Text, Image, TouchableOpacity } from 'react-native';
import { usePagination } from '../../hooks/usePagination';

const { height, width } = Dimensions.get('window');

export const TravelFeedScreen = () => {
  const { data, loading, loadMore } = usePagination('/feed/');

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <View style={styles.reelContainer}>
            <Image source={{ uri: 'https://via.placeholder.com/1080x1920' }} style={styles.videoPlaceholder} />
            <View style={styles.overlay}>
              <Text style={styles.creator}>{item.creator_name || '@ViajeroSarita'}</Text>
              <Text style={styles.caption}>{item.caption || 'Increíble atardecer en el Río Meta #SafariSarita'}</Text>

              <View style={styles.actions}>
                <TouchableOpacity style={styles.actionBtn}><Text style={styles.actionText}>❤️ {item.likes || 0}</Text></TouchableOpacity>
                <TouchableOpacity style={styles.actionBtn}><Text style={styles.actionText}>💬 {item.comments || 0}</Text></TouchableOpacity>
                <TouchableOpacity style={styles.actionBtn}><Text style={styles.actionText}>🔗 Compartir</Text></TouchableOpacity>
              </View>

              <TouchableOpacity style={styles.viewTourBtn}>
                <Text style={styles.viewTourText}>VER TOUR RELACIONADO</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
        pagingEnabled
        showsVerticalScrollIndicator={false}
        onEndReached={loadMore}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
  reelContainer: { height: height, width: width },
  videoPlaceholder: { width: '100%', height: '100%', opacity: 0.8 },
  overlay: { position: 'absolute', bottom: 100, left: 20, right: 20 },
  creator: { color: '#fff', fontSize: 18, fontWeight: 'bold' },
  caption: { color: '#fff', fontSize: 14, marginTop: 10, lineHeight: 20 },
  actions: { position: 'absolute', right: 0, bottom: 50 },
  actionBtn: { marginBottom: 20, alignItems: 'center' },
  actionText: { color: '#fff', fontSize: 12, fontWeight: 'bold' },
  viewTourBtn: { backgroundColor: '#f59e0b', padding: 15, borderRadius: 10, alignItems: 'center', marginTop: 20 },
  viewTourText: { color: '#fff', fontWeight: 'bold' }
});
