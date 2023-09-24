from django.urls import path, re_path

from .views import ParticipantView, ParticipantAdminView

urlpatterns = [
    re_path('participants+', ParticipantView.as_view()),
    re_path('results+', ParticipantAdminView.as_view()),
]
