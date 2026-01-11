"""
Módulo de Memoria del Agente General.

Este archivo define las estructuras y clases responsables de gestionar la memoria
del Agente General Sarita, permitiéndole mantener el contexto a corto, mediano
y largo plazo.
"""

class Memory:
    """
    Gestiona los diferentes tipos de memoria para el Agente General.
    """

    def __init__(self):
        """
        Inicializa los almacenes de memoria.
        """
        self.short_term_memory = {}  # Memoria para la orden actual
        self.medium_term_memory = {} # Memoria para la sesión del usuario
        self.long_term_memory = {}   # (Preparado) Acceso a una base de datos vectorial o similar

    def store_short_term(self, key: str, value):
        """
        Almacena información en la memoria de corto plazo.
        """
        print(f"MEMORIA CORTO PLAZO: Almacenando '{key}'")
        self.short_term_memory[key] = value

    def retrieve_short_term(self, key: str):
        """
        Recupera información de la memoria de corto plazo.
        """
        return self.short_term_memory.get(key)

    def clear_short_term(self):
        """
        Limpia la memoria de corto plazo, típicamente después de una orden.
        """
        print("MEMORIA CORTO PLAZO: Limpiando memoria.")
        self.short_term_memory.clear()

# Puedes añadir más clases o funciones según la complejidad requerida.
