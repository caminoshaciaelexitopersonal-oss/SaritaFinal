from django.db import models
from django.db.models import Sum, Avg, Count, F
from django.utils import timezone
from datetime import timedelta
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta, ReciboCaja
from apps.prestadores.mi_negocio.gestion_contable.compras.models import FacturaCompra
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class GovernanceMetricsService:
    """
    Servicio de Inteligencia de Negocio para el Super Admin.
    Consolida información de todos los prestadores de forma READ-ONLY.
    """

    @staticmethod
    def get_global_summary():
        """
        Retorna un resumen ejecutivo global del sistema.
        """
        total_revenue = FacturaVenta.objects.aggregate(total=Sum('total'))['total'] or 0
        total_collections = ReciboCaja.objects.aggregate(total=Sum('monto'))['total'] or 0
        total_providers = ProviderProfile.objects.count()
        total_products = Product.objects.count()

        # Rendimiento promedio (Ingreso por Prestador)
        avg_revenue_per_provider = total_revenue / total_providers if total_providers > 0 else 0

        return {
            "total_revenue": total_revenue,
            "total_collections": total_collections,
            "active_providers": total_providers,
            "total_catalog_size": total_products,
            "avg_revenue_per_provider": avg_revenue_per_provider,
            "timestamp": timezone.now()
        }

    @staticmethod
    def get_comparative_analysis():
        """
        Compara el rendimiento financiero por tipo de prestador y región.
        """
        types_analysis = []
        for p_type in ProviderProfile.ProviderTypes.choices:
            type_code = p_type[0]
            profiles = ProviderProfile.objects.filter(provider_type=type_code)
            ids = profiles.values_list('id', flat=True)

            revenue = FacturaVenta.objects.filter(perfil_ref_id__in=ids).aggregate(total=Sum('total'))['total'] or 0

            types_analysis.append({
                "type": type_code,
                "label": str(p_type[1]),
                "count": profiles.count(),
                "revenue": revenue
            })

        return {
            "by_type": types_analysis,
        }

    @staticmethod
    def get_provider_ranking(limit=10):
        """
        Ranking de prestadores por volumen de facturación.
        """
        # Obtenemos ingresos agregados por perfil_ref_id
        top_revenues = FacturaVenta.objects.values('perfil_ref_id').annotate(
            total_revenue=Sum('total')
        ).order_by('-total_revenue')[:limit]

        ranking = []
        for entry in top_revenues:
            profile = ProviderProfile.objects.filter(id=entry['perfil_ref_id']).first()
            ranking.append({
                "provider_name": profile.nombre_comercial if profile else "Desconocido",
                "revenue": entry['total_revenue'],
                "type": profile.provider_type if profile else "N/A"
            })

        return ranking
