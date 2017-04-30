from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('interests', )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User, UserAdmin)
