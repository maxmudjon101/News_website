from django.urls import path
from .views import HomeView,DeteilNew,aloqa

urlpatterns=[
    path('',HomeView,name="bosh_sahifa"),
    path('alo/',aloqa,name="alo"),
    path('detail/<slug:slug>/',DeteilNew,name="detailn"),
]
