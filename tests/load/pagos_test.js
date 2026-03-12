import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '15m', target: 1000000 },
        { duration: '15m', target: 1000000 },
        { duration: '15m', target: 0 },
    ],
};

export default function () {
    const payload = JSON.stringify({ amount: 100, method: 'wallet' });
    const params = { headers: { 'Content-Type': 'application/json' } };
    const res = http.post('http://sarita-backend.default.svc.cluster.local:8000/api/v1/finance/wallet/pay/', payload, params);
    check(res, { 'status is 201': (r) => r.status === 201 });
    sleep(1);
}
