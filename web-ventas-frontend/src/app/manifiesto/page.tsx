'use client';

import React from 'react';
import { FiShield, FiArrowRight, FiActivity, FiGlobe, FiCpu, FiMap, FiLayers } from 'react-icons/fi';

const LOGIN_URL = process.env.NEXT_PUBLIC_SARITA_APP_URL || 'http://localhost:3000/login';

export default function ManifiestoPage() {
  return (
    <div className="bg-slate-950 text-slate-200 min-h-screen font-sans selection:bg-indigo-500/30">
      <nav className="fixed top-0 w-full z-50 p-6 flex justify-between items-center bg-slate-950/50 backdrop-blur-xl border-b border-white/5">
         <div className="flex items-center gap-2 font-black tracking-tighter text-xl">
            <div className="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center text-white"><FiShield size={16}/></div>
            SARITA
         </div>
         <a href={LOGIN_URL} className="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg font-bold text-sm transition-all">Acceder al Sistema</a>
      </nav>

      <main className="pt-32 pb-20 px-6 max-w-4xl mx-auto space-y-20">
        <section className="space-y-8">
           <h1 className="text-4xl md:text-6xl font-black text-white leading-tight">
             SARITA: <span className="text-indigo-500 italic">Infraestructura Digital Soberana</span>
           </h1>
           <p className="text-2xl text-slate-400 font-medium leading-relaxed italic border-l-4 border-indigo-500 pl-8">
             “SARITA” no es un nombre simbólico ni una marca arbitraria. Es un acrónimo estructural que define con precisión la naturaleza, el alcance y la responsabilidad del sistema.
           </p>
        </section>

        <section className="grid grid-cols-1 md:grid-cols-2 gap-10">
           <FeatureBox
             title="Sistema Autónomo en Red"
             desc="Diseñado como una infraestructura digital de nueva generación para la gestión integral de territorios y ecosistemas económicos complejos."
             icon={<FiGlobe />}
           />
           <FeatureBox
             title="Inteligente y Territorial"
             desc="IA gobernada que reconoce el territorio como variable central que condiciona la operación y la toma de decisiones."
             icon={<FiCpu />}
           />
        </section>

        <article className="prose prose-invert prose-indigo max-w-none space-y-8 text-lg text-slate-300 font-medium leading-relaxed">
           <p>
             SARITA no se trata de una aplicación aislada ni de un conjunto de módulos independientes, sino de un sistema coherente que articula gobernanza, operación, inteligencia artificial y administración bajo un mismo marco de control soberano y trazabilidad total.
           </p>
           <p>
             El sistema fue concebido para operar en contextos reales, donde convergen múltiples actores con responsabilidades diferenciadas: entidades gubernamentales, operadores turísticos como organizaciones públicas privadas y ciudadanos. SARITA integra estas realidades mediante una arquitectura de triple vía, que separa claramente los dominios de gobierno, operación empresarial y experiencia ciudadana.
           </p>
           <div className="p-8 bg-slate-900 rounded-2xl border border-white/5">
              <h3 className="text-white font-black uppercase tracking-widest text-sm mb-4">Gobernanza de la IA</h3>
              <p>
                La autonomía de SARITA no es ciega ni desregulada. El sistema incorpora inteligencia artificial gobernada, capaz de detectar patrones, proponer optimizaciones y ejecutar acciones dentro de límites explícitos definidos por un núcleo de gobernanza. Toda decisión relevante es auditable, explicable y sujeta a intervención humana soberana.
              </p>
           </div>
           <p>
             SARITA opera en red desde su diseño, permitiendo la integración de múltiples territorios, entidades y organizaciones sin perder control ni soberanía local. Cada nodo conserva su identidad, sus reglas y su capacidad de decisión, mientras se beneficia de una infraestructura común.
           </p>
           <p>
             Finalmente, SARITA es un sistema profundamente administrativo. Gestiona procesos, recursos, decisiones y responsabilidades con rigor técnico y legal. De este modo, se posiciona como una infraestructura digital soberana, preparada para soportar la administración inteligente de sistemas complejos.
           </p>
        </article>

        <section className="text-center py-20 border-t border-white/5">
           <h2 className="text-3xl font-black text-white mb-10 uppercase tracking-tighter italic">Comience el Despliegue Territorial</h2>
           <div className="flex flex-wrap justify-center gap-6">
              <a href={LOGIN_URL} className="px-10 py-5 bg-white text-slate-950 rounded-2xl font-black uppercase tracking-widest text-xs hover:bg-indigo-600 hover:text-white transition-all shadow-xl flex items-center gap-3">
                Gobernanza Institucional <FiArrowRight />
              </a>
              <a href={LOGIN_URL} className="px-10 py-5 bg-slate-800 text-white rounded-2xl font-black uppercase tracking-widest text-xs hover:bg-indigo-600 transition-all border border-white/10 flex items-center gap-3">
                Portal Empresarial <FiArrowRight />
              </a>
           </div>
        </section>
      </main>

      <footer className="p-10 text-center text-slate-600 text-[10px] font-black uppercase tracking-[0.3em]">
         &copy; 2026 SARITA ecosystem · sovereign administrative network
      </footer>
    </div>
  );
}

function FeatureBox({ title, desc, icon }: any) {
  return (
    <div className="p-10 rounded-[2rem] bg-slate-900/50 border border-white/5 hover:border-indigo-500/30 transition-all space-y-6">
      <div className="w-14 h-14 bg-indigo-600/10 text-indigo-500 rounded-2xl flex items-center justify-center">
         {React.cloneElement(icon, { size: 28 })}
      </div>
      <h3 className="text-xl font-bold text-white tracking-tight">{title}</h3>
      <p className="text-slate-400 font-medium leading-relaxed text-sm">{desc}</p>
    </div>
  );
}
