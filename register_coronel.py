import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarita.settings')
django.setup()

from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

print("Registrando Coronel Archivístico General...")

GovernanceKernel.register_agent("CoronelArchivisticoGeneral", {
    "nivel": "CORONEL_GENERAL",
    "superior": "GeneralSarita",
    "dominio": "GESTION_ARCHIVISTICA",
    "mision": "Gobernar toda la política documental de SARITA",
    "eventos": ["politica_documental_actualizada"]
})

print("Registro completado.")
