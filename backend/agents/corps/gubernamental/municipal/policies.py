"""
Módulo de Políticas de Dominio para Gobernanza Municipal.

Este archivo define las reglas de negocio, normativas y constantes
que rigen el dominio de la administración municipal.
"""

from datetime import date, timedelta
from enum import Enum

class EstadoLicencia(Enum):
    """Enumeración de los estados de una licencia comercial."""
    VALIDA = "VALIDA"
    PROXIMA_A_VENCER = "PROXIMA_A_VENCER"
    VENCIDA = "VENCIDA"
    REVOCADA = "REVOCADA"

class GubernamentalMunicipalPolicies:
    """
    Contiene las políticas y validaciones específicas del dominio municipal.
    """
    # Días de antelación para notificar sobre una licencia que está por vencer.
    DIAS_AVISO_VENCIMIENTO_LICENCIA = 30

    @staticmethod
    def clasificar_estado_licencia(fecha_vencimiento: date) -> EstadoLicencia:
        """
        Clasifica el estado de una licencia basado en su fecha de vencimiento.

        Args:
            fecha_vencimiento: La fecha en que la licencia expira.

        Returns:
            Un miembro de la enumeración EstadoLicencia.
        """
        hoy = date.today()
        if fecha_vencimiento < hoy:
            return EstadoLicencia.VENCIDA

        aviso_previo = timedelta(days=GubernamentalMunicipalPolicies.DIAS_AVISO_VENCIMIENTO_LICENCIA)
        if fecha_vencimiento <= hoy + aviso_previo:
            return EstadoLicencia.PROXIMA_A_VENCER

        return EstadoLicencia.VALIDA

    @staticmethod
    def requiere_inspeccion_para_actividad(actividad_comercial: str) -> bool:
        """
        Determina si una nueva solicitud de licencia requiere una inspección física.
        """
        actividades_de_riesgo = ["restaurante", "bar", "construccion", "evento_masivo"]

        requiere = any(actividad in actividad_comercial.lower() for actividad in actividades_de_riesgo)

        print(f"POLICIES: Verificando si la actividad '{actividad_comercial}' requiere inspección: {'Sí' if requiere else 'No'}")
        return requiere

# Ejemplo de uso de las políticas
if __name__ == '__main__':
    print("--- Verificación de Estado de Licencias ---")
    licencia_vencida = date.today() - timedelta(days=10)
    licencia_ok = date.today() + timedelta(days=100)
    licencia_por_vencer = date.today() + timedelta(days=15)

    print(f"Licencia 1 (vence {licencia_vencida}): Estado = {GubernamentalMunicipalPolicies.clasificar_estado_licencia(licencia_vencida).name}")
    print(f"Licencia 2 (vence {licencia_ok}): Estado = {GubernamentalMunicipalPolicies.clasificar_estado_licencia(licencia_ok).name}")
    print(f"Licencia 3 (vence {licencia_por_vencer}): Estado = {GubernamentalMunicipalPolicies.clasificar_estado_licencia(licencia_por_vencer).name}")

    print("\n--- Verificación de Necesidad de Inspección ---")
    GubernamentalMunicipalPolicies.requiere_inspeccion_para_actividad("Apertura de nuevo restaurante gourmet")
    GubernamentalMunicipalPolicies.requiere_inspeccion_para_actividad("Consultoría de software")
