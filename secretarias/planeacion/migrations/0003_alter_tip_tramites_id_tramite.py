# Generated by Django 4.1.3 on 2022-11-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeacion', '0002_alter_tip_tramites_id_tramite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip_tramites',
            name='id_tramite',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
