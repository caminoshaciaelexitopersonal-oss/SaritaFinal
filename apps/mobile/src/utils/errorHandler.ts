export const errorHandler = (error: any) => {
  if (!error.response) {
    return { type: 'network', message: 'No hay conexión a internet' };
  }

  const status = error.response.status;
  if (status === 401) return { type: 'auth', message: 'Sesión no válida' };
  if (status === 403) return { type: 'auth', message: 'Sin permisos' };
  if (status === 400) return { type: 'validation', message: 'Datos inválidos' };

  return { type: 'server', message: 'Error en el servidor' };
};
