# Generated by Django 2.0.1 on 2018-01-20 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('matricula', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_credito', models.IntegerField()),
                ('d_credito_p', models.IntegerField()),
                ('a_credito_o', models.IntegerField()),
                ('a_credito_l', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=30)),
                ('obr_let', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Credito')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Curso')),
                ('d_requisito', models.ManyToManyField(to='coredrca.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('tipo', models.IntegerField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Professor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Secretaria'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='credito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Credito'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredrca.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to='coredrca.Disciplina'),
        ),
    ]
