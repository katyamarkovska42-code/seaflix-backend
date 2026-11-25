from django.contrib import admin
from screenings.models import Auditorium


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'building',
        'capacity',
        'is_active',
    )

    search_fields = (
        'name',
        'building',
    )

    list_filter = (
        'building',
        'is_active',
    )

    ordering = ('building', 'name')
