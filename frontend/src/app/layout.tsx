import type { Metadata } from 'next';
import { AuthProvider } from '@/contexts/AuthContext';
import { EntityProvider } from '@/contexts/EntityContext';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './globals.css';

export const metadata: Metadata = {
  title: 'Sarita - Sistema de Turismo',
  description: 'Plataforma integral de gestión turística',
};

type Props = {
  children: React.ReactNode;
};

export default function RootLayout({ children }: Props) {
  return (
    <html lang="es">
      <body>
        <EntityProvider>
          <AuthProvider>
            {children}
            <ToastContainer
              position="top-right"
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
          </AuthProvider>
        </EntityProvider>
      </body>
    </html>
  );
}
