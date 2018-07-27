from django.contrib import admin

from .models import Asset
from .models import Transaction
from .models import Historic

admin.site.register(Asset)

admin.site.register(Transaction)

admin.site.register(Historic)