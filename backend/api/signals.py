 # SaritaUnificado/backend/api/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AsistenciaCapacitacion, Resena, ScoringRule
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil


@receiver(post_save, sender=AsistenciaCapacitacion)
def update_score_on_capacitacion(sender, instance, created, **kwargs):
    if created:
        try:
            perfil = Perfil.objects.get(usuario=instance.usuario)
            puntos = instance.capacitacion.puntos_asistencia
            perfil.puntuacion_capacitacion += puntos
            perfil.save(update_fields=['puntuacion_capacitacion'])
            perfil.recalcular_puntuacion_total()
        except Perfil.DoesNotExist:
            pass


@receiver(post_save, sender=Resena)
def update_score_on_resena(sender, instance, **kwargs):
    if instance.aprobada and instance.content_type.model_class() == Perfil:
        try:
            perfil = Perfil.objects.get(pk=instance.object_id)
            rules = ScoringRule.load()
            puntos = instance.calificacion * rules.puntos_por_estrella_reseña

            # Recalcular la puntuación total de reseñas desde cero para evitar duplicados
            reseñas_aprobadas = Resena.objects.filter(
                content_type=instance.content_type,
                object_id=instance.object_id,
                aprobada=True
            )
            total_puntos_reseñas = sum(
                r.calificacion * rules.puntos_por_estrella_reseña for r in reseñas_aprobadas
            )

            perfil.puntuacion_reseñas = total_puntos_reseñas
            perfil.save(update_fields=['puntuacion_reseñas'])
            perfil.recalcular_puntuacion_total()
        except Perfil.DoesNotExist:
            pass
