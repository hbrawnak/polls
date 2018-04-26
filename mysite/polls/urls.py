from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<question_id>/', views.detail, name='detail'),
    path('<question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.votes, name='votes'),
]