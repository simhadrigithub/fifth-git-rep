from django.contrib import admin
from django.urls import path
from app.views import nature

urlpatterns =[
    path('admin/',admin.site.urls),
    path('',nature,name=nature),
]