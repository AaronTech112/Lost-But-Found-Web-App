from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.dashboard, name = "dashboard"),
    path("report",views.report, name = "report"),
    path("profile",views.profile, name = "profile"),
    path("login",views.login_user, name = "login"),
    path("logout",views.logout_user, name = "logout"),
    path("register",views.register, name = "register"),
    path("all_items",views.all_items, name = "all_items"),
    path('update_status/<int:item_id>/', views.update_status, name='update_status'),
    path('item_detail/<int:pk>/', views.item_detail, name='item_detail'),
]


