
import { Card, CardContent, CardHeader, CardTitle, Button } from '@/components/ui';
import { FiDownload, FiSmartphone, FiMonitor, FiCheckCircle } from 'react-icons/fi';
import { FaApple, FaAndroid, FaWindows, FaApple as FaMac } from 'react-icons/fa';

interface DownloadLink {
    id: number;
    nombre: string;
    plataforma: string;
    url: string;
    version: string;
    instrucciones?: string;
}

async function getDownloadLinks(): Promise<DownloadLink[]> {
    // Simulación de enlaces si el backend no está disponible durante el build
    const staticLinks: DownloadLink[] = [
        { id: 1, nombre: 'SARITA Mobile (Beta)', plataforma: 'ANDROID', url: '#', version: '1.0.4', instrucciones: 'Descarga el APK e instálalo permitiendo fuentes desconocidas.' },
        { id: 2, nombre: 'SARITA Desktop', plataforma: 'WINDOWS', url: '#', version: '2.1.0', instrucciones: 'Ejecuta el instalador .exe y sigue los pasos.' },
        { id: 3, nombre: 'SARITA macOS', plataforma: 'MACOS', url: '#', version: '2.1.0', instrucciones: 'Arrastra la aplicación a tu carpeta de Applications.' }
    ];

    try {
        const res = await fetch('http://localhost:8000/api/downloads/public/links/', {
            next: { revalidate: 3600 }
        });
        if (!res.ok) return staticLinks;
        const data = await res.json();
        return data.results && data.results.length > 0 ? data.results : staticLinks;
    } catch (error) {
        return staticLinks;
    }
}

const PlatformIcon = ({ platform }: { platform: string }) => {
    switch (platform.toUpperCase()) {
        case 'IOS': return <FaApple className="text-gray-800" />;
        case 'ANDROID': return <FaAndroid className="text-green-500" />;
        case 'WINDOWS': return <FaWindows className="text-blue-500" />;
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
        <div className="min-h-screen bg-gray-50 py-16 px-4">
            <div className="max-w-6xl mx-auto">
                <header className="text-center mb-16">
                    <h1 className="text-5xl font-extrabold text-gray-900 mb-4 tracking-tight">
                        Lleva SARITA contigo
                    </h1>
                    <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                        Descarga nuestras aplicaciones oficiales para una experiencia optimizada en todos tus dispositivos.
                    </p>
                </header>

                <div className="grid md:grid-cols-2 gap-12 mb-16">
                    {/* SECCIÓN MÓVIL */}
                    <div className="space-y-6">
                        <div className="flex items-center gap-3 mb-4">
                            <div className="p-3 bg-blue-100 rounded-lg text-blue-600">
                                <FiSmartphone size={24} />
                            </div>
                            <h2 className="text-2xl font-bold text-gray-800">Aplicación Móvil</h2>
                        </div>

                        {mobileLinks.length > 0 ? mobileLinks.map(link => (
                            <Card key={link.id} className="overflow-hidden hover:shadow-md transition-shadow border-blue-100">
                                <CardHeader className="flex flex-row items-center justify-between pb-2">
                                    <div className="flex items-center gap-3">
                                        <div className="text-3xl">
                                            <PlatformIcon platform={link.plataforma} />
                                        </div>
                                        <CardTitle className="text-lg">{link.nombre}</CardTitle>
                                    </div>
                                    <span className="text-xs font-bold bg-blue-50 text-blue-600 px-2 py-1 rounded">v{link.version}</span>
                                </CardHeader>
                                <CardContent>
                                    <p className="text-sm text-gray-500 mb-6">{link.instrucciones}</p>
                                    <div className="flex gap-4">
                                        <Button className="flex-1 bg-gray-900 hover:bg-black">
                                            <FiDownload className="mr-2" /> Descargar APK/IPA
                                        </Button>
                                        <div className="w-20 h-20 bg-gray-200 rounded flex items-center justify-center text-[8px] text-gray-400 text-center p-2">
                                            QR CODE PLACEHOLDER
                                        </div>
                                    </div>
                                </CardContent>
                            </Card>
                        )) : (
                            <p className="text-gray-400 italic">No hay descargas móviles disponibles.</p>
                        )}
                    </div>

                    {/* SECCIÓN ESCRITORIO */}
                    <div className="space-y-6">
                        <div className="flex items-center gap-3 mb-4">
                            <div className="p-3 bg-purple-100 rounded-lg text-purple-600">
                                <FiMonitor size={24} />
                            </div>
                            <h2 className="text-2xl font-bold text-gray-800">Versión de Escritorio</h2>
                        </div>

                        {desktopLinks.length > 0 ? desktopLinks.map(link => (
                            <Card key={link.id} className="hover:shadow-md transition-shadow">
                                <CardHeader className="flex flex-row items-center justify-between pb-2">
                                    <div className="flex items-center gap-3">
                                        <div className="text-3xl">
                                            <PlatformIcon platform={link.plataforma} />
                                        </div>
                                        <CardTitle className="text-lg">{link.nombre}</CardTitle>
                                    </div>
                                    <span className="text-xs font-bold bg-purple-50 text-purple-600 px-2 py-1 rounded">v{link.version}</span>
                                </CardHeader>
                                <CardContent>
                                    <p className="text-sm text-gray-500 mb-6">{link.instrucciones}</p>
                                    <Button className="w-full bg-blue-600 hover:bg-blue-700">
                                        <FiDownload className="mr-2" /> Descargar para {link.plataforma}
                                    </Button>
                                </CardContent>
                            </Card>
                        )) : (
                            <p className="text-gray-400 italic">No hay descargas de escritorio disponibles.</p>
                        )}
                    </div>
                </div>

                <section className="bg-white p-10 rounded-2xl shadow-sm border border-gray-100 text-center">
                    <h3 className="text-2xl font-bold mb-6">¿Por qué usar nuestras aplicaciones?</h3>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="space-y-2">
                            <FiCheckCircle className="mx-auto text-green-500 text-2xl" />
                            <h4 className="font-bold">Modo Offline</h4>
                            <p className="text-sm text-gray-500">Accede a tus mapas y reservas sin conexión a internet.</p>
                        </div>
                        <div className="space-y-2">
                            <FiCheckCircle className="mx-auto text-green-500 text-2xl" />
                            <h4 className="font-bold">Notificaciones</h4>
                            <p className="text-sm text-gray-500">Recibe alertas en tiempo real sobre tus tours y vuelos.</p>
                        </div>
                        <div className="space-y-2">
                            <FiCheckCircle className="mx-auto text-green-500 text-2xl" />
                            <h4 className="font-bold">Mayor Velocidad</h4>
                            <p className="text-sm text-gray-500">Interfaz optimizada nativamente para tu hardware.</p>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    );
}
