from django.urls import path
from . import views

urlpatterns = [
      path('', views.register, name="register"),
       path('doctor_register',views.doctor_register,name="doctor_register"),
      path('login', views.login, name="login"),
      path('profile',views.profile,name="profile"),
     path('patient',views.patient,name="patient"),
      path('doctor',views.doctor,name="doctor"),
      path('redirect',views.profile_redirect,name="redirect")


]
