import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  variant?: 'primary' | 'outline' | 'ghost' | 'icon';
  color?: 'primary' | 'danger';
}

export const Button = ({
  children,
  variant = 'primary',
  color = 'primary',
  className = '',
  ...props
}: ButtonProps) => {
  const baseClasses = 'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none';

  const variantClasses = {
    primary: `text-white ${color === 'primary' ? 'bg-blue-600 hover:bg-blue-700 focus:ring-blue-500' : 'bg-red-600 hover:bg-red-700 focus:ring-red-500'}`,
    outline: `border ${color === 'primary' ? 'border-blue-600 text-blue-600 hover:bg-blue-50' : 'border-red-600 text-red-600 hover:bg-red-50'}`,
    ghost: 'hover:bg-gray-100',
    icon: `hover:bg-gray-200 rounded-full p-2 ${color === 'danger' ? 'text-red-600 hover:bg-red-100' : 'text-gray-600'}`,
  };

  const sizeClasses = variant === 'icon' ? 'h-8 w-8' : 'px-4 py-2';

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};