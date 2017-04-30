from django.contrib import admin

from .models import Interest


class InterestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interest, InterestAdmin)
