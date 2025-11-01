// Placeholder for Badge component
import React from 'react';

const Badge = ({ children }: { children: React.ReactNode }) => {
  return <span style={{ padding: '4px 8px', borderRadius: '12px', backgroundColor: '#eee' }}>{children}</span>;
};

export default Badge;
