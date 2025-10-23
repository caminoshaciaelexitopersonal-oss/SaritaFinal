import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "../globals.css";
import { AuthProvider } from "@/contexts/AuthContext";
import { EntityProvider } from "@/contexts/EntityContext";
import { LanguageProvider } from "@/contexts/LanguageContext";
import { AgentProvider } from "@/contexts/AgentContext";
import { NextIntlClientProvider } from "next-intl";
import { getMessages } from "next-intl/server";
import ClientLayout from "@/components/ClientLayout"; // Importar el nuevo componente

const geist = Geist({
  subsets: ["latin"],
  variable: "--font-geist-sans",
});

export const metadata: Metadata = {
  title: "Turismo Puerto Gaitán",
  description: "Plataforma de Turismo del Municipio de Puerto Gaitán",
  manifest: "/manifest.json",
  themeColor: "#0070f3",
};

export default async function LocaleLayout({
  children,
  params: {locale}
}: {
  children: React.ReactNode;
  params: {locale: string};
}) {
  const messages = await getMessages();

  return (
    <html lang={locale} className="h-full">
      <body
        className={`${geist.variable} antialiased flex flex-col min-h-full`}
      >
        <NextIntlClientProvider messages={messages}>
          <AuthProvider>
            <EntityProvider>
              <LanguageProvider>
                <AgentProvider>
                  <ClientLayout>{children}</ClientLayout>
                </AgentProvider>
              </LanguageProvider>
            </EntityProvider>
          </AuthProvider>
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
