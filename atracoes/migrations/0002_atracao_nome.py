# Generated by Django 3.2.8 on 2021-10-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='nome',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
