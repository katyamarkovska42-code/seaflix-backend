from django.core.validators import MinValueValidator
from django.db import models


class Auditorium(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['building', 'name']
        verbose_name = 'Auditorium'
        verbose_name_plural = 'Auditoriums'
        constraints = [
            models.UniqueConstraint(
                fields=['building', 'name'],
                name='unique_auditorium_in_building',
            ),
        ]

    def __str__(self):
        return f'{self.name} ({self.building})'
     