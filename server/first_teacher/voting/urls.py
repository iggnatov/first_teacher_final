from django.urls import path, re_path

from voting.views import ParticipantView, JudgeView, show_participants, CriteriaView, VotingView

urlpatterns = [
    re_path('voting+', show_participants),
    re_path('participants+', ParticipantView.as_view()),
    re_path('judge+', JudgeView.as_view()),
    re_path('criterias+', CriteriaView.as_view()),
    re_path('get_votes+', VotingView.as_view()),
]
