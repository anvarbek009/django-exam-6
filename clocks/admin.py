from django.contrib import admin
from .models import Review,Watch,Cart,CartItem
# Register your models here.

admin.site.register(Review)
admin.site.register(Watch)
admin.site.register(Cart)
admin.site.register(CartItem)

