# Generated by Django 4.0.3 on 2022-05-25 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labtienda', '0006_rename_descripción_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=100)),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('actualizada', models.DateTimeField(auto_now=True)),
                ('pagada', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-creada',),
            },
        ),
        migrations.CreateModel(
            name='OrdenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='labtienda.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_orden', to='labtienda.producto')),
            ],
        ),
    ]