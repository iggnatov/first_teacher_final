from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from voting.models import Participant, Judge
from voting.serializers import ParticipantSerializer, ParticipantAdminSerializer


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
