# Generated by Django 4.1.2 on 2022-11-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EjemploORM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='perfil',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
