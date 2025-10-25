import { test, expect } from './mocks';

const BASE_URL = 'http://localhost:3000';

test.describe('Flujo de Subdominios', () => {

  test('debería mostrar la información de la entidad correcta basada en el subdominio', async ({ page }) => {
    // Para que esta prueba funcione, el archivo `hosts` del sistema debe tener:
    // 127.0.0.1 turismo-meta.localhost
    // Y la entidad con slug 'turismo-meta' debe existir en la base de datos.
    const entityName = 'Turismo del Meta';
    const subdomainUrl = 'http://turismo-meta.localhost:3000';

    await page.goto(subdomainUrl);

    // Verificar que el header muestra el nombre de la entidad del subdominio
    await expect(page.locator('header')).toContainText(entityName, { timeout: 10000 });
  });
});