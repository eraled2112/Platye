from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(ProductImg)
admin.site.register(Features)

