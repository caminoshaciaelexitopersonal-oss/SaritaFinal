import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95% de las peticiones < 500ms
        http_req_failed: ['rate<0.01'],   // Menos del 1% de errores
    },
};

const BASE_URL = 'http://localhost:8000/api/v1';

export default function () {
    // 1. Auth Flow
    const loginRes = http.post(`${BASE_URL}/auth/login/`, {
        email: 'user@example.com',
        password: 'securepassword123'
    });
    check(loginRes, { 'status is 200': (r) => r.status === 200 });

    // 2. Bookings Flow
    const bookingRes = http.get(`${BASE_URL}/operativa/reservas/`);
    check(bookingRes, { 'bookings loaded': (r) => r.status === 200 });

    // 3. Search Flow
    const searchRes = http.get(`${BASE_URL}/atractivos/?search=puerto`);
    check(searchRes, { 'search successful': (r) => r.status === 200 });

    sleep(1);
}
