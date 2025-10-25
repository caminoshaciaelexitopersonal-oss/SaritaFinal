# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/rat/utils.py

def rat_directory_path(instance, filename):
    """
    Genera la ruta de subida para los archivos del RAT de un prestador.
    """
    return f'prestadores/{instance.perfil.usuario.username}/rat/{filename}'
