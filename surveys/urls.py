from django.urls import path
from .views import ListPoll, CreatePoll, PollDetail, ListPassedPoll


urlpatterns = [
    path('', ListPoll.as_view(), name='poll'),
    path('passed/<int:user_pk>/', ListPassedPoll.as_view(), name='passedpoll'),
    path('<int:pk>/', PollDetail.as_view(), name='polldetail'),
    path('create/', CreatePoll.as_view(), name='createpoll')
]