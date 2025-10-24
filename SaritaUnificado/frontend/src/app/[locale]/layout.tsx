// src/app/[locale]/layout.tsx
import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "../globals.css"; // Ruta corregida
import { NextIntlClientProvider } from "next-intl";
import { getMessages } from "next-intl/server";
import Providers from "@/components/Providers";

const geist = Geist({
  subsets: ["latin"],
  variable: "--font-geist-sans",
});

export const metadata: Metadata = {
  title: "Turismo Puerto Gaitán",
  description: "Plataforma de Turismo del Municipio de Puerto Gaitán",
};

export default async function LocaleLayout({
  children,
  params
}: {
  children: React.ReactNode;
  params: {locale: string};
}) {
  const messages = await getMessages();
  const { locale } = params;

  return (
    <html lang={locale} className="h-full">
      <body className={`${geist.variable} antialiased flex flex-col min-h-full`}>
        <NextIntlClientProvider locale={locale} messages={messages}>
          <Providers>{children}</Providers>
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
