"use client";

import React from 'react';

// Interfaz para tipar los datos del formulario
interface ClientFormState {
  nombre: string;
  email: string;
  telefono: string;
  notas: string;
}

interface ClientFormProps {
  initialData?: Partial<ClientFormState>;
  onSubmit: (data: ClientFormState) => void;
  onCancel: () => void;
  isSaving: boolean;
}

export default function ClientForm({ initialData, onSubmit, onCancel, isSaving }: ClientFormProps) {
  const [formData, setFormData] = React.useState<ClientFormState>(
    {
      nombre: '',
      email: '',
      telefono: '',
      notas: '',
      ...initialData,
    }
  );

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div>
        <label htmlFor="nombre" className="block text-sm font-medium text-gray-700">Nombre Completo</label>
        <input type="text" name="nombre" id="nombre" value={formData.nombre} onChange={handleChange} required className="mt-1 input-class" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
          <input type="email" name="email" id="email" value={formData.email} onChange={handleChange} className="mt-1 input-class" />
        </div>
        <div>
          <label htmlFor="telefono" className="block text-sm font-medium text-gray-700">Teléfono</label>
          <input type="tel" name="telefono" id="telefono" value={formData.telefono} onChange={handleChange} className="mt-1 input-class" />
        </div>
      </div>

      <div>
        <label htmlFor="notas" className="block text-sm font-medium text-gray-700">Notas Internas</label>
        <textarea name="notas" id="notas" value={formData.notas} onChange={handleChange} rows={4} className="mt-1 input-class" />
      </div>

      <div className="flex justify-end space-x-4">
        <button type="button" onClick={onCancel} className="bg-gray-200 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-300">
          Cancelar
        </button>
        <button type="submit" disabled={isSaving} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:bg-gray-400">
          {isSaving ? 'Guardando...' : 'Guardar Cliente'}
        </button>
      </div>
    </form>
  );
}
