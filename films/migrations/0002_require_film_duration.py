from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration_minutes',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
