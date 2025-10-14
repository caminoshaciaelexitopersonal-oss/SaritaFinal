import json
from django.core.management.base import BaseCommand
from api.models import Department, Municipality

class Command(BaseCommand):
    help = 'Load departments and municipalities from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found at: {file_path}"))
            return

        for entry in data:
            department_name = entry.get('department')
            if not department_name:
                continue

            department, created = Department.objects.get_or_create(name=department_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created department: {department.name}"))

            for municipality_name in entry.get('municipalities', []):
                municipality, created = Municipality.objects.get_or_create(name=municipality_name, department=department)
                if created:
                    self.stdout.write(f"  - Created municipality: {municipality.name}")

        self.stdout.write(self.style.SUCCESS('Successfully loaded all departments and municipalities.'))