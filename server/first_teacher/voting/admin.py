from django.contrib import admin

from voting.models import Participant, Judge, Criteria, Voting

admin.site.register(Participant)
admin.site.register(Judge)
admin.site.register(Criteria)
admin.site.register(Voting)