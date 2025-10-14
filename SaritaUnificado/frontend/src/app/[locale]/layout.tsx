import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "./globals.css";
import { AuthProvider } from "@/contexts/AuthContext";
import { EntityProvider } from "@/contexts/EntityContext";
import { LanguageProvider } from "@/contexts/LanguageContext";
import { AgentProvider } from "@/contexts/AgentContext";
import AgentController from "@/components/agent/AgentController";
import Footer from "@/components/Footer";
import Header from "@/components/Header";
import Chatbot from '@/components/shared/Chatbot';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

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

import { NextIntlClientProvider } from "next-intl";
import { getMessages } from "next-intl/server";

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
                <Header />
                <main className="flex-grow flex flex-col">
                  {children}
                </main>
                <ToastContainer
                  position="bottom-right"
                  autoClose={5000}
                  hideProgressBar={false}
                  newestOnTop={false}
                  closeOnClick
                  rtl={false}
                  pauseOnFocusLoss
                  draggable
                  pauseOnHover
                  theme="light"
                />
                <Footer />
                <Chatbot />
                <AgentController />
              </AgentProvider>
            </LanguageProvider>
          </EntityProvider>
        </AuthProvider>
        </NextIntlClientProvider>
      </body>
    </html>
  );
}