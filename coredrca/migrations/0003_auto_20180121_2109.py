# Generated by Django 2.0.1 on 2018-01-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coredrca', '0002_auto_20180121_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to='coredrca.Disciplina'),
        ),
    ]
