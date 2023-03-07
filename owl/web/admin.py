from django.contrib import admin
from web.models import Monuments
# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    fields = ('id','name', 'description','slug')
    readonly_fields = ('id','slug')

admin.site.register(Monuments, MyModelAdmin)
