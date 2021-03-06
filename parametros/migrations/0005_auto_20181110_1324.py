# Generated by Django 2.0.3 on 2018-11-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0004_auto_20181109_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Andador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4, unique=True)),
                ('modelo', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CadeiraDeBanho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4, unique=True)),
                ('modelo', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Muleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4, unique=True)),
                ('modelo', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='modelo',
            field=models.CharField(default=111, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
