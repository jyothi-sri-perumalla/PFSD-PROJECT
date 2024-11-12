from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpage/', views.exceptionpage, name='exceptionpage'),
    path('randompagecall', views.randompagecall, name='randompagecall'),
    path('randomlogic', views.randomlogic, name='randomlogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic', views.calculatorlogic, name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimelogic/', views.datetimelogic, name='datetimelogic'),
    path('registerpagecall/', views.registerpagecall, name='registerpagecall'),
    path('registerpagelogic/', views.registerpagelogic, name='registerpagelogic'),
    path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
    path('loginpagelogic/', views.loginpagelogic, name='loginpagelogic'),
    path('logout/', views.logout, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
]