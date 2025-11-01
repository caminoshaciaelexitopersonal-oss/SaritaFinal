// Placeholder for Card component
import React from 'react';

const Card = ({ children }: { children: React.ReactNode }) => {
  return <div style={{ border: '1px solid #ccc', padding: '16px', margin: '16px 0' }}>{children}</div>;
};

export default Card;
