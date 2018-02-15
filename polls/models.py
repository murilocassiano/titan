from django.db import models
import datetime

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

class Date(models.Model):
    date =  models.DateTimeField(
        default= datetime.date(1000,1,1),
        unique=True)

    weekday = models.CharField(
        max_length=20,
        choices = [
           ('0', 'Monday'),
           ('1', 'Tuesday'),
           ('2', 'Wednesday'),
           ('3', 'Thursday'),
           ('4', 'Friday'),
           ('5', 'Saturday'),
           ('6', 'Sunday')
        ],
    ) 

    month = models.CharField(
        max_length=20,
        choices = [
           ('1', 'Jan'),
           ('2', 'Feb'),
           ('3', 'Mar'),
           ('4', 'Apr'),
           ('5', 'May'),
           ('6', 'Jun'),
           ('7', 'Jul'),
           ('8', 'Ago'),
           ('9', 'Sep'),
           ('10', 'Oct'),
           ('11', 'Nov'),
           ('12', 'Dec'),
        ],
    ) 

class Transaction(models.Model):
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
    class Meta:
        unique_together = ('nature','price', 'quantity')

class AssetsAnalytics(models.Model):
    assetId = models.ForeignKey(Asset)

    dateId = models.ForeignKey(Date)

    transactionId = models.ForeignKey(
        Transaction,
        default = 0)

    tpe = models.CharField(
        max_length=20,
        choices =[('TR', 'Transactional'), ('DV', 'Daily Value')],
        default = "DV"
        )

    class Meta:
        unique_together = ('assetId','dateId', 'transactionId', 'tpe')
