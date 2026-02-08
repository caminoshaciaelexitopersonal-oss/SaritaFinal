from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import CustomUser
from .models import WalletAccount
from apps.companies.models import Company

@receiver(post_save, sender=CustomUser)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        # Buscamos una compañía por defecto para el tenant inicial
        company = Company.objects.first()
        if not company:
            # Creamos una compañía SARITA si no existe
            company = Company.objects.create(name="SARITA Institutional", code="SAR")

        owner_type = WalletAccount.OwnerType.TOURIST
        if instance.role == CustomUser.Role.PRESTADOR:
            owner_type = WalletAccount.OwnerType.PROVIDER
        elif instance.role == CustomUser.Role.DELIVERY:
            owner_type = WalletAccount.OwnerType.DELIVERY

        WalletAccount.objects.create(
            user=instance,
            company=company,
            owner_type=owner_type,
            owner_id=str(instance.id),
            balance=0.00
        )
