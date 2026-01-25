# backend/apps/sarita_agents/agents/teniente_template.py

from apps.sarita_agents.models import TareaDelegada, RegistroDeEjecucion

class TenienteTemplate:
    """
    Plantilla base para todos los Tenientes.
    Son los ejecutores finales de las tareas atómicas.
    """
    def execute_task(self, tarea: TareaDelegada) -> dict:
        """
        Ejecuta una tarea, registrando el proceso en la BD.
        """
        teniente_name = self.__class__.__name__
        print(f"TENIENTE ({teniente_name}): Ejecutando tarea {tarea.id} - {tarea.descripcion_tarea}")

        tarea.estado = 'EN_PROGRESO'
        tarea.save()

        log = RegistroDeEjecucion.objects.create(
            tarea_delegada=tarea,
            exitoso=False # Asumimos fallo hasta que se complete
        )

        try:
            # --- LA LÓGICA DE NEGOCIO REAL SE IMPLEMENTA AQUÍ ---
            resultado = self.perform_action(tarea.parametros)

            tarea.estado = 'COMPLETADA'
            log.exitoso = True
            log.resultado = resultado

            print(f"TENIENTE ({teniente_name}): Tarea {tarea.id} completada con éxito.")
            return {"status": "SUCCESS", "result": resultado}

        except Exception as e:
            tarea.estado = 'FALLIDA'
            log.salida_log = str(e)

            print(f"TENIENTE ({teniente_name}): Tarea {tarea.id} falló - {e}")
            return {"status": "ERROR", "message": str(e)}

        finally:
            tarea.save()
            log.save()

    def perform_action(self, parametros: dict):
        """
        Este es el método que las subclases deben implementar.
        Contiene la lógica de negocio atómica.
        """
        raise NotImplementedError("El método perform_action() debe ser implementado por cada Teniente.")
