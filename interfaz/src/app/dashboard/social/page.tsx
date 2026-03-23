'use client';

import React, { useEffect, useMemo, useState } from 'react';
import {
  listSocialConversations,
  createSocialConversation,
  listSocialMessages,
  sendSocialMessage,
  listSocialGiftCatalog,
  sendSocialGift,
  listSocialSuggestions,
  SocialConversation,
  SocialMessage,
  SocialGiftCatalog,
  SocialPreference,
} from '@/services/socialService';

export default function SocialSuperAppPage() {
  const [conversations, setConversations] = useState<SocialConversation[]>([]);
  const [selectedConversation, setSelectedConversation] = useState<SocialConversation | null>(null);
  const [messages, setMessages] = useState<SocialMessage[]>([]);
  const [giftCatalog, setGiftCatalog] = useState<SocialGiftCatalog[]>([]);
  const [suggestions, setSuggestions] = useState<SocialPreference[]>([]);
  const [messageInput, setMessageInput] = useState('');
  const [newConversationTitle, setNewConversationTitle] = useState('');
  const [receiverId, setReceiverId] = useState('');
  const [selectedGiftId, setSelectedGiftId] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const canSendGift = useMemo(
    () => Boolean(receiverId && selectedGiftId),
    [receiverId, selectedGiftId]
  );

  const loadInitialData = async (): Promise<void> => {
    setLoading(true);
    setError(null);
    try {
      const [conv, catalog, sugg] = await Promise.all([
        listSocialConversations(),
        listSocialGiftCatalog(),
        listSocialSuggestions(),
      ]);
      setConversations(conv);
      setGiftCatalog(catalog);
      setSuggestions(sugg);
      if (conv.length > 0) {
        setSelectedConversation(conv[0]);
      }
    } catch (err: unknown) {
      const apiError = err as { response?: { data?: { detail?: string } } };
      setError(apiError?.response?.data?.detail || 'No fue posible cargar el módulo social.');
    } finally {
      setLoading(false);
    }
  };

  const loadMessages = async (conversationId: string): Promise<void> => {
    try {
      const msgs = await listSocialMessages(conversationId);
      setMessages(msgs);
    } catch (err: unknown) {
      const apiError = err as { response?: { data?: { detail?: string } } };
      setError(apiError?.response?.data?.detail || 'No fue posible cargar mensajes.');
    }
  };

  useEffect(() => {
    void loadInitialData();
  }, []);

  useEffect(() => {
    if (selectedConversation?.id) {
      void loadMessages(selectedConversation.id);
    } else {
      setMessages([]);
    }
  }, [selectedConversation?.id]);

  const handleCreateConversation = async (): Promise<void> => {
    if (!newConversationTitle.trim()) return;
    try {
      const created = await createSocialConversation({
        conversation_type: 'group',
        title: newConversationTitle.trim(),
      });
      setConversations((prev: SocialConversation[]) => [created, ...prev]);
      setSelectedConversation(created);
      setNewConversationTitle('');
    } catch (err: unknown) {
      const apiError = err as { response?: { data?: { detail?: string } } };
      setError(apiError?.response?.data?.detail || 'No se pudo crear la conversación.');
    }
  };

  const handleSendMessage = async (): Promise<void> => {
    if (!selectedConversation?.id || !messageInput.trim()) return;
    try {
      const created = await sendSocialMessage({
        conversation: selectedConversation.id,
        message_type: 'text',
        content: messageInput.trim(),
      });
      setMessages((prev: SocialMessage[]) => [...prev, created]);
      setMessageInput('');
    } catch (err: unknown) {
      const apiError = err as { response?: { data?: { detail?: string } } };
      setError(apiError?.response?.data?.detail || 'No se pudo enviar el mensaje.');
    }
  };

  const handleSendGift = async (): Promise<void> => {
    if (!canSendGift) return;
    try {
      await sendSocialGift({
        receiver_id: receiverId.trim(),
        gift_id: selectedGiftId,
        conversation_id: selectedConversation?.id,
      });
      alert('Regalo enviado correctamente.');
    } catch (err: unknown) {
      const apiError = err as { response?: { data?: { detail?: string } } };
      setError(apiError?.response?.data?.detail || 'No se pudo enviar el regalo.');
    }
  };

  if (loading) {
    return <div className="p-6">Cargando Super App Social...</div>;
  }

  return (
    <div className="p-6 space-y-6">
      <header>
        <h1 className="text-2xl font-bold">Vía 3 · Super App Social</h1>
        <p className="text-sm text-gray-500">
          Chat real, matching social y regalos integrados con backend SARITA.
        </p>
      </header>

      {error && (
        <div className="rounded-lg border border-red-300 bg-red-50 p-3 text-red-700 text-sm">
          {error}
        </div>
      )}

      <section className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div className="border rounded-xl p-4 space-y-3">
          <h2 className="font-semibold">Conversaciones</h2>
          <div className="flex gap-2">
            <input
              value={newConversationTitle}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setNewConversationTitle(e.target.value)}
              className="border rounded px-3 py-2 text-sm flex-1"
              placeholder="Título de conversación"
            />
            <button onClick={handleCreateConversation} className="px-3 py-2 text-sm bg-black text-white rounded">
              Crear
            </button>
          </div>
          <div className="max-h-80 overflow-auto space-y-2">
            {conversations.map((c: SocialConversation) => (
              <button
                key={c.id}
                onClick={() => setSelectedConversation(c)}
                className={`w-full text-left p-2 rounded border ${
                  selectedConversation?.id === c.id ? 'bg-gray-100 border-gray-400' : 'border-gray-200'
                }`}
              >
                <p className="font-medium text-sm">{c.title || 'Sin título'}</p>
                <p className="text-xs text-gray-500">{c.conversation_type}</p>
              </button>
            ))}
          </div>
        </div>

        <div className="border rounded-xl p-4 space-y-3 lg:col-span-2">
          <h2 className="font-semibold">Chat</h2>
          <div className="h-72 overflow-auto border rounded p-3 bg-gray-50 space-y-2">
            {messages.map((m: SocialMessage) => (
              <div key={m.id} className="bg-white border rounded p-2">
                <p className="text-xs text-gray-500">{m.message_type}</p>
                <p className="text-sm">{m.content}</p>
              </div>
            ))}
            {messages.length === 0 && <p className="text-sm text-gray-500">Sin mensajes aún.</p>}
          </div>
          <div className="flex gap-2">
            <input
              value={messageInput}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setMessageInput(e.target.value)}
              className="border rounded px-3 py-2 text-sm flex-1"
              placeholder="Escribe un mensaje..."
            />
            <button onClick={handleSendMessage} className="px-3 py-2 text-sm bg-indigo-600 text-white rounded">
              Enviar
            </button>
          </div>
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <div className="border rounded-xl p-4 space-y-3">
          <h2 className="font-semibold">Regalos</h2>
          <input
            value={receiverId}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => setReceiverId(e.target.value)}
            className="border rounded px-3 py-2 text-sm w-full"
            placeholder="UUID receptor"
          />
          <select
            value={selectedGiftId}
            onChange={(e: React.ChangeEvent<HTMLSelectElement>) => setSelectedGiftId(e.target.value)}
            className="border rounded px-3 py-2 text-sm w-full"
          >
            <option value="">Selecciona un regalo</option>
            {giftCatalog.map((gift: SocialGiftCatalog) => (
              <option key={gift.id} value={gift.id}>
                {gift.name} · ${gift.price}
              </option>
            ))}
          </select>
          <button
            onClick={handleSendGift}
            disabled={!canSendGift}
            className="px-3 py-2 text-sm rounded bg-emerald-600 text-white disabled:bg-gray-300"
          >
            Enviar regalo
          </button>
        </div>

        <div className="border rounded-xl p-4 space-y-3">
          <h2 className="font-semibold">Matching (sugerencias)</h2>
          <div className="space-y-2 max-h-56 overflow-auto">
            {suggestions.map((s: SocialPreference) => (
              <div key={s.id} className="border rounded p-2">
                <p className="text-sm font-medium">Usuario: {s.user}</p>
                <p className="text-xs text-gray-500">Intereses: {(s.interests || []).join(', ') || 'N/A'}</p>
                <p className="text-xs text-gray-500">Destinos: {(s.preferred_destinations || []).join(', ') || 'N/A'}</p>
              </div>
            ))}
            {suggestions.length === 0 && <p className="text-sm text-gray-500">Sin sugerencias disponibles.</p>}
          </div>
        </div>
      </section>
    </div>
  );
}
