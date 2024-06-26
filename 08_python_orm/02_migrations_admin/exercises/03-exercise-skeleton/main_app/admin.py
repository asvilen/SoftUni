from django.contrib import admin
from .models import Shoe
from .models import EventRegistration


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    pass


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'participant_name', 'registration_date')
    list_filter = ('event_name', 'registration_date')
    search_fields = ('event_name', 'participant_name')