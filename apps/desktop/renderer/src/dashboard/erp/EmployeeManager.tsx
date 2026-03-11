import React, { useState, useEffect } from 'react';
import { Card, Button, Text, Input } from '@/components';
import { erpService } from '@/services/erpService';

export const EmployeeManager = () => {
  const [employees, setEmployees] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadEmployees();
  }, []);

  const loadEmployees = async () => {
    try {
      const res = await erpService.getEmployees();
      setEmployees(res.data);
    } catch (err) {
      console.error("Error loading employees", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <Text variant="headingL">Gestión de Personal</Text>
        <Button label="Registrar Empleado" />
      </div>

      <Card>
        <table className="w-full text-left">
          <thead>
            <tr className="border-b">
              <th className="py-3 px-4">Nombre</th>
              <th className="py-3 px-4">Cargo</th>
              <th className="py-3 px-4">Estado</th>
              <th className="py-3 px-4">Acciones</th>
            </tr>
          </thead>
          <tbody>
            {employees.map(emp => (
              <tr key={emp.id} className="border-b hover:bg-gray-50">
                <td className="py-3 px-4">{emp.first_name} {emp.last_name}</td>
                <td className="py-3 px-4">{emp.position}</td>
                <td className="py-3 px-4">
                  <span className={`px-2 py-1 rounded-full text-xs ${emp.is_active ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
                    {emp.is_active ? 'Activo' : 'Inactivo'}
                  </span>
                </td>
                <td className="py-3 px-4">
                  <Button label="Ver Perfil" variant="ghost" />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
};
