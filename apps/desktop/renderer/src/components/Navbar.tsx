import React from 'react';
import { Link } from 'react-router-dom';

export const Navbar = () => (
  <nav className="bg-primary p-4 flex justify-between items-center text-white shadow-lg">
    <div className="text-xl font-bold">SARITA Travel</div>
    <div className="flex gap-6 items-center">
      <Link to="/" className="hover:text-secondary">Explorar</Link>
      <Link to="/" className="hover:text-secondary">Destinos</Link>
      <Link to="/" className="hover:text-secondary">Restaurantes</Link>
      <Link to="/login" className="bg-secondary text-primary px-4 py-2 rounded font-bold hover:bg-yellow-500 transition">
        Acceso Portal
      </Link>
    </div>
  </nav>
);
