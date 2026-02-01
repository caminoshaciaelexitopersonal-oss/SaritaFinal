// frontend/src/components/ui/Dialog.tsx
import React from 'react';

export const Dialog = ({ children, ...props }: React.HTMLAttributes<HTMLDivElement>) => <div {...props}>{children}</div>;
export const DialogTrigger = ({ children, ...props }: React.HTMLAttributes<HTMLButtonElement>) => <button {...props}>{children}</button>;
export const DialogContent = ({ children, ...props }: React.HTMLAttributes<HTMLDivElement>) => <div {...props} style={{ border: '1px solid black', padding: '2rem', background: 'white' }}>{children}</div>;
export const DialogHeader = ({ children, ...props }: React.HTMLAttributes<HTMLDivElement>) => <div {...props}>{children}</div>;
export const DialogTitle = ({ children, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => <h2 {...props}>{children}</h2>;
export const DialogDescription = ({ children, ...props }: React.HTMLAttributes<HTMLParagraphElement>) => <p {...props}>{children}</p>;
export const DialogFooter = ({ children, ...props }: React.HTMLAttributes<HTMLDivElement>) => <div {...props}>{children}</div>;
export const DialogClose = ({ children, ...props }: React.HTMLAttributes<HTMLButtonElement>) => <button {...props}>{children}</button>;
