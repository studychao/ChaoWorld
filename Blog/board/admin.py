from django.contrib import admin
from .models import usercomment

class commentAdmin(admin.ModelAdmin):
    list_display = ['text','reply']
admin.site.register(usercomment,commentAdmin)
