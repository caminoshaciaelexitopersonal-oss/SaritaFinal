import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '5m', target: 10000 },
        { duration: '10m', target: 10000 },
        { duration: '5m', target: 0 },
    ],
};

export default function () {
    const res = http.get('http://sarita-backend.default.svc.cluster.local:8000/api/v1/mi-negocio/reservas/');
    check(res, { 'status is 200': (r) => r.status === 200 });
    sleep(1);
}
