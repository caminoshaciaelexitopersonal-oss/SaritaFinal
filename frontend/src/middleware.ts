import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('sarita_token')?.value;
  const { pathname } = request.nextUrl;

  // Rutas protegidas
  if (pathname.startsWith('/dashboard')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }

    // Validación básica de firma de sesión (Simulada para esta fase)
    const isValidSession = token.length > 20; // Check real si el token existe
    if (!isValidSession) {
      const response = NextResponse.redirect(new URL('/login', request.url));
      response.cookies.delete('sarita_token');
      return response;
    }
  }

  // Protección contra Clickjacking
  const response = NextResponse.next();
  response.headers.set('X-Frame-Options', 'DENY');
  response.headers.set('X-Content-Type-Options', 'nosniff');
  response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  response.headers.set(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' http://localhost:8000;"
  );

  return response;
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
