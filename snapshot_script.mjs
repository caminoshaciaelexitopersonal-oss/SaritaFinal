import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  console.log('Capturing Login...');
  try {
    await page.goto('http://localhost:3001/dashboard/login', { waitUntil: 'networkidle' });
    await page.screenshot({ path: 'snapshot-login.png' });
  } catch (e) { console.error('Login failed', e); }

  console.log('Capturing Root...');
  try {
    await page.goto('http://localhost:3001/', { waitUntil: 'networkidle' });
    await page.screenshot({ path: 'snapshot-root.png' });
  } catch (e) { console.error('Root failed', e); }

  await browser.close();
})();
