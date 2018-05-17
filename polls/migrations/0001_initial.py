# Generated by Django 2.0.3 on 2018-03-15 21:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=200, verbose_name='Nome do Ativo')),
                ('asset_code', models.CharField(max_length=200, unique=True, verbose_name='Código do Ativo')),
                ('typ', models.CharField(max_length=200, verbose_name='tipo de ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_price', models.FloatField(verbose_name='preço do dia')),
                ('date', models.DateTimeField(default=datetime.date(1000, 1, 1))),
                ('Open', models.FloatField(verbose_name='Open')),
                ('High', models.FloatField(verbose_name='High')),
                ('Low', models.FloatField(verbose_name='Low')),
                ('Close', models.FloatField(verbose_name='Close')),
                ('Volume', models.FloatField(verbose_name='Volume')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(choices=[('CP', 'Compra'), ('VD', 'Venda')], default='CP', max_length=20)),
                ('fraction', models.BooleanField(verbose_name='Fracionado')),
                ('unit_price', models.FloatField(verbose_name='Valor unitário da Transação')),
                ('quantity', models.FloatField(verbose_name='Quantidade')),
                ('transaction_date', models.DateTimeField(default=datetime.date(1000, 1, 1))),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Asset')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('asset', 'unit_price', 'nature', 'quantity', 'transaction_date')},
        ),
        migrations.AlterUniqueTogether(
            name='historic',
            unique_together={('date', 'asset', 'High'), ('date', 'asset', 'Open'), ('date', 'asset', 'Volume'), ('date', 'asset', 'Close'), ('date', 'asset', 'Low')},
        ),
    ]