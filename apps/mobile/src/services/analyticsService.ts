/**
 * SARITA Analytics Service (Fase 02)
 * Simulación de eventos para tracking de usuario.
 */

export const analyticsService = {
  logEvent(eventName: string, params: any = {}) {
    console.log(`[Analytics] Event: ${eventName}`, params);
    // Aquí se integraría Firebase Analytics en producción
  },

  logTourView(tourId: string) {
    this.logEvent('tour_view', { tour_id: tourId });
  },

  logTourBooked(tourId: string, amount: number) {
    this.logEvent('tour_booked', { tour_id: tourId, value: amount });
  },

  logSearch(query: string) {
    this.logEvent('search_used', { query });
  }
};
