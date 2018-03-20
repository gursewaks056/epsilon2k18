from django.contrib import admin
from .models import RegistrationTable, EventTable

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'college')

class PostAdmin2(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'event')

admin.site.register(RegistrationTable, PostAdmin)
admin.site.register(EventTable, PostAdmin2)
admin.site.site_header = "Epsilon Administration"
