from django.urls import path
from post import views

urlpatterns = [
    path('form/', views.FormList.as_view()),
]
