# Generated by Django 4.2.5 on 2023-09-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_remove_participant_code_for_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='previous_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
