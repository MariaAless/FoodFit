# Generated by Django 4.2.7 on 2023-11-28 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('receita', '0006_remove_receita_rendimento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receita.receita')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
