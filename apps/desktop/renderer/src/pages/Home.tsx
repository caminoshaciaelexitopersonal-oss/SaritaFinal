import React from 'react';
import { Navbar } from '../components/Navbar';

export const HomePage = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      {/* Hero Section */}
      <section className="bg-primary text-white py-20 px-10 text-center">
        <h1 className="text-5xl font-bold mb-6">Descubre la Magia de los Llanos</h1>
        <p className="text-xl mb-10 opacity-80">Explora tours, gastronomía y experiencias únicas en Puerto Gaitán.</p>
        <div className="max-w-2xl mx-auto flex gap-2">
          <input
            type="text"
            placeholder="¿Qué experiencia buscas hoy?"
            className="flex-1 p-4 rounded text-gray-800 outline-none"
          />
          <button className="bg-secondary text-primary px-8 py-4 rounded font-bold hover:bg-yellow-500 transition shadow-lg">
            Buscar
          </button>
        </div>
      </section>

      {/* Featured Destinations */}
      <section className="py-16 px-10 max-w-7xl mx-auto">
        <h2 className="text-3xl font-bold mb-10 text-gray-800">Destinos Destacados</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {['Río Manacacías', 'Safari Llanero', 'Muelle de los Sueños'].map(dest => (
            <div key={dest} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition cursor-pointer">
              <div className="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Imagen Destino</div>
              <div className="p-6">
                <h3 className="text-xl font-bold text-primary">{dest}</h3>
                <p className="text-gray-600 mt-2 text-sm">Explora la biodiversidad y cultura única de esta región.</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};
