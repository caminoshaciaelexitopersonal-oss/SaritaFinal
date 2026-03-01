import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { importSPKI, jwtVerify } from 'jose';

const PUBLIC_KEY_PEM = `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt767M4dLr04Xe0IR+dh1
FWPw503Y0TFJQpAuLOKJKWyOW3WiH25TICpXaqZjE3kPpobFfLrDKOBDRrahWcFn
5kReSCDhb+dADFHICAg9R+uAPWoArobwsM5vnoYiJ/pDAUSLfd3Z1Do9w5YUKpN6
d3wYqAmUev8pexKXGTao8y8zyY32R4tdP3CVUOVHi+zy+jC8EatuwWJFU1iO9UdN
UT5AXhBtw6ARk0kIYn7VnrhS47k2P/oxwdde8yvQYhM3xbJCLP5gIuceYvcF7V4Y
RG0U79DbD4FBRFHifWeQJKTE7l69aie8/ZmNw9GF2l+s6W6RHn6b1ehmfEkr+b5J
zwIDAQAB
-----END PUBLIC KEY-----`;

export async function middleware(request: NextRequest) {
  const token = request.cookies.get('sarita-auth')?.value;
  const { pathname } = request.nextUrl;

  // Rutas protegidas
  if (pathname.startsWith('/dashboard')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }

    try {
      const publicKey = await importSPKI(PUBLIC_KEY_PEM, 'RS256');
      await jwtVerify(token, publicKey);
      // Si llegamos aquí, el token es válido y está firmado correctamente
    } catch (error) {
      console.error('JWT Verification failed:', error);
      const response = NextResponse.redirect(new URL('/login', request.url));
      response.cookies.delete('sarita-auth');
      response.cookies.delete('sarita-refresh');
      return response;
    }
  }

  // Protección contra Clickjacking y CSP endurecido
  const response = NextResponse.next();
  response.headers.set('X-Frame-Options', 'DENY');
  response.headers.set('X-Content-Type-Options', 'nosniff');
  response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  response.headers.set(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; connect-src 'self' http://localhost:8000 http://127.0.0.1:8000;"
  );

  return response;
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
