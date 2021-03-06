from django.urls import path

from . import views

# 다른 앱에서도 이름 detail인게 있을 경우
# template의 {% url %} 이 둘을 구분 할수 있게 하기위해
# namespace를 나눈다.
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]