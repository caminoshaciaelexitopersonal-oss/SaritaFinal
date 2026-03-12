import React, { useEffect, useState } from 'react';
import { ReservationTable, ReservationForm, Text, Button, KPIWidget } from '@sarita/shared-ui';
import { ReservationService, ReservationData } from '@sarita/shared-sdk';

export const DesktopReservationsDashboard = () => {
  const [reservations, setReservations] = useState<ReservationData[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(true);

  const fetchReservations = async () => {
    setLoading(true);
    try {
      // Mock data for ERP Desktop consistency
      const data: ReservationData[] = [
        { id: '101', client: 'Andrés Villamil', service: 'Cabaña Familiar', startDate: '2026-03-15', endDate: '2026-03-18', status: 'EN_CURSO', price: '$850,000' },
        { id: '102', client: 'Marina Silva', service: 'Parque Nacional', startDate: '2026-03-22', endDate: '2026-03-22', status: 'CONFIRMADA', price: '$220,000' }
      ];
      setReservations(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchReservations();
  }, []);

  return (
    <div className="p-8 space-y-8 animate-in fade-in duration-500">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold">Gestión de Agenda y Reservas</h1>
          <p className="text-gray-500">Administración de disponibilidad y vinculación con POS ERP.</p>
        </div>
        <div className="flex gap-4">
          <Button
             label={showForm ? "Ver Listado" : "Nueva Reserva Manual"}
             variant={showForm ? "ghost" : "primary"}
             onPress={() => setShowForm(!showForm)}
          />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <KPIWidget label="Reservas Activas" value="42" trend="+3 hoy" isPositive />
        <KPIWidget label="Ingresos Proyectados" value="$18.5M" trend="Estable" isPositive />
        <KPIWidget label="Cancelaciones" value="2%" trend="-0.5%" isPositive />
        <KPIWidget label="Ocupación" value="92%" trend="+5%" isPositive />
      </div>

      {showForm ? (
        <div className="max-w-3xl mx-auto">
          <ReservationForm onSubmit={(d) => { console.log(d); setShowForm(false); }} />
        </div>
      ) : (
        <ReportTable
          title="Consolidado de Reservas"
          columns={[
            { key: 'id', header: 'ID' },
            { key: 'client', header: 'Cliente' },
            { key: 'service', header: 'Servicio' },
            { key: 'startDate', header: 'Desde' },
            { key: 'endDate', header: 'Hasta' },
            { key: 'status', header: 'Estado' },
            { key: 'price', header: 'Total' }
          ]}
          data={reservations}
        />
      )}
    </div>
  );
};
