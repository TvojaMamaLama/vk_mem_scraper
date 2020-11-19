from django.contrib import admin

from .models import Group, Request, Meme


admin.site.register(Group)
admin.site.register(Request)
admin.site.register(Meme)
