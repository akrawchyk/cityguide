from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Interest, Profile, User


class InterestAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interest, InterestAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)
