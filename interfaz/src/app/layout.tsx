// frontend/src/app/layout.tsx
import './globals.css';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    template: '%s | SARITA SADI',
    default: 'SARITA - Sistema Autónomo de Inteligencia y Turismo',
  },
  description: 'Infraestructura digital soberana para la gobernanza turística y el desarrollo económico regional.',
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000'),
  openGraph: {
    title: 'SARITA - Ecosistema Turístico Inteligente',
    description: 'La plataforma oficial para la gestión del turismo y la economía regional.',
    url: '/',
    siteName: 'SARITA SADI',
    locale: 'es_CO',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'SARITA - Inteligencia Territorial',
    description: 'Transformando la gestión pública y privada del turismo.',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "GovernmentOrganization",
              "name": "SARITA / SADI Puerto Gaitán",
              "url": "https://sarita.travel",
              "logo": "https://sarita.travel/logo.png",
              "description": "Plataforma inteligente para la gobernanza turística territorial."
            }),
          }}
        />
      </head>
      <body style={{ margin: 0, padding: 0 }}>
        {children}
      </body>
    </html>
  );
}
