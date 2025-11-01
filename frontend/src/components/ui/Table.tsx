// Placeholder for Table component
import React from 'react';

const Table = ({ children }: { children: React.ReactNode }) => <table>{children}</table>;
const TableHeader = ({ children }: { children: React.ReactNode }) => <thead>{children}</thead>;
const TableRow = ({ children }: { children: React.ReactNode }) => <tr>{children}</tr>;
const TableHead = ({ children }: { children: React.ReactNode }) => <th>{children}</th>;
const TableBody = ({ children }: { children: React.ReactNode }) => <tbody>{children}</tbody>;
const TableCell = ({ children }: { children: React.ReactNode }) => <td>{children}</td>;

export { Table, TableHeader, TableRow, TableHead, TableBody, TableCell };
