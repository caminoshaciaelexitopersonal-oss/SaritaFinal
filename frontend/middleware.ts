// SaritaUnificado/frontend/middleware.ts
import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
  locales: ['en', 'es'],
  defaultLocale: 'es'
});

export const config = {
  // Skip all paths that should not be internationalized. This includes the API routes.
  matcher: ['/((?!api|_next|.*\\..*).*)']
};
