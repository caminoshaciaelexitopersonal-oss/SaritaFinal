import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativaTuristica(CoronelTemplate):
    """
    Nuevo Coronel unificado para Operativa Turística (Fase 16).
    Gestiona tanto Operadores Directos como Cadena Productiva.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_turistico")

    def _get_capitanes(self) -> dict:
        # Importación diferida para reflejar la nueva estructura jerárquica
        from .directos.agencias.capitanes.capitan_agencia import CapitanAgencia
        from .directos.transporte.capitanes.capitan_despacho_flota import CapitanDespachoFlota
        from .directos.guias.capitanes.capitan_gestion_guias import CapitanGestionGuias
        from .directos.nocturno.capitanes.capitan_operacion_nocturna import CapitanOperacionNocturna
        from .directos.hospedaje.capitanes.capitan_gestion_habitaciones import CapitanGestionHabitaciones
        from .directos.gastronomia.capitanes.capitan_servicio_mesa import CapitanServicioMesa

        from .cadena_productiva.artesanos.capitanes.capitan_taller import CapitanTaller

        return {
            "agencia": CapitanAgencia(coronel=self),
            "transporte": CapitanDespachoFlota(coronel=self),
            "guias": CapitanGestionGuias(coronel=self),
            "nocturno": CapitanOperacionNocturna(coronel=self),
            "hospedaje": CapitanGestionHabitaciones(coronel=self),
            "gastronomia": CapitanServicioMesa(coronel=self),
            "artesano": CapitanTaller(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        domain = directiva.get("domain")
        mapping = {
            "operativo_agencia": "agencia",
            "operativo_transporte": "transporte",
            "operativo_guias": "guias",
            "operativo_nocturno": "nocturno",
            "operativo_hospedaje": "hospedaje",
            "operativo_gastronomia": "gastronomia",
            "operativo_artesano": "artesano",
        }
        cap_key = mapping.get(domain)
        if cap_key:
            return self.capitanes.get(cap_key)

        # Fallback por acción si el dominio es genérico operativo_turistico
        action = directiva.get("action", "")
        if "PACKAGE" in action: return self.capitanes.get("agencia")
        if "TRANSPORT" in action: return self.capitanes.get("transporte")
        if "GUIDE" in action: return self.capitanes.get("guias")
        if "RAW_MATERIAL" in action or "WORKSHOP" in action: return self.capitanes.get("artesano")

        return next(iter(self.capitanes.values()))
