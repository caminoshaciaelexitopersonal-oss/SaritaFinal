import random
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import CustomUser, PrestadorServicio, CategoriaPrestador, Department, Municipality
from empresa.models import Producto, RegistroCliente, Inventario, Costo, Recurso, ReglaPrecio
from restaurante.models import CategoriaMenu, ProductoMenu, Mesa
from turismo.models import Hotel, Habitacion

class Command(BaseCommand):
    help = 'Crea datos de prueba para la plataforma SaritaUnificado.'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('--- Iniciando la creación de datos de prueba ---'))

        # Limpiar datos antiguos
        self.stdout.write('Limpiando datos antiguos...')
        CustomUser.objects.filter(username='prestador_test').delete()
        CategoriaPrestador.objects.all().delete()

        # Crear datos básicos
        self.stdout.write('Creando categorías y ubicaciones...')
        cat_hotel, _ = CategoriaPrestador.objects.get_or_create(nombre='Hoteles', slug='hoteles')
        cat_restaurante, _ = CategoriaPrestador.objects.get_or_create(nombre='Restaurantes', slug='restaurantes')
        dep, _ = Department.objects.get_or_create(name='Meta')
        mun, _ = Municipality.objects.get_or_create(name='Villavicencio', department=dep)

        # --- Crear Prestador de Servicios de tipo Hotel y Restaurante ---
        self.stdout.write('Creando usuario de prueba: prestador_test')
        user, created = CustomUser.objects.get_or_create(
            username='prestador_test',
            defaults={'email': 'prestador@test.com', 'role': CustomUser.Role.PRESTADOR}
        )
        if created:
            user.set_password('password123')
            user.save()

        prestador, _ = PrestadorServicio.objects.get_or_create(
            usuario=user,
            defaults={
                'nombre_negocio': 'Hotel y Restaurante El Paraíso',
                'categoria': cat_hotel, # Asignamos una categoría principal
                'department': dep,
                'municipality': mun,
                'aprobado': True,
            }
        )
        # El modelo no soporta categorías adicionales, se asigna una principal.
        # prestador.categorias_adicionales.add(cat_restaurante)

        # --- Datos para Módulos Genéricos (Empresa) ---
        self.stdout.write('Creando datos para módulos genéricos...')
        Producto.objects.create(prestador=prestador, nombre='Noche en Habitación Estándar', precio=150000)
        Producto.objects.create(prestador=prestador, nombre='Desayuno Americano', precio=25000)
        RegistroCliente.objects.create(prestador=prestador, pais_origen='Colombia', cantidad=10, fecha_registro='2024-10-01')
        Inventario.objects.create(prestador=prestador, nombre_item='Almohadas', cantidad=50, unidad='unidades', punto_reorden=10)
        Costo.objects.create(prestador=prestador, concepto='Nómina Octubre', monto=5000000, fecha='2024-10-01', tipo_costo='FIJO')
        Recurso.objects.create(prestador=prestador, nombre='Recepcionista Turno A', tipo_recurso='HUMANO')

        # --- Datos para Módulos de Restaurante ---
        self.stdout.write('Creando datos para módulos de restaurante...')
        cat_bebidas = CategoriaMenu.objects.create(prestador=prestador, nombre='Bebidas')
        ProductoMenu.objects.create(categoria=cat_bebidas, nombre='Jugo de Naranja', precio=8000)
        Mesa.objects.create(prestador=prestador, numero_mesa='1', capacidad=4, estado='DISPONIBLE')

        # --- Datos para Módulos de Hotel ---
        self.stdout.write('Creando datos para módulos de hotel...')
        hotel_profile, _ = Hotel.objects.get_or_create(prestador=prestador, defaults={'categoria_estrellas': 4})
        Habitacion.objects.create(hotel=hotel_profile, nombre_o_numero='101', tipo_habitacion='DOBLE', capacidad=2, precio_por_noche=150000)

        self.stdout.write(self.style.SUCCESS('--- Proceso completado exitosamente ---'))