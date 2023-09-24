from rest_framework.response import Response
from rest_framework.views import APIView

from voting.models import Participant
from voting.serializers import ParticipantSerializer, ParticipantAdminSerializer


class ParticipantView(APIView):
    def get(self, request):

        # jid = request.query_params['jid']
        group = request.query_params['group_number']

        participants = Participant.objects.filter(group_number=group)
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)


class ParticipantAdminView(APIView):
    def get(self, request):

        # jid = request.query_params['jid']
        group = request.query_params['group_number']

        participants = Participant.objects.filter(group_number=group)
        serializer = ParticipantAdminSerializer(participants, many=True)
        return Response(serializer.data)
