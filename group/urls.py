from django.urls import path
from .views import Get_GroupsView,GruopId_All_Students

urlpatterns = [
    path('',Get_GroupsView.as_view()),
    path('<int:id>',Get_GroupsView.as_view()),
    path('<int:id>/students',GruopId_All_Students.as_view())
]