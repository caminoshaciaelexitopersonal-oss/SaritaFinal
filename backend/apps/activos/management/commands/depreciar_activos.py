# backend/apps/activos/management/commands/depreciar_activos.py
from django.core.management.base import BaseCommand
from datetime import date
from django.db import models
from apps.activos.models import ActivoFijo
from apps.activos.services import depreciar_activo_un_mes

class Command(BaseCommand):
    help = 'Calcula y registra la depreciación mensual para todos los activos fijos.'

    def handle(self, *args, **options):
        hoy = date.today()
        activos_a_depreciar = ActivoFijo.objects.filter(valor_en_libros__gt=models.F('valor_residual'))

        self.stdout.write(f"Iniciando proceso de depreciación para {hoy.strftime('%Y-%m')}...")
        count = 0
        for activo in activos_a_depreciar:
            registro = depreciar_activo_un_mes(activo, hoy)
            if registro:
                self.stdout.write(self.style.SUCCESS(
                    f"  - Depreciado activo '{activo.nombre}' por {registro.monto}"
                ))
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Proceso finalizado. {count} activos depreciados."))
