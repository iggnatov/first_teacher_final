from rest_framework import serializers

from voting.models import Participant, Judge, Criteria


class ParticipantAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["id", "last_name", "first_name", "father_name", "region", "city",
                  "chosen_topic", "group_number", "order_number"]


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'

