from django.urls import path
from .views import index, notices, Events_view,DetailEvents_view

urlpatterns = [
    path("",index,name="home"),
    path("notices/",notices,name="notices"),
    path("events/",Events_view,name="events"),
    path("detail-event/<int:pk>",DetailEvents_view.as_view(),name="detailevent"),
]