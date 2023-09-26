from django.urls import path, re_path

from .views import ParticipantView, JudgeView, show_participants

urlpatterns = [
    re_path('voting+', show_participants),
    re_path('participants+', ParticipantView.as_view()),
    re_path('judge+', JudgeView.as_view()),
]
