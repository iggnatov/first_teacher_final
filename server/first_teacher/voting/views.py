from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from voting.models import Participant, Judge, Voting, Criteria
from voting.serializers import ParticipantSerializer, ParticipantAdminSerializer, VotingSerializer, CriteriaSerializer


def show_participants(request):
    return render(request, "voting.html")


class ParticipantView(APIView):
    def get(self, request):
        group = request.query_params['group_number']
        participants = Participant.objects.filter(group_number=group).order_by('order_number')
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)


class JudgeView(APIView):

    def get(self, request):
        jid = request.query_params['jid']
        judge = Judge.objects.get(code_for_link=jid)
        serializer = ParticipantAdminSerializer(judge)
        return Response(serializer.data)


class CriteriaView(APIView):
    def get(self, request):
        tour = request.query_params['tour']
        criterias = Criteria.objects.filter(tour=tour)
        serializer = CriteriaSerializer(criterias, many=True)
        return Response(serializer.data)


class VotingView(APIView):
    def get(self, request):
        jid = request.query_params['jid']
        j = Judge.objects.get(code_for_link=jid)

        votings = Voting.objects.filter(judge=j)
        serializer = VotingSerializer(votings, many=True)
        return Response(serializer.data)


class ScoreView(APIView):
    def get(self, request):
        jid = request.query_params['jid']
        rid = request.query_params['rid']
        score = request.query_params['score']
        j = Judge.objects.get(code_for_link=jid)
        print(j, jid, rid, score)

        current_voting = Voting.objects.filter(judge=j).filter(participant=int(rid))
        print(current_voting[0])
        gi = current_voting[0].id
        di = Voting.objects.get(pk=gi)
        di.score = score
        di.save()
        print(di)
        print(current_voting[0])
        print(current_voting)
        # serializer = VotingSerializer(votings, many=True)

        response = {
            'jid': jid,
            'rid': rid,
            'score': score
        }
        return Response(response)

# admin views


def help_admin(request):
    return render(request, "help_admin.html")


class SetAdminVotesView(APIView):
    def get(self, request):
        print('start')

        judges = Judge.objects.all()
        participants = Participant.objects.all()

        for judge in judges:
            for participant in participants:
                if participant.group_number == judge.group_number:
                    print(judge.pk, participant.pk, 0)
                    j = judges.get(pk=judge.pk)
                    p = participants.get(pk=participant.pk)
                    Voting.objects.create(judge=j, participant=p, score=0)


        start_score = Voting.objects.all()
        serializer = VotingSerializer(start_score, many=True)
        return Response(serializer.data)


