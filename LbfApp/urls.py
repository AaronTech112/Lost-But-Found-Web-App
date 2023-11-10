from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.dashboard, name = "dashboard"),
    path("report",views.report, name = "report"),
    path("profile",views.profile, name = "profile"),
    path("login",views.login, name = "login"),
    path("logout",views.logout_user, name = "logout"),
    path("register",views.register, name = "register"),
]


