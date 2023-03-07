from django.urls import path
from tree import views
from tree.models import Discipline

urlpatterns = [
    path('', views.index),
    path('user/discipline', views.main_discipline),
    path('data2', views.main_student),
    path('data3', views.main_group),
    path('<int:group_id>', views.stud_by_group),
    path('info/<int:stud_id>/', views.stud_info)
]
