# Generated by Django 4.1.3 on 2022-11-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip_tramites',
            name='id_tramite',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False),
        ),
    ]