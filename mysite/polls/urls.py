from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<question_id>/', views.detail, name='detail'),
    path('<question_id>/results', views.results, name='results'),
    path('<question_id>/votes', views.votes, name='votes'),
]