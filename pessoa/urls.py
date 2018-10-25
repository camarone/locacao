from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /contribuinte/5/
    path('<int:pessoa_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('gerarcontrato/<int:cadastrodealuguel_id>/', views.gerarcontrato, name='gerarcontrato'),

]