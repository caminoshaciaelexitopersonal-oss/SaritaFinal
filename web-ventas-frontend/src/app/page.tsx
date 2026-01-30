'use client';

import React, { useState, useEffect, useRef } from 'react';
import { FiMic, FiMicOff, FiSend, FiUser, FiZap, FiCheckCircle } from 'react-icons/fi';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface Message {
  role: 'sarita' | 'user';
  text: string;
  audio_url?: string;
}

export default function HomePage() {
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

        // Flujo conversacional según la directiva 4-M
        let saritaResponse = "Entiendo perfectamente. Mis agentes comerciales están analizando tu perfil para ofrecerte la mejor solución.";

        if (data.intent === 'quiero_vender_turismo') {
          saritaResponse = "Excelente. Sarita evita que pierdas dinero por desorden y te organiza las ventas de tu negocio. ¿Trabajas solo o tienes un equipo?";
        } else if (data.intent === 'soy_gobierno') {
          saritaResponse = "Entendido. Nuestra plataforma gubernamental centraliza inventarios y mejora la gobernanza del destino. ¿Hoy usan sistemas manuales o ya tienen algo digital?";
        } else if (data.intent === 'quiero_precio') {
          saritaResponse = "Nuestros planes se adaptan al impacto que generamos en tu negocio. Cuéntame primero, ¿cuántos servicios gestionas actualmente?";
        } else if (data.intent === 'explorar_plataforma') {
          saritaResponse = "¡Genial! Sarita es el sistema de triple vía que conecta gobierno, prestadores y turistas. ¿Por cuál de estas áreas te gustaría empezar el recorrido?";
        }

        setMessages([...newMessages as any, { role: 'sarita', text: saritaResponse }]);
      } else {
        setMessages([...newMessages as any, { role: 'sarita', text: 'Lo siento, tuve un pequeño inconveniente técnico. ¿Podrías repetirme eso?' }]);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const startRecording = () => {
    setIsRecording(true);
  };

  const stopRecording = () => {
    setIsRecording(false);
    // Simulación de envío tras grabación
    handleSendMessage("Quiero conocer más sobre la plataforma para prestadores.");
  };

  return (
    <main className="bg-slate-950 text-white min-h-screen flex flex-col font-sans">
      {/* Micrófono Persistente & Header Agente */}
      <header className="p-6 border-b border-slate-800 flex justify-between items-center bg-slate-900/50 backdrop-blur-md sticky top-0 z-10 shadow-2xl">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-indigo-600 rounded-full flex items-center justify-center shadow-lg shadow-indigo-500/40">
            <FiZap className="text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight">SARITA <span className="text-indigo-400">Marketing AI</span></h1>
            <p className="text-[10px] text-slate-500 uppercase tracking-widest font-bold">Agente Comercial Proactivo</p>
          </div>
        </div>
        <div className="flex gap-2">
           <span className="px-3 py-1 bg-green-900/30 text-green-400 text-xs rounded-full border border-green-800/50 flex items-center gap-1 font-medium">
             <div className="w-1.5 h-1.5 bg-green-400 rounded-full animate-pulse"></div>
             SADI Online
           </span>
        </div>
      </header>

      {/* Chat Area - No navegación clásica */}
      <div
        ref={scrollRef}
        className="flex-1 overflow-y-auto p-4 sm:p-8 space-y-6 max-w-4xl mx-auto w-full scroll-smooth"
      >
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[85%] p-5 rounded-2xl shadow-xl ${
              msg.role === 'user'
                ? 'bg-indigo-600 text-white rounded-tr-none'
                : 'bg-slate-800 text-slate-200 rounded-tl-none border border-slate-700/50'
            }`}>
              <div className="flex items-center gap-2 mb-2">
                {msg.role === 'sarita' ? <FiZap className="text-indigo-400 text-[10px]" /> : <FiUser className="text-slate-500 text-[10px]" />}
                <span className="text-[9px] uppercase font-black tracking-[0.2em] opacity-40">
                  {msg.role === 'sarita' ? 'Sarita AI' : 'Visitante'}
                </span>
              </div>
              <p className="text-sm leading-relaxed font-medium">{msg.text}</p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-slate-800/50 p-4 rounded-2xl rounded-tl-none border border-slate-700/30">
               <div className="flex gap-1.5">
                 <div className="w-1.5 h-1.5 bg-indigo-500 rounded-full animate-bounce"></div>
                 <div className="w-1.5 h-1.5 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                 <div className="w-1.5 h-1.5 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.4s]"></div>
               </div>
            </div>
          </div>
        )}
      </div>

      {/* Control de Voz & Texto */}
      <div className="p-8 bg-slate-900 border-t border-slate-800 shadow-[0_-20px_50px_-12px_rgba(0,0,0,0.5)]">
        <div className="max-w-3xl mx-auto flex items-center gap-6">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className={`w-20 h-20 rounded-full flex items-center justify-center transition-all duration-500 transform hover:scale-105 active:scale-95 ${
              isRecording
                ? 'bg-red-500 shadow-[0_0_40px_rgba(239,68,68,0.6)] animate-pulse'
                : 'bg-indigo-600 hover:bg-indigo-700 shadow-[0_10px_30px_rgba(79,70,229,0.4)]'
            }`}
          >
            {isRecording ? <FiMicOff size={32} /> : <FiMic size={32} />}
          </button>

          <div className="flex-1 relative group">
            <input
              type="text"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage(inputText)}
              placeholder="Habla con SARITA o escribe tu consulta..."
              className="w-full bg-slate-800/80 border border-slate-700 rounded-2xl py-5 px-8 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 text-base transition-all placeholder:text-slate-600"
            />
            <button
              onClick={() => handleSendMessage(inputText)}
              className="absolute right-6 top-1/2 -translate-y-1/2 text-indigo-400 hover:text-indigo-200 transition-colors p-2"
            >
              <FiSend size={24} />
            </button>
          </div>
        </div>
        <p className="text-center text-[10px] text-slate-600 mt-6 uppercase tracking-[0.3em] font-bold">
          {isRecording ? 'Sarita está escuchando...' : 'Mantén presionado el círculo para hablar'}
        </p>
      </div>
    </main>
  );
}
