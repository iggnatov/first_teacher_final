from django.db import models


class Participant(models.Model):
    last_name = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    father_name = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    code_for_link = models.CharField(max_length=10, blank=True, unique=True)
    participant_id = models.SmallIntegerField(blank=True, unique=True)
    previous_score = models.SmallIntegerField(blank=True)
    chosen_topic = models.CharField(max_length=255, blank=True)
    group_number = models.SmallIntegerField(blank=True, default=0)
    order_number = models.SmallIntegerField(blank=True, default=0)
    final_1tour_score = models.SmallIntegerField(blank=True, default=0)
    is_final = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]}'


class Judge(models.Model):
    last_name = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    father_name = models.CharField(max_length=30, blank=True)
    code_for_link = models.CharField(max_length=10, blank=True, unique=True)
    group_number = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]}'


class Voting(models.Model):
    personal_judge_code = models.ForeignKey(
        Judge,
        to_field='code_for_link',
        blank=True,
        on_delete=models.CASCADE,
    )
    personal_participant_code = models.ForeignKey(
        Participant,
        to_field='code_for_link',
        blank=True,
        on_delete=models.CASCADE,
    )
    score_1tour_1criteria = models.SmallIntegerField(blank=True, default=0)
    score_1tour_2criteria = models.SmallIntegerField(blank=True, default=0)
    score_1tour_3criteria = models.SmallIntegerField(blank=True, default=0)
    score_1tour_4criteria = models.SmallIntegerField(blank=True, default=0)
    score_1tour_5criteria = models.SmallIntegerField(blank=True, default=0)


    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]}'
