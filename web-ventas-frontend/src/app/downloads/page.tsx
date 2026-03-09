
import { Card, CardContent, CardHeader, CardTitle, Button } from '@/components/ui';
import { FiDownload, FiSmartphone, FiMonitor, FiCheckCircle, FiShield, FiZap, FiGlobe } from 'react-icons/fi';
import { FaApple, FaAndroid, FaWindows, FaApple as FaMac } from 'react-icons/fa';

interface DownloadLink {
    id: number;
    nombre: string;
    plataforma: string;
    url: string;
    version: string;
    instrucciones?: string;
}

/**
 * Servicio de obtención de enlaces de descarga con fallback robusto.
 */
async function getDownloadLinks(): Promise<DownloadLink[]> {
    const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'https://api.sarita.travel/api';

    const staticLinks: DownloadLink[] = [
        {
            id: 1,
            nombre: 'SARITA Mobile Business',
            plataforma: 'ANDROID',
            url: 'https://api.sarita.travel/downloads/android/sarita_latest.apk',
            version: '1.2.5',
            instrucciones: '1. Descarga el archivo APK. 2. Abre el archivo en tu dispositivo. 3. Si el sistema lo solicita, autoriza la instalación desde fuentes desconocidas.'
        },
        {
            id: 2,
            nombre: 'SARITA Desktop ERP',
            plataforma: 'WINDOWS',
            url: 'https://api.sarita.travel/downloads/windows/sarita_setup.exe',
            version: '2.3.0',
            instrucciones: '1. Descarga el instalador .exe. 2. Ejecútalo como administrador. 3. Sigue los pasos del asistente de instalación de SARITA.'
        },
        {
            id: 3,
            nombre: 'SARITA Desktop para Mac',
            plataforma: 'MACOS',
            url: 'https://api.sarita.travel/downloads/macos/sarita_desktop.dmg',
            version: '2.3.0',
            instrucciones: '1. Descarga el archivo .dmg. 2. Ábrelo y arrastra el icono de SARITA a tu carpeta de Aplicaciones.'
        },
        {
            id: 4,
            nombre: 'SARITA Mobile para iOS',
            plataforma: 'IOS',
            url: 'https://apps.apple.com/app/sarita-travel/id123456789',
            version: '1.2.5',
            instrucciones: 'Instala directamente desde la Apple App Store oficial.'
        }
    ];

    try {
        const res = await fetch(`${API_BASE}/downloads/public/links/`, {
            next: { revalidate: 300 } // Revalidar cada 5 minutos
        });
        if (!res.ok) return staticLinks;
        const data = await res.json();
        // Si el backend devuelve resultados, los usamos; de lo contrario, fallback.
        return data.results && data.results.length > 0 ? data.results : staticLinks;
    } catch (error) {
        return staticLinks;
    }
}

const PlatformIcon = ({ platform }: { platform: string }) => {
    switch (platform.toUpperCase()) {
        case 'IOS': return <FaApple className="text-gray-800" />;
        case 'ANDROID': return <FaAndroid className="text-green-600" />;
        case 'WINDOWS': return <FaWindows className="text-blue-600" />;
        case 'MACOS': return <FaMac className="text-gray-900" />;
        default: return <FiSmartphone />;
    }
};

export default async function DownloadsPage() {
    const links = await getDownloadLinks();

    const mobilePlatforms = ['IOS', 'ANDROID'];
    const desktopPlatforms = ['WINDOWS', 'MACOS', 'LINUX'];

    const mobileLinks = links.filter(l => mobilePlatforms.includes(l.plataforma.toUpperCase()));
    const desktopLinks = links.filter(l => desktopPlatforms.includes(l.plataforma.toUpperCase()));

    return (
        <div className="min-h-screen bg-[#F8FAFC] py-20 px-4">
            <div className="max-w-7xl mx-auto">
                {/* HERO SECTION */}
                <header className="text-center mb-20">
                    <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 text-blue-700 text-sm font-bold mb-6 border border-blue-100 shadow-sm">
                        <FiZap className="animate-pulse" /> Ecosistema Multi-Plataforma SARITA
                    </div>
                    <h1 className="text-6xl font-black text-slate-900 mb-6 tracking-tighter">
                        La Potencia de SARITA <br /><span className="text-blue-600">en Todos tus Dispositivos</span>
                    </h1>
                    <p className="text-xl text-slate-500 max-w-3xl mx-auto leading-relaxed">
                        Accede a la gestión comercial, operativa y financiera desde cualquier lugar. Aplicaciones nativas optimizadas para máxima velocidad y seguridad SHA-256.
                    </p>
                </header>

                <div className="grid lg:grid-cols-2 gap-16 mb-24">
                    {/* SECCIÓN MÓVIL */}
                    <div className="space-y-8">
                        <div className="flex items-center gap-4">
                            <div className="w-12 h-12 bg-blue-600 rounded-2xl flex items-center justify-center text-white shadow-lg shadow-blue-200">
                                <FiSmartphone size={24} />
                            </div>
                            <div>
                                <h2 className="text-3xl font-black text-slate-800">SARITA Mobile</h2>
                                <p className="text-slate-500 font-medium italic">Vía 1 (Turistas) y Vía 2 (Empresarios)</p>
                            </div>
                        </div>

                        {mobileLinks.length > 0 ? mobileLinks.map(link => (
                            <Card key={link.id} className="group border-none shadow-xl shadow-slate-200/50 hover:shadow-2xl hover:shadow-blue-200/40 transition-all duration-300 rounded-3xl overflow-hidden bg-white">
                                <CardHeader className="p-8 pb-4">
                                    <div className="flex justify-between items-start">
                                        <div className="flex items-center gap-4">
                                            <div className="text-5xl group-hover:scale-110 transition-transform duration-300">
                                                <PlatformIcon platform={link.plataforma} />
                                            </div>
                                            <div>
                                                <CardTitle className="text-xl font-bold text-slate-800">{link.nombre}</CardTitle>
                                                <p className="text-xs font-black text-blue-600 tracking-widest uppercase mt-1">Versión {link.version}</p>
                                            </div>
                                        </div>
                                        <div className="p-3 bg-slate-50 rounded-xl group-hover:bg-blue-50 transition-colors">
                                            <FiSmartphone className="text-slate-400 group-hover:text-blue-600" />
                                        </div>
                                    </div>
                                </CardHeader>
                                <CardContent className="p-8 pt-0">
                                    <div className="bg-slate-50 p-6 rounded-2xl mb-8 border border-slate-100">
                                        <h4 className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-3">Instrucciones de Despliegue</h4>
                                        <p className="text-sm text-slate-600 leading-relaxed font-medium">{link.instrucciones}</p>
                                    </div>
                                    <div className="flex flex-col sm:flex-row gap-6 items-center">
                                        <a href={link.url} className="w-full sm:flex-1">
                                            <Button className="w-full h-14 bg-slate-900 hover:bg-blue-600 text-white font-bold rounded-2xl shadow-lg shadow-slate-200 transition-all text-lg group">
                                                <FiDownload className="mr-3 group-hover:animate-bounce" /> Descargar Ahora
                                            </Button>
                                        </a>
                                        <div className="relative group/qr">
                                            <div className="w-24 h-24 bg-white border-2 border-slate-100 rounded-2xl flex flex-col items-center justify-center p-2 shadow-sm transition-all group-hover/qr:border-blue-600">
                                                <div className="w-full h-full bg-slate-100 rounded-lg flex items-center justify-center">
                                                    <FiGlobe size={24} className="text-slate-300" />
                                                </div>
                                                <span className="text-[8px] font-bold text-slate-400 mt-1 uppercase">Escanear</span>
                                            </div>
                                        </div>
                                    </div>
                                </CardContent>
                            </Card>
                        )) : (
                            <p className="text-slate-400 italic">No hay descargas móviles disponibles en este momento.</p>
                        )}
                    </div>

                    {/* SECCIÓN ESCRITORIO */}
                    <div className="space-y-8">
                        <div className="flex items-center gap-4">
                            <div className="w-12 h-12 bg-purple-600 rounded-2xl flex items-center justify-center text-white shadow-lg shadow-purple-200">
                                <FiMonitor size={24} />
                            </div>
                            <div>
                                <h2 className="text-3xl font-black text-slate-800">SARITA Desktop</h2>
                                <p className="text-slate-500 font-medium italic">Vía 2 (ERP Mi Negocio) y Vía 3 (Admin)</p>
                            </div>
                        </div>

                        {desktopLinks.length > 0 ? desktopLinks.map(link => (
                            <Card key={link.id} className="group border-none shadow-xl shadow-slate-200/50 hover:shadow-2xl hover:shadow-purple-200/40 transition-all duration-300 rounded-3xl overflow-hidden bg-white">
                                <CardHeader className="p-8 pb-4">
                                    <div className="flex justify-between items-start">
                                        <div className="flex items-center gap-4">
                                            <div className="text-5xl group-hover:scale-110 transition-transform duration-300">
                                                <PlatformIcon platform={link.plataforma} />
                                            </div>
                                            <div>
                                                <CardTitle className="text-xl font-bold text-slate-800">{link.nombre}</CardTitle>
                                                <p className="text-xs font-black text-purple-600 tracking-widest uppercase mt-1">Versión {link.version}</p>
                                            </div>
                                        </div>
                                        <div className="p-3 bg-slate-50 rounded-xl group-hover:bg-purple-50 transition-colors">
                                            <FiMonitor className="text-slate-400 group-hover:text-purple-600" />
                                        </div>
                                    </div>
                                </CardHeader>
                                <CardContent className="p-8 pt-0">
                                    <div className="bg-slate-50 p-6 rounded-2xl mb-8 border border-slate-100">
                                        <h4 className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-3">Instrucciones de Instalación</h4>
                                        <p className="text-sm text-slate-600 leading-relaxed font-medium">{link.instrucciones}</p>
                                    </div>
                                    <a href={link.url} className="block w-full">
                                        <Button className="w-full h-14 bg-blue-600 hover:bg-purple-600 text-white font-bold rounded-2xl shadow-lg shadow-blue-200 transition-all text-lg group">
                                            <FiDownload className="mr-3 group-hover:animate-bounce" /> Obtener para {link.plataforma}
                                        </Button>
                                    </a>
                                </CardContent>
                            </Card>
                        )) : (
                            <p className="text-slate-400 italic">No hay descargas de escritorio disponibles.</p>
                        )}
                    </div>
                </div>

                {/* FEATURE HIGHLIGHTS */}
                <section className="bg-slate-900 p-16 rounded-[3rem] shadow-2xl relative overflow-hidden">
                    <div className="absolute top-0 right-0 w-96 h-96 bg-blue-600/10 rounded-full blur-[100px] -mr-48 -mt-48"></div>
                    <div className="absolute bottom-0 left-0 w-96 h-96 bg-purple-600/10 rounded-full blur-[100px] -ml-48 -mb-48"></div>

                    <h3 className="text-3xl font-black text-white text-center mb-16 relative z-10">¿Por qué elegir las aplicaciones nativas de SARITA?</h3>
                    <div className="grid md:grid-cols-3 gap-12 relative z-10">
                        <div className="bg-white/5 p-8 rounded-[2rem] border border-white/10 hover:bg-white/10 transition-colors group">
                            <div className="w-14 h-14 bg-green-500/20 rounded-2xl flex items-center justify-center text-green-400 mb-6 group-hover:scale-110 transition-transform">
                                <FiGlobe size={28} />
                            </div>
                            <h4 className="text-xl font-bold text-white mb-4">Modo Offline Resiliente</h4>
                            <p className="text-slate-400 leading-relaxed font-medium">Accede a tus datos contables y operativos sin conexión a internet. Sincronización automática asegurada por el Sargento N5.</p>
                        </div>
                        <div className="bg-white/5 p-8 rounded-[2rem] border border-white/10 hover:bg-white/10 transition-colors group">
                            <div className="w-14 h-14 bg-blue-500/20 rounded-2xl flex items-center justify-center text-blue-400 mb-6 group-hover:scale-110 transition-transform">
                                <FiShield size={28} />
                            </div>
                            <h4 className="text-xl font-bold text-white mb-4">Seguridad SHA-256</h4>
                            <p className="text-slate-400 leading-relaxed font-medium">Cada documento y transacción es inmutable. Firmas digitales integradas con el Ledger Engine del backend.</p>
                        </div>
                        <div className="bg-white/5 p-8 rounded-[2rem] border border-white/10 hover:bg-white/10 transition-colors group">
                            <div className="w-14 h-14 bg-purple-500/20 rounded-2xl flex items-center justify-center text-purple-400 mb-6 group-hover:scale-110 transition-transform">
                                <FiZap size={28} />
                            </div>
                            <h4 className="text-xl font-bold text-white mb-4">Paridad UX Total</h4>
                            <p className="text-slate-400 leading-relaxed font-medium">La misma potencia y diseño del dashboard web oficial, optimizada para el hardware de tu dispositivo móvil o desktop.</p>
                        </div>
                    </div>
                </section>

                <footer className="mt-20 text-center">
                    <p className="text-slate-400 font-medium">
                        Certificado por el Cerebro Global SARITA 2026. <br />
                        <span className="text-xs uppercase tracking-widest font-black text-slate-300 mt-2 block">Maturity Level 10 · Production Ready</span>
                    </p>
                </footer>
            </div>
        </div>
    );
}
