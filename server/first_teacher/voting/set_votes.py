from voting.models import Participant, Judge, Voting, Criteria

judges = Judge.objects.all()
print(judges)
# vote = Voting.objects.create()