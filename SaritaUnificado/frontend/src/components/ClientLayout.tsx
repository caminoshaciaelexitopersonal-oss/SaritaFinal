"use client";

import { usePathname } from 'next/navigation';
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Chatbot from '@/components/shared/Chatbot';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AgentController from "@/components/agent/AgentController";
// Importamos el layout del dashboard, su ruta correcta es relativa a la carpeta app
import DashboardLayout from '../app/dashboard/layout';

const ClientLayout = ({ children }: { children: React.ReactNode }) => {
  const pathname = usePathname();
  // Asumiendo que el locale no forma parte del pathname que quieres chequear para el dashboard
  const isDashboard = pathname.split('/').slice(2).join('/').startsWith('dashboard');

  return (
    <>
      {!isDashboard && <Header />}
      <main className={`flex-grow flex flex-col ${!isDashboard ? '' : 'h-full'}`}>
        {isDashboard ? <DashboardLayout>{children}</DashboardLayout> : children}
      </main>
      {!isDashboard && (
        <>
          <Footer />
          <Chatbot />
        </>
      )}
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
      <AgentController />
    </>
  );
};

export default ClientLayout;
