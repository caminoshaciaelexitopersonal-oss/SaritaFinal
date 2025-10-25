// tests/aislamiento.spec.ts
import { test, expect } from '@playwright/test';

test('Página de aislamiento se renderiza correctamente', async ({ page }) => {
  // Navegar a la página de prueba
  await page.goto('http://localhost:3000/es/test-page');

  // Esperar a que el título sea visible
  await expect(page.locator('h1')).toBeVisible();

  // Tomar una captura de pantalla para verificación visual
  await page.screenshot({ path: 'test-results/aislamiento-screenshot.png' });
});
