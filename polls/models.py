from django.db import models
import datetime

class Asset(models.Model):
    asset_name = models.CharField(
        max_length=200,
        verbose_name="Nome do Ativo"
    )

    asset_code = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Código do Ativo"
    )

class Transaction(models.Model):
    asset = models.ForeignKey(Asset)

    nature = models.CharField(
        max_length=20,
        choices = (('CP', 'Compra'), ('VD', 'Venda')),
        default = "CP"
    )

    unit_price = models.FloatField(
        verbose_name="Valor unitário da Transação"
    )

    quantity = models.FloatField(
        verbose_name="Quantidade"
    )

    transaction_date = models.DateTimeField(
        default=datetime.date(1000,1,1)
    )

    class Meta:
        unique_together = ('asset','unit_price','nature','quantity', 'transaction_date')


class Historic(models.Model):
    asset = models.ForeignKey(Asset)
    day_price = models.FloatField(
        verbose_name="preço do dia"
    )

    date = models.DateTimeField(
        default=datetime.date(1000,1,1)
    )    