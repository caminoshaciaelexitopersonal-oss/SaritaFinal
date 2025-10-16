'use client';

import React from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';

// Configurar el localizador para moment.js
const localizer = momentLocalizer(moment);

// Tipado para los eventos del calendario
interface EventoCalendario {
  id: number;
  title: string;
  start: Date;
  end: Date;
  allDay?: boolean;
  resource?: any; // Para asociar a un recurso (habitación, mesa, etc.)
}

interface CalendarioReservasProps {
  eventos: EventoCalendario[];
  onSelectSlot: (slotInfo: { start: Date; end: Date; }) => void;
  onSelectEvent: (event: EventoCalendario) => void;
}

const CalendarioReservas: React.FC<CalendarioReservasProps> = ({ eventos, onSelectSlot, onSelectEvent }) => {
  return (
    <div style={{ height: 600 }}>
      <Calendar
        localizer={localizer}
        events={eventos}
        startAccessor="start"
        endAccessor="end"
        style={{ height: '100%' }}
        selectable
        onSelectSlot={onSelectSlot}
        onSelectEvent={onSelectEvent}
        messages={{
            next: "Sig",
            previous: "Ant",
            today: "Hoy",
            month: "Mes",
            week: "Semana",
            day: "Día"
        }}
      />
    </div>
  );
};

export default CalendarioReservas;