import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, StyleSheet, TextInput, KeyboardAvoidingView, Platform } from 'react-native';
import { useRoute } from '@react-navigation/native';
import { api } from '../../services/api';
import { Button } from '../../components/Button';

export const ChatScreen = () => {
  const route = useRoute<any>();
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    // Simulación de carga de historial y conexión WebSocket
    const loadHistory = async () => {
      try {
        const response = await api.get(`/chats/${route.params.reservationId}/`);
        setMessages(response.data || []);
      } catch (error) {
        setMessages([
          { id: '1', sender: 'operator', text: '¡Hola! Soy tu guía para el Safari Río Meta. ¿Tienes alguna duda?', timestamp: '10:00 AM' }
        ]);
      }
    };
    loadHistory();
  }, [route.params.reservationId]);

  const sendMessage = () => {
    if (!input.trim()) return;
    const newMessage = { id: Date.now().toString(), sender: 'client', text: input, timestamp: 'Justo ahora' };
    setMessages([...messages, newMessage]);
    setInput('');
    // Aquí se enviaría vía WebSocket: socket.emit('message', newMessage);
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      keyboardVerticalOffset={90}
    >
      <FlatList
        data={messages}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <View style={[styles.messageRow, item.sender === 'client' ? styles.clientRow : styles.operatorRow]}>
            <View style={[styles.bubble, item.sender === 'client' ? styles.clientBubble : styles.operatorBubble]}>
              <Text style={item.sender === 'client' ? styles.clientText : styles.operatorText}>{item.text}</Text>
              <Text style={styles.timestamp}>{item.timestamp}</Text>
            </View>
          </View>
        )}
        contentContainerStyle={styles.list}
      />
      <View style={styles.inputArea}>
        <TextInput
          style={styles.input}
          value={input}
          onChangeText={setInput}
          placeholder="Escribe un mensaje..."
        />
        <Button title="Enviar" onPress={sendMessage} style={styles.sendBtn} />
      </View>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  list: { padding: 20 },
  messageRow: { marginBottom: 15, flexDirection: 'row' },
  clientRow: { justifyContent: 'flex-end' },
  operatorRow: { justifyContent: 'flex-start' },
  bubble: { maxWidth: '80%', padding: 12, borderRadius: 15 },
  clientBubble: { backgroundColor: '#1e3a8a' },
  operatorBubble: { backgroundColor: '#f3f4f6' },
  clientText: { color: '#fff' },
  operatorText: { color: '#1f2937' },
  timestamp: { fontSize: 10, marginTop: 5, alignSelf: 'flex-end', opacity: 0.6 },
  inputArea: { flexDirection: 'row', padding: 15, borderTopWidth: 1, borderColor: '#e5e7eb', alignItems: 'center' },
  input: { flex: 1, height: 40, backgroundColor: '#f9fafb', borderRadius: 20, paddingHorizontal: 15, marginRight: 10 },
  sendBtn: { paddingVertical: 8, paddingHorizontal: 15 }
});
