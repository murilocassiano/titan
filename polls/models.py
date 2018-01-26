from django.db import models


class Asset(models.Model):
    asset_name = models.CharField(max_length=200)
    asset_code = models.DateTimeField('date published')


class Transaction(models.Model):
    asset = models.ForeignKey(Asset)

    nature = (
        ('CP', 'Compra'),
        ('VD', 'Venda'),
    )

    price = models.FloatField(
        verbose_name="Valor Transação"
    )

    quantity = models.FloatField(
        verbose_name="Quantidade"
    )
