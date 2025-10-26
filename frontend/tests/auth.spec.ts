import { test, expect } from '@playwright/test';

test.describe('Flujo de Autenticación y Carga del Sidebar', () => {

  test('debe iniciar sesión como Administrador y capturar logs', async ({ page }) => {
    // Registrar mensajes de consola
    page.on('console', msg => {
      console.log(`[BROWSER LOG] ${msg.type()}: ${msg.text()}`);
    });

    // Registrar errores no capturados
    page.on('pageerror', error => {
      console.log(`[BROWSER ERROR] ${error.message}`);
    });

    // Registrar fallos de red
    page.on('requestfailed', request => {
      console.log(`[NETWORK ERROR] ${request.url()} → ${request.failure()?.errorText}`);
    });

    await page.goto('http://localhost:3000/es/dashboard/login');

    // Iniciar sesión
    await page.fill('input[name="email"]', 'admin@example.com');
    await page.fill('input[name="password"]', 'testpassword123');
    await page.click('button[type="submit"]');

    // Esperar a que la redirección al dashboard ocurra
    await page.waitForURL('http://localhost:3000/es/dashboard');

    // Verificar que el Sidebar se carga y muestra el nombre de usuario
    const sidebar = page.locator('aside');
    await expect(sidebar).toBeVisible();
    await expect(sidebar.getByText('admin')).toBeVisible();

    // Verificar que se muestran los ítems del menú de Administrador
    await expect(sidebar.getByText('Gestión de Contenido')).toBeVisible();
  });
});
