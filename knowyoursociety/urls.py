from django.urls import path
from django.shortcuts import redirect
from .views import *

urlpatterns = [
    path("",redirect_managing_committee),
    path("managing-committee/",managing_committee,name="managingCommittee"),
    path("do-s-and-dont-s/",dosAndDonts_view,name="dosanddonts"),
    path("rules-and-regulations/",rar_view,name="rar"),
    path("expenses/",expenses_view,name="expenses"),
]