import React, { createContext, useContext } from 'react';

// Define the shape of your context data if you have any
type DashboardContextType = object;

const DashboardContext = createContext<DashboardContextType | undefined>(undefined);

// Custom hook to use the DashboardContext
export const useDashboard = () => {
  const context = useContext(DashboardContext);
  if (context === undefined) {
    throw new Error('useDashboard must be used within a DashboardProvider');
  }
  return context;
};

// You might also want a Provider component
export const DashboardProvider = ({ children }: { children: React.ReactNode }) => {
  const value = {}; // Your context logic here
  return <DashboardContext.Provider value={value}>{children}</DashboardContext.Provider>;
};

export default DashboardContext;
