import json
from django.core.management.base import BaseCommand
from api.models import Department, Municipality

class Command(BaseCommand):
    help = 'Carga departamentos y municipios desde un archivo JSON.'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='La ruta al archivo JSON que contiene los datos de las ubicaciones.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['json_file']
        self.stdout.write(self.style.NOTICE(f"Iniciando la carga de ubicaciones desde {file_path}..."))

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Error: El archivo {file_path} no fue encontrado."))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Error: El archivo {file_path} no es un JSON válido."))
            return

        departments_created = 0
        municipalities_created = 0

        for entry in data:
            departamento_nombre = entry.get('departamento')
            municipios_nombres = entry.get('municipios', [])

            if not departamento_nombre:
                self.stdout.write(self.style.WARNING("Omitiendo entrada sin nombre de departamento."))
                continue

            department, created = Department.objects.get_or_create(name=departamento_nombre)
            if created:
                departments_created += 1
                self.stdout.write(f"  Departamento creado: {department.name}")

            for municipio_nombre in municipios_nombres:
                _, created = Municipality.objects.get_or_create(name=municipio_nombre, department=department)
                if created:
                    municipalities_created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Proceso completado. Departamentos creados: {departments_created}. Municipios creados: {municipalities_created}."
        ))