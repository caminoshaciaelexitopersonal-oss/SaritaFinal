from django.test import TestCase
from api.models import CustomUser
from apps.companies.models import Company
from apps.wallet.models import WalletAccount, WalletTransaction
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel, AuthorityLevel
from decimal import Decimal

class WalletIntegrationTest(TestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            username='admin_test', email='admin_test@test.com', password='password'
        )
        self.company = Company.objects.create(name='Test Company Wallet', code='TCW')
        self.tourist_user = CustomUser.objects.create_user(
            username='tourist_test', email='tourist_test@test.com', password='password',
            role=CustomUser.Role.TURISTA
        )
        self.provider_user = CustomUser.objects.create_user(
            username='provider_test', email='provider_test@test.com', password='password',
            role=CustomUser.Role.PRESTADOR
        )

        # Get or create wallets (signals might have created them)
        self.tourist_wallet, _ = WalletAccount.objects.get_or_create(
            user=self.tourist_user,
            defaults={
                'owner_type': WalletAccount.OwnerType.TOURIST,
                'owner_id': str(self.tourist_user.id),
                'company': self.company,
                'balance': Decimal('100.00')
            }
        )
        if self.tourist_wallet.balance < Decimal('100.00'):
            self.tourist_wallet.balance = Decimal('100.00')
            self.tourist_wallet.save()

        self.provider_wallet, _ = WalletAccount.objects.get_or_create(
            user=self.provider_user,
            defaults={
                'owner_type': WalletAccount.OwnerType.PROVIDER,
                'owner_id': 'some-uuid-for-provider-test',
                'company': self.company,
                'balance': Decimal('0.00')
            }
        )

    def test_governance_payment(self):
        kernel = GovernanceKernel(user=self.tourist_user)

        # Perform payment through kernel
        result = kernel.resolve_and_execute(
            intention_name="WALLET_PAY",
            parameters={
                "to_wallet_id": str(self.provider_wallet.id),
                "amount": 50.00,
                "description": "Test Payment"
            }
        )

        self.assertEqual(result['status'], 'SUCCESS')
        self.tourist_wallet.refresh_from_db()
        self.provider_wallet.refresh_from_db()

        self.assertEqual(self.tourist_wallet.balance, Decimal('50.00'))
        self.assertEqual(self.provider_wallet.balance, Decimal('50.00'))

        # Check transaction
        tx = WalletTransaction.objects.get(id=result['transaction_id'])
        self.assertEqual(tx.amount, Decimal('50.00'))
        self.assertEqual(tx.type, WalletTransaction.TransactionType.PAYMENT)

    def test_insufficient_funds(self):
        kernel = GovernanceKernel(user=self.tourist_user)

        with self.assertRaises(ValueError):
            kernel.resolve_and_execute(
                intention_name="WALLET_PAY",
                parameters={
                    "to_wallet_id": str(self.provider_wallet.id),
                    "amount": 150.00
                }
            )

    def test_freeze_wallet(self):
        kernel = GovernanceKernel(user=self.admin)

        result = kernel.resolve_and_execute(
            intention_name="WALLET_FREEZE",
            parameters={
                "wallet_id": str(self.tourist_wallet.id),
                "motivo": "Auditoria de seguridad"
            }
        )

        self.assertEqual(result['status'], 'SUCCESS')
        self.tourist_wallet.refresh_from_db()
        self.assertEqual(self.tourist_wallet.status, WalletAccount.Status.FROZEN)

        # Now payment should fail
        kernel_tourist = GovernanceKernel(user=self.tourist_user)
        with self.assertRaises(PermissionError):
            kernel_tourist.resolve_and_execute(
                intention_name="WALLET_PAY",
                parameters={
                    "to_wallet_id": str(self.provider_wallet.id),
                    "amount": 10.00
                }
            )
