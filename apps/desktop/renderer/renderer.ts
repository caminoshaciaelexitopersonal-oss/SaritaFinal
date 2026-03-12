/**
 * SARITA Desktop Renderer
 *
 * Se comunica con el API central a través del Shared SDK.
 */

window.addEventListener('DOMContentLoaded', () => {
  const statusEl = document.getElementById('status');
  const infoEl = document.getElementById('system-info');

  if (statusEl) {
    statusEl.innerText = 'Conectado al API Gateway de SARITA';
  }

  if (infoEl) {
    infoEl.innerText = `Plataforma: ${window.navigator.platform} | Versión 1.0.0`;
  }

  console.log('SARITA: Desktop Renderer inicializado.');
});
