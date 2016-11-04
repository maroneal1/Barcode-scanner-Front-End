from django.contrib import admin
from .models import Question,Location,Item,Choice,Device,LocDev

admin.site.register(Question)
admin.site.register(Location)
admin.site.register(Device)
admin.site.register(LocDev)
admin.site.register(Item)
admin.site.register(Choice)
# Register your models here.
