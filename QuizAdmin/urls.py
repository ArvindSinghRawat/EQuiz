from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^CreateQuiz', views.create_quiz, name='create_quiz'),
    url(r'^ajax/send_code/$', views.send_code, name='send_code'),
]
