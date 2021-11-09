from django.urls import path
from .views import CreateQuestion, QuestionDetail, ChoiceView, ChoiceDetail


urlpatterns = [
    path('<int:pk>/', QuestionDetail.as_view(), name='questiondetail'),
    path('<int:pk>/choice/', ChoiceView.as_view(), name='choices'),
    path('<int:pk>/choice/<int:choice_pk>/', ChoiceDetail.as_view(), name='choicedetail'),
    path('create/', CreateQuestion.as_view(), name='createquestion'),
]