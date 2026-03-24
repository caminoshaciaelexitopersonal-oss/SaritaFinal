import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, StyleSheet, TextInput, KeyboardAvoidingView, Platform, TouchableOpacity, Image, Modal, Alert } from 'react-native';
import { useRoute } from '@react-navigation/native';
import { socialService, SocialMessage, SocialConversation } from '../../services/socialService';
import { Button } from '../../components/Button';

export const ChatScreen = () => {
  const route = useRoute<any>();
  const conversationId = route.params?.conversationId;

  const [messages, setMessages] = useState<SocialMessage[]>([]);
  const [input, setInput] = useState('');
  const [conversation, setConversation] = useState<SocialConversation | null>(null);

  const [showGifts, setShowGifts] = useState(false);
  const [gifts, setGifts] = useState<any[]>([]);

  const loadData = async () => {
    if (!conversationId) return;
    try {
      const msgs = await socialService.getMessages(conversationId);
      setMessages(msgs);

      const convs = await socialService.getConversations();
      const current = convs.find((c: any) => c.id === conversationId);
      if (current) setConversation(current);
    } catch (error) {
      console.error(error);
    }
  };

  const loadGifts = async () => {
    try {
      const g = await socialService.getGifts();
      setGifts(g);
    } catch (e) {}
  }

  useEffect(() => {
    loadData();
    loadGifts();
  }, [conversationId]);

  const sendMessage = async () => {
    if (!input.trim() || !conversationId) return;
    try {
      const msg = await socialService.sendMessage(conversationId, input.trim());
      setMessages([...messages, msg]);
      setInput('');
    } catch (e) {
      Alert.alert('Error', 'No se pudo enviar el mensaje.');
    }
  };

  const sendGift = async (gift: any) => {
    if (!conversationId) return;
    try {
      // For testing, we assume the other participant's ID
      // In a real app, we'd get it from membership
      const receiverId = conversation?.memberships?.find((m: any) => m.user !== route.params?.myId)?.user;

      if (!receiverId) {
          Alert.alert('Error', 'No se pudo identificar al receptor.');
          return;
      }

      await socialService.sendGift(receiverId, gift.id, conversationId);
      setShowGifts(false);
      loadData(); // Reload to see the GIFT message
      Alert.alert('Éxito', `Regalo ${gift.name} enviado.`);
    } catch (e: any) {
      Alert.alert('Error Financiero', e.response?.data?.detail || 'Fondos insuficientes.');
    }
  }

  const renderMessage = ({ item }: { item: SocialMessage }) => {
    const isGift = item.message_type === 'gift';
    return (
      <View style={[styles.messageRow, item.sender === 'me' ? styles.clientRow : styles.operatorRow]}>
        <View style={[
          styles.bubble,
          item.sender === 'me' ? styles.clientBubble : styles.operatorBubble,
          isGift && styles.giftBubble
        ]}>
          <Text style={item.sender === 'me' ? styles.clientText : styles.operatorText}>
             {isGift ? `🎁 ${item.content}` : item.content}
          </Text>
        </View>
      </View>
    );
  }

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      keyboardVerticalOffset={90}
    >
      <View style={styles.header}>
        <Text style={styles.headerTitle}>{conversation?.title || 'Chat'}</Text>
        {conversation?.conversation_type.includes('room') && (
          <View style={styles.videoBadge}>
            <Text style={styles.videoText}>VIDEO SALA</Text>
          </View>
        )}
      </View>

      <FlatList
        data={messages}
        keyExtractor={item => item.id}
        renderItem={renderMessage}
        contentContainerStyle={styles.list}
      />

      <View style={styles.inputArea}>
        <TouchableOpacity onPress={() => setShowGifts(true)} style={styles.giftIcon}>
           <Text style={{fontSize: 20}}>🎁</Text>
        </TouchableOpacity>
        <TextInput
          style={styles.input}
          value={input}
          onChangeText={setInput}
          placeholder="Escribe un mensaje..."
        />
        <Button title="Enviar" onPress={sendMessage} style={styles.sendBtn} />
      </View>

      <Modal visible={showGifts} animationType="slide" transparent>
         <View style={styles.modalOverlay}>
            <View style={styles.giftPanel}>
               <Text style={styles.modalTitle}>Enviar un Regalo (Comisión 2%)</Text>
               <FlatList
                  data={gifts}
                  numColumns={2}
                  keyExtractor={item => item.id}
                  renderItem={({item}) => (
                    <TouchableOpacity onPress={() => sendGift(item)} style={styles.giftItem}>
                       <Text style={{fontSize: 30}}>{item.icon_url}</Text>
                       <Text style={styles.giftName}>{item.name}</Text>
                       <Text style={styles.giftPrice}>${item.price}</Text>
                    </TouchableOpacity>
                  )}
               />
               <Button title="Cerrar" onPress={() => setShowGifts(false)} variant="secondary" />
            </View>
         </View>
      </Modal>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  header: { padding: 15, borderBottomWidth: 1, borderColor: '#eee', flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' },
  headerTitle: { fontWeight: 'bold', fontSize: 18 },
  videoBadge: { backgroundColor: '#ef4444', paddingHorizontal: 8, paddingVertical: 4, borderRadius: 5 },
  videoText: { color: 'white', fontSize: 10, fontWeight: 'bold' },
  list: { padding: 20 },
  messageRow: { marginBottom: 15, flexDirection: 'row' },
  clientRow: { justifyContent: 'flex-end' },
  operatorRow: { justifyContent: 'flex-start' },
  bubble: { maxWidth: '80%', padding: 12, borderRadius: 15 },
  clientBubble: { backgroundColor: '#1e3a8a' },
  operatorBubble: { backgroundColor: '#f3f4f6' },
  giftBubble: { backgroundColor: '#fdf2f8', borderColor: '#fbcfe8', borderWidth: 1 },
  clientText: { color: '#fff' },
  operatorText: { color: '#1f2937' },
  timestamp: { fontSize: 10, marginTop: 5, alignSelf: 'flex-end', opacity: 0.6 },
  inputArea: { flexDirection: 'row', padding: 15, borderTopWidth: 1, borderColor: '#e5e7eb', alignItems: 'center' },
  input: { flex: 1, height: 40, backgroundColor: '#f9fafb', borderRadius: 20, paddingHorizontal: 15, marginRight: 10 },
  giftIcon: { marginRight: 10 },
  sendBtn: { paddingVertical: 8, paddingHorizontal: 15 },
  modalOverlay: { flex: 1, backgroundColor: 'rgba(0,0,0,0.5)', justifyContent: 'flex-end' },
  giftPanel: { backgroundColor: 'white', borderTopLeftRadius: 25, borderTopRightRadius: 25, padding: 20, minHeight: 400 },
  modalTitle: { fontWeight: 'bold', fontSize: 16, marginBottom: 15, textAlign: 'center' },
  giftItem: { flex: 1, alignItems: 'center', padding: 15, margin: 5, borderWidth: 1, borderColor: '#eee', borderRadius: 10 },
  giftName: { fontSize: 12, fontWeight: '600', marginTop: 5 },
  giftPrice: { fontSize: 10, color: '#059669' }
});
