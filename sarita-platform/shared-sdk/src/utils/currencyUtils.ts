/**
 * Utilidad de Conversión de Moneda Unificada
 * Implementado en el Shared SDK para uso en Web, Mobile y Desktop.
 */

export const currencyUtils = {
  formatCurrency: (amount: number, currency: string = 'COP') => {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: currency,
    }).format(amount);
  },

  convertPrice: (amount: number, rate: number) => {
    return amount * rate;
  }
};
