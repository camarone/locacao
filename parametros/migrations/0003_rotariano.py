# Generated by Django 2.1.2 on 2018-11-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_auto_20181107_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rotariano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('fone', models.CharField(max_length=150)),
            ],
        ),
    ]