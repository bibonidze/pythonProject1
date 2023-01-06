from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("register", views.register_request, name="register"),
    path("create", views.create, name="create"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("task_delete", views.task_delete, name="task_delete"),
]
