import React, { useState, useEffect } from 'react';
import { socialService } from '../services/socialService';

export const SocialModule: React.FC = () => {
  const [conversations, setConversations] = useState<any[]>([]);
  const [selectedConv, setSelectedConv] = useState<any>(null);
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState('');
  const [gifts, setGifts] = useState<any[]>([]);

  useEffect(() => {
    loadConvs();
    loadGifts();
  }, []);

  const loadConvs = async () => {
    const data = await socialService.getConversations();
    setConversations(data);
  };

  const loadGifts = async () => {
    const data = await socialService.getGifts();
    setGifts(data);
  };

  const loadMessages = async (id: string) => {
    const data = await socialService.getMessages(id);
    setMessages(data);
  };

  const handleSelectConv = (conv: any) => {
    setSelectedConv(conv);
    loadMessages(conv.id);
  };

  const handleSend = async () => {
    if (!input.trim() || !selectedConv) return;
    const msg = await socialService.sendMessage(selectedConv.id, input);
    setMessages([...messages, msg]);
    setInput('');
  };

  const handleJoin = async (id: string) => {
    try {
        await socialService.joinRoom(id);
        loadConvs();
    } catch (e: any) {
        alert(e.response?.data?.detail || "Error al unirse");
    }
  };

  const handleSendGift = async (gift: any) => {
      // Mocking receiver for UI demo
      const receiverId = selectedConv?.memberships?.[0]?.user;
      if (!receiverId) return;
      try {
          await socialService.sendGift(receiverId, gift.id, selectedConv.id);
          loadMessages(selectedConv.id);
          alert("Regalo enviado con éxito (+2% comisión)");
      } catch (e: any) {
          alert(e.response?.data?.detail || "Fallo financiero");
      }
  };

  return (
    <div className="flex h-screen bg-gray-100 p-4 gap-4">
      {/* Sidebar: Rooms */}
      <div className="w-1/3 bg-white rounded-xl shadow-lg p-4 flex flex-col">
        <h2 className="text-xl font-bold mb-4">Salas de Citas & Chat</h2>
        <div className="overflow-y-auto flex-1 space-y-2">
          {conversations.map(c => (
            <div
              key={c.id}
              className={`p-3 rounded-lg border cursor-pointer flex justify-between items-center ${selectedConv?.id === c.id ? 'bg-indigo-50 border-indigo-500' : 'hover:bg-gray-50'}`}
              onClick={() => handleSelectConv(c)}
            >
              <div>
                <p className="font-semibold text-sm">{c.title}</p>
                <div className="flex gap-2">
                    <span className="text-[10px] uppercase text-gray-400">{c.conversation_type}</span>
                    {c.is_adult_only && <span className="text-[10px] text-red-500 font-bold">18+</span>}
                </div>
              </div>
              {!c.is_member && (
                  <button onClick={(e) => { e.stopPropagation(); handleJoin(c.id); }} className="bg-indigo-600 text-white text-[10px] px-2 py-1 rounded">Entrar</button>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Main: Chat & Video */}
      <div className="flex-1 bg-white rounded-xl shadow-lg flex flex-col">
        {selectedConv ? (
          <>
            <div className="p-4 border-b flex justify-between items-center">
                <h3 className="font-bold">{selectedConv.title}</h3>
                {selectedConv.conversation_type.includes('room') && (
                    <div className="bg-red-600 text-white px-3 py-1 rounded text-xs animate-pulse">LIVE VIDEO</div>
                )}
            </div>
            <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-gray-50">
                {messages.map(m => (
                    <div key={m.id} className={`max-w-[70%] p-2 rounded-lg ${m.message_type === 'gift' ? 'bg-pink-100 border border-pink-200' : 'bg-white shadow-sm'}`}>
                        <p className="text-xs text-gray-400 mb-1">{m.sender_name || 'Usuario'}</p>
                        <p className="text-sm">{m.message_type === 'gift' ? `🎁 ${m.content}` : m.content}</p>
                    </div>
                ))}
            </div>
            <div className="p-4 border-t flex gap-2">
                <button className="text-xl" title="Enviar Regalo">🎁</button>
                <input
                    className="flex-1 border rounded-lg px-4 py-2"
                    placeholder="Escribe un mensaje..."
                    value={input}
                    onChange={e => setInput(e.target.value)}
                />
                <button onClick={handleSend} className="bg-indigo-600 text-white px-6 py-2 rounded-lg">Enviar</button>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-gray-400">
              Selecciona una sala para comenzar
          </div>
        )}
      </div>

      {/* Sidebar Right: Gifts */}
      <div className="w-64 bg-white rounded-xl shadow-lg p-4">
          <h4 className="font-bold mb-4">Tienda de Regalos</h4>
          <p className="text-[10px] text-gray-400 mb-4">Apoya a tus ciudadanos favoritos. 2% comisión plataforma.</p>
          <div className="grid grid-cols-2 gap-2 overflow-y-auto max-h-[80vh]">
              {gifts.map(g => (
                  <button
                    key={g.id}
                    onClick={() => handleSendGift(g)}
                    className="p-2 border rounded-lg hover:border-pink-500 transition-colors flex flex-col items-center"
                  >
                      <span className="text-2xl">{g.icon_url}</span>
                      <span className="text-[10px] font-bold mt-1 text-center">{g.name}</span>
                      <span className="text-[10px] text-green-600">${g.price}</span>
                  </button>
              ))}
          </div>
      </div>
    </div>
  );
};
