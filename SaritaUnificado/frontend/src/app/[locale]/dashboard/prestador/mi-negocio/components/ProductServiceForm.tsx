"use client";

import React from 'react';

// Interfaz para tipar los datos del formulario
interface ProductServiceFormState {
  nombre: string;
  descripcion: string;
  precio: string;
  tipo: 'PRODUCTO' | 'SERVICIO';
  activo: boolean;
}

interface ProductServiceFormProps {
  initialData?: ProductServiceFormState;
  onSubmit: (data: ProductServiceFormState) => void;
  onCancel: () => void;
  isSaving: boolean;
}

export default function ProductServiceForm({ initialData, onSubmit, onCancel, isSaving }: ProductServiceFormProps) {
  const [formData, setFormData] = React.useState<ProductServiceFormState>(
    initialData || {
      nombre: '',
      descripcion: '',
      precio: '0.00',
      tipo: 'SERVICIO',
      activo: true,
    }
  );

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value, type } = e.target;
    const isCheckbox = type === 'checkbox';

    setFormData(prevState => ({
      ...prevState,
      [name]: isCheckbox ? (e.target as HTMLInputElement).checked : value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div>
        <label htmlFor="nombre" className="block text-sm font-medium text-gray-700">Nombre</label>
        <input type="text" name="nombre" id="nombre" value={formData.nombre} onChange={handleChange} required className="mt-1 input-class" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label htmlFor="precio" className="block text-sm font-medium text-gray-700">Precio</label>
          <input type="number" name="precio" id="precio" value={formData.precio} onChange={handleChange} required className="mt-1 input-class" step="0.01" />
        </div>
        <div>
          <label htmlFor="tipo" className="block text-sm font-medium text-gray-700">Tipo</label>
          <select name="tipo" id="tipo" value={formData.tipo} onChange={handleChange} className="mt-1 input-class">
            <option value="SERVICIO">Servicio</option>
            <option value="PRODUCTO">Producto</option>
          </select>
        </div>
      </div>

      <div>
        <label htmlFor="descripcion" className="block text-sm font-medium text-gray-700">Descripción</label>
        <textarea name="descripcion" id="descripcion" value={formData.descripcion} onChange={handleChange} rows={4} className="mt-1 input-class" />
      </div>

      <div className="flex items-center">
        <input type="checkbox" name="activo" id="activo" checked={formData.activo} onChange={handleChange} className="h-4 w-4 text-blue-600 border-gray-300 rounded" />
        <label htmlFor="activo" className="ml-2 block text-sm text-gray-900">Activo</label>
      </div>

      <div className="flex justify-end space-x-4">
        <button type="button" onClick={onCancel} className="bg-gray-200 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-300">
          Cancelar
        </button>
        <button type="submit" disabled={isSaving} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:bg-gray-400">
          {isSaving ? 'Guardando...' : 'Guardar'}
        </button>
      </div>
    </form>
  );
}

// Estilos de input compartidos para evitar repetición
const styles = `
  .input-class {
    display: block;
    width: 100%;
    padding: 0.5rem 0.75rem;
    border: 1px solid #D1D5DB;
    border-radius: 0.375rem;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    outline: none;
  }
  .input-class:focus {
    ring: 2px solid #3B82F6;
    border-color: #3B82F6;
  }
`;

// Inyectar estilos en el head del documento (una forma de manejar estilos compartidos en componentes)
if (typeof window !== 'undefined') {
  const styleSheet = document.createElement("style");
  styleSheet.type = "text/css";
  styleSheet.innerText = styles;
  document.head.appendChild(styleSheet);
}
