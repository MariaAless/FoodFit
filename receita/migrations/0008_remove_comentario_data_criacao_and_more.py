# Generated by Django 4.2.7 on 2023-11-28 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0007_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='data_criacao',
        ),
        migrations.AddField(
            model_name='comentario',
            name='data_publicacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
