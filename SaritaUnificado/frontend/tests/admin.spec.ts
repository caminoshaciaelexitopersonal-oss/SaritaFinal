import { test, expect } from './mocks';

const BASE_URL = 'http://localhost:3000';

test.describe('Flujo de Admin de Entidad', () => {
  // Asumimos que existe un usuario con rol ADMIN_ENTIDAD en la base de datos de prueba
  // y que está asociado a una entidad.
  const adminEmail = 'admin_entidad@example.com';
  const adminPassword = 'password123';
  const newEntityName = `Mi Entidad de Turismo ${Date.now()}`;

  test.beforeEach(async ({ page }) => {
    // Iniciar sesión como admin de entidad
    await page.goto(`${BASE_URL}/login`);
    await page.getByLabel('Correo Electrónico o Usuario').fill(adminEmail);
    await page.getByLabel('Contraseña').fill(adminPassword);
    await page.getByRole('button', { name: 'Ingresar' }).click();
    await page.waitForURL(`${BASE_URL}/dashboard`);
  });

  test('debería poder actualizar los datos de su entidad', async ({ page }) => {
    // Ir a la página de administración de la entidad
    // (Este enlace/botón debería existir en el dashboard del admin)
    await page.goto(`${BASE_URL}/dashboard/entity-settings`);

    // Actualizar el nombre de la entidad
    await page.getByLabel('Nombre de la Entidad').fill(newEntityName);
    await page.getByRole('button', { name: 'Guardar Cambios' }).click();

    // Verificar el mensaje de éxito
    await expect(page.locator('text=Entidad actualizada con éxito')).toBeVisible();

    // Recargar la página para verificar que el header se actualiza
    await page.reload();

    // Verificar que el header ahora muestra el nuevo nombre
    await expect(page.locator('header')).toContainText(newEntityName);
  });

  test('debería poder cambiar el idioma de la interfaz', async ({ page }) => {
    // El header debería estar en español por defecto
    await expect(page.locator('header')).toContainText('Panel de Control');

    // Cambiar a inglés
    await page.getByLabel('Language switcher').selectOption('en');

    // Verificar que la URL ahora contiene /en/
    await page.waitForURL('**/en/dashboard');

    // Verificar que el header ahora está en inglés
    await expect(page.locator('header')).toContainText('Dashboard');

    // Cambiar de vuelta a español
    await page.getByLabel('Language switcher').selectOption('es');
    await page.waitForURL('**/es/dashboard');
    await expect(page.locator('header')).toContainText('Panel de Control');
  });
});