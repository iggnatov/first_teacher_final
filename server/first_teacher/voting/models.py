from django.db import models


class Participant(models.Model):
    last_name = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    father_name = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    previous_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    chosen_topic = models.CharField(max_length=255, blank=True)
    group_number = models.SmallIntegerField(blank=True, default=0)
    order_number = models.SmallIntegerField(blank=True, default=0)
    final_1tour_score = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]} {self.father_name[:1]} ' \
               f'- GroupNumber: {self.group_number} - OrderNumber: {self.order_number} ' \
               f'- Final_1tour_score: {self.final_1tour_score};'


class Judge(models.Model):
    last_name = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    father_name = models.CharField(max_length=30, blank=True)
    code_for_link = models.CharField(max_length=10, blank=True, unique=True)
    group_number = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]} {self.father_name[:1]} ' \
               f'- CodeForLink: {self.code_for_link} - GroupNumber: {self.group_number}'


class Criteria(models.Model):
    tour = models.SmallIntegerField(blank=True, default=1)
    description = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return f'{self.pk} - {self.tour} - {self.description}'


class Voting(models.Model):
    judge = models.ForeignKey(
        Judge,
        # to_field='last_name',
        on_delete=models.CASCADE,
    )
    participant = models.ForeignKey(
        Participant,
        # to_field='last_name',
        on_delete=models.CASCADE,
    )
    # criteria = models.ForeignKey(
    #     Criteria,
    #     to_field='description',
    #     on_delete=models.CASCADE,
    # )
    score = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.judge} - {self.participant} - {self.score}'
