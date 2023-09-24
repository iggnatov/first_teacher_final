# Generated by Django 4.2.5 on 2023-09-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigJudge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('father_name', models.CharField(blank=True, max_length=30)),
                ('code_for_link', models.CharField(blank=True, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinalParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('father_name', models.CharField(blank=True, max_length=30)),
                ('code_for_link', models.CharField(blank=True, max_length=10, unique=True)),
                ('participant_id', models.SmallIntegerField(blank=True, unique=True)),
                ('previous_score', models.SmallIntegerField(blank=True)),
                ('score_2tour_1criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_2tour_2criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_2tour_3criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_2tour_4criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_2tour_5criteria', models.SmallIntegerField(blank=True, default=0)),
                ('final_2tour_score', models.SmallIntegerField(blank=True)),
                ('is_winner', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('father_name', models.CharField(blank=True, max_length=30)),
                ('code_for_link', models.CharField(blank=True, max_length=10, unique=True)),
                ('group_number', models.SmallIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('father_name', models.CharField(blank=True, max_length=30)),
                ('code_for_link', models.CharField(blank=True, max_length=10, unique=True)),
                ('participant_id', models.SmallIntegerField(blank=True, unique=True)),
                ('previous_score', models.SmallIntegerField(blank=True)),
                ('group_number', models.SmallIntegerField(blank=True)),
                ('order_number', models.SmallIntegerField(blank=True)),
                ('score_1tour_1criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_1tour_2criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_1tour_3criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_1tour_4criteria', models.SmallIntegerField(blank=True, default=0)),
                ('score_1tour_5criteria', models.SmallIntegerField(blank=True, default=0)),
                ('final_1tour_score', models.SmallIntegerField(blank=True)),
                ('is_final', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
