"""
Módulo de Políticas de Dominio para SG-SST.

Este archivo define las reglas de negocio, normativas y constantes
que rigen el dominio de Seguridad y Salud en el Trabajo. El Coronel
utiliza estas políticas para validar planes y tareas.
"""

from enum import Enum

class NivelRiesgo(Enum):
    """Enumeración de los niveles de riesgo laboral."""
    BAJO = 1
    MEDIO = 2
    ALTO = 3
    CRITICO = 4

class SSTPolicies:
    """
    Contiene las políticas y validaciones específicas del dominio SG-SST.
    """
    # Constante que define el nivel de riesgo máximo aceptable sin acción inmediata.
    MAX_RIESGO_SIN_ACCION_INMEDIATA = NivelRiesgo.ALTO

    # Normativa sobre la frecuencia de inspección de equipos de emergencia (en días).
    FRECUENCIA_INSPECCION_EXTINTORES_DIAS = 30
    FRECUENCIA_INSPECCION_BOTIQUINES_DIAS = 15

    @staticmethod
    def es_riesgo_critico(nivel_riesgo: NivelRiesgo) -> bool:
        """
        Verifica si un nivel de riesgo requiere una acción inmediata según las políticas.

        Args:
            nivel_riesgo: El nivel de riesgo a evaluar.

        Returns:
            True si el riesgo es mayor que el máximo permitido, False en caso contrario.
        """
        if not isinstance(nivel_riesgo, NivelRiesgo):
            raise TypeError("El valor proporcionado debe ser un miembro de NivelRiesgo.")

        print(f"POLICIES: Verificando si el riesgo '{nivel_riesgo.name}' excede el umbral '{SSTPolicies.MAX_RIESGO_SIN_ACCION_INMEDIATA.name}'")

        es_critico = nivel_riesgo.value >= SSTPolicies.MAX_RIESGO_SIN_ACCION_INMEDIATA.value

        if es_critico:
            print("POLICIES: ¡Alerta! Riesgo crítico detectado. Requiere acción inmediata.")
        else:
            print("POLICIES: Riesgo dentro de los parámetros aceptables.")

        return es_critico

    @staticmethod
    def obtener_protocolo_por_riesgo(nivel_riesgo: NivelRiesgo) -> str:
        """
        Devuelve el protocolo de acción estándar para un nivel de riesgo dado.
        """
        protocolos = {
            NivelRiesgo.BAJO: "Documentar y revisar anualmente.",
            NivelRiesgo.MEDIO: "Implementar controles administrativos y seguimiento trimestral.",
            NivelRiesgo.ALTO: "Requiere ingeniería de controles y reporte a gerencia.",
            NivelRiesgo.CRITICO: "Cese de actividades inmediato y plan de mitigación urgente."
        }
        return protocolos.get(nivel_riesgo, "Protocolo no definido.")

# Ejemplo de uso de las políticas
if __name__ == '__main__':
    riesgo_evaluado = NivelRiesgo.CRITICO

    print(f"Evaluando un riesgo de nivel: {riesgo_evaluado.name}")

    if SSTPolicies.es_riesgo_critico(riesgo_evaluado):
        protocolo = SSTPolicies.obtener_protocolo_por_riesgo(riesgo_evaluado)
        print(f"Acción requerida: {protocolo}")

    print("-" * 20)

    riesgo_evaluado = NivelRiesgo.BAJO
    print(f"Evaluando un riesgo de nivel: {riesgo_evaluado.name}")
    if not SSTPolicies.es_riesgo_critico(riesgo_evaluado):
        print("No se requiere acción inmediata.")
