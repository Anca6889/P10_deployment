from django.urls import path
from authentication import views

urlpatterns = [
    path('sign_in/', views.sign_in, name= "sign_in"),
    path('login/', views.login, name="login"),
]
