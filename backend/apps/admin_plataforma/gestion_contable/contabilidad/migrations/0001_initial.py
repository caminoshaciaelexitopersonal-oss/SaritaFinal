from django.db import migrations, models
import django.db.models.deletion
import uuid
from django.conf import settings

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_operativa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminChartOfAccounts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_adminchartofaccounts_records', to='admin_operativa.providerprofile')),
            ],
            options={'verbose_name': 'Plan de Cuentas (Admin)', 'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='AdminFiscalPeriod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('locked', 'Locked')], default='open', max_length=20)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_adminfiscalperiod_records', to='admin_operativa.providerprofile')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='AdminAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('asset', 'Asset'), ('liability', 'Liability'), ('equity', 'Equity'), ('income', 'Income'), ('expense', 'Expense')], max_length=20)),
                ('initial_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('chart_of_accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_accounts', to='admin_contabilidad.adminchartofaccounts')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_adminaccount_records', to='admin_operativa.providerprofile')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_children', to='admin_contabilidad.adminaccount')),
                ('parent_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_accounts', to='admin_contabilidad.adminaccount')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='AdminJournalEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('reference', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_posted', models.BooleanField(default=False)),
                ('currency', models.CharField(default='COP', max_length=3)),
                ('exchange_rate', models.DecimalField(decimal_places=6, default=1.0, max_digits=18)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_entries_created', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_adminjournalentry_records', to='admin_operativa.providerprofile')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='admin_entries', to='admin_contabilidad.adminfiscalperiod')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='AdminAccountingTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_code', models.CharField(max_length=20)),
                ('debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='admin_contabilidad.adminaccount')),
                ('journal_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='admin_contabilidad.adminjournalentry')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
    ]
