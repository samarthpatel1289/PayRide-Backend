from django.urls import path, include
from core import views as coreView

urlpatterns = [
    path('register/', coreView.Register.as_view()),
    path('login/', coreView.Login.as_view()),
]