from django.urls import path
from . import views
urlpatterns = [
    path('', views.headpage),
    path('services', views.services),
    path('appointments', views.appointments),
    path('portfolio', views.portfolio),
    path('adduser', views.adduser),
    path('logout', views.logout),
    path('login', views.login),
    path('signin', views.signin),
    path('thankyou', views.thankyou),
    path('delete/<int:id>', views.delete),
    ]