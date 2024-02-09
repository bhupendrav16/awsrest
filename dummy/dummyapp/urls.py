from django.contrib import admin
from django.urls import path
from dummyapp.views import StudentGet,AddStudent

urlpatterns = [
    path("allstudent/",StudentGet.as_view()),
    path("addstudent/",AddStudent.as_view())
]
