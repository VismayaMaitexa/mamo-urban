from django.contrib import admin

from .models import Consumer,Booking,Payment,Worker,Cart,Services

# Register your models here.

admin.site.register(Consumer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Worker)
admin.site.register(Cart)
admin.site.register(Services)
