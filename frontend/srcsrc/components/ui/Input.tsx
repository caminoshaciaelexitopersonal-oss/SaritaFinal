// Placeholder for Input component
import React from 'react';

const Input = (props: React.InputHTMLAttributes<HTMLInputElement>) => {
  return <input {...props} style={{ border: '1px solid #ccc', padding: '8px' }} />;
};

export default Input;
