'use client';

import React, { useState, useEffect, useRef } from 'react';
import { FiMic, FiMicOff, FiSend, FiUser, FiZap, FiCheckCircle } from 'react-icons/fi';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface Message {
  role: 'sarita' | 'user';
  text: string;
  audio_url?: string;
}

export default function ConversationalFunnelPage() {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'sarita', text: 'Hola, soy SARITA. Tu asistente inteligente de turismo. ¿Quieres vender servicios turísticos, gestionar una plataforma gubernamental, o solo vienes a explorar?' }
  ]);
  const [inputText, setInputText] = useState('');
  const [isRecording, setIsRecording] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSendMessage = async (text: string) => {
    if (!text.trim()) return;

    const newMessages = [...messages, { role: 'user', text }];
    setMessages(newMessages as any);
    setInputText('');
    setIsLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/api/voice/marketing/intent/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (response.ok) {
        const data = await response.json();
        // Simulamos respuesta verbal inmediata basada en intención para el demo
        let saritaResponse = "Entiendo perfectamente. Mis agentes comerciales están analizando tu caso.";

        if (data.intent === 'quiero_vender_turismo') {
          saritaResponse = "Excelente elección. Sarita te ayuda a organizar tus ventas y evitar el caos operativo. ¿Eres dueño de un hotel o restaurante?";
        } else if (data.intent === 'soy_gobierno') {
          saritaResponse = "Entendido. Nuestra plataforma para gobiernos centraliza inventarios y mejora la gobernanza del destino. ¿Te gustaría ver un demo?";
        }

        setMessages([...newMessages as any, { role: 'sarita', text: saritaResponse }]);
      } else {
        setMessages([...newMessages as any, { role: 'sarita', text: 'Lo siento, tuve un pequeño problema técnico. ¿Podrías repetirlo?' }]);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const startRecording = () => {
    setIsRecording(true);
    // Lógica real de Web Audio API iría aquí
  };

  const stopRecording = () => {
    setIsRecording(false);
    // Simulación: al detener, enviamos un texto de ejemplo
    handleSendMessage("Quiero vender turismo con mi hotel.");
  };

  return (
    <main className="bg-slate-950 text-white min-h-screen flex flex-col font-sans">
      {/* Header Estilo Agente */}
      <header className="p-6 border-b border-slate-800 flex justify-between items-center bg-slate-900/50 backdrop-blur-md sticky top-0 z-10">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-indigo-600 rounded-full flex items-center justify-center animate-pulse">
            <FiZap className="text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight">SARITA <span className="text-indigo-400">Marketing AI</span></h1>
            <p className="text-xs text-slate-400">Agente Comercial de Triple Vía</p>
          </div>
        </div>
        <div className="flex gap-2">
           <span className="px-3 py-1 bg-green-900/30 text-green-400 text-xs rounded-full border border-green-800/50 flex items-center gap-1">
             <FiCheckCircle /> SADI Online
           </span>
        </div>
      </header>

      {/* Chat Area */}
      <div
        ref={scrollRef}
        className="flex-1 overflow-y-auto p-4 sm:p-8 space-y-6 max-w-3xl mx-auto w-full"
      >
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[85%] p-4 rounded-2xl ${
              msg.role === 'user'
                ? 'bg-indigo-600 text-white rounded-tr-none'
                : 'bg-slate-800 text-slate-200 rounded-tl-none border border-slate-700'
            }`}>
              <div className="flex items-center gap-2 mb-1">
                {msg.role === 'sarita' ? <FiZap className="text-indigo-400 text-xs" /> : <FiUser className="text-slate-400 text-xs" />}
                <span className="text-[10px] uppercase font-bold tracking-widest opacity-50">
                  {msg.role === 'sarita' ? 'Sarita AI' : 'Visitante'}
                </span>
              </div>
              <p className="text-sm leading-relaxed">{msg.text}</p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-slate-800 p-4 rounded-2xl rounded-tl-none border border-slate-700">
               <div className="flex gap-1">
                 <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce"></div>
                 <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                 <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.4s]"></div>
               </div>
            </div>
          </div>
        )}
      </div>

      {/* Input Area - Voice First */}
      <div className="p-6 bg-slate-900 border-t border-slate-800">
        <div className="max-w-3xl mx-auto flex items-center gap-4">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className={`w-16 h-16 rounded-full flex items-center justify-center transition-all duration-300 ${
              isRecording
                ? 'bg-red-500 animate-ping'
                : 'bg-indigo-600 hover:bg-indigo-700 shadow-lg shadow-indigo-500/20'
            }`}
          >
            {isRecording ? <FiMicOff size={24} /> : <FiMic size={24} />}
          </button>

          <div className="flex-1 relative">
            <input
              type="text"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage(inputText)}
              placeholder="Habla o escribe aquí..."
              className="w-full bg-slate-800 border border-slate-700 rounded-full py-4 px-6 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm"
            />
            <button
              onClick={() => handleSendMessage(inputText)}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-indigo-400 hover:text-indigo-300"
            >
              <FiSend size={20} />
            </button>
          </div>
        </div>
        <p className="text-center text-[10px] text-slate-500 mt-4 uppercase tracking-widest font-bold">
          Mantén presionado el micrófono para hablar con SARITA
        </p>
      </div>
    </main>
  );
}
