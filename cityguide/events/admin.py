from django.contrib import admin
from .models import Event
from cityguide.interests.models import Interest


class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ('attendees', 'interests', )


admin.site.register(Event, EventAdmin)
