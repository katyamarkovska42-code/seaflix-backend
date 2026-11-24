from django.contrib import admin
from films.models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'original_title',
        'release_year',
        'duration_minutes',
        'country',
    )

    search_fields = (
        'title',
        'original_title',
        'country',
    )

    list_filter = (
        'release_year',
        'country',
    )

    ordering = ('title',)