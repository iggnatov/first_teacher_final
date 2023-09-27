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


