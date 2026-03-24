import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, Image, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import { useRoute } from '@react-navigation/native';
import { socialService } from '../../services/socialService';

export const SocialProfileScreen = () => {
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    const load = async () => {
        try {
            const data = await socialService.getMyProfile();
            setProfile(data);
        } catch (e) {}
    }
    load();
  }, []);

  if (!profile) return <View style={styles.center}><Text>Cargando Perfil...</Text></View>;

  return (
    <ScrollView style={styles.container}>
      <View style={styles.cover}>
         {profile.presentation_photo ? (
             <Image source={{uri: profile.presentation_photo}} style={styles.photo} />
         ) : (
             <View style={[styles.photo, styles.placeholder]} />
         )}
         <View style={styles.infoOverlay}>
            <Text style={styles.name}>{profile.user}</Text>
            {profile.is_dating_active && (
                <View style={styles.datingBadge}>
                    <Text style={styles.datingText}>DATING ACTIVO</Text>
                </View>
            )}
         </View>
      </View>

      <View style={styles.content}>
          <Text style={styles.sectionTitle}>Sobre mí</Text>
          <Text style={styles.bio}>{profile.bio || 'Sin biografía.'}</Text>

          <Text style={styles.sectionTitle}>Galería Multimedia</Text>
          <FlatList
            data={profile.media_gallery}
            horizontal
            keyExtractor={item => item.id}
            renderItem={({item}) => (
                <View style={styles.mediaItem}>
                   {item.media_type === 'image' ? (
                       <Image source={{uri: item.media_url}} style={styles.mediaThumb} />
                   ) : (
                       <View style={[styles.mediaThumb, styles.videoPlaceholder]}>
                           <Text>VIDEO</Text>
                       </View>
                   )}
                </View>
            )}
          />

          <Text style={styles.sectionTitle}>Intereses</Text>
          <View style={styles.tagCloud}>
             {(profile.interests || []).map((interest: string) => (
                 <View key={interest} style={styles.tag}>
                    <Text style={styles.tagText}>{interest}</Text>
                 </View>
             ))}
          </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
    container: { flex: 1, backgroundColor: '#fff' },
    center: { flex: 1, justifyContent: 'center', alignItems: 'center' },
    cover: { width: '100%', height: 350, backgroundColor: '#eee', position: 'relative' },
    photo: { width: '100%', height: '100%' },
    placeholder: { backgroundColor: '#cbd5e1' },
    infoOverlay: { position: 'absolute', bottom: 20, left: 20, right: 20 },
    name: { color: '#fff', fontSize: 28, fontWeight: 'bold', textShadowColor: 'rgba(0, 0, 0, 0.75)', textShadowOffset: {width: -1, height: 1}, textShadowRadius: 10 },
    datingBadge: { backgroundColor: '#ec4899', alignSelf: 'flex-start', paddingHorizontal: 10, paddingVertical: 4, borderRadius: 20, marginTop: 5 },
    datingText: { color: 'white', fontWeight: 'bold', fontSize: 10 },
    content: { padding: 20 },
    sectionTitle: { fontSize: 18, fontWeight: 'bold', marginTop: 20, marginBottom: 10 },
    bio: { color: '#4b5563', lineHeight: 22 },
    mediaItem: { marginRight: 10 },
    mediaThumb: { width: 120, height: 160, borderRadius: 10, backgroundColor: '#eee' },
    videoPlaceholder: { justifyContent: 'center', alignItems: 'center' },
    tagCloud: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
    tag: { backgroundColor: '#f3f4f6', paddingHorizontal: 12, paddingVertical: 6, borderRadius: 15 },
    tagText: { color: '#1f2937', fontSize: 12 }
});
