

# Register your models here.
from django.contrib import admin

from Bank1.models import Sogebanque, Unibanque


class SogebanqueAdmin(admin.ModelAdmin):
    list_display=('nom','username','password','email','compte','active','Update_compte')


class UnibankAdmin(admin.ModelAdmin):
    list_display=('nom','username','password','compte','active','Update_compte')

admin.site.register(Sogebanque,SogebanqueAdmin)
admin.site.register(Unibanque,UnibankAdmin)
