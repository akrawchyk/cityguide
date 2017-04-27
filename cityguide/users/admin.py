from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Interest, User, UserProfile


class InterestAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interest, InterestAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User, UserProfileAdmin)
