import { api } from './api';

export const socialService = {
  getConversations: async () => {
    const { data } = await api.get('/social/conversations/');
    return data?.results || data || [];
  },

  getMessages: async (conversationId: string) => {
    const { data } = await api.get('/social/messages/', { params: { conversation_id: conversationId } });
    return data?.results || data || [];
  },

  sendMessage: async (conversationId: string, text: string, type: string = 'text') => {
    const { data } = await api.post('/social/messages/', {
      conversation: conversationId,
      message_type: type,
      content: text
    });
    return data;
  },

  joinRoom: async (conversationId: string) => {
    const { data } = await api.post(`/social/conversations/${conversationId}/join/`);
    return data;
  },

  getGifts: async () => {
    const { data } = await api.get('/social/gift-catalog/');
    return data?.results || data || [];
  },

  sendGift: async (receiverId: string, giftId: string, conversationId?: string) => {
    const { data } = await api.post('/social/gift-transactions/send_gift/', {
      receiver_id: receiverId,
      gift_id: giftId,
      conversation_id: conversationId
    });
    return data;
  },

  getMyProfile: async () => {
    const { data } = await api.get('/social/preferences/me/');
    return data;
  }
};
