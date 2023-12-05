from django.urls import path
from .views import Get_GroupsView

urlpatterns = [
    path('gr/',Get_GroupsView.as_view()),
    path('gr/<int:id>',Get_GroupsView.as_view())
]