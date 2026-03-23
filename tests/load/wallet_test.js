import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '10m', target: 100000 },
        { duration: '10m', target: 100000 },
        { duration: '10m', target: 0 },
    ],
};

export default function () {
    const res = http.get('http://sarita-backend.default.svc.cluster.local:8000/api/v1/finance/wallet/balance/');
    check(res, { 'status is 200': (r) => r.status === 200 });
    sleep(1);
}
