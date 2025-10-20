from langchain_core.tools import tool
from typing import List, Dict
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.models.perfil import Perfil as PrestadorServicio


@tool
def gestionar_oferta_prestador(prestador_id: int, detalles_oferta: str) -> Dict:
    """
    (SOLDADO DE OFERTAS) Crea o actualiza la sección de 'promociones_ofertas'
    para un prestador de servicio específico.
    'prestador_id' es el ID del prestador.
    'detalles_oferta' es el texto que describe la promoción, menú o paquete.
    """
    print(f"--- 💥 SOLDADO (Oferta Turística): ¡ACCIÓN! Gestionando oferta para el prestador {prestador_id}. ---")
    try:
        prestador = PrestadorServicio.objects.get(id=prestador_id)
        prestador.promociones_ofertas = detalles_oferta
        prestador.save(update_fields=['promociones_ofertas'])
        return {
            "status": "success",
            "message": f"La oferta para el prestador '{prestador.nombre_negocio}' (ID: {prestador_id}) ha sido actualizada."
        }
    except PrestadorServicio.DoesNotExist:
        return {
            "status": "error",
            "message": f"No se encontró un prestador con el ID {prestador_id}."
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Ocurrió un error inesperado: {str(e)}"
        }


def get_oferta_soldiers() -> List:
    """ Recluta y devuelve la Escuadra de Oferta Turística completa. """
    return [
        gestionar_oferta_prestador,
    ]