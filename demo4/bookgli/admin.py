from django.contrib import admin

from .models import Users,Books,Histroys

# Register your models here.

admin.site.register(Users)
admin.site.register(Books)
admin.site.register(Histroys)