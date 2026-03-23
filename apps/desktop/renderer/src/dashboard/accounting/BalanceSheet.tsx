import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';

const BalanceSheet = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    accountingService.getBalanceSheet().then(setData);
  }, []);

  return (
    <div>
      <h2>Balance General</h2>
      {data ? (
        <table>
          <thead>
            <tr><th>Cuenta</th><th>Saldo</th></tr>
          </thead>
          <tbody>
            {data.assets.map(a => <tr key={a.id}><td>{a.name}</td><td>{a.balance}</td></tr>)}
            {/* Liabilities, Equity */}
          </tbody>
        </table>
      ) : 'Loading...'}
    </div>
  );
};

export default BalanceSheet;

