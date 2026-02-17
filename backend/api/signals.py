# SaritaUnificado/backend/api/signals.py

# TODO: Lógica de Puntuación Desactivada Temporalmente
# El siguiente código de señales ha sido comentado porque depende del modelo obsoleto 'Perfil'
# y de campos de puntuación ('puntuacion_capacitacion', 'puntuacion_reseñas') que ya no existen
# en el modelo refactorizado 'ProviderProfile'.
# Es necesario re-evaluar e implementar una nueva lógica de scoring acorde a la nueva arquitectura.

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import AsistenciaCapacitacion, Resena, ScoringRule
# from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile


# @receiver(post_save, sender=AsistenciaCapacitacion)
# def update_score_on_capacitacion(sender, instance, created, **kwargs):
#     if created:
#         try:
#             perfil = ProviderProfile.objects.get(usuario=instance.usuario)
#             puntos = instance.capacitacion.puntos_asistencia
#             perfil.puntuacion_capacitacion += puntos
#             perfil.save(update_fields=['puntuacion_capacitacion'])
#             perfil.recalcular_puntuacion_total()
#         except ProviderProfile.DoesNotExist:
#             pass

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Artesano
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

@receiver(post_save, sender=Artesano)
def activar_perfil_comercial_artesano(sender, instance, **kwargs):
    """
    FASE 16: Activación automática del perfil productivo turístico
    tras la aprobación gubernamental del artesano.
    """
    if instance.aprobado:
        perfil, created = ProviderProfile.objects.get_or_create(
            usuario=instance.usuario,
            defaults={
                'nombre_comercial': instance.nombre_taller,
                'provider_type': ProviderProfile.ProviderTypes.ARTISAN,
                'is_active': True,
                'is_verified': True
            }
        )
        if not created and not perfil.is_active:
            perfil.is_active = True
            perfil.is_verified = True
            perfil.save(update_fields=['is_active', 'is_verified'])


# @receiver(post_save, sender=Resena)
# def update_score_on_resena(sender, instance, **kwargs):
#     if instance.aprobada and instance.content_type.model_class() == ProviderProfile:
#         try:
#             perfil = ProviderProfile.objects.get(pk=instance.object_id)
#             rules = ScoringRule.load()
#             puntos = instance.calificacion * rules.puntos_por_estrella_reseña

#             # Recalcular la puntuación total de reseñas desde cero para evitar duplicados
#             reseñas_aprobadas = Resena.objects.filter(
#                 content_type=instance.content_type,
#                 object_id=instance.object_id,
#                 aprobada=True
#             )
#             total_puntos_reseñas = sum(
#                 r.calificacion * rules.puntos_por_estrella_reseña for r in reseñas_aprobadas
#             )

#             perfil.puntuacion_reseñas = total_puntos_reseñas
#             perfil.save(update_fields=['puntuacion_reseñas'])
#             perfil.recalcular_puntuacion_total()
#         except ProviderProfile.DoesNotExist:
#             pass
