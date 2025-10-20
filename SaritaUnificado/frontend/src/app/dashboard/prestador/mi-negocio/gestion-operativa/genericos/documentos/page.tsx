'use client';

import DocumentoManager from '@/components/prestador/DocumentoManager';
import { AuthGuard } from '@/components/ui/AuthGuard';

const DocumentosPage = () => {
  return (
    <AuthGuard allowedRoles={['PRESTADOR']}>
      <DocumentoManager />
    </AuthGuard>
  );
};

export default DocumentosPage;
