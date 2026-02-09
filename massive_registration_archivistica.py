import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarita.settings')
django.setup()

from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

print("Iniciando Registro Masivo de Agentes Archivísticos (Fase 2.1)...")

# 1. Capitanes
capitanes = [
    ("CapitanCapturaDocumental", "CoronelArchivisticoGeneral", "Gobernar el ingreso y digitalización de documentos."),
    ("CapitanClasificacionMetadatos", "CoronelArchivisticoGeneral", "Gobernar la taxonomía y asignación de metadatos."),
    ("CapitanCustodiaAlmacenamiento", "CoronelArchivisticoGeneral", "Gobernar el almacenamiento seguro y cifrado."),
    ("CapitanAccesoConsulta", "CoronelArchivisticoGeneral", "Gobernar los permisos y visualización de documentos."),
    ("CapitanVersionadoTrazabilidad", "CoronelArchivisticoGeneral", "Gobernar el historial de cambios y hashes."),
    ("CapitanConservacionRetencion", "CoronelArchivisticoGeneral", "Gobernar el ciclo de vida y permanencia."),
    ("CapitanEliminacionGobernada", "CoronelArchivisticoGeneral", "Gobernar la destrucción certificada y auditada."),
    ("CapitanAuditoriaArchivistica", "CoronelArchivisticoGeneral", "Gobernar la verificación de integridad sistémica.")
]

for name, sup, mision in capitanes:
    GovernanceKernel.register_agent(name, {
        "nivel": "CAPITAN",
        "superior": sup,
        "dominio": "GESTION_ARCHIVISTICA",
        "mision": mision
    })

# 2. Tenientes
tenientes_map = {
    "CapitanCapturaDocumental": ["TenienteDigitalizacionDirecta", "TenienteIngresoLote"],
    "CapitanClasificacionMetadatos": ["TenienteTaxonomiaAutomatica", "TenienteValidacionMetadatos"],
    "CapitanCustodiaAlmacenamiento": ["TenienteCifradoArchivos", "TenienteGestionBoveda"],
    "CapitanAccesoConsulta": ["TenienteControlPermisos", "TenienteMotorBusqueda"],
    "CapitanVersionadoTrazabilidad": ["TenienteSeguimientoCambios", "TenienteSelladoTiempo"],
    "CapitanConservacionRetencion": ["TenientePoliticasPurga", "TenientePreservacionDigital"],
    "CapitanEliminacionGobernada": ["TenienteDestruccionCertificada", "TenienteAuditoriaEliminacion"],
    "CapitanAuditoriaArchivistica": ["TenienteMuestreoAleatorio", "TenienteInformesCumplimiento"]
}

for sup, tenientes in tenientes_map.items():
    for t in tenientes:
        GovernanceKernel.register_agent(t, {
            "nivel": "TENIENTE",
            "superior": sup,
            "dominio": "GESTION_ARCHIVISTICA",
            "mision": f"Coordinación táctica para {sup}"
        })

# 3. Sargentos
sargentos_map = {
    "TenienteDigitalizacionDirecta": ["SargentoEscaneoFisico"],
    "TenienteIngresoLote": ["SargentoProcesamientoZip"],
    "TenienteTaxonomiaAutomatica": ["SargentoEtiquetadoIA"],
    "TenienteValidacionMetadatos": ["SargentoVerificacionCampos"],
    "TenienteCifradoArchivos": ["SargentoCifradoAES"],
    "TenienteGestionBoveda": ["SargentoReplicacionCloud"],
    "TenienteControlPermisos": ["SargentoValidacionACL"],
    "TenienteMotorBusqueda": ["SargentoIndexacionElastic"],
    "TenienteSeguimientoCambios": ["SargentoRegistroVersiones"],
    "TenienteSelladoTiempo": ["SargentoNotarizacionBlockchain"],
    "TenientePoliticasPurga": ["SargentoMarcadoEliminacion"],
    "TenientePreservacionDigital": ["SargentoConversionFormato"],
    "TenienteDestruccionCertificada": ["SargentoBorradoSeguro"],
    "TenienteAuditoriaEliminacion": ["SargentoCertificacionDestruccion"],
    "TenienteMuestreoAleatorio": ["SargentoSeleccionAuditoria"],
    "TenienteInformesCumplimiento": ["SargentoGeneracionReporte"]
}

for sup, sargentos in sargentos_map.items():
    for s in sargentos:
        GovernanceKernel.register_agent(s, {
            "nivel": "SARGENTO",
            "superior": sup,
            "dominio": "GESTION_ARCHIVISTICA",
            "mision": f"Ejecución atómica para {sup}"
        })

# 4. Soldados (Massive)
for sup_teniente, sargentos in sargentos_map.items():
    for s in sargentos:
        prefix = s.replace("Sargento", "")
        for i in range(1, 6):
            soldado_name = f"Soldado{prefix}_{i}"
            GovernanceKernel.register_agent(soldado_name, {
                "nivel": "SOLDADO",
                "superior": s,
                "dominio": "GESTION_ARCHIVISTICA",
                "mision": f"Tarea manual {i} para {s}"
            })

print(f"Registro completado. Total agentes en Kernel: {len(GovernanceKernel._agent_registry)}")
