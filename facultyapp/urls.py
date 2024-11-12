from django.urls import path, include
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('FacultyHomePage/', views.FacultyHomePage, name='FacultyHomePage'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_student_list/', views.view_student_list, name='view_student_list'),
]
