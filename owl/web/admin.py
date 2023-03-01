from django.contrib import admin
from web.models import Monuments
# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    fields = ('id','name', 'description')
    readonly_fields = ('id',)

admin.site.register(Monuments, MyModelAdmin)
