# Generated by Django 3.2.8 on 2021-10-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('horario_funcionamento', models.TextField()),
                ('idade_minima', models.IntegerField()),
            ],
        ),
    ]
