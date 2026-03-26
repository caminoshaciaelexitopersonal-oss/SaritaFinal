'use client';

import React from 'react';
import Link from 'next/link';
import { FiArrowRight, FiShield, FiGlobe, FiCpu, FiMap, FiActivity, FiLayers, FiBriefcase, FiUsers } from 'react-icons/fi';

const LOGIN_URL = process.env.NEXT_PUBLIC_SARITA_APP_URL || 'http://localhost:3000/login';

export default function LandingPage() {
  return (
    <div className="bg-slate-950 text-slate-200 min-h-screen font-sans selection:bg-indigo-500/30">
      {/* Abstract Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none z-0">
         <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] bg-indigo-900/10 blur-[120px] rounded-full" />
         <div className="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-violet-900/10 blur-[120px] rounded-full" />
      </div>

      {/* Hero Section */}
      <header className="relative z-10 pt-32 pb-20 px-6 max-w-7xl mx-auto text-center">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-black uppercase tracking-[0.2em] mb-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
           <FiShield /> Infraestructura Digital Soberana
        </div>
        <h1 className="text-6xl md:text-8xl font-black text-white tracking-tighter mb-8 leading-[0.9] animate-in fade-in slide-in-from-bottom-8 duration-1000">
          SARITA
        </h1>
        <p className="text-xl md:text-2xl text-slate-400 max-w-3xl mx-auto font-medium leading-relaxed mb-12 animate-in fade-in slide-in-from-bottom-12 duration-1000">
          No es una marca. Es un acrónimo estructural que define la naturaleza de la gestión territorial e institucional de nueva generación.
        </p>
        <div className="flex flex-col md:flex-row justify-center gap-6 animate-in fade-in slide-in-from-bottom-12 duration-1000">
          <a
            href={LOGIN_URL}
            className="px-10 py-5 bg-white text-slate-950 rounded-2xl font-black uppercase tracking-widest text-sm hover:bg-indigo-500 hover:text-white transition-all shadow-2xl shadow-white/10 flex items-center justify-center gap-3 group"
          >
            Acceder al Sistema <FiArrowRight className="group-hover:translate-x-1 transition-transform" />
          </a>
          <Link
            href="#definicion"
            className="px-10 py-5 bg-slate-900 text-white rounded-2xl font-black uppercase tracking-widest text-sm border border-white/10 hover:bg-slate-800 transition-all flex items-center justify-center gap-3"
          >
            Explorar Manifiesto
          </Link>
        </div>
      </header>

      {/* The Acronym Breakdown */}
      <section id="definicion" className="relative z-10 py-32 px-6 bg-slate-900/30 backdrop-blur-3xl border-y border-white/5">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
            <div className="md:col-span-2 lg:col-span-1">
              <h2 className="text-4xl font-black text-white mb-6 uppercase italic tracking-tighter">
                Definición <span className="text-indigo-500">Estructural</span>
              </h2>
              <p className="text-lg text-slate-400 leading-relaxed font-medium">
                SARITA es un <strong>Sistema Autónomo en Red, Inteligente, Territorial y Administrativo</strong>, diseñado como una infraestructura digital para la gestión integral de territorios y ecosistemas económicos complejos.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-8 lg:col-span-2">
              <FeatureItem
                icon={<FiActivity />}
                title="Sistema Autónomo"
                desc="Capacidad de ejecución y optimización interna bajo reglas de gobernanza soberana."
              />
              <FeatureItem
                icon={<FiGlobe />}
                title="En Red"
                desc="Arquitectura distribuida que integra múltiples territorios conservando la soberanía local."
              />
              <FeatureItem
                icon={<FiCpu />}
                title="Inteligente"
                desc="IA gobernada capaz de detectar patrones y proponer optimizaciones auditables."
              />
              <FeatureItem
                icon={<FiMap />}
                title="Territorial"
                desc="Reconocimiento del territorio como variable estructural que condiciona la operación."
              />
              <FeatureItem
                icon={<FiLayers />}
                title="Administrativo"
                desc="Rigor técnico y legal en la gestión de recursos, procesos y responsabilidades."
              />
            </div>
          </div>
        </div>
      </section>

      {/* Triple Via Architecture */}
      <section className="relative z-10 py-32 px-6 max-w-7xl mx-auto">
        <div className="text-center mb-20">
          <h2 className="text-4xl md:text-5xl font-black text-white uppercase tracking-tighter mb-6 italic">
            Arquitectura de <span className="text-indigo-500">Triple Vía</span>
          </h2>
          <p className="text-xl text-slate-400 max-w-3xl mx-auto font-medium">
            Integramos realidades convergentes mediante la separación clara de dominios operativos.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
           <ViaCard
             title="Vía 1: Gobierno"
             desc="Gestión institucional, políticas públicas y supervisión territorial con trazabilidad total."
             icon={<FiShield />}
             color="border-indigo-500/50"
           />
           <ViaCard
             title="Vía 2: Prestadores"
             desc="Operación empresarial, ERP contable y gestión comercial para el sector público-privado."
             icon={<FiBriefcase />}
             color="border-emerald-500/50"
           />
           <ViaCard
             title="Vía 3: Ciudadanos"
             desc="Experiencia de usuario, acceso a servicios y participación ciudadana protegida."
             icon={<FiUsers />}
             color="border-blue-500/50"
           />
        </div>
      </section>

      {/* The Manifesto / Full Text */}
      <section className="relative z-10 py-32 px-6 bg-white text-slate-950 rounded-[3rem] mx-4 md:mx-10 mb-20">
        <div className="max-w-4xl mx-auto space-y-10">
          <h2 className="text-3xl font-black uppercase tracking-widest text-indigo-600 mb-10">El Manifiesto SARITA</h2>

          <p className="text-xl md:text-2xl font-bold leading-tight">
            SARITA no es una aplicación aislada ni un conjunto de módulos independientes, sino un sistema coherente que articula gobernanza, operación, inteligencia artificial y administración bajo un mismo marco de control soberano.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-10 text-slate-600 font-medium leading-relaxed">
             <div className="space-y-6">
                <p>
                  El sistema fue concebido para operar en contextos reales, donde convergen múltiples actores con responsabilidades diferenciadas. SARITA integra estas realidades garantizando aislamiento funcional, seguridad y cumplimiento normativo.
                </p>
                <p>
                  La autonomía de SARITA no es ciega ni desregulada. El sistema incorpora inteligencia artificial gobernada, capaz de detectar patrones y proponer optimizaciones. Toda decisión relevante es auditable, explicable y sujeta a intervención humana soberana.
                </p>
             </div>
             <div className="space-y-6">
                <p>
                  SARITA opera en red desde su diseño, permitiendo la integración de territorios sin perder control local. Cada nodo conserva su identidad y reglas, mientras se beneficia de una infraestructura común que habilita la interoperabilidad.
                </p>
                <p>
                  Finalmente, SARITA es un sistema profundamente administrativo. Gestiona procesos, recursos y decisiones con rigor técnico y legal. Cada acción queda registrada y cada flujo puede ser auditado, soportando la administración inteligente a largo plazo.
                </p>
             </div>
          </div>

          <div className="pt-10 border-t border-slate-100 flex justify-between items-center">
             <p className="text-sm font-black uppercase tracking-tighter text-slate-400 italic">Infraestructura Digital de Nueva Generación</p>
             <a
                href={LOGIN_URL}
                className="text-indigo-600 font-black flex items-center gap-2 group"
              >
                Acceder ahora <FiArrowRight className="group-hover:translate-x-1 transition-transform" />
              </a>
          </div>
        </div>
      </section>

      {/* CTA Footer */}
      <footer className="relative z-10 py-20 px-6 text-center border-t border-white/5">
        <h3 className="text-3xl font-black text-white mb-8 uppercase tracking-tighter italic">¿Listo para el despliegue soberano?</h3>
        <div className="flex flex-wrap justify-center gap-4">
           <a href={LOGIN_URL} className="px-8 py-4 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 transition-all">Gobernanza Institucional</a>
           <a href={LOGIN_URL} className="px-8 py-4 bg-emerald-600 text-white rounded-xl font-bold hover:bg-emerald-700 transition-all">Portal Prestadores</a>
           <a href={LOGIN_URL} className="px-8 py-4 bg-blue-600 text-white rounded-xl font-bold hover:bg-blue-700 transition-all">Acceso Turistas</a>
        </div>
        <p className="mt-12 text-slate-500 text-xs font-black uppercase tracking-widest">&copy; 2026 SARITA Ecosystem · SADI Intelligence Engine</p>
      </footer>
    </div>
  );
}

function FeatureItem({ icon, title, desc }: any) {
  return (
    <div className="flex gap-4 p-6 rounded-2xl bg-white/5 border border-white/5 hover:border-indigo-500/30 transition-all group">
      <div className="w-12 h-12 rounded-xl bg-indigo-500/10 text-indigo-400 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
        {React.cloneElement(icon, { size: 24 })}
      </div>
      <div>
        <h4 className="text-white font-bold mb-2">{title}</h4>
        <p className="text-sm text-slate-500 leading-relaxed font-medium">{desc}</p>
      </div>
    </div>
  );
}

function ViaCard({ title, desc, icon, color }: any) {
  return (
    <div className={`p-10 rounded-[2.5rem] bg-slate-900/50 border-2 ${color} backdrop-blur-xl hover:translate-y-[-8px] transition-all duration-500`}>
      <div className="w-16 h-16 rounded-2xl bg-white/5 flex items-center justify-center text-white mb-8">
         {React.cloneElement(icon, { size: 32 })}
      </div>
      <h3 className="text-2xl font-black text-white mb-4 italic uppercase tracking-tighter">{title}</h3>
      <p className="text-slate-400 font-medium leading-relaxed">{desc}</p>
    </div>
  );
}
