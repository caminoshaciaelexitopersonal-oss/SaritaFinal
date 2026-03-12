import { group, sleep } from 'k6';
import http from 'k6/http';
import { check } from 'k6';

export const options = {
    scenarios: {
        initial_stability: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '5m', target: 10000 },
                { duration: '10m', target: 10000 },
            ],
            gracefulRampDown: '5m',
        },
        massive_load: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '10m', target: 100000 },
                { duration: '10m', target: 100000 },
            ],
            startTime: '20m',
        },
        regional_scale: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '15m', target: 1000000 },
                { duration: '15m', target: 1000000 },
            ],
            startTime: '45m',
        }
    },
    thresholds: {
        http_req_duration: ['p(95)<800'],
        http_req_failed: ['rate<0.02'],
    },
};

export default function () {
    group('User Flow', function () {
        // Simple mixed flow for generic scenario
        http.get('http://sarita-backend.default.svc.cluster.local:8000/api/v1/mi-negocio/status/');
        sleep(1);
    });
}
