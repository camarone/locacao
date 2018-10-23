# Generated by Django 2.0.2 on 2018-05-14 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=200)),
                ('bairro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='endereco.Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Localidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='endereco.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='endereco.Pais'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='endereco.Municipio'),
        ),
    ]