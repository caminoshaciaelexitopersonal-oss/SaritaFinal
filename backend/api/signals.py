# SaritaUnificado/backend/api/signals.py

# TODO: Lógica de Puntuación Desactivada Temporalmente
# El siguiente código de señales ha sido comentado porque depende del modelo obsoleto 'Perfil'
# y de campos de puntuación ('puntuacion_capacitacion', 'puntuacion_reseñas') que ya no existen
# en el modelo refactorizado 'ProviderProfile'.
# Es necesario re-evaluar e implementar una nueva lógica de scoring acorde a la nueva arquitectura.

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AsistenciaCapacitacion, Resena, ScoringRule, Artesano
from apps.domain_business.operativa.models import ProviderProfile


@receiver(post_save, sender=AsistenciaCapacitacion)
def update_score_on_capacitacion(sender, instance, created, **kwargs):
    """
    Actualiza la puntuación del artesano o prestador por asistir a capacitaciones.
    """
    if created:
        try:
            # Intentar encontrar el perfil de artesano primero
            if hasattr(instance.usuario, 'perfil_artesano'):
                artesano = instance.usuario.perfil_artesano
                puntos = instance.capacitacion.puntos_asistencia
                artesano.puntuacion_capacitacion += puntos
                artesano.save(update_fields=['puntuacion_capacitacion'])
                artesano.recalcular_puntuacion_total()

            # También actualizar el perfil de dominio si existe
            perfil = ProviderProfile.objects.filter(user=instance.usuario).first()
            if perfil:
                # El modelo ProviderProfile actual no tiene campos de puntuación específicos,
                # pero se emite un evento para que la inteligencia de negocio lo registre.
                from apps.core_erp.event_bus import EventBus
                EventBus.emit("SCORE_UPDATED", {
                    "user_id": str(instance.usuario.id),
                    "type": "CAPACITACION",
                    "points": instance.capacitacion.puntos_asistencia
                })
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(f"Error actualizando puntuación: {e}")


def register_security_monitors():
    from django.contrib.auth.signals import user_login_failed
    from apps.core_erp.event_bus import EventBus

    @receiver(user_login_failed)
    def track_failed_login(sender, credentials, request, **kwargs):
        """
        Omnisciencia: Monitoreo de intentos de login fallidos (Fase 4.4.2).
        """
        EventBus.emit(
            "LOGIN_FAILED",
            {
                "username": credentials.get('username'),
                "ip": request.META.get('REMOTE_ADDR') if request else "unknown",
                "user_agent": request.META.get('HTTP_USER_AGENT') if request else "unknown"
            },
            severity="warning"
        )

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


@receiver(post_save, sender=Resena)
def update_score_on_resena(sender, instance, **kwargs):
    """
    Actualiza la puntuación basada en las reseñas aprobadas.
    """
    if instance.aprobada:
        try:
            rules = ScoringRule.load()
            model_class = instance.content_type.model_class()

            if model_class == Artesano:
                artesano = Artesano.objects.get(pk=instance.object_id)
                # Recalcular la puntuación total de reseñas desde cero para evitar inconsistencias
                reseñas_aprobadas = Resena.objects.filter(
                    content_type=instance.content_type,
                    object_id=instance.object_id,
                    aprobada=True
                )
                total_puntos_reseñas = sum(
                    r.calificacion * rules.puntos_por_estrella_reseña for r in reseñas_aprobadas
                )

                artesano.puntuacion_reseñas = total_puntos_reseñas
                artesano.save(update_fields=['puntuacion_reseñas'])
                artesano.recalcular_puntuacion_total()

            elif model_class == ProviderProfile:
                from apps.core_erp.event_bus import EventBus
                EventBus.emit("SCORE_UPDATED", {
                    "entity_id": str(instance.object_id),
                    "type": "RESENA",
                    "rating": instance.calificacion,
                    "points": instance.calificacion * rules.puntos_por_estrella_reseña
                })
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(f"Error actualizando puntuación de reseña: {e}")
