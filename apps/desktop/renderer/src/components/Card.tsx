import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  onClick?: () => void;
}

export const Card: React.FC<CardProps> = ({ children, className = '', onClick }) => {
  return (
    <div
      className={`bg-white rounded-xl shadow-sm border border-gray-100 p-6 ${onClick ? 'cursor-pointer hover:shadow-md transition' : ''} ${className}`}
      onClick={onClick}
    >
      {children}
    </div>
  );
};
