from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True)
    release_year = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    country = models.CharField(max_length=100, blank=True)
    poster_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return f'{self.title} ({self.release_year})'