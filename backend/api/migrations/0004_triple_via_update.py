from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customuser_role'),
        ('turismo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(
                choices=[
                    ('ADMIN', 'Super Administrador'),
                    ('ADMIN_ENTIDAD', 'Admin de Entidad'),
                    ('ADMIN_NACIONAL', 'Admin Entidad Nacional'),
                    ('ADMIN_DEPARTAMENTAL', 'Admin Entidad Departamental'),
                    ('ADMIN_MUNICIPAL', 'Admin Entidad Municipal'),
                    ('DIRECTIVO_NACIONAL', 'Directivo Nacional'),
                    ('DIRECTIVO_DEPARTAMENTAL', 'Directivo Departamental'),
                    ('DIRECTIVO_MUNICIPAL', 'Directivo Municipal'),
                    ('FUNCIONARIO_DIRECTIVO', 'Funcionario Directivo'),
                    ('FUNCIONARIO_PROFESIONAL', 'Funcionario Profesional'),
                    ('FUNCIONARIO_TECNICO', 'Funcionario Técnico'),
                    ('FUNCIONARIO_ASISTENCIAL', 'Funcionario Asistencial'),
                    ('PRESTADOR', 'Prestador de Servicio (Genérico)'),
                    ('BUSINESS_OWNER', 'Propietario de Negocio'),
                    ('BUSINESS_ADMIN', 'Administrador de Negocio'),
                    ('BUSINESS_OPERATOR', 'Operador de Negocio'),
                    ('BUSINESS_EMPLOYEE', 'Empleado de Negocio'),
                    ('ARTESANO', 'Artesano'),
                    ('DELIVERY', 'Delivery / Logística (Genérico)'),
                    ('DELIVERY_ADMIN', 'Administrador de Delivery'),
                    ('DELIVERY_DRIVER', 'Repartidor / Mensajero'),
                    ('DELIVERY_OPERATOR', 'Operador Logístico'),
                    ('TURISTA', 'Turista'),
                    ('CONSEJO_CONSULTIVO_TURISMO', 'Consejo Consultivo de Turismo'),
                ],
                max_length=50,
                verbose_name='Rol'
            ),
        ),
        migrations.CreateModel(
            name='GovernmentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('nivel', models.CharField(choices=[('NACIONAL', 'Nacional'), ('DEPARTAMENTAL', 'Departamental'), ('MUNICIPAL', 'Municipal')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officials_created', to='api.customuser')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officials', to='api.entity')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='government_profile', to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='turismo.tourismprovider')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_user_profile', to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='TouristProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(default='Colombiana', max_length=100)),
                ('preferences', models.JSONField(default=dict)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tourist_profile', to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('vehicle_type', models.CharField(blank=True, max_length=100)),
                ('license_plate', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(default='OFFLINE', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_profile', to='api.customuser')),
            ],
        ),
    ]
