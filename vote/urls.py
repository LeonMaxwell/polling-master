from django.urls import path
from .views import CreateVote

urlpatterns = [
    path('', CreateVote.as_view(), name='vote'),
]