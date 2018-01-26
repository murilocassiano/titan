from django.contrib import admin

from .models import Asset

from .models import Transaction

admin.site.register(Asset)

admin.site.register(Transaction)
