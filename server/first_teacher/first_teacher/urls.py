from django.contrib import admin
from django.urls import include, path

import voting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voting.urls')),
]
