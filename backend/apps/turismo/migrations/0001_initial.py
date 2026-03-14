from django.db import migrations, models
import django.db.models.deletion
import uuid
from django.conf import settings

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TourismProvider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(max_length=255)),
                ('provider_type', models.CharField(choices=[('HOTEL', 'Hotel'), ('RESTAURANT', 'Restaurante'), ('GUIDE', 'Guía Turístico'), ('TRAVEL_AGENCY', 'Agencia de Viajes'), ('TOUR_OPERATOR', 'Operador Turístico'), ('TRANSPORT', 'Transporte Turístico'), ('VEHICLE_RENTAL', 'Alquiler de Vehículos'), ('ARTISAN', 'Artesano'), ('EVENT_ORGANIZER', 'Organizador de Eventos'), ('EXPERIENCE_PROVIDER', 'Experiencias Turísticas')], max_length=20)),
                ('location', models.JSONField(default=dict, help_text='Coordenadas y dirección')),
                ('contact', models.JSONField(default=dict, help_text='Teléfonos, redes sociales, etc.')),
                ('status', models.CharField(default='ACTIVE', max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tourism_providers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourismService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('service_type', models.CharField(choices=[('ACCOMMODATION', 'Habitación / Alojamiento'), ('TOUR', 'Tour / Recorrido'), ('FOOD', 'Comida / Gastronomía'), ('TRANSPORT', 'Transporte'), ('EXPERIENCE', 'Experiencia'), ('PRODUCT', 'Producto Físico')], max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('availability', models.BooleanField(default=True)),
                ('delivery_available', models.BooleanField(default=False)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='turismo.tourismprovider')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
