from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.turismo.models.provider_models import TourismSubClassification

class Command(BaseCommand):
    help = 'Seeds the detailed sub-classifications for tourism providers (50 variants per category)'

    def handle(self, *args, **options):
        # 1. Hoteles (50)
        hoteles_data = [
            ("Hotel Boutique", "🏨"), ("Hotel de Lujo", "💎"), ("Hotel Económico", "💰"), ("Hotel Cápsula", "💊"),
            ("Hotel Temático", "🎭"), ("Hotel Ecológico (Eco-hotel)", "🌿"), ("Hotel Sostenible", "♻️"),
            ("Hotel Inteligente (Smart hotel)", "📱"), ("Hotel de Diseño", "🎨"), ("Hotel Histórico", "🏛️"),
            ("Hotel de Playa", "🏖️"), ("Hotel de Ciudad", "🏙️"), ("Hotel Rural", "🚜"), ("Hotel de Montaña", "⛰️"),
            ("Hotel de Selva", "🌳"), ("Hotel de Aeropuerto", "✈️"), ("Hotel en Carretera", "🛣️"),
            ("Hotel Flotante", "⚓"), ("Hotel en Isla", "🏝️"), ("Hotel en Desierto", "🏜️"),
            ("Hotel Todo Incluido", "🍹"), ("Hotel de Media Pensión", "🍲"), ("Hotel Solo Alojamiento", "🛏️"),
            ("Hotel Bed and Breakfast", "🍳"), ("Hotel de Larga Estancia", "📅"), ("Hotel de Negocios", "💼"),
            ("Hotel con Centro de Convenciones", "🤝"), ("Hotel Wellness (Bienestar)", "🧘"), ("Hotel Spa", "💆"),
            ("Hotel Médico", "🏥"), ("Hotel Familiar", "👨‍👩‍👧"), ("Hotel Solo Adultos", "🔞"),
            ("Hotel para Parejas", "💕"), ("Hotel para Mochileros", "🎒"), ("Hotel Pet-friendly", "🐾"),
            ("Hotel LGBTQ+ Friendly", "🏳️‍🌈"), ("Hotel para Ejecutivos", "👨‍💼"), ("Hotel Estudiantil", "🎓"),
            ("Hotel Deportivo", "⚽"), ("Hotel para Eventos", "🎈"), ("Glamping", "🏕️"), ("Resort", "⛱️"),
            ("Apartahotel", "🏢"), ("Hostal", "🛌"), ("Posada Turística", "🏡"), ("Lodge", "🪵"),
            ("Cabañas Turísticas", "🛖"), ("Hacienda Turística", "🐄"), ("Motel", "🚗"), ("Parador Turístico", "🚦")
        ]

        # 2. Restaurantes (50)
        restaurantes_data = [
            ("Restaurante a la Carta", "🍽️"), ("Restaurante Buffet", "🥗"), ("Restaurante Autoservicio", "🍱"),
            ("Restaurante de Comida Rápida", "🍔"), ("Restaurante Casual", "👕"), ("Restaurante de Alta Cocina", "👔"),
            ("Restaurante de Menú del Día", "🍲"), ("Restaurante de Comida para Llevar", "🥡"),
            ("Restaurante con Servicio a Domicilio", "🛵"), ("Restaurante tipo Food Court", "🏛️"),
            ("Restaurante de Comida Italiana", "🇮🇹"), ("Restaurante de Comida Mexicana", "🇲🇽"),
            ("Restaurante de Comida China", "🇨🇳"), ("Restaurante de Comida Japonesa", "🇯🇵"),
            ("Restaurante de Comida Mediterránea", "🇬🇷"), ("Restaurante de Comida Árabe", "🇱🇧"),
            ("Restaurante de Comida Francesa", "🇫🇷"), ("Restaurante de Comida Peruana", "🇵🇪"),
            ("Restaurante de Comida Colombiana Típica", "🇨🇴"), ("Restaurante de Mariscos", "🍤"),
            ("Restaurante Vegetariano", "🌱"), ("Restaurante Vegano", "🌿"), ("Restaurante Saludable", "🍎"),
            ("Restaurante Orgánico", "🚜"), ("Restaurante Sin Gluten", "🌾"), ("Restaurante Keto", "🥓"),
            ("Restaurante Fitness", "💪"), ("Restaurante Macrobiótico", "☯️"), ("Restaurante de Comida Dietética", "⚖️"),
            ("Restaurante Sostenible", "♻️"), ("Restaurante Temático", "🎭"), ("Restaurante Interactivo", "🎮"),
            ("Restaurante con Espectáculo", "🎤"), ("Restaurante Romántico", "🕯️"), ("Restaurante Familiar", "👨‍👩‍👧"),
            ("Restaurante Pet-friendly", "🐾"), ("Restaurante al Aire Libre", "🌳"), ("Restaurante con Vista Panorámica", "🔭"),
            ("Restaurante Ecológico", "🍃"), ("Restaurante Cultural", "🎨"), ("Restaurante Gourmet", "⭐"),
            ("Bistró", "🇫🇷"), ("Cafetería", "☕"), ("Trattoria", "🇮🇹"), ("Brasserie", "🍺"),
            ("Food Truck", "🚚"), ("Restaurante Pop-up", "✨"), ("Restaurante de Autor", "✍️"),
            ("Restaurante Fusión", "🧪"), ("Restaurante de Mercado", "🍅")
        ]

        # 3. Bares (50)
        bares_data = [
            ("Bar Tradicional", "🍸"), ("Bar de Cócteles", "🍹"), ("Bar de Autoservicio", "🥃"),
            ("Bar con Servicio a la Mesa", "🤵"), ("Bar tipo Pub", "🇬🇧"), ("Bar Lounge", "🛋️"),
            ("Bar de Hotel", "🏨"), ("Bar Restaurante", "🍽️"), ("Bar de Eventos", "🎈"), ("Bar Nocturno", "🌙"),
            ("Bar Cervecero", "🍺"), ("Bar de Cervezas Artesanales", "🍻"), ("Bar de Vinos", "🍷"),
            ("Bar de Licores Premium", "🥃"), ("Bar de Coctelería de Autor", "🧪"), ("Bar de Whisky", "🥃"),
            ("Bar de Ron", "🥃"), ("Bar de Tequila", "🇲🇽"), ("Bar de Ginebra", "🍸"),
            ("Bar de Bebidas Sin Alcohol", "🥤"), ("Bar Temático", "🎭"), ("Bar Deportivo", "⚽"),
            ("Bar Musical", "🎶"), ("Bar Karaoke", "🎤"), ("Bar de Música en Vivo", "🎸"),
            ("Bar Cultural", "🎨"), ("Bar Retro", "📻"), ("Bar Urbano", "🏙️"), ("Bar Alternativo", "💿"),
            ("Bar de Salsa", "💃"), ("Bar al Aire Libre", "🌳"), ("Bar en Terraza", "🌇"),
            ("Bar Ecológico", "🌿"), ("Bar Sostenible", "♻️"), ("Bar Pet-friendly", "🐾"),
            ("Bar Exclusivo", "👑"), ("Bar Romántico", "💕"), ("Bar Interactivo", "🎮"),
            ("Bar Clandestino", "🗝️"), ("Bar Experiencial", "✨"), ("Bar de Playa", "🏖️"),
            ("Bar de Piscina", "🏊"), ("Bar de Montaña", "⛰️"), ("Bar Rural", "🚜"), ("Bar Móvil", "🚚"),
            ("Bar en Food Truck", "🚚"), ("Bar Flotante", "⚓"), ("Bar en Discoteca", "🕺"),
            ("Bar Turístico", "🗺️"), ("Bar de Casino", "🎰")
        ]

        # 4. Discotecas (50)
        discos_data = [
            ("Discoteca Electrónica", "🎧"), ("Discoteca de Reguetón", "🍑"), ("Discoteca de Música Crossover", "🔀"),
            ("Discoteca de Salsa", "💃"), ("Discoteca de Vallenato", "🪗"), ("Discoteca de Música Popular", "🤠"),
            ("Discoteca de Rock", "🎸"), ("Discoteca de Techno", "⚡"), ("Discoteca de House", "🏠"),
            ("Discoteca de Música Latina", "🔥"), ("Discoteca Temática", "🎭"), ("Discoteca Retro", "🕺"),
            ("Discoteca Urbana", "🏙️"), ("Discoteca Cultural", "🎨"), ("Discoteca Alternativa", "👽"),
            ("Discoteca Tropical", "🌴"), ("Discoteca de Música en Vivo", "🎤"), ("Discoteca con DJ Internacional", "🌎"),
            ("Discoteca de Shows", "✨"), ("Discoteca con Espectáculo", "🎬"), ("Discoteca Juvenil", "👶"),
            ("Discoteca para Adultos", "🔞"), ("Discoteca Exclusiva", "💎"), ("Discoteca para Turistas", "📸"),
            ("Discoteca LGBTQ+ Friendly", "🏳️‍🌈"), ("Discoteca Universitaria", "🎓"), ("Discoteca para Parejas", "💕"),
            ("Discoteca para Grupos", "👨‍👩‍👧‍👦"), ("Discoteca Inclusiva", "♿"), ("Discoteca para Eventos Privados", "🔒"),
            ("Discoteca tipo Club", "🏢"), ("Discoteca Lounge", "🛋️"), ("Discoteca en Terraza", "🌇"),
            ("Discoteca al Aire Libre", "🌳"), ("Discoteca en Hotel", "🏨"), ("Discoteca en Bar", "🍸"),
            ("Discoteca Móvil", "🚚"), ("Discoteca Flotante", "⚓"), ("Discoteca en Centro Comercial", "🏢"),
            ("Discoteca en Zona Rural", "🚜"), ("Discoteca de Lujo", "👑"), ("Discoteca Temática Inmersiva", "🌀"),
            ("Discoteca Interactiva", "🕹️"), ("Discoteca Tecnológica", "🚨"), ("Discoteca Silenciosa", "🎧"),
            ("Discoteca Ecológica", "🌿"), ("Discoteca Sostenible", "♻️"), ("Discoteca After Party", "🌅"),
            ("Discoteca Underground", "🚇"), ("Discoteca Turística", "📍")
        ]

        # 5. Agencias (50)
        agencias_data = [
            ("Agencia de Viajes Mayorista", "✈️"), ("Agencia de Viajes Minorista", "🎫"),
            ("Agencia Mayorista-Minorista", "🏢"), ("Operador Turístico", "🚌"), ("Agencia Emisiva", "📤"),
            ("Agencia Receptiva", "📥"), ("Agencia Emisiva-Receptiva", "🔄"), ("Agencia Consolidadora", "📦"),
            ("Agencia Intermediaria", "🤝"), ("Agencia Organizadora de Eventos", "🎈"),
            ("Agencia de Turismo de Aventura", "🧗"), ("Agencia de Ecoturismo", "🌿"),
            ("Agencia de Turismo Cultural", "🎨"), ("Agencia de Turismo Religioso", "⛪"),
            ("Agencia de Turismo Gastronómico", "🍲"), ("Agencia de Turismo Comunitario", "🤝"),
            ("Agencia de Turismo Rural", "🚜"), ("Agencia de Turismo de Naturaleza", "🌳"),
            ("Agencia de Turismo Sostenible", "♻️"), ("Agencia de Turismo Científico", "🔬"),
            ("Agencia Corporativa", "💼"), ("Agencia para Estudiantes", "🎓"), ("Agencia para Mochileros", "🎒"),
            ("Agencia de Lujo", "💎"), ("Agencia para Familias", "👨‍👩‍👧"), ("Agencia para Adultos Mayores", "👵"),
            ("Agencia Especializada en Parejas", "💕"), ("Agencia Inclusiva", "♿"),
            ("Agencia LGBTQ+ Friendly", "🏳️‍🌈"), ("Agencia para Grupos", "👨‍👩‍👧‍👦"),
            ("Agencia de Viajes Online", "💻"), ("Agencia Tradicional", "🏛️"), ("Agencia Híbrida", "🔄"),
            ("Agencia Móvil", "📱"), ("Agencia por Redes Sociales", "📸"), ("Agencia Afiliada", "🏢"),
            ("Agencia Independiente", "🚶"), ("Agencia Marketplace", "🛒"), ("Agencia con Atención Virtual", "🤖"),
            ("Agencia Automatizada", "⚙️"), ("Agencia de Viajes Internacionales", "🌎"),
            ("Agencia de Viajes Nacionales", "🇨🇴"), ("Agencia Especializada en Cruceros", "🚢"),
            ("Agencia de Turismo Médico", "🏥"), ("Agencia de Turismo Deportivo", "⚽"),
            ("Agencia de Viajes Educativos", "📚"), ("Agencia de Turismo de Bienestar", "🧘"),
            ("Agencia de Viajes de Negocios", "🤝"), ("Agencia de Viajes de Lujo Experiencial", "✨"),
            ("Agencia de Viajes Personalizados", "✍️")
        ]

        # 6. Guías (50)
        guias_data = [
            ("Guía de Turismo Cultural", "🏛️"), ("Guía de Turismo Histórico", "📜"),
            ("Guía de Turismo Patrimonial", "🏺"), ("Guía de Turismo Gastronómico", "🥘"),
            ("Guía de Turismo Religioso", "⛪"), ("Guía de Turismo Arqueológico", "🗿"),
            ("Guía de Turismo Urbano", "🏙️"), ("Guía de Turismo Rural", "🚜"),
            ("Guía de Turismo Comunitario", "🤝"), ("Guía de Turismo Científico", "🔬"),
            ("Guía de Ecoturismo", "🌿"), ("Guía de Turismo de Naturaleza", "🌳"),
            ("Guía de Turismo de Aventura", "🧗"), ("Guía de Avistamiento de Aves", "🦜"),
            ("Guía de Senderismo", "🥾"), ("Guía de Turismo de Montaña", "⛰️"),
            ("Guía de Turismo de Selva", "🌴"), ("Guía de Turismo Marino", "⚓"),
            ("Guía de Turismo Sostenible", "♻️"), ("Guía de Turismo de Bienestar", "🧘"),
            ("Guía Bilingüe", "🗣️"), ("Guía Multilingüe", "🌎"), ("Guía Intérprete Cultural", "🗣️"),
            ("Guía Animador Turístico", "🎭"), ("Guía Educativo", "📚"), ("Guía Ambiental", "🍃"),
            ("Guía Especializado en Primeros Auxilios", "⛑️"), ("Guía Facilitador Comunitario", "🤝"),
            ("Guía Acompañante", "🚶"), ("Guía Coordinador de Grupos", "👨‍👩‍👧‍👦"),
            ("Guía para Grupos", "🚌"), ("Guía Personalizado", "👤"), ("Guía para Estudiantes", "🎓"),
            ("Guía para Adultos Mayores", "👵"), ("Guía para Familias", "👨‍👩‍👧"),
            ("Guía para Turistas Extranjeros", "📸"), ("Guía Inclusivo", "♿"), ("Guía para Mochileros", "🎒"),
            ("Guía para Turismo de Lujo", "💎"), ("Guía para Eventos", "🎈"), ("Guía Local", "📍"),
            ("Guía Nacional", "🇨🇴"), ("Guía Freelance", "🚶"), ("Guía Vinculado a Agencia", "🏢"),
            ("Guía de Cruceros", "🚢"), ("Guía de Excursiones", "🥾"), ("Guía de City Tour", "🏙️"),
            ("Guía de Rutas Temáticas", "🎭"), ("Guía Virtual", "💻"), ("Guía Digital", "📱")
        ]

        # 7. Transporte (50)
        transporte_data = [
            ("Transporte Terrestre Turístico", "🚌"), ("Transporte Aéreo Turístico", "✈️"),
            ("Transporte Fluvial Turístico", "🚤"), ("Transporte Marítimo Turístico", "🚢"),
            ("Transporte Ferroviario Turístico", "🚂"), ("Buses Turísticos", "🚌"),
            ("Vans Turísticas", "🚐"), ("Automóviles Privados", "🚗"), ("Motocicletas Turísticas", "🏍️"),
            ("Bicicletas Turísticas", "🚲"), ("Transporte Privado", "👤"), ("Transporte Compartido", "👥"),
            ("Transporte Puerta a Puerta", "🏠"), ("Transporte por Horas", "⏱️"), ("Transporte por Rutas", "🗺️"),
            ("Transporte de Lujo", "💎"), ("Transporte Económico", "💰"), ("Transporte Ejecutivo", "💼"),
            ("Transporte Todo Incluido", "🍹"), ("Transporte con Conductor Guía", "🗣️"),
            ("Transporte Local", "📍"), ("Transporte Regional", "🏘️"), ("Transporte Nacional", "🇨🇴"),
            ("Transporte Internacional", "🌎"), ("Transporte Urbano", "🏙️"), ("Transporte Intermunicipal", "🏘️"),
            ("Transporte Rural", "🚜"), ("Transporte de Aeropuerto", "✈️"), ("Transporte Hotelero", "🏨"),
            ("Transporte para Eventos", "🎈"), ("Transporte para Grupos", "🚌"), ("Transporte para Familias", "👨‍👩‍👧"),
            ("Transporte Corporativo", "💼"), ("Transporte Escolar", "🎓"), ("Transporte para Adultos Mayores", "👵"),
            ("Transporte Accesible", "♿"), ("Transporte VIP", "👑"), ("Transporte para Mochileros", "🎒"),
            ("Transporte para Parejas", "💕"), ("Transporte para Cruceristas", "🚢"),
            ("Transporte Ecológico", "🌿"), ("Transporte de Aventura (4x4)", "🚜"),
            ("Transporte Cultural", "🎨"), ("Transporte Gastronómico", "🥘"), ("Transporte Religioso", "⛪"),
            ("Transporte de Naturaleza", "🌳"), ("City Tour", "🏙️"), ("Transporte Panorámico", "🔭"),
            ("Transporte Nocturno", "🌙"), ("Transporte Temático", "🎭")
        ]

        # 8. Asociaciones (50)
        asociaciones_data = [
            ("Asociación de Prestadores", "🤝"), ("Asociación de Empresarios", "💼"),
            ("Asociación Gremial", "🏛️"), ("Asociación Comunitaria", "👥"),
            ("Asociación Sin Ánimo de Lucro", "💖"), ("Cooperativa Turística", "🤝"),
            ("Corporación Turística", "🏢"), ("Fundación Turística", "🎗️"), ("Red Turística", "🌐"),
            ("Clúster Turístico", "🧩"), ("Asociación Local", "📍"), ("Asociación Municipal", "🏙️"),
            ("Asociación Regional", "🏘️"), ("Asociación Departamental", "🗺️"),
            ("Asociación Nacional", "🇨🇴"), ("Asociación Binacional", "🇨🇴🇻🇪"), ("Asociación Rural", "🚜"),
            ("Asociación Urbana", "🏙️"), ("Asociación de Destino", "📍"), ("Asociación de Corredor Turístico", "🛣️"),
            ("Asociación de Hoteles", "🏨"), ("Asociación de Restaurantes", "🍽️"),
            ("Asociación de Agencias", "✈️"), ("Asociación de Guías", "🧭"),
            ("Asociación de Transportadores", "🚌"), ("Asociación de Artesanos", "🎨"),
            ("Asociación de Operadores", "🚌"), ("Asociación de Emprendedores", "🚀"),
            ("Asociación de Turismo Comunitario", "🤝"), ("Asociación de Prestadores Mixtos", "🔄"),
            ("Asociación de Ecoturismo", "🌿"), ("Asociación de Turismo Sostenible", "♻️"),
            ("Asociación de Turismo de Naturaleza", "🌳"), ("Asociación de Turismo Cultural", "🎨"),
            ("Asociación de Turismo Gastronómico", "🥘"), ("Asociación de Turismo de Aventura", "🧗"),
            ("Asociación de Turismo Rural", "🚜"), ("Asociación de Turismo Religioso", "⛪"),
            ("Asociación de Turismo de Bienestar", "🧘"), ("Asociación de Turismo Accesible", "♿"),
            ("Promoción Turística", "📣"), ("Comercialización Turística", "🛒"),
            ("Fortalecimiento Empresarial", "💪"), ("Capacitación Turística", "📚"),
            ("Innovación Turística", "💡"), ("Desarrollo Turístico", "🏗️"),
            ("Planificación Turística", "🗺️"), ("Integración Turística", "🤝"),
            ("Representación Gremial", "🏛️"), ("Gestión de Destinos", "📊")
        ]

        # 9. Artesanos (50)
        artesanos_data = [
            ("Tejedor", "🧵"), ("Bordador", "🪡"), ("Tallador", "🔨"), ("Alfarero", "🏺"),
            ("Ceramista", "🍯"), ("Orfebre", "💍"), ("Joyero", "💎"), ("Ebanista", "🪑"),
            ("Carpintero", "🪵"), ("Talabartero", "👢"), ("Artesano en Madera", "🪵"),
            ("Artesano en Cerámica", "🍯"), ("Artesano en Barro", "🏺"), ("Artesano en Cuero", "👞"),
            ("Artesano en Piedra", "🗿"), ("Artesano en Metal", "🛠️"), ("Artesano en Vidrio", "🍷"),
            ("Artesano en Fibras Naturales", "🌿"), ("Artesano en Papel", "📄"), ("Artesano en Textiles", "👔"),
            ("Artesano Tradicional", "🏛️"), ("Artesano Indígena", "🏹"), ("Artesano Afrodescendiente", "🥁"),
            ("Artesano Campesino", "🚜"), ("Artesano Ancestral", "📜"), ("Artesano Contemporáneo", "🎨"),
            ("Artesano Urbano", "🏙️"), ("Artesano Rural", "🏡"), ("Artesano Étnico", "🎭"),
            ("Artesano Patrimonial", "🏺"), ("Decoración", "🏡"), ("Bisutería", "📿"),
            ("Joyería", "💎"), ("Mobiliario", "🛋️"), ("Instrumentos Musicales", "🎸"), ("Juguetes", "🧸"),
            ("Utensilios Domésticos", "🥣"), ("Prendas de Vestir", "👔"), ("Accesorios", "👜"),
            ("Arte Religioso", "⛪"), ("Independiente", "🚶"), ("Asociado", "🤝"),
            ("Emprendedor", "🚀"), ("Exportador", "🌎"), ("Sostenible", "♻️"), ("Ecológico", "🌿"),
            ("Innovador", "💡"), ("Tradicional-Comercial", "🛒"), ("Economía Solidaria", "🤝"),
            ("Artesano Turístico", "📸")
        ]

        # 10. Delivery (50)
        delivery_data = [
            ("Comida Preparada", "🍽️"), ("Comida Rápida", "🍔"), ("Mercado", "🛒"), ("Farmacia", "💊"),
            ("Bebidas", "🥤"), ("Postres", "🍰"), ("Productos Orgánicos", "🌿"), ("Flores", "💐"),
            ("Regalos", "🎁"), ("Mascotas", "🐾"), ("Restaurantes Gourmet", "⭐"), ("Comida Casera", "🏠"),
            ("Comida Saludable", "🥗"), ("Comida Internacional", "🌎"), ("Comida Típica", "🇨🇴"),
            ("Comida Vegetariana", "🌱"), ("Comida Vegana", "🌿"), ("Snacks", "🥨"), ("Panadería", "🥖"),
            ("Café", "☕"), ("Delivery Propio", "🛵"), ("Delivery Tercerizado", "🚚"),
            ("Plataformas Digitales", "📱"), ("Delivery Colaborativo", "🤝"), ("Exprés", "⚡"),
            ("Programado", "📅"), ("Por Suscripción", "🔁"), ("Última Milla", "📦"), ("Cadena Fría", "❄️"),
            ("Vehículos Eléctricos", "⚡"), ("App Móvil", "📱"), ("Página Web", "💻"),
            ("Redes Sociales", "📸"), ("WhatsApp", "💬"), ("Automatizado", "⚙️"), ("Con IA", "🤖"),
            ("Seguimiento en Tiempo Real", "📍"), ("Sin Contacto", "🛡️"), ("Pago Digital", "💳"),
            ("Omnicanal", "🔄"), ("Local", "🏠"), ("Urbano", "🏙️"), ("Rural", "🚜"), ("Corporativo", "💼"),
            ("Eventos", "🎈"), ("Turistas", "📸"), ("Ecológico", "🌿"), ("Inclusivo", "♿"),
            ("De Lujo", "👑"), ("Comunitario", "🤝")
        ]

        master_list = [
            ('HOTEL', hoteles_data),
            ('RESTAURANT', restaurantes_data),
            ('BAR', bares_data),
            ('DISCO', discos_data),
            ('AGENCY', agencias_data),
            ('GUIDE', guias_data),
            ('TRANSPORT', transporte_data),
            ('ASSOCIATION', asociaciones_data),
            ('ARTISAN', artesanos_data),
            ('DELIVERY', delivery_data),
        ]

        for category, items in master_list:
            for name, icon in items:
                slug = slugify(f"{category}-{name}")
                TourismSubClassification.objects.update_or_create(
                    slug=slug,
                    defaults={
                        'category': category,
                        'name': name,
                        'icon': icon
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 500 sub-classifications.'))
