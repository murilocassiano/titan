from django.db import models
from datetime import datetime

class Asset(models.Model):
    asset_name = models.CharField(
    	max_length=200,
    	unique=True,
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
        choices = [('CP', 'Compra'), ('VD', 'Venda')],
        default = "CP"
    )

    price = models.FloatField(
        verbose_name="Valor Transação"
    )

    quantity = models.FloatField(
        verbose_name="Quantidade"
    )

    date = models.DateTimeField(
    	default=datetime.now())

    class Meta:
    	unique_together = ('asset','price','nature','quantity', 'date')