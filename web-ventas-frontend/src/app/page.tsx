'use client';

import React, { useState, useEffect, useRef } from 'react';
import { FiMic, FiMicOff, FiSend, FiUser, FiZap, FiCheckCircle, FiShield, FiTrendingUp, FiActivity, FiGlobe } from 'react-icons/fi';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface Message {
  role: 'sarita' | 'user';
  text: string;
}

export default function HomePage() {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'sarita', text: 'Hola, soy SARITA. Tu asistente comercial inteligente. He detectado tu interés en el ecosistema turístico. ¿Buscas escalar tu negocio privado o gestionar una plataforma gubernamental?' }
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
        let saritaResponse = "Entiendo perfectamente. Mis agentes de inteligencia están analizando tu perfil operativo para ofrecerte la integración más rentable.";

        if (data.intent === 'quiero_vender_turismo') {
          saritaResponse = "Excelente. Sarita elimina las fugas de capital por desorden administrativo y centraliza tu flujo de caja. ¿Tu operación es hotelera, gastronómica o de servicios?";
        } else if (data.intent === 'soy_gobierno') {
          saritaResponse = "Entendido. Nuestra capa de gobernanza digital permite monitorear el cumplimiento normativo y automatizar inventarios turísticos nacionales. ¿Deseas ver el módulo de supervisión?";
        } else if (data.intent === 'quiero_precio') {
          saritaResponse = "Nuestros modelos de suscripción se basan en el ROI generado. Cuéntame primero, ¿cuál es el volumen transaccional mensual de tu nodo?";
        } else if (data.intent === 'explorar_plataforma') {
          saritaResponse = "¡Genial! Sarita conecta la Triple Vía: Gobierno, Prestadores y Turistas en un solo núcleo. ¿Por cuál dominio te gustaría iniciar el despliegue?";
        }

        setMessages([...newMessages as any, { role: 'sarita', text: saritaResponse }]);
      } else {
        // VERDAD OPERATIVA: No ocultar el fallo del servicio.
        setMessages([...newMessages as any, {
            role: 'sarita',
            text: `SERVICIO NO DISPONIBLE: SADI Engine reportó un error (${response.status}). La capa de marketing conversacional ha sido interrumpida por inestabilidad en el nodo de inteligencia.`
        }]);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="bg-slate-950 text-white min-h-screen flex flex-col font-sans selection:bg-indigo-500/30">
      {/* Dynamic Background Elements */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
         <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-indigo-900/20 blur-[120px] rounded-full animate-pulse" />
         <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-violet-900/20 blur-[120px] rounded-full animate-pulse" style={{ animationDelay: '2s' }} />
      </div>

      {/* Persistent Header */}
      <header className="p-8 border-b border-white/5 flex justify-between items-center bg-slate-950/50 backdrop-blur-2xl sticky top-0 z-50">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 bg-gradient-to-tr from-indigo-600 to-violet-600 rounded-2xl flex items-center justify-center shadow-2xl shadow-indigo-500/40">
            <FiZap className="text-white" size={24} />
          </div>
          <div>
            <h1 className="text-2xl font-black tracking-tighter uppercase">SARITA <span className="text-indigo-400">Marketing AI</span></h1>
            <p className="text-[10px] text-slate-500 uppercase tracking-[0.4em] font-black">Autonomous Sales Agent v2.0</p>
          </div>
        </div>

        <div className="hidden md:flex gap-8 items-center">
           <div className="flex flex-col items-end">
              <span className="text-[10px] font-black text-emerald-500 uppercase tracking-widest">SADI Engine</span>
              <span className="text-xs text-slate-400">Operational</span>
           </div>
           <div className="w-px h-8 bg-white/10" />
           <div className="flex gap-2">
              <div className="w-2 h-2 bg-emerald-500 rounded-full animate-ping" />
              <div className="w-2 h-2 bg-emerald-500 rounded-full" />
           </div>
        </div>
      </header>

      {/* Interactive Canvas */}
      <div className="flex-1 flex flex-col max-w-6xl mx-auto w-full relative z-10">
         <div
           ref={scrollRef}
           className="flex-1 overflow-y-auto p-6 md:p-12 space-y-10 scroll-smooth custom-scrollbar"
         >
           {messages.map((msg, i) => (
             <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in slide-in-from-bottom-4 duration-500`}>
               <div className={`max-w-[80%] p-8 rounded-[2rem] shadow-2xl ${
                 msg.role === 'user'
                   ? 'bg-indigo-600 text-white rounded-tr-none'
                   : 'bg-slate-900 text-slate-200 rounded-tl-none border border-white/5'
               }`}>
                 <div className="flex items-center gap-3 mb-4">
                   <div className={`w-6 h-6 rounded-lg flex items-center justify-center ${msg.role === 'sarita' ? 'bg-indigo-500/20 text-indigo-400' : 'bg-white/10 text-slate-400'}`}>
                      {msg.role === 'sarita' ? <FiZap size={14} /> : <FiUser size={14} />}
                   </div>
                   <span className="text-[10px] uppercase font-black tracking-widest opacity-40">
                     {msg.role === 'sarita' ? 'Sarita Neural Link' : 'Prospecto'}
                   </span>
                 </div>
                 <p className="text-lg leading-relaxed font-medium tracking-tight italic">"{msg.text}"</p>
               </div>
             </div>
           ))}
           {isLoading && (
             <div className="flex justify-start">
               <div className="bg-slate-900/50 p-6 rounded-3xl rounded-tl-none border border-white/5">
                  <div className="flex gap-2">
                    <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce" />
                    <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.2s]" />
                    <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.4s]" />
                  </div>
               </div>
             </div>
           )}
         </div>

         {/* Strategic Control Center */}
         <div className="p-8 md:p-12 bg-slate-900/50 backdrop-blur-3xl border-t border-white/5 shadow-[0_-40px_100px_-20px_rgba(0,0,0,0.8)]">
           <div className="max-w-4xl mx-auto">
             <div className="flex items-center gap-8 bg-slate-950 p-4 rounded-[2.5rem] border border-white/10 focus-within:border-indigo-500/50 transition-all shadow-inner">
               <button
                 onMouseDown={() => setIsRecording(true)}
                 onMouseUp={() => { setIsRecording(false); handleSendMessage("Deseo escalar mi agencia de viajes con Sarita."); }}
                 className={`w-24 h-24 rounded-[2rem] flex items-center justify-center transition-all duration-700 transform hover:scale-105 active:scale-95 group ${
                   isRecording
                     ? 'bg-red-500 shadow-[0_0_60px_rgba(239,68,68,0.4)] animate-pulse'
                     : 'bg-indigo-600 hover:bg-indigo-700 shadow-[0_20px_50px_rgba(79,70,229,0.3)]'
                 }`}
               >
                 {isRecording ? <FiMicOff size={36} /> : <FiMic size={36} />}
               </button>

               <div className="flex-1 relative">
                 <input
                   type="text"
                   value={inputText}
                   onChange={(e) => setInputText(e.target.value)}
                   onKeyPress={(e) => e.key === 'Enter' && handleSendMessage(inputText)}
                   placeholder="Instruye a Sarita..."
                   className="w-full bg-transparent border-none py-6 px-4 focus:outline-none text-xl placeholder:text-slate-700 font-medium tracking-tight"
                 />
                 <button
                   onClick={() => handleSendMessage(inputText)}
                   className="absolute right-4 top-1/2 -translate-y-1/2 w-14 h-14 bg-white/5 hover:bg-indigo-500 hover:text-white rounded-2xl transition-all flex items-center justify-center text-slate-500"
                 >
                   <FiSend size={24} />
                 </button>
               </div>
             </div>

             <div className="mt-8 flex justify-center gap-12">
                <div className="flex items-center gap-2">
                   <FiShield size={14} className="text-emerald-500" />
                   <span className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Conexión Encriptada</span>
                </div>
                <div className="flex items-center gap-2">
                   <FiActivity size={14} className="text-indigo-500" />
                   <span className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Análisis Sensorial Activo</span>
                </div>
                <div className="flex items-center gap-2">
                   <FiGlobe size={14} className="text-blue-500" />
                   <span className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Nodo Central Gaitan</span>
                </div>
             </div>
           </div>
         </div>
      </div>

      <style jsx global>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.05);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.1);
        }
      `}</style>
    </main>
  );
}
