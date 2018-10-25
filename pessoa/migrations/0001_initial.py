# Generated by Django 2.1 on 2018-08-28 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(blank=True, max_length=20)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=25)),
                ('rg', models.CharField(blank=True, max_length=15)),
                ('cep', models.CharField(blank=True, max_length=15, verbose_name='Cep')),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=15)),
                ('telefone', models.CharField(blank=True, max_length=16)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('bairro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parametros.Bairro')),
                ('etadocivil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parametros.Estadocivil')),
                ('municipios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parametros.Cidade')),
                ('profissao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parametros.Profissao')),
                ('uf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parametros.Estado')),
            ],
        ),
    ]
