'use client';

import React from 'react';

// Simulated internal components for the visual audit/screenshot
const Card = ({ children, style }: any) => (
  <div style={{
    backgroundColor: '#ffffff',
    padding: '24px',
    borderRadius: '16px',
    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    border: '1px solid #f3f4f6',
    ...style
  }}>
    {children}
  </div>
);

const StatCard = ({ title, value, trend, up }: any) => (
  <Card>
    <p style={{ color: '#6b7280', fontSize: '14px', fontWeight: '600', marginBottom: '8px' }}>{title}</p>
    <div style={{ display: 'flex', alignItems: 'baseline', gap: '8px' }}>
      <h2 style={{ fontSize: '28px', fontWeight: 'bold', color: '#111827' }}>{value}</h2>
      {trend && (
        <span style={{ fontSize: '14px', fontWeight: '600', color: up ? '#10b981' : '#ef4444' }}>
          {trend}
        </span>
      )}
    </div>
  </Card>
);

const AlertItem = ({ title, desc, severity }: any) => {
  const colors: any = {
    critical: '#fee2e2',
    high: '#ffedd5',
    medium: '#dbeafe'
  };
  const textColors: any = {
    critical: '#991b1b',
    high: '#9a3412',
    medium: '#1e40af'
  };
  return (
    <div style={{
      padding: '12px 16px',
      backgroundColor: colors[severity],
      borderRadius: '8px',
      marginBottom: '8px',
      borderLeft: `4px solid ${textColors[severity]}`
    }}>
      <p style={{ fontWeight: 'bold', color: textColors[severity], margin: 0 }}>{title}</p>
      <p style={{ fontSize: '13px', color: textColors[severity], margin: '4px 0 0 0' }}>{desc}</p>
    </div>
  );
};

export default function AdminDashboardVisualAudit() {
  const data = {
    stats: {
      totalUsers: "4,520",
      activeProviders: "128",
      totalRevenue: "$12.5M",
      occupancyRate: "78%"
    },
    providers: [
      { name: "Hotel Grand Paradise", cat: "Alojamiento", status: "Activo" },
      { name: "EcoTours Meta", cat: "Agencia", status: "Activo" },
      { name: "Sabor Llanero", cat: "Gastronomía", status: "Inactivo" }
    ]
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f9fafb', padding: '40px', fontFamily: 'system-ui, sans-serif' }}>
      {/* Header */}
      <header style={{ marginBottom: '40px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ fontSize: '32px', fontWeight: '800', color: '#1e40af', margin: 0 }}>Torre de Control SARITA</h1>
          <p style={{ color: '#6b7280', marginTop: '4px' }}>Auditoría Gubernamental y Monitoreo Territorial</p>
        </div>
        <div style={{ backgroundColor: '#1e40af', color: 'white', padding: '8px 16px', borderRadius: '8px', fontWeight: 'bold' }}>
          Marzo 2026 - Producción
        </div>
      </header>

      {/* Stats Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '24px', marginBottom: '40px' }}>
        <StatCard title="USUARIOS TOTALES" value={data.stats.totalUsers} trend="+12.5%" up />
        <StatCard title="PRESTADORES ACTIVOS" value={data.stats.activeProviders} trend="+4.2%" up />
        <StatCard title="INGRESOS REGIONALES (ARR)" value={data.stats.totalRevenue} trend="+18.1%" up />
        <StatCard title="TASA DE OCUPACIÓN" value={data.stats.occupancyRate} trend="-1.2%" />
      </div>

      {/* Main Content */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '24px' }}>
        {/* Monitoring */}
        <Card>
          <h3 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '20px' }}>Monitoreo de Prestadores en Tiempo Real</h3>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ textAlign: 'left', borderBottom: '2px solid #f3f4f6' }}>
                <th style={{ padding: '12px', color: '#6b7280', fontSize: '12px' }}>NOMBRE DEL NEGOCIO</th>
                <th style={{ padding: '12px', color: '#6b7280', fontSize: '12px' }}>CATEGORÍA</th>
                <th style={{ padding: '12px', color: '#6b7280', fontSize: '12px' }}>ESTADO</th>
              </tr>
            </thead>
            <tbody>
              {data.providers.map((p, i) => (
                <tr key={i} style={{ borderBottom: '1px solid #f3f4f6' }}>
                  <td style={{ padding: '16px 12px', fontWeight: '600' }}>{p.name}</td>
                  <td style={{ padding: '16px 12px', color: '#4b5563' }}>{p.cat}</td>
                  <td style={{ padding: '16px 12px' }}>
                    <span style={{
                      padding: '4px 8px',
                      borderRadius: '9999px',
                      fontSize: '11px',
                      fontWeight: 'bold',
                      backgroundColor: p.status === 'Activo' ? '#dcfce7' : '#fee2e2',
                      color: p.status === 'Activo' ? '#166534' : '#991b1b'
                    }}>
                      {p.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>

        {/* Alerts & Risk */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          <Card>
            <h3 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '20px' }}>Alertas de Integridad</h3>
            <AlertItem title="Fallo en Enlace DIAN" desc="Interrupción en facturación electrónica." severity="critical" />
            <AlertItem title="Pico de Demanda" desc="Zona Meta reporta 95% de ocupación." severity="high" />
            <AlertItem title="Sincronización POS" desc="3 terminales offline en Puerto Gaitán." severity="medium" />
          </Card>

          <Card style={{ backgroundColor: '#1e293b', color: 'white' }}>
            <h3 style={{ fontSize: '16px', fontWeight: 'bold', marginBottom: '15px' }}>Salud del Sistema (IA Audit)</h3>
            <div style={{ height: '8px', backgroundColor: '#334155', borderRadius: '4px', marginBottom: '8px' }}>
              <div style={{ width: '92%', height: '100%', backgroundColor: '#10b981', borderRadius: '4px' }} />
            </div>
            <p style={{ fontSize: '12px', color: '#94a3b8' }}>Índice de Resiliencia: 0.92 / Normal</p>
          </Card>
        </div>
      </div>

      {/* Map Placeholder */}
      <div style={{ marginTop: '40px' }}>
        <Card style={{ height: '300px', display: 'flex', alignItems: 'center', justifyContent: 'center', backgroundColor: '#eff6ff', border: '2px dashed #bfdbfe' }}>
           <div style={{ textAlign: 'center' }}>
             <p style={{ fontSize: '24px', fontWeight: 'bold', color: '#1e40af', margin: 0 }}>MAPA TERRITORIAL DINÁMICO</p>
             <p style={{ color: '#60a5fa' }}>Visualización de flujo turístico y geolocalización de prestadores</p>
           </div>
        </Card>
      </div>
    </div>
  );
}
