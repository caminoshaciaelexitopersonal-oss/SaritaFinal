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
            name='PlanDeCuentas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_plandecuentas_records', to='admin_operativa.providerprofile')),
            ],
            options={'verbose_name': 'Plan de Cuentas (Admin)', 'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='PeriodoContable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_closed', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_periodocontable_records', to='admin_operativa.providerprofile')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('account_type', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('saldo_inicial', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_cuenta_records', to='admin_operativa.providerprofile')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_children', to='admin_contabilidad.cuenta')),
                ('plan_de_cuentas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_cuentas', to='admin_contabilidad.plandecuentas')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='AsientoContable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('reference', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_posted', models.BooleanField(default=False)),
                ('creado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_asientos_creados', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_contabilidad_asientocontable_records', to='admin_operativa.providerprofile')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='admin_asientos', to='admin_contabilidad.periodocontable')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='admin_contabilidad.asientocontable')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='admin_contabilidad.cuenta')),
            ],
            options={'app_label': 'admin_contabilidad'},
        ),
    ]
