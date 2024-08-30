from django.contrib import admin
from .models import UPIAccount, Transaction

admin.site.register(UPIAccount)
admin.site.register(Transaction)

