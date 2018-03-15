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

    typ = models.CharField(
        max_length=200,
        verbose_name="tipo de ativo"
        )

class Transaction(models.Model):
    asset = models.ForeignKey('Asset', on_delete=models.DO_NOTHING)

    nature = models.CharField(
        max_length=20,
        choices = (('CP', 'Compra'), ('VD', 'Venda')),
        default = "CP"
    )

    fraction = models.BooleanField(
        verbose_name="Fracionado"
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
    asset = models.ForeignKey('Asset', on_delete=models.DO_NOTHING)

    day_price = models.FloatField(
        verbose_name="preço do dia"
    )

    date = models.DateTimeField(
        default=datetime.date(1000,1,1)
    )    

    Open = models.FloatField(
        verbose_name="Open"
    )

    High = models.FloatField(
        verbose_name="High"
    )

    Low = models.FloatField(
        verbose_name="Low"
    )

    Close = models.FloatField(
        verbose_name="Close"
    )

    Volume =models.FloatField(
        verbose_name="Volume"
    )
    class Meta:
        unique_together = (('date','asset','Open'),('date','asset','High'),('date','asset','Low'),('date','asset','Close'),('date','asset','Volume'))
