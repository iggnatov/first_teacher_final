from django.contrib import admin

from voting.models import Participant, Judge

admin.site.register(Participant)
admin.site.register(Judge)