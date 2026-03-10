import React from 'react';
import { Navbar } from '../organisms/Navbar';
import { spacing } from '../tokens/spacing';

interface DashboardLayoutProps {
  children: React.ReactNode;
  title: string;
  sidebar?: React.ReactNode;
}

export const DashboardLayout: React.FC<DashboardLayoutProps> = ({
  children,
  title,
  sidebar
}) => {
  return (
    <div style={{ display: 'flex', minHeight: '100vh', flexDirection: 'column' }}>
      <Navbar title={title} />
      <div style={{ display: 'flex', flex: 1 }}>
        {sidebar && (
          <aside style={{ width: '260px', borderRight: '1px solid #eaeaea' }}>
            {sidebar}
          </aside>
        )}
        <main style={{ flex: 1, padding: spacing.lg }}>
          {children}
        </main>
      </div>
    </div>
  );
};
