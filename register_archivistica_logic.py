import os
import sys

# Setup Django environment
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarita.settings')
django.setup()

from apps.admin_plataforma.services.governance_kernel import GovernanceKernel, GovernanceIntention, AuthorityLevel
from api.models import CustomUser

domains = [
    "captura", "clasificacion", "custodia", "acceso",
    "versionado", "conservacion", "eliminacion", "auditoria"
]

def snake_to_camel(snake_str):
    return "".join(x.title() for x in snake_str.split("_"))

print("Registrando Agentes de Gestión Archivística...")

# 1. Coronel General
GovernanceKernel.register_agent("CoronelArchivisticoGeneral", {
    "nivel": "CORONEL_GENERAL",
    "superior": "GeneralSarita",
    "dominio": "GESTION_ARCHIVISTICA",
    "mision": "Gobernar toda la política documental de SARITA",
    "eventos": ["mision_archivistica_recibida"]
})

for domain in domains:
    camel_domain = snake_to_camel(domain)
    coronel_name = f"Coronel{camel_domain}"
    capitan_name = f"Capitan{camel_domain}"
    teniente_name = f"Teniente{camel_domain}"
    sargento_name = f"Sargento{camel_domain}"

    # 2. Coroneles de Dominio
    GovernanceKernel.register_agent(coronel_name, {
        "nivel": "CORONEL",
        "superior": "CoronelArchivisticoGeneral",
        "dominio": f"GESTION_ARCHIVISTICA.{domain.upper()}",
        "mision": f"Gobernar el dominio de {domain}",
        "eventos": ["mision_dominio_recibida"]
    })

    # 3. Capitanes
    GovernanceKernel.register_agent(capitan_name, {
        "nivel": "CAPITAN",
        "superior": coronel_name,
        "dominio": "GESTION_ARCHIVISTICA",
        "mision": f"Gobernar la planificación estratégica de {domain}",
        "eventos": ["mision_planificada"]
    })

    # 4. Tenientes
    GovernanceKernel.register_agent(teniente_name, {
        "nivel": "TENIENTE",
        "superior": capitan_name,
        "dominio": "GESTION_ARCHIVISTICA",
        "mision": f"Coordinar la táctica de {domain}",
        "eventos": ["tarea_coordinada"]
    })

    # 5. Sargentos
    GovernanceKernel.register_agent(sargento_name, {
        "nivel": "SARGENTO",
        "superior": teniente_name,
        "dominio": "GESTION_ARCHIVISTICA",
        "mision": f"Ejecutar acciones atómicas de {domain}",
        "eventos": ["accion_ejecutada"]
    })

    # 6. Soldados
    for i in range(1, 6):
        soldado_name = f"Soldado{camel_domain}_{i}"
        GovernanceKernel.register_agent(soldado_name, {
            "nivel": "SOLDADO",
            "superior": sargento_name,
            "dominio": "GESTION_ARCHIVISTICA",
            "mision": f"Ejecución manual de {domain}",
            "eventos": ["tarea_manual_completada"]
        })

print("Registrando Intenciones de Gestión Archivística...")

archivistica_intentions = [
    ("ARCHIVE_CAPTURE", "captura", AuthorityLevel.OPERATIONAL, ["document_type", "source"]),
    ("ARCHIVE_CLASSIFY", "clasificacion", AuthorityLevel.OPERATIONAL, ["document_id", "metadata"]),
    ("ARCHIVE_STORE", "custodia", AuthorityLevel.DELEGATED, ["document_id", "vault_id"]),
    ("ARCHIVE_ACCESS", "acceso", AuthorityLevel.OPERATIONAL, ["document_id"]),
    ("ARCHIVE_VERSION", "versionado", AuthorityLevel.OPERATIONAL, ["document_id"]),
    ("ARCHIVE_PRESERVE", "conservacion", AuthorityLevel.DELEGATED, ["document_id"]),
    ("ARCHIVE_PURGE", "eliminacion", AuthorityLevel.SOVEREIGN, ["document_id", "reason"]),
    ("ARCHIVE_AUDIT", "auditoria", AuthorityLevel.DELEGATED, ["period"]),
]

for name, domain_suffix, level, params in archivistica_intentions:
    GovernanceKernel.register_intention(GovernanceIntention(
        name=name,
        domain="archivistico",
        required_role=CustomUser.Role.ADMIN,
        required_params=params,
        min_authority=level
    ))

print("Proceso de registro archivístico completado.")
