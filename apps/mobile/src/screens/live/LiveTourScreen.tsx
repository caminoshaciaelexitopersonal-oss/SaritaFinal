import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';
import { Button } from '../../components/Button';

export const LiveTourScreen = () => {
  return (
    <View style={styles.container}>
      <Image source={{ uri: 'https://via.placeholder.com/1080x1920' }} style={styles.streamPlaceholder} />

      <View style={styles.header}>
        <View style={styles.liveBadge}><Text style={styles.liveText}>EN VIVO</Text></View>
        <Text style={styles.tourName}>Expedición Río Meta</Text>
      </View>

      <View style={styles.controls}>
        <TouchableOpacity style={styles.chatIcon}><Text>💬</Text></TouchableOpacity>
        <Button title="Reservar este Tour ahora" onPress={() => {}} style={styles.bookBtn} />
      </View>

      <View style={styles.footer}>
        <Text style={styles.viewers}>👁️ 1,245 viendo ahora</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
  streamPlaceholder: { width: '100%', height: '100%', opacity: 0.9 },
  header: { position: 'absolute', top: 50, left: 20, right: 20, flexDirection: 'row', alignItems: 'center' },
  liveBadge: { backgroundColor: '#ef4444', paddingHorizontal: 10, paddingVertical: 5, borderRadius: 5, marginRight: 15 },
  liveText: { color: '#fff', fontWeight: 'bold', fontSize: 10 },
  tourName: { color: '#fff', fontSize: 18, fontWeight: 'bold' },
  controls: { position: 'absolute', bottom: 100, left: 20, right: 20, flexDirection: 'row', alignItems: 'center' },
  chatIcon: { width: 50, height: 50, borderRadius: 25, backgroundColor: 'rgba(255,255,255,0.3)', justifyContent: 'center', alignItems: 'center', marginRight: 15 },
  bookBtn: { flex: 1, backgroundColor: '#f59e0b' },
  footer: { position: 'absolute', bottom: 50, left: 20 },
  viewers: { color: 'rgba(255,255,255,0.6)', fontSize: 12 }
});
