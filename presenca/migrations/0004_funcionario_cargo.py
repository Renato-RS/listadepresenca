# Generated by Django 4.2.6 on 2023-10-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presenca', '0003_rename_nome_obra_atividade'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(default='Operario', max_length=50),
        ),
    ]