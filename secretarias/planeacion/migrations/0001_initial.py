# Generated by Django 4.1.3 on 2022-11-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tip_tramites',
            fields=[
                ('id_tramite', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_tramite', models.CharField(max_length=50)),
                ('descripcion_tramite', models.CharField(max_length=100)),
                ('responsable_tramite', models.CharField(max_length=200)),
            ],
        ),
    ]
