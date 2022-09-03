from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path("",views.taketoLoginpage,name="loginpage"),
    path("registrationpg",views.taketoRegisterpage,name="registrationpg"),
    path("registerpage",views.registered,name="registerpage"),
    path("taketoMainpage",views.taketomainpage,name="taketoMainpage"),
    path("logintoMain <str:pk>",views.MainPage,name="logintoMain"),
    path("addthetask <str:pk>",views.Addtask,name="addthetask"),
    path("deletetask <str:pk>",views.DeleteTask,name="deletetask"),
    path("logout",views.Logout,name="logout"),
]
