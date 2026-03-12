from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaaSLead',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('CONTACTED', 'Contacted'), ('QUALIFIED', 'Qualified'), ('PROPOSAL_SENT', 'Proposal Sent'), ('NEGOTIATION', 'Negotiation'), ('CONVERTED', 'Converted'), ('LOST', 'Lost')], default='NEW', max_length=20)),
                ('score', models.IntegerField(default=0)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('estimated_size', models.IntegerField(default=1, help_text='Number of employees or estimated scale.')),
                ('source', models.CharField(default='web', max_length=100)),
                ('utm_source', models.CharField(blank=True, max_length=100, null=True)),
                ('utm_campaign', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lead SaaS',
                'verbose_name_plural': 'Leads SaaS',
            },
        ),
        migrations.CreateModel(
            name='SaaSPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('monthly_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('annual_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('billing_type', models.CharField(choices=[('FLAT', 'Flat Fee'), ('USAGE', 'Usage Based'), ('HYBRID', 'Hybrid')], default='FLAT', max_length=20)),
                ('included_usage', models.IntegerField(default=0, help_text='Units included in flat fee.')),
                ('overage_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=12)),
                ('trial_days', models.IntegerField(default=14)),
                ('user_limit', models.IntegerField(default=1)),
                ('storage_limit_gb', models.IntegerField(default=5)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Plan SaaS',
                'verbose_name_plural': 'Planes SaaS',
            },
        ),
        migrations.CreateModel(
            name='SaaSSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_id', models.UUIDField(db_index=True, unique=True)),
                ('status', models.CharField(choices=[('TRIAL', 'Trial'), ('ACTIVE', 'Active'), ('SUSPENDED', 'Suspended'), ('CANCELLED', 'Cancelled')], default='ACTIVE', max_length=20)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('renewal_date', models.DateField()),
                ('billing_cycle', models.CharField(choices=[('MONTHLY', 'Monthly'), ('ANNUAL', 'Annual')], default='MONTHLY', max_length=20)),
                ('mrr', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('currency', models.CharField(default='COP', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='commercial_engine.saasplan')),
            ],
        ),
        migrations.CreateModel(
            name='CommercialKPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_name', models.CharField(db_index=True, max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=18)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='LeadPipelineLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_status', models.CharField(max_length=50)),
                ('to_status', models.CharField(max_length=50)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('duration_in_stage_hours', models.FloatField(blank=True, null=True)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipeline_logs', to='commercial_engine.saaslead')),
            ],
        ),
        migrations.CreateModel(
            name='SaaSInvoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=50)),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(default='DRAFT', max_length=30)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('currency', models.CharField(default='COP', max_length=3)),
                ('company_id', models.UUIDField(db_index=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='commercial_engine.saassubscription')),
            ],
            options={
                'verbose_name': 'Factura SaaS',
            },
        ),
        migrations.CreateModel(
            name='SaaSInvoiceLine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, default=1.0, max_digits=18)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=18)),
                ('tax_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='commercial_engine.saasinvoice')),
            ],
        ),
    ]
